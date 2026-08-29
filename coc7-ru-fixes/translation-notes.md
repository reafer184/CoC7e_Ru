# Переводческие заметки

Модуль `coc7-ru-fixes` накладывает исправленные строки поверх системы CoC7, не изменяя её файлы.
Источник сверки — `source/coc7-ru-full-source.json` (экспорт `static/lang/en.json`, `static/lang/ru.json`
и шаблонов `investigator-v3` / `investigator-wizard`).

## Итог

- Всего ключей в модуле: **37**
- Отсутствовали в штатном `ru.json` системы: **6** (AddArmor, ClearExperiencePackageName, DeleteBookProgress, ExperiencePackageSkill, SkillExperiencePackage, ModifiedByActiveEffect)
- Формулировка уточнена относительно штатного перевода: **26**
- Совпадает со штатным переводом (закреплено для устойчивости порядка слияния): **5**

## Принципы

- Термины листа приводятся к единой системе: «Базовое значение» / «Профессия» / «Личные интересы» / «Опыт» / «Итог».
- Подсказки-действия формулируются инфинитивом («Добавить броню», «Передать или убрать предмет»), а не калькой с английского.
- Статусы персонажа — краткие прилагательные/причастия в мужском роде, как в остальных статусах Foundry.
- HTML-разметка в подсказках (`<br>`, `<label>`, `<ul>`) сохраняется без изменений — её ожидают шаблоны `.hbs`.
- Названия навыков, профессий и архетипов сюда не входят: они приходят из документов CoCID (`i.skill.*`,
  `i.occupation.*`, `i.archetype.*`) и требуют отдельного content-пака.

## Согласованные термины

| Ключ | English | Штатный русский | В модуле | Статус |
|---|---|---|---|---|
| `CoC7.AddArmor` | Add armor | — (отсутствует) | Добавить броню | нет ключа |
| `CoC7.ClearExperiencePackageName` | Clear Experience Package name | — (отсутствует) | Сбросить пакет опыта | нет ключа |
| `CoC7.DeleteBookProgress` | Remove book progress | — (отсутствует) | Удалить прогресс изучения книги | нет ключа |
| `CoC7.ExperiencePackageSkill` | Experience Package Skill | — (отсутствует) | Навык из пакета опыта | нет ключа |
| `CoC7.SkillExperiencePackage` | Experience Package | — (отсутствует) | Пакет опыта | нет ключа |
| `CoC7.ModifiedByActiveEffect` | This is modified by an Active Effect and can not be edited directly | — (отсутствует) | Значение изменено активным эффектом и недоступно для прямого редактирования | нет ключа |
| `CoC7.ActorDataLinked` | Actor data are linked | Данные персонажа связаны | Данные персонажа связаны | без изменений |
| `CoC7.ActorDataNotLinked` | Actor data are NOT linked | Данные персонажа НЕ связаны | Данные персонажа не связаны | уточнено |
| `CoC7.ActorIsSyntheticActor` | Actor is a synthetic actor (instance of an actor) | Персонаж является синтетическим персонажем (экземпляром персонажа) | Это синтетический персонаж | уточнено |
| `CoC7.ActorIsTokenHint` | Actor is a token | Персонаж является токеном | Персонаж используется как токен | уточнено |
| `CoC7.AddSanityLossEncounter` | Add Sanity Loss Encounter | Добавить встречу с потерей рассудка | Добавить событие потери рассудка | уточнено |
| `CoC7.DeleteSanityLossEncounter` | Delete Sanity Loss Encounter | Удалить встречу с потерей рассудка | Удалить событие потери рассудка | уточнено |
| `CoC7.AddSanityLossImmunity` | Add Sanity Loss Immunity | Добавить иммунитет к потере рассудка | Добавить невосприимчивость к потере рассудка | уточнено |
| `CoC7.DeleteSanityLossImmunity` | Delete Sanity Loss Immunity | Удалить иммунитет к потере рассудка | Удалить невосприимчивость к потере рассудка | уточнено |
| `CoC7.SanityLossImmunity` | Sanity loss immunity | Иммунитет к потере рассудка | Невосприимчивость к потере рассудка | уточнено |
| `CoC7.BackgroundFlagsMythosExperienced` | 5% Insanity Mythos Awarded | 5% безумия Мифоса награждены | Получено 5% навыка «Мифы Ктулху» за безумие | уточнено |
| `CoC7.BackgroundFlagsMythosHardened` | Mythos Hardened | Мифос закален | Закалён Мифами Ктулху | уточнено |
| `CoC7.CriticalWounds` | Major Wound | Серьезное ранение | Тяжёлая рана | уточнено |
| `CoC7.Dead` | Dead | Мертв | Мёртв | уточнено |
| `CoC7.Dying` | Dying | Умирает | При смерти | уточнено |
| `CoC7.Prone` | Prone | Лежа | Сбит с ног | уточнено |
| `CoC7.Unconscious` | Unconscious | Без сознания | Без сознания | без изменений |
| `CoC7.AutoCreditValues` | Toggle Automatic calculation | Переключить автоматический расчет | Включить или выключить автоматический расчёт | уточнено |
| `CoC7.DailySanIconOver` | Reset | Сброс | Сбросить | уточнено |
| `CoC7.NoSkill` | No skill | Нет навыка | Навык не назначен | уточнено |
| `CoC7.Reload` | Left/Right click : add/remove 1 bullet<br>Shift + Left/Right click : Reload/Empty | Левый/Правый клик : добавить/убрать 1 пулю Shift + Левый/Правый клик : Перезарядить/Опустошить | ЛКМ/ПКМ: добавить или убрать 1 патрон<br>Shift + ЛКМ/ПКМ: перезарядить или разрядить оружие | уточнено |
| `CoC7.SkillBase` | Base | Базовое | Базовое значение | уточнено |
| `CoC7.SkillDetail` | Detail | Деталь | Сведения о навыке | уточнено |
| `CoC7.SkillExperience` | Experience | Опыт | Опыт | без изменений |
| `CoC7.SkillOccupation` | Occupation | Профессия | Профессия | без изменений |
| `CoC7.SkillPersonal` | Personal | Личное | Личные интересы | уточнено |
| `CoC7.Value` | Value | Значение | Итог | уточнено |
| `CoC7.TradeItem` | Trade / Store Item | Обменять / Хранить предмет | Передать или убрать предмет | уточнено |
| `CoC7.OccupationSkill` | Occupation Skill | Навык профессии | Профессиональный навык | уточнено |
| `CoC7.ArchetypeSkill` | Archetype Skill | Навык архетипа | Навык архетипа | без изменений |
| `CoC7.ToolTipAutoToggle` | <label>Automatic calculation toggle</label><ul><li><strong>Left click</strong> Toggle automatic calculation / manual entry</li> | <label>Переключатель автоматического расчета</label><ul><li><strong>Левый клик</strong> Переключить автоматический расчет / ручной ввод</li> | <label>Переключатель автоматического расчёта</label><ul><li><strong>ЛКМ</strong>: переключить между автоматическим расчётом и ручным вводом</li></ul> | уточнено |
| `CoC7.ToolTipDB` | <label>Damage Bonus</label><ul><li><strong>Left click</strong> Immediate roll</li></ul> | <label>Бонус к урону</label><ul><li><strong>Левый клик</strong> Немедленный бросок</li></ul> | <label>Бонус к урону</label><ul><li><strong>ЛКМ</strong>: немедленно бросить кубики</li></ul> | уточнено |
