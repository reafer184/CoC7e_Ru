/**
 * coc7-ru-fixes
 *
 * Модуль не изменяет файлы системы CoC7. Он накладывает исправленные русские
 * строки поверх штатного словаря.
 *
 * Слой 1: lang/ru.json регистрируется как языковой файл модуля — Foundry
 *         сливает его со словарём системы при загрузке локали.
 * Слой 2: этот скрипт повторно применяет тот же файл на хуке "ready" с
 *         overwrite: true. Это страхует порядок слияния переводов: если
 *         системный или сторонний ru.json загрузился позже, наши формулировки
 *         всё равно окажутся сверху.
 *
 * Единственный источник строк — lang/ru.json, словарь здесь не дублируется.
 */

const MODULE_ID = 'coc7-ru-fixes'
const OVERRIDES_PATH = `modules/${MODULE_ID}/lang/ru.json`

/**
 * Загружает словарь исправлений.
 * @returns {Promise<object|null>}
 */
async function loadOverrides () {
  try {
    if (typeof foundry?.utils?.fetchJsonWithTimeout === 'function') {
      return await foundry.utils.fetchJsonWithTimeout(OVERRIDES_PATH)
    }
    const response = await fetch(OVERRIDES_PATH)
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`)
    }
    return await response.json()
  } catch (error) {
    console.error(
      `${MODULE_ID} | Не удалось загрузить ${OVERRIDES_PATH}:`,
      error
    )
    return null
  }
}

/**
 * Считает количество листовых строк в словаре.
 * @param {object} node
 * @returns {number}
 */
function countStrings (node) {
  let total = 0
  for (const value of Object.values(node)) {
    if (value !== null && typeof value === 'object') {
      total += countStrings(value)
    } else {
      total += 1
    }
  }
  return total
}

Hooks.once('ready', async () => {
  const lang = game.i18n?.lang ?? ''
  if (!lang.toLowerCase().startsWith('ru')) {
    return
  }

  const overrides = await loadOverrides()
  if (overrides === null) {
    return
  }

  const merge = foundry?.utils?.mergeObject ?? mergeObject
  merge(game.i18n.translations, overrides, {
    inplace: true,
    overwrite: true
  })

  console.info(
    `${MODULE_ID} | Исправления русской локализации применены: ` +
      `${countStrings(overrides)} строк.`
  )

  Hooks.callAll(`${MODULE_ID}.applied`, overrides)
})
