/**
 * coc7-ru-content — русские CoCID-документы для системы CoC7.
 *
 * Переопределение не требует никаких хаков: система сама выбирает документ,
 * у которого flags.CoC7.cocidFlag.lang совпадает с game.i18n.lang, и
 * отбрасывает англоязычных кандидатов с тем же CoCID
 * (см. coc7/apps/coc-id.js, #filterByLanguage и #compareCoCIDPriority).
 *
 * Этот скрипт ничего не патчит. Он только:
 *   1) повторно применяет lang/ru.json (имена навыков для резервных проверок
 *      системы по CoC7.CoCIDFlag.keys.*) с overwrite: true, чтобы они всегда
 *      совпадали с именами документов в паках;
 *   2) предупреждает, если язык мира не русский (тогда паки не применятся);
 *   3) даёт диагностику по CoCID: game.modules.get('coc7-ru-content').api.report()
 */

const MODULE_ID = 'coc7-ru-content'
const SYSTEM_ID = 'CoC7'
const LANG_PATH = `modules/${MODULE_ID}/lang/ru.json`

/**
 * Повторно наложить имена CoCID поверх словаря локализации.
 * @returns {Promise<number>} количество применённых строк
 */
async function applyNames () {
  let strings
  try {
    strings = typeof foundry?.utils?.fetchJsonWithTimeout === 'function'
      ? await foundry.utils.fetchJsonWithTimeout(LANG_PATH)
      : await (await fetch(LANG_PATH)).json()
  } catch (error) {
    console.error(`${MODULE_ID} | Не удалось загрузить ${LANG_PATH}:`, error)
    return 0
  }
  const expand = foundry?.utils?.expandObject ?? (value => value)
  const merge = foundry?.utils?.mergeObject ?? mergeObject
  merge(game.i18n.translations, expand(strings), { inplace: true, overwrite: true })
  return Object.keys(strings).length
}

/**
 * Собрать сводку по русским документам модуля.
 * @returns {Promise<object>}
 */
async function report () {
  const rows = []
  for (const pack of game.packs) {
    if (pack.metadata.packageName !== MODULE_ID) continue
    if (!pack.indexed) await pack.getIndex()
    for (const entry of pack.index) {
      const flag = entry.flags?.[SYSTEM_ID]?.cocidFlag
      if (!flag?.id) continue
      rows.push({
        cocid: flag.id,
        lang: flag.lang,
        priority: flag.priority ?? 0,
        name: entry.name,
        pack: pack.metadata.id
      })
    }
  }
  rows.sort((a, b) => a.cocid.localeCompare(b.cocid))
  const wrongLang = rows.filter(r => r.lang !== 'ru')
  console.group(`${MODULE_ID}: ${rows.length} документов с CoCID`)
  console.table(rows)
  if (wrongLang.length) {
    console.warn(`${MODULE_ID}: у ${wrongLang.length} документов lang !== 'ru'`, wrongLang)
  }
  if (!game.i18n.lang.startsWith('ru')) {
    console.warn(`${MODULE_ID}: язык интерфейса — '${game.i18n.lang}'. Система подставит английские документы; переключите язык на русский.`)
  }
  console.groupEnd()
  return { total: rows.length, rows, wrongLang, lang: game.i18n.lang }
}

/**
 * Проверить, какой документ система реально выберет для набора CoCID.
 * @param {string[]} cocids
 * @returns {Promise<object[]>}
 */
async function resolve (cocids = ['i.skill.dodge', 'i.setup.s-setup', 'i.archetype.peacemaker', 'i.occupation.street-vendor', 'rt..backstory-traits']) {
  const out = []
  for (const cocid of cocids) {
    let doc
    try {
      doc = await game[SYSTEM_ID].cocid.fromCoCID(cocid)
    } catch (error) {
      out.push({ cocid, error: error.message })
      continue
    }
    const first = Array.isArray(doc) ? doc[0] : doc
    out.push({
      cocid,
      name: first?.name ?? '—',
      lang: first?.flags?.[SYSTEM_ID]?.cocidFlag?.lang ?? '—',
      pack: first?.pack ?? 'world'
    })
  }
  console.table(out)
  return out
}

Hooks.once('init', () => {
  const module = game.modules.get(MODULE_ID)
  if (module) {
    module.api = { report, resolve }
  }
})

Hooks.once('ready', async () => {
  if (game.i18n.lang.toLowerCase().startsWith('ru')) {
    const applied = await applyNames()
    if (applied) {
      console.info(`${MODULE_ID} | Имена CoCID применены: ${applied} строк.`)
    }
  }
  if (!game.i18n.lang.startsWith('ru')) {
    console.warn(`${MODULE_ID}: язык интерфейса — '${game.i18n.lang}'. Русские компендиумы подключены, но система будет использовать английские документы, пока язык мира не русский.`)
  } else {
    console.log(`${MODULE_ID}: русские CoCID-компендиумы активны. Диагностика: game.modules.get('${MODULE_ID}').api.report()`)
  }
})
