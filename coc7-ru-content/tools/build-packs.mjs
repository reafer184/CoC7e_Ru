/**
 * Сборка бинарных компендиумов (LevelDB) модуля coc7-ru-content
 * из YAML-исходников в ./compendiums.
 *
 * Логика повторяет сборщик системы CoC7
 * (scripts/src/generate-compendiums.js + template-helpers.js):
 *   - ключи !items!<id>, !folders!<id>, !tables!<id>
 *   - вложенные результаты таблиц: !tables.results!<tableId>.<resultId>
 *   - идентификаторы детерминированы: md5(name + lang + JSON.stringify(eras))
 *   - для навыков из имени «Специализация (Уточнение)» выводятся
 *     system.specialization и system.skillName
 *
 * Дополнительно (нет в системе): в результатах таблиц можно указать
 *   documentCoCID: i.status.acrophobia
 * — сборщик сам подставит documentCollection и documentId нужного документа.
 *
 * Запуск:  node tools/build-packs.mjs     (из корня модуля)
 */
import * as crypto from 'crypto'
import * as fs from 'fs'
import * as path from 'path'
import { loadAll } from 'js-yaml'
import { ClassicLevel } from 'classic-level'

const LANG = 'ru'
const FOLDER_ID = 'CoC7'
const root = process.cwd()
const moduleJson = JSON.parse(fs.readFileSync(path.join(root, 'module.json'), 'utf8'))

const collisions = {}

function buildId (idSource) {
  const id = crypto.createHash('md5').update(idSource).digest('base64').replace(/[+=/\\]/g, '').substring(0, 16)
  if (typeof collisions[id] !== 'undefined') {
    throw new Error('Коллизия идентификаторов: ' + idSource)
  }
  collisions[id] = true
  return id
}

function cocidFlag (doc) {
  return doc?.flags?.[FOLDER_ID]?.cocidFlag
}

/** Первый проход: читаем YAML, назначаем _id, строим карту CoCID → документ */
const packs = []
const byCoCID = {}

for (const pack of moduleJson.packs) {
  const name = pack.path.replace(/^packs\//, '')
  const yamlPath = path.join(root, 'compendiums', name + '.yaml')
  if (!fs.existsSync(yamlPath)) {
    throw new Error('Нет исходника ' + yamlPath)
  }
  const docs = loadAll(fs.readFileSync(yamlPath, 'utf8')).filter(d => d)
  for (const doc of docs) {
    if (doc.type === 'folder') {
      if (!doc._id) doc._id = buildId(doc.name + LANG + 'folder')
      continue
    }
    if (!doc._id) {
      doc._id = buildId(doc.name + LANG + JSON.stringify(cocidFlag(doc)?.eras))
    }
    const id = cocidFlag(doc)?.id
    if (!id) throw new Error('Документ без CoCID: ' + doc.name + ' (' + name + ')')
    if (byCoCID[id]) throw new Error('CoCID встречается дважды: ' + id)
    byCoCID[id] = { pack: name, doc }
  }
  packs.push({ name, type: pack.type, docs })
}

/** Второй проход: обработка документов и запись LevelDB */
for (const pack of packs) {
  const documents = {}
  for (const doc of pack.docs) {
    if (doc.type === 'folder') {
      const folder = { ...doc, type: pack.type }
      documents['!folders!' + doc._id] = folder
      continue
    }
    if (pack.type === 'Item' && doc.type === 'skill') {
      const match = doc.name.match(/^(.+)\s*\((.+)\)$/)
      doc.system = doc.system || {}
      if (match) {
        doc.system.specialization = match[1].trim()
        doc.system.skillName = match[2].trim()
      } else {
        doc.system.skillName = doc.name
        doc.system.specialization = ''
      }
    }
    if (pack.type === 'RollTable' && typeof doc.results !== 'undefined') {
      let range = 0
      for (const offset in doc.results) {
        const result = doc.results[offset]
        if (!result._id) {
          result._id = buildId(doc.name + LANG + JSON.stringify(cocidFlag(doc)?.eras) + offset)
        }
        if (!result.range) {
          range++
          result.range = [range, range]
        } else {
          range = result.range[1]
        }
        if (result.type === 'text') {
          result.text = '<strong>' + result.name + '</strong> ' + result.description
        }
        if (typeof result.documentCoCID === 'string') {
          const target = byCoCID[result.documentCoCID]
          if (!target) throw new Error('Не найдена цель ' + result.documentCoCID + ' в таблице ' + doc.name)
          result.documentCollection = moduleJson.id + '.' + target.pack
          result.documentId = target.doc._id
          delete result.documentCoCID
        }
      }
      if (!doc.formula) doc.formula = '1d' + range
    }
    const key = pack.type === 'RollTable' ? '!tables!' : '!items!'
    documents[key + doc._id] = doc
  }

  const groups = { results: /^!(tables)!([a-zA-Z0-9]{16})$/ }
  const batch = Object.keys(documents).reduce((c, i) => {
    const all = { [i]: JSON.parse(JSON.stringify(documents[i])) }
    for (const group in groups) {
      const array = i.match(groups[group])
      if (array) {
        for (const offset in documents[i][group]) {
          const arrayKey = '!' + array[1] + '.' + group + '!' + array[2] + '.' + documents[i][group][offset]._id
          all[arrayKey] = documents[i][group][offset]
          all[i][group][offset] = documents[i][group][offset]._id
        }
      }
    }
    for (const key in all) {
      c.push({ type: 'put', key, value: all[key], valueEncoding: 'json' })
    }
    return c
  }, [])

  const target = path.join(root, 'packs', pack.name)
  if (fs.existsSync(target)) {
    await ClassicLevel.destroy(target)
    fs.rmSync(target, { recursive: true, force: true })
  }
  fs.mkdirSync(target, { recursive: true })
  const db = new ClassicLevel(target, { keyEncoding: 'utf8', valueEncoding: 'json' })
  await db.batch(batch, { valueEncoding: 'utf8' })
  await db.close()
  console.log('Собран packs/' + pack.name + ': ' + batch.length + ' записей')
}
