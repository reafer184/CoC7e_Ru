# Редакционные примечания к coc7-ru-fixes

Модуль не изменяет файлы системы CoC7. Он перекрывает интерфейсные ключи `CoC7.*`, которые используются мастером создания сыщика (`apps/investigator-wizard`) и листом Investigator (`actors/investigator-v3`).

## Сводка

- Всего ключей в модуле: **731**
- Отсутствовали в штатном русском словаре системы: **21**
- Переформулированы относительно штатного перевода: **134**
- Совпадают со штатным переводом и закреплены намеренно: **81**

Источник сверки — `static/lang/en.json` и `static/lang/ru.json` upstream-проекта [CoC7-FoundryVTT](https://github.com/Miskatonic-Investigative-Society/CoC7-FoundryVTT) и экспорт `source/coc7-ru-full-source.json`.

## Терминология

| Английский термин | Принятый вариант | Обоснование |
| --- | --- | --- |
| Investigator | сыщик | тип героя CoC7; «персонаж» оставлен для общесистемных сообщений |
| Investigator Creation Wizard | Мастер создания сыщика | единый заголовок всех шагов |
| Keeper | Хранитель | устоявшийся перевод |
| Characteristics | Характеристики | STR/CON/… — базовые |
| Attributes | Производные характеристики | ОЗ, ОМ, Удача, Рассудок, БУ, телосложение |
| Setup | Набор правил | CoCID `i.setup.*` задаёт эпоху и навыки по умолчанию |
| Occupation | Профессия | — |
| Occupation skill points | Очки профессиональных навыков | было «Очки навыков профессии» |
| Personal interest points | Очки личных интересов | — |
| Archetype | Архетип | Pulp Cthulhu |
| Credit Rating | Средства | так на официальном листе сыщика (короткая графа) |
| Experience package | Пакет опыта | — |
| Hit Points / HP | Пункты здоровья / ПЗ | как в официальном издании |
| Magic Points / MP | Пункты магии / ПМ | как в официальном издании |
| Damage Bonus / DB | Бонус к урону / БкУ | сокращение с официального листа; согласовано с «+БкУ», «+БкУ/2» |
| Move rate / Mov | Скорость / СКО | сокращение с официального листа |
| Major Wound | Серьёзная рана | формулировка официального листа |
| Dying | При смерти | вместо «Умирает» |
| Prone | Сбит с ног | вместо «Лежа» |
| Sanity loss immunity | Невосприимчивость к потере рассудка | вместо «иммунитет» |
| Sanity Loss Encounter | Событие потери рассудка | вместо «встреча» |
| Indefinite insanity | Бессрочное безумие | чекбокс официального листа |
| Mythos Hardened | Закалён Мифами Ктулху | вместо «Мифос закален» |
| Mythos Experienced | Начислено 5% к «Мифам Ктулху» за безумие | раскрыт смысл флага |
| Uncommon skills | Редкие навыки | вместо «нечастые навыки» |
| Status | Состояние | вместо «Статус» — речь о состояниях персонажа |
| Pronoun | Местоимение | в upstream поле переименовано из Sex |
| Left/Right click | ЛКМ/ПКМ | единый стиль подсказок |
| Build | Комплекция (Компл.) | «Телосложение» закреплено за SIZ (ТЕЛ) |
| Push roll | Повторная проверка | формулировка официального листа вместо «продавить бросок» |
| Spot Hidden | Внимание | официальное издание |
| Fast Talk | Красноречие | официальное издание (Charm — «Обаяние») |
| Characteristics abbr. | СИЛ ВЫН ТЕЛ ЛВК НАР ИНТ МОЩ ОБР | сокращения официального листа |

## Новые ключи (21) — в штатном ru.json отсутствуют

| Ключ | Английский | В модуле | Где используется |
| --- | --- | --- | --- |
| `CoC7.ActorConfig.NaturalHealing` | Natural Healing Per Day | Естественное восстановление за день | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.AddArmor` | Add armor | Добавить броню | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.BookProgressSummary` | {fullStudies} ({currentPercent}%) | {fullStudies} ({currentPercent}%) | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.ClearExperiencePackageName` | Clear Experience Package name | Сбросить название пакета опыта | actors/investigator-v3/parts/biography.hbs |
| `CoC7.DeleteBookProgress` | Remove book progress | Удалить прогресс изучения книги | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.ExperiencePackageSkill` | Experience Package Skill | Навык из пакета опыта | actors/investigator-v3/tabs/development.hbs |
| `CoC7.Idea` | Idea | Идея | actors/investigator-v3/parts/attributes-derived.hbs |
| `CoC7.InvestigatorWizard.ChooseAfterRoll` | Choose where to place rolled characteristics | Распределить выпавшие значения характеристик вручную | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.PersonalDescription` | Personal Description | Описание внешности |  |
| `CoC7.Know` | Know | Знание | actors/investigator-v3/parts/attributes-derived.hbs |
| `CoC7.Lck` | Lck | Удача | actors/investigator-v3/parts/attributes-secondary.hbs |
| `CoC7.ModifiedByActiveEffect` | This is modified by an Active Effect and can not be edited directly | Значение изменено активным эффектом и недоступно для прямого редактирования | actors/investigator-v3/parts/attributes-derived.hbs, actors/investigator-v3/parts/attributes-primary.hbs, actors/investigator-v3/parts/attributes-secondary.hbs |
| `CoC7.PortraitOptions` | Portrait Options | Настройки портрета | actors/investigator-v3/tabs/portrait-config.hbs |
| `CoC7.RollDamageRange` | Range {range} yards | Дистанция {range} ярдов | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.SheetExperiencePackageName` | Experience | Опыт | actors/investigator-v3/parts/biography.hbs |
| `CoC7.SkillExperiencePackage` | Experience Package | Пакет опыта | actors/investigator-v3/tabs/development.hbs |
| `CoC7.SkillTotalExperiencePackagePoints` | Experience Package points | Очки пакета опыта | actors/investigator-v3/tabs/development.hbs |
| `CoC7.UseLuck` | Use Luck | Использовать Удачу | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.UseLuckForAvoidDeath` | Spend {luck} luck to avoid death | Потратить {luck} Удачи, чтобы избежать смерти | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.UseLuckForAvoidUnconsciousness` | Spend {luck} luck to avoid unconsciousness for one round | Потратить {luck} Удачи, чтобы не потерять сознание на один раунд | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.UseLuckForHeal` | Spend 20 luck to recover 1D6 hit points | Потратить 20 Удачи, чтобы восстановить 1D6 очков здоровья | actors/investigator-v3/tabs/possession.hbs |

## Переформулированные ключи (134)

| Ключ | Английский | Штатный русский | В модуле | Где используется |
| --- | --- | --- | --- | --- |
| `CoC7.ActorIsSyntheticActor` | Actor is a synthetic actor (instance of an actor) | Персонаж является синтетическим персонажем (экземпляром персонажа) | Это синтетический персонаж (экземпляр персонажа) | actors/investigator-v3/parts/sheet-extras.hbs |
| `CoC7.ActorIsTokenHint` | Actor is a token | Персонаж является токеном | Персонаж используется как токен | actors/investigator-v3/parts/sheet-extras.hbs |
| `CoC7.AddSanityLossEncounter` | Add Sanity Loss Encounter | Добавить встречу с потерей рассудка | Добавить событие потери рассудка | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.AddSanityLossImmunity` | Add Sanity Loss Immunity | Добавить иммунитет к потере рассудка | Добавить невосприимчивость к потере рассудка | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.AnySpecName` | Any | Любое | Любая | investigator-wizard.js |
| `CoC7.AutoCreditValues` | Toggle Automatic calculation | Переключить автоматический расчет | Включить или выключить автоматический расчёт | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.BackgroundEncounters` | Losses from Strange Entities | Потери от странных сущностей | Столкновения со странными существами | actors/investigator-v3/tabs/background.hbs |
| `CoC7.BackgroundFlags` | Flags | Флаги | Отметки | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.BackgroundFlagsMythosExperienced` | 5% Insanity Mythos Awarded | 5% безумия Мифоса награждены | Начислено 5% к «Мифам Ктулху» за безумие | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.BackgroundFlagsMythosHardened` | Mythos Hardened | Мифос закален | Закалён Мифами Ктулху | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.BackgroundNewSection` | Add new section | Добавить новый раздел | Добавить раздел | actors/investigator-v3/tabs/background.hbs |
| `CoC7.BonusDamage` | Bonus Damage | Бонусный урон | Бонус к урону | investigator-wizard.js |
| `CoC7.ClearAllConditions` | Clear All Conditions | Очистить все условия | Снять все состояния | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.CreditOutOfRange` | Credit rating should be between {min} and {max} | Рейтинг кредита должен быть между {min} и {max} | Кредитоспособность должна быть от {min} до {max} | apps/investigator-wizard/points-skills.hbs |
| `CoC7.CriticalWounds` | Major Wound | Серьезное ранение | Тяжёлая рана | actors/investigator-v3/parts/portrait-frame.hbs |
| `CoC7.DB` | DB | БкУ | БУ | actors/investigator-v3/parts/attributes-derived.hbs |
| `CoC7.DailyLoss` | Daily | Ежедневно | За день | actors/investigator-v3/parts/attributes-derived.hbs |
| `CoC7.DailySanIconOver` | Reset | Сброс | Сбросить | actors/investigator-v3/parts/attributes-derived.hbs |
| `CoC7.Dead` | Dead | Мертв | Мёртв | actors/investigator-v3/parts/portrait-frame.hbs |
| `CoC7.DeleteSanityLossEncounter` | Delete Sanity Loss Encounter | Удалить встречу с потерей рассудка | Удалить событие потери рассудка | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.DeleteSanityLossImmunity` | Delete Sanity Loss Immunity | Удалить иммунитет к потере рассудка | Удалить невосприимчивость к потере рассудка | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.DevFailure` | {item} NOT upgraded ({die}/{score}%) | {item} НЕ улучшен ({die}/{score}%) | {item}: развитие не удалось ({die}/{score}%) | investigator-wizard.js |
| `CoC7.DevSuccess` | {item} upgraded ({die}/{score}%) by {augment}% | {item} улучшен ({die}/{score}%) на {augment}% | {item}: развитие удалось ({die}/{score}%), прибавка {augment}% | investigator-wizard.js |
| `CoC7.Dying` | Dying | Умирает | При смерти | actors/investigator-v3/parts/portrait-frame.hbs |
| `CoC7.DyingCheck` | Check if you'll die immediately | Проверьте, умрете ли вы сразу | Проверить, погибнет ли сыщик немедленно | actors/investigator-v3/parts/portrait-frame.hbs |
| `CoC7.EditItem` | Edit item | Редактировать предмет | Изменить предмет | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.EditSkill` | Edit skill | Редактировать навык | Изменить навык | actors/investigator-v3/tabs/combat.hbs, actors/investigator-v3/tabs/skills.hbs |
| `CoC7.EditWeapon` | Edit Weapon | Редактировать оружие | Изменить оружие | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.EmptyCharacterSkillList` | Add a setup, occupation, or skill by dropping it here. | Добавьте настройку, профессию или навык, перетащив их сюда. | Перетащите сюда набор правил, профессию или навык, чтобы добавить их. | actors/investigator-v3/tabs/skills.hbs |
| `CoC7.HP` | HP | ПЗ | ОЗ | actors/investigator-v3/parts/attributes-secondary.hbs |
| `CoC7.HitPoints` | Hit Points | Пункты здоровья | Очки здоровья | investigator-wizard.js |
| `CoC7.IndefiniteInsanity` | Indefinite insanity | Неопределенное безумие | Долговременное безумие | actors/investigator-v3/parts/portrait-frame.hbs |
| `CoC7.InventoryIsCurrentlyEmpty` | Inventory is currently empty. | Инвентарь в настоящее время пуст. | Снаряжение пока пусто. | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.InvestigatorWizard.AddBonusPointsToSkills` | <strong>Add {bonusPoints} bonus skill points divided among any of the following skills:</strong> {skills} | <strong>Добавьте {bonusPoints} бонусных очков навыков, разделенных между любыми из следующих навыков:</strong> {skills} | <strong>Распределите {bonusPoints} дополнительных очков навыков между любыми из перечисленных навыков:</strong> {skills} | apps/investigator-wizard/select-archetype.hbs |
| `CoC7.InvestigatorWizard.AgeRange` | Age (15-89): | Возраст (15-89): | Возраст (15–89): | apps/investigator-wizard/set-characteristics.hbs |
| `CoC7.InvestigatorWizard.AllowRerolls` | Allow characteristics to be rerolled | Разрешить переброску характеристик | Разрешить переброс характеристик | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.ArchetypeCounts` | You currently have {count} archetypes. The system comes with a default archetypes with a CoC ID set. You can add more archetypes with valid CoC ID values using the header on then archetypes item sheet. Compendiums with these values set will automatically be added to the available list. | У вас есть {count} архетипов. Система поставляется с архетипами по умолчанию с установленным CoC ID. Вы можете добавить больше архетипов с действительными значениями CoC ID, используя заголовок на листе элемента архетипа. Справочники с установленными этими значениями будут автоматически добавлены в доступный список. | Сейчас доступно архетипов: {count}. В системе есть архетип по умолчанию с заданным CoC ID. Добавить свои архетипы можно, указав корректный CoC ID в заголовке листа архетипа. Компендиумы с заданными значениями попадают в список доступных автоматически. | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.ArchetypeDefaultSkills` | All {count} of the following skill(s) | Все {count} из следующих навыков | Все перечисленные навыки ({count}) | apps/investigator-wizard/set-archetype-skills.hbs |
| `CoC7.InvestigatorWizard.ArchetypeOptionalSkills` | Check with your keeper before selecting the following skills | Согласуйте с вашим Хранителем, прежде чем выбирать следующие навыки | Согласуйте с Хранителем, прежде чем выбирать эти навыки | apps/investigator-wizard/set-archetype-skills.hbs |
| `CoC7.InvestigatorWizard.ArchetypePage` | Selecting your character archetype will set additional default skills on your character sheet. | Выбор вашего архетипа персонажа установит дополнительные навыки по умолчанию на вашем листе персонажа. | Выбор архетипа добавит в лист сыщика дополнительные навыки по умолчанию. | apps/investigator-wizard/select-archetype.hbs |
| `CoC7.InvestigatorWizard.ArchetypeSelect` | Select your archetype | Выберите ваш архетип | Выберите архетип | apps/investigator-wizard/select-archetype.hbs |
| `CoC7.InvestigatorWizard.Archetypes` | Pulp Archetypes | Пульп-архетипы | Архетипы Pulp Cthulhu | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.ChangingEraDelay` | Changing era please wait | Изменение эпохи, пожалуйста, подождите | Меняем эпоху, подождите | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.CharacterAvatarImage` | Avatar Image | Изображение аватара | Портрет | apps/investigator-wizard/set-investigator.hbs |
| `CoC7.InvestigatorWizard.CharacterTokenImage` | Token Image | Изображение жетона | Изображение токена | apps/investigator-wizard/set-investigator.hbs |
| `CoC7.InvestigatorWizard.CharacteristicDragInformation` | Drag your characteristics | Перетащите свои характеристики | Перетащите значения характеристик | apps/investigator-wizard/set-characteristics.hbs |
| `CoC7.InvestigatorWizard.CreateInstructions` | Click create to create your character. You Keeper needs to be online for the character to be created. | Нажмите создать, чтобы создать своего персонажа. Ваш Хранитель должен быть в сети, чтобы персонаж был создан. | Нажмите «Создать», чтобы создать сыщика. Хранитель должен быть в сети, иначе персонаж не будет создан. | apps/investigator-wizard/create.hbs |
| `CoC7.InvestigatorWizard.CreatingInvestigator` | Please wait while the keeper creates your investigator. | Пожалуйста, подождите, пока Хранитель создает вашего исследователя. | Подождите, Хранитель создаёт вашего сыщика. | investigator-wizard.js |
| `CoC7.InvestigatorWizard.DeductPointsFromCharacteristics` | Deduct {total} points among {from} | Вычтите {total} очков среди {from} | Вычтите {total} очков из характеристик: {from} | apps/investigator-wizard/set-attributes.hbs |
| `CoC7.InvestigatorWizard.EnforcePointBuy` | Enforce point buy | Принудительно использовать покупку очков | Обязательное распределение очков | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.Introduction` | The Investigator Creation Wizard is a step-by-step process for creating a brand-new investigator. | Мастер создания исследователя - это пошаговый процесс создания нового исследователя. | Мастер создания сыщика проведёт вас по всем шагам создания нового персонажа. | apps/investigator-wizard/introduction.hbs |
| `CoC7.InvestigatorWizard.IntroductionKeeper` | Your world is set to the "{era}" era this can be changed under settings or on the next page. | Ваш мир установлен на эпоху "{era}". Это можно изменить в настройках или на следующей странице. | В вашем мире выбрана эпоха «{era}». Её можно изменить в настройках или на следующем шаге. | apps/investigator-wizard/introduction.hbs |
| `CoC7.InvestigatorWizard.MakeEDUImprovementCheck` | Make an improvement check for EDU | Сделайте проверку на улучшение EDU | Сделайте проверку роста ОБР | apps/investigator-wizard/set-attributes.hbs |
| `CoC7.InvestigatorWizard.MakeEDUImprovementChecks` | Make {total} improvement checks for EDU | Сделайте {total} проверок на улучшение EDU | Сделайте проверок роста ОБР: {total} | apps/investigator-wizard/set-attributes.hbs |
| `CoC7.InvestigatorWizard.OccupationCounts` | You currently have {count} occupations. The system comes with a default occupation with a CoC ID set. You can add more occupations with valid CoC ID values using the header on then occupation item sheet. Compendiums with these values set will automatically be added to the available list. | У вас есть {count} профессий. Система поставляется с профессией по умолчанию с установленным CoC ID. Вы можете добавить больше профессий с действительными значениями CoC ID, используя заголовок на листе элемента профессии. Справочники с установленными этими значениями будут автоматически добавлены в доступный список. | Сейчас доступно профессий: {count}. В системе есть профессия по умолчанию с заданным CoC ID. Добавить свои профессии можно, указав корректный CoC ID в заголовке листа профессии. Компендиумы с заданными значениями попадают в список доступных автоматически. | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.OccupationCreditRating` | Credit Rating | Кредитный рейтинг | Кредитоспособность | apps/investigator-wizard/select-occupation.hbs |
| `CoC7.InvestigatorWizard.OccupationDefaultSkills` | All {count} of the following skill(s) | Все {count} из следующих навыков | Все перечисленные навыки ({count}) | apps/investigator-wizard/set-occupation-skills.hbs |
| `CoC7.InvestigatorWizard.OccupationPage` | Occupations give you a set of bonus points to split between eight skills and credit rating | Профессии дают вам набор бонусных очков, которые можно разделить между восьмью навыками и кредитным рейтингом | Профессия даёт запас очков, которые распределяются между восемью навыками и кредитоспособностью | apps/investigator-wizard/select-occupation.hbs |
| `CoC7.InvestigatorWizard.OccupationPersonalThisMany` | {count} personal skill(s) | {count} личных навыков | Личные навыки: {count} | apps/investigator-wizard/select-occupation.hbs |
| `CoC7.InvestigatorWizard.OccupationPickThisMany` | {count} of the following skill(s) | {count} из следующих навыков | Выберите {count} из перечисленных навыков | apps/investigator-wizard/select-occupation.hbs, apps/investigator-wizard/set-occupation-skills.hbs |
| `CoC7.InvestigatorWizard.OccupationSelect` | Select your occupation | Выберите вашу профессию | Выберите профессию | apps/investigator-wizard/select-occupation.hbs |
| `CoC7.InvestigatorWizard.OccupationSkillPoints` | Occupation Skill Points | Очки навыков профессии | Очки профессиональных навыков | apps/investigator-wizard/select-occupation.hbs |
| `CoC7.InvestigatorWizard.OccupationSkills` | Occupation Skills | Навыки профессии | Профессиональные навыки | apps/investigator-wizard/select-occupation.hbs |
| `CoC7.InvestigatorWizard.OtherPlayerOwnership` | Default permission level for players that did not create this investigator | Уровень разрешения по умолчанию для игроков, которые не создавали этого исследователя | Права по умолчанию для игроков, которые не создавали этого сыщика | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.PlayerEnabled` | Allow players without actor creation permission to create investigators | Разрешить игрокам без разрешения на создание актеров создавать исследователей | Разрешить создавать сыщиков игрокам без права создавать персонажей | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.PlayerQuantity` | How many investigators can one player have ownership of? | Сколько исследователей может иметь один игрок? | Сколько сыщиков может принадлежать одному игроку? | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.QuickFireValues` | Quick fire characteristics values | Быстрые значения характеристик | Быстрый ввод значений характеристик | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.RollTwiceForLuck` | Roll a second time for luck | Бросьте еще раз за удачу | Бросать кубики для Удачи второй раз | investigator-wizard.js, apps/investigator-wizard/set-attributes.hbs |
| `CoC7.InvestigatorWizard.SetupAny` | No default | Без настройки | Без значения по умолчанию | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.SetupCounts` | You currently have {count} setup options. It is recommended you set a single setup for all your players to set the default skills on your character sheet. The system comes with a default setup with a CoC ID set. You can add more setups with valid CoC ID values using the header on then setup item sheet. Compendiums with these values set will automatically be added to the available list. | У вас есть {count} варианта настройки. Рекомендуется установить одну настройку для всех ваших игроков, чтобы задать навыки по умолчанию на вашем листе персонажа. Система поставляется с настройкой по умолчанию с установленным CoC ID. Вы можете добавить больше настроек с действительными значениями CoC ID, используя заголовок на листе элемента настройки. Справочники с установленными этими значениями будут автоматически добавлены в доступный список. | Сейчас доступно наборов правил: {count}. Рекомендуется задать один набор для всех игроков, чтобы определить навыки по умолчанию в листе сыщика. В системе есть набор по умолчанию с заданным CoC ID. Добавить свои наборы можно, указав корректный CoC ID в заголовке листа набора. Компендиумы с заданными значениями попадают в список доступных автоматически. | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.SetupPage` | Selecting your era will set the default skills on your character sheet. | Выбор вашей эпохи установит навыки по умолчанию на вашем листе персонажа. | Выбор эпохи задаст навыки по умолчанию в листе сыщика. | apps/investigator-wizard/select-setup.hbs |
| `CoC7.InvestigatorWizard.SetupSelect` | Select your investigator setup | Выберите настройку исследователя | Выберите набор правил для сыщика | apps/investigator-wizard/configuration.hbs, apps/investigator-wizard/select-setup.hbs |
| `CoC7.InvestigatorWizard.SkillSpendArchetypeCountIncorrect` | You have selected {count} of {max} archetype skills, check with your Keeper before removing standard archetype skills. | Вы выбрали {count} из {max} навыков архетипа, согласуйте с вашим Хранителем, прежде чем удалять стандартные навыки архетипа. | Выбрано {count} из {max} навыков архетипа. Согласуйте с Хранителем, прежде чем убирать стандартные навыки архетипа. | apps/investigator-wizard/set-archetype-skills.hbs |
| `CoC7.InvestigatorWizard.SkillSpendArchetypePoints` | Archetype points {count} of {total} remaining {remaining} | Очки архетипа {count} из {total} осталось {remaining} | Очки архетипа: {count} из {total}, осталось {remaining} | apps/investigator-wizard/points-skills.hbs |
| `CoC7.InvestigatorWizard.SkillSpendInterestPoints` | Personal interest points {count} of {total} remaining {remaining} | Очки личных интересов {count} из {total} осталось {remaining} | Очки личных интересов: {count} из {total}, осталось {remaining} | apps/investigator-wizard/points-skills.hbs |
| `CoC7.InvestigatorWizard.SkillSpendOccupationCountIncorrect` | You have selected {count} of {max} occupation skills, check with your Keeper before removing standard occupation skills. | Вы выбрали {count} из {max} навыков профессии, проверьте с вашим Хранителем, прежде чем удалять стандартные навыки профессии. | Выбрано {count} из {max} профессиональных навыков. Согласуйте с Хранителем, прежде чем убирать стандартные навыки профессии. | apps/investigator-wizard/set-occupation-skills.hbs |
| `CoC7.InvestigatorWizard.SkillSpendOccupationPoints` | Occupation skill points {count} of {total} remaining {remaining} | Очки навыков профессии {count} из {total} осталось {remaining} | Очки профессиональных навыков: {count} из {total}, осталось {remaining} | apps/investigator-wizard/points-skills.hbs |
| `CoC7.InvestigatorWizard.SuggestedOccupations` | <strong>Suggested Occupations:</strong> {suggested} | <strong>Предлагаемые профессии:</strong> {suggested} | <strong>Подходящие профессии:</strong> {suggested} | apps/investigator-wizard/select-archetype.hbs |
| `CoC7.InvestigatorWizard.SuggestedTraits` | <strong>Suggested Traits:</strong> {suggested} | <strong>Предлагаемые черты:</strong> {suggested} | <strong>Подходящие черты:</strong> {suggested} | apps/investigator-wizard/select-archetype.hbs |
| `CoC7.InvestigatorWizard.Title` | Investigator Creation Wizard | Мастер создания исследователя | Мастер создания сыщика | investigator-wizard.js, apps/investigator-wizard/introduction.hbs |
| `CoC7.InvestigatorWizard.TitleAttributes` | Attributes | Атрибуты | Производные характеристики | apps/investigator-wizard/view-attributes.hbs |
| `CoC7.InvestigatorWizard.TitleBackstory` | Investigator Backstory | Предыстория исследователя | Предыстория сыщика | apps/investigator-wizard/backstory.hbs |
| `CoC7.InvestigatorWizard.TitleCreate` | Create Investigator | Создать исследователя | Создание сыщика | apps/investigator-wizard/create.hbs |
| `CoC7.InvestigatorWizard.TitleDetails` | Investigator Details | Детали исследователя | Сведения о сыщике | apps/investigator-wizard/set-investigator.hbs |
| `CoC7.InvestigatorWizard.TitleKeeperConfiguration` | Keeper Configuration | Конфигурация Хранителя | Настройки Хранителя | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.TitlePointsSkills` | Spend Skill Points | Потратить очки навыков | Распределение очков навыков | apps/investigator-wizard/points-skills.hbs |
| `CoC7.InvestigatorWizard.TitleSelectSetup` | Investigator Setup | Настройка исследователя | Набор правил сыщика | apps/investigator-wizard/select-setup.hbs |
| `CoC7.InvestigatorWizard.UseSetupMethod` | Use method from setup item | Использовать метод из элемента настройки | Использовать способ из набора правил | apps/investigator-wizard/configuration.hbs |
| `CoC7.LockActor` | Lock Actor | Заблокировать персонажа | Заблокировать лист | actors/investigator-v3/parts/sheet-extras.hbs |
| `CoC7.ManualCreditValues` | Manual Credit Values | Ручные значения кредита | Ручной ввод кредитоспособности | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.MeleeWeapons` | Melee weapons | Рукопашное оружие | Оружие ближнего боя | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.MonetaryAssets` | Assets : | Активы : | Имущество: | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.MonetaryAssetsDetails` | Assets details | Детали активов | Сведения об имуществе | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.MonetaryCash` | Cash : | Наличные : | Наличные: | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.MonetaryCreditRatingMax` | Max | Макс | Макс. | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.MonetaryCreditRatingMin` | Min | Мин | Мин. | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.MonetaryFormatTitle` | Money Format : | Формат денег : | Формат денег: | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.MonetarySpendingLevel` | Spending level : | Уровень расходов : | Уровень расходов: | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.MonetarySpent` | Spent : | Потрачено : | Потрачено: | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.MonetarySymbol` | Symbol : | Символ : | Символ: | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.MonetaryTitle` | Cash and Assets | Наличные и активы | Наличные и имущество | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.MonetaryValueAssets` | Assets | Активы | Имущество | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.Mov` | Mov | СКО | ДВ | actors/investigator-v3/parts/attributes-derived.hbs |
| `CoC7.NoSkill` | No skill | Нет навыка | Навык не назначен | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.OccupationSkill` | Occupation Skill | Навык профессии | Профессиональный навык | actors/investigator-v3/tabs/development.hbs |
| `CoC7.PossessionsNotes` | Notes : | Заметки : | Заметки: | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.Prone` | Prone | Лежа | Сбит с ног | actors/investigator-v3/parts/portrait-frame.hbs |
| `CoC7.PulpTalents` | Pulp Talents | Пульп-таланты | Таланты Pulp Cthulhu | actors/investigator-v3/tabs/development.hbs, actors/investigator-v3/tabs/possession.hbs |
| `CoC7.RangeSkills` | Range Skills | Навыки дальнего боя | Навыки стрельбы | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.RecoverLuckPoints` | Recover Luck Points | Восстановить очки удачи | Восстановить очки Удачи | actors/investigator-v3/tabs/development.hbs |
| `CoC7.Reload` | Left/Right click : add/remove 1 bullet<br>Shift + Left/Right click : Reload/Empty | Левый/Правый клик : добавить/убрать 1 пулю Shift + Левый/Правый клик : Перезарядить/Опустошить | ЛКМ/ПКМ: добавить или убрать 1 патрон<br>Shift + ЛКМ/ПКМ: перезарядить или разрядить оружие | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.RollAll4Dev` | Rolling all skills for development | Бросить все навыки для развития | Бросить все навыки на развитие | investigator-wizard.js |
| `CoC7.RollDice` | Roll ! | Бросить ! | Бросок! | apps/investigator-wizard/set-attributes.hbs, apps/investigator-wizard/set-characteristics.hbs |
| `CoC7.SanityLossEncounters` | Sanity Loss Encounters | Встречи с потерей рассудка | События потери рассудка | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.SanityLossImmunities` | Sanity Loss Immunities | Иммунитеты к потере рассудка | Невосприимчивость к потере рассудка | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.SanityLossImmunity` | Sanity loss immunity | Иммунитет к потере рассудка | Невосприимчивость к потере рассудка | actors/investigator-v3/tabs/background.hbs |
| `CoC7.Settings.WorldEra.Name` | Era for the world | Эпоха для мира | Эпоха мира | apps/investigator-wizard/configuration.hbs |
| `CoC7.Sex` | Pronoun | Пол | Местоимение | actors/investigator-v3/parts/biography.hbs |
| `CoC7.SkillBase` | Base | Базовое | Базовое значение | actors/investigator-v3/tabs/development.hbs, apps/investigator-wizard/points-skills.hbs |
| `CoC7.SkillDetail` | Detail | Деталь | Уточнение | actors/investigator-v3/tabs/combat.hbs, actors/investigator-v3/tabs/skills.hbs |
| `CoC7.SkillPersonal` | Personal | Личное | Личные интересы | actors/investigator-v3/tabs/development.hbs, apps/investigator-wizard/points-skills.hbs |
| `CoC7.SkillTotalPersonal` | Personal points | Личные очки | Очки личных интересов | actors/investigator-v3/tabs/development.hbs |
| `CoC7.SortBySkillValue` | Sort by skill percent | Сортировать по проценту навыка | Сортировать по значению навыка | actors/investigator-v3/tabs/skills.hbs |
| `CoC7.Status` | Status | Статус | Состояние | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.ToolTipAutoToggle` | <label>Automatic calculation toggle</label><ul><li><strong>Left click</strong> Toggle automatic calculation / manual entry</li> | <label>Переключатель автоматического расчета</label><ul><li><strong>Левый клик</strong> Переключить автоматический расчет / ручной ввод</li> | <label>Автоматический расчёт</label><ul><li><strong>ЛКМ</strong>: переключить автоматический расчёт и ручной ввод</li></ul> | actors/investigator-v3/parts/attributes-derived.hbs, actors/investigator-v3/parts/attributes-secondary.hbs |
| `CoC7.ToolTipDB` | <label>Damage Bonus</label><ul><li><strong>Left click</strong> Immediate roll</li></ul> | <label>Бонус к урону</label><ul><li><strong>Левый клик</strong> Немедленный бросок</li></ul> | <label>Бонус к урону</label><ul><li><strong>ЛКМ</strong>: немедленный бросок</li></ul> | actors/investigator-v3/parts/attributes-derived.hbs |
| `CoC7.ToolTipSkillFlagToggle` | <label>{status}</label><div><strong>Double Click</strong> Toggle flag status</div> | <label>{status}</label><ul><li><strong>Двойной клик</strong> Переключить статус флага</li> | <label>{status}</label><div><strong>Двойной щелчок</strong>: переключить отметку</div> | actors/investigator-v3/tabs/combat.hbs, actors/investigator-v3/tabs/skills.hbs |
| `CoC7.TradeItem` | Trade / Store Item | Обменять / Хранить предмет | Передать или убрать предмет | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.UncommonSkillsHide` | Hide uncommon skills | Скрыть нечастые навыки | Скрыть редкие навыки | actors/investigator-v3/tabs/skills.hbs |
| `CoC7.UncommonSkillsShow` | Show uncommon skills | Показать нечастые навыки | Показать редкие навыки | actors/investigator-v3/tabs/skills.hbs |
| `CoC7.UnlockActor` | Unlock Actor | Разблокировать персонажа | Разблокировать лист | actors/investigator-v3/parts/sheet-extras.hbs |
| `CoC7.Value` | Value | Значение | Итог | actors/investigator-v3/tabs/development.hbs, apps/investigator-wizard/points-skills.hbs, apps/investigator-wizard/set-characteristics.hbs |
| `CoC7.WeaponAddDb` | +DB | +ПБ | +БУ | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.WeaponAddHalfDb` | +DB/2 | +ПБ/2 | +БУ/2 | actors/investigator-v3/tabs/combat.hbs |

## Закреплённые без изменений (81)

| Ключ | Английский | Штатный русский | В модуле | Где используется |
| --- | --- | --- | --- | --- |
| `CoC7.ActorDataLinked` | Actor data are linked | Данные персонажа связаны | Данные персонажа связаны | actors/investigator-v3/parts/sheet-extras.hbs |
| `CoC7.ActorDataNotLinked` | Actor data are NOT linked | Данные персонажа НЕ связаны | Данные персонажа НЕ связаны | actors/investigator-v3/parts/sheet-extras.hbs |
| `CoC7.AddBook` | Add book | Добавить книгу | Добавить книгу | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.AddItem` | Add item | Добавить предмет | Добавить предмет | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.AddSkill` | Add skill | Добавить навык | Добавить навык | actors/investigator-v3/tabs/combat.hbs, actors/investigator-v3/tabs/skills.hbs |
| `CoC7.AddSpell` | Add spell | Добавить заклинание | Добавить заклинание | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.AddWeapon` | Add weapon | Добавить оружие | Добавить оружие | actors/investigator-v3/tabs/combat.hbs, actors/investigator-v3/tabs/possession.hbs |
| `CoC7.Age` | Age | Возраст | Возраст | actors/investigator-v3/parts/biography.hbs |
| `CoC7.Archetype` | Archetype | Архетип | Архетип | actors/investigator-v3/parts/biography.hbs |
| `CoC7.ArchetypeSkill` | Archetype Skill | Навык архетипа | Навык архетипа | actors/investigator-v3/tabs/development.hbs |
| `CoC7.Armor` | Armor | Броня | Броня | actors/investigator-v3/parts/attributes-derived.hbs, actors/investigator-v3/tabs/possession.hbs |
| `CoC7.AutomaticFire` | Automatic Fire | Автоматический огонь | Автоматический огонь | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.Background` | Backstory | Предыстория | Предыстория | actors/investigator-v3/tabs/background.hbs |
| `CoC7.BackgroundDeleteSection` | Delete section | Удалить раздел | Удалить раздел | actors/investigator-v3/tabs/background.hbs |
| `CoC7.BackgroundSectionMoveDown` | Move Down | Переместить вниз | Переместить вниз | actors/investigator-v3/tabs/background.hbs |
| `CoC7.BackgroundSectionMoveUp` | Move Up | Переместить вверх | Переместить вверх | actors/investigator-v3/tabs/background.hbs |
| `CoC7.BackgroundSectionNameHolder` | Enter section title | Введите название раздела | Введите название раздела | actors/investigator-v3/tabs/background.hbs |
| `CoC7.Birthplace` | Birthplace | Место рождения | Место рождения | actors/investigator-v3/parts/biography.hbs, apps/investigator-wizard/set-investigator.hbs |
| `CoC7.Books` | Books | Книги | Книги | actors/investigator-v3/tabs/keeper.hbs, actors/investigator-v3/tabs/possession.hbs |
| `CoC7.BoutOfMadness` | Bout of madness | Приступ безумия | Приступ безумия | actors/investigator-v3/parts/portrait-frame.hbs |
| `CoC7.Build` | Build | Телосложение | Телосложение | investigator-wizard.js, actors/investigator-v3/parts/attributes-derived.hbs |
| `CoC7.Characteristics` | Characteristics | Характеристики | Характеристики | apps/investigator-wizard/configuration.hbs |
| `CoC7.CharacteristicsPoints` | Characteristics points | Очки характеристик | Очки характеристик | apps/investigator-wizard/configuration.hbs, apps/investigator-wizard/set-attributes.hbs, apps/investigator-wizard/set-characteristics.hbs |
| `CoC7.Combat` | Combat | Бой | Бой | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.DeleteItem` | Delete Item | Удалить предмет | Удалить предмет | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.DeleteSkill` | Delete skill | Удалить навык | Удалить навык | actors/investigator-v3/tabs/combat.hbs, actors/investigator-v3/tabs/skills.hbs |
| `CoC7.DeleteWeapon` | Delete Weapon | Удалить оружие | Удалить оружие | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.Development` | Development | Развитие | Развитие | actors/investigator-v3/tabs/development.hbs |
| `CoC7.DevelopmentPhase` | Development Phase | Фаза развития | Фаза развития | actors/investigator-v3/tabs/development.hbs |
| `CoC7.Effects` | Effects | Эффекты | Эффекты | actors/investigator-v3/tabs/active-effects.hbs |
| `CoC7.GmNotes` | Keeper's notes | Заметки Хранителя | Заметки Хранителя | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.InvestigatorWizard.BackStep` | Back | Назад | Назад | investigator-wizard.js |
| `CoC7.InvestigatorWizard.Characteristics` | Characteristic values | Значения характеристик | Значения характеристик | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.CoreCharacteristicName` | <strong>Core characteristic:</strong> {coreCharacteristic}. | <strong>Основная характеристика:</strong> {coreCharacteristic}. | <strong>Основная характеристика:</strong> {coreCharacteristic}. | apps/investigator-wizard/select-archetype.hbs, apps/investigator-wizard/set-characteristics.hbs |
| `CoC7.InvestigatorWizard.CoreCharacteristicSelect` | Archetype core characteristic | Основная характеристика архетипа | Основная характеристика архетипа | apps/investigator-wizard/set-characteristics.hbs |
| `CoC7.InvestigatorWizard.CreateStep` | Create | Создать | Создать | investigator-wizard.js |
| `CoC7.InvestigatorWizard.NextStep` | Next | Далее | Далее | investigator-wizard.js |
| `CoC7.InvestigatorWizard.Occupations` | Occupations | Профессии | Профессии | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.ReducePointsFromCharacteristic` | Reduce {from} by {total} | Уменьшите {from} на {total} | Уменьшите {from} на {total} | apps/investigator-wizard/set-attributes.hbs |
| `CoC7.InvestigatorWizard.Setups` | Character sheets | Листы персонажей | Листы персонажей | apps/investigator-wizard/configuration.hbs |
| `CoC7.InvestigatorWizard.TitleAdjustCharacteristics` | Adjust Characteristics | Корректировка характеристик | Корректировка характеристик | apps/investigator-wizard/set-attributes.hbs |
| `CoC7.InvestigatorWizard.TitleArchetypeSkills` | Archetype Skills | Навыки архетипа | Навыки архетипа | apps/investigator-wizard/set-archetype-skills.hbs |
| `CoC7.InvestigatorWizard.TitleCharacteristics` | Characteristics | Характеристики | Характеристики | apps/investigator-wizard/set-characteristics.hbs |
| `CoC7.InvestigatorWizard.TitleOccupationSkills` | Occupation Skills | Профессиональные навыки | Профессиональные навыки | apps/investigator-wizard/set-occupation-skills.hbs |
| `CoC7.InvestigatorWizard.TitleSelectArchetype` | Archetype Selection | Выбор архетипа | Выбор архетипа | apps/investigator-wizard/select-archetype.hbs |
| `CoC7.InvestigatorWizard.TitleSelectOccupation` | Occupation Selection | Выбор профессии | Выбор профессии | apps/investigator-wizard/select-occupation.hbs |
| `CoC7.Items` | Items | Предметы | Предметы | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.Luck` | Luck | Удача | Удача | investigator-wizard.js, apps/investigator-wizard/set-attributes.hbs |
| `CoC7.MP` | MP | ОМ | ОМ | actors/investigator-v3/parts/attributes-secondary.hbs |
| `CoC7.MagicPoints` | Magic Points | Очки магии | Очки магии | investigator-wizard.js |
| `CoC7.MeleeSkills` | Melee Skills | Навыки ближнего боя | Навыки ближнего боя | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.MonetaryValueCash` | Cash | Наличные | Наличные | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.MonetaryValueSpendingLevel` | Spending | Расходы | Расходы | actors/investigator-v3/tabs/keeper.hbs |
| `CoC7.Movement` | Movement | Движение | Движение | investigator-wizard.js |
| `CoC7.Name` | Name | Имя | Имя | actors/investigator-v3/parts/biography.hbs, actors/investigator-v3/tabs/keeper.hbs, apps/investigator-wizard/set-investigator.hbs |
| `CoC7.Occupation` | Occupation | Профессия | Профессия | actors/investigator-v3/parts/biography.hbs |
| `CoC7.Or` | or | или | или | investigator-wizard.js |
| `CoC7.Organization` | Organization | Организация | Организация | actors/investigator-v3/parts/biography.hbs |
| `CoC7.PlayerName` | Player | Игрок | Игрок | actors/investigator-v3/parts/biography.hbs |
| `CoC7.Possessions` | Gear & Cash | Снаряжение и деньги | Снаряжение и деньги | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.PossessionsNotesHolder` | Notes | Заметки | Заметки | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.RangeWeapons` | Range weapons | Дальнобойное оружие | Дальнобойное оружие | actors/investigator-v3/tabs/combat.hbs |
| `CoC7.ResetArchetype` | Reset Archetype | Сбросить архетип | Сбросить архетип | actors/investigator-v3/parts/biography.hbs |
| `CoC7.ResetOccupation` | Reset Occupation | Сбросить профессию | Сбросить профессию | actors/investigator-v3/parts/biography.hbs |
| `CoC7.Residence` | Residence | Место жительства | Место жительства | actors/investigator-v3/parts/biography.hbs, apps/investigator-wizard/set-investigator.hbs |
| `CoC7.SAN` | SAN | РАС | РАС | actors/investigator-v3/parts/attributes-secondary.hbs |
| `CoC7.Sanity` | Sanity | Рассудок | Рассудок | investigator-wizard.js |
| `CoC7.SkillArchetype` | Archetype | Архетип | Архетип | actors/investigator-v3/tabs/development.hbs, apps/investigator-wizard/points-skills.hbs |
| `CoC7.SkillExperience` | Experience | Опыт | Опыт | actors/investigator-v3/tabs/development.hbs |
| `CoC7.SkillOccupation` | Occupation | Профессия | Профессия | actors/investigator-v3/tabs/development.hbs, apps/investigator-wizard/points-skills.hbs |
| `CoC7.SkillTotalArchetype` | Archetype points | Очки архетипа | Очки архетипа | actors/investigator-v3/tabs/development.hbs |
| `CoC7.SkillTotalExperience` | Experience points | Очки опыта | Очки опыта | actors/investigator-v3/tabs/development.hbs |
| `CoC7.SkillTotalOccupation` | Occupation points | Очки профессии | Очки профессии | actors/investigator-v3/tabs/development.hbs |
| `CoC7.Skills` | Skills | Навыки | Навыки | actors/investigator-v3/tabs/skills.hbs |
| `CoC7.SortBySkillName` | Sort by skill name | Сортировать по названию навыка | Сортировать по названию навыка | actors/investigator-v3/tabs/skills.hbs |
| `CoC7.Spells` | Spells | Заклинания | Заклинания | actors/investigator-v3/tabs/possession.hbs |
| `CoC7.ToolTipSkillFlagged` | Flagged for development | Отмечен для развития | Отмечен для развития | actors/investigator-v3/tabs/combat.hbs, actors/investigator-v3/tabs/skills.hbs |
| `CoC7.ToolTipSkillUnflagged` | Not flagged for development | Не отмечен для развития | Не отмечен для развития | actors/investigator-v3/tabs/combat.hbs, actors/investigator-v3/tabs/skills.hbs |
| `CoC7.Unconscious` | Unconscious | Без сознания | Без сознания | actors/investigator-v3/parts/portrait-frame.hbs |
| `CoC7.UnderlyingInsanity` | Underlying insanity | Скрытое безумие | Скрытое безумие | actors/investigator-v3/parts/portrait-frame.hbs |
| `CoC7.Weapons` | Weapons | Оружие | Оружие | actors/investigator-v3/tabs/possession.hbs |

## Что этим модулем не исправляется

- Названия и описания навыков, профессий, архетипов, наборов правил, предысторий, оружия, книг, заклинаний и талантов. Мастер подтягивает CoCID-документы (`i.skill.*`, `i.occupation.*`, `i.archetype.*`, `i.setup.*`, `rt..backstory-*`) и выводит `item.name`, поэтому UI-словарь их не переименует. Нужен отдельный content-пак `coc7-ru-content`.
- Буквальные английские строки в `.hbs`-шаблонах вида `title="Throw"`, которые не проходят через `game.i18n`. Их следует править upstream-PR или переопределением шаблона.

## Второй заход (0.3.0): остальные 488 ключей
До версии 0.3.0 модуль правил только лист сыщика и мастер создания. В 0.3.0
переведены все оставшиеся ключи `static/lang/en.json`, которых не было в
штатном русском словаре системы (или которые в нём совпадали с английским).
Итог: 1649 ключей системы — 0 без русского перевода.

### Проверки, которые прошёл этот заход
- Набор ключей совпадает с исходным списком буква-в-букву (ни добавленных, ни потерянных).
- Плейсхолдеры `{name}`, `{value}`, `{actorName}` и подобные совпадают с английским оригиналом в каждой строке.
- Ни одна строка не осталась латиницей, кроме технических: `ID`, `Foundry ID`, `Foundry UUID`, названия клавиш `Ctrl`/`Shift`, имена собственные (Chaosium, Foundry VTT, Pulp Cthulhu, Down Darker Trails).
- Пустые подсказки (`CoC7.Settings.PulpRules.*.Hint`, `ShowWorldEra.Hint`) оставлены пустыми, как в оригинале.

### Названия специализаций — сверка с паками
| Ключ | Английский | Штатный `ru.json` | Здесь | Почему |
| --- | --- | --- | --- | --- |
| `CoC7.FightingSpecializationName` | Fighting | Борьба | Ближний бой | сравнивается с `system.specialization` в `skill-system.js`, должно совпасть с паком |
| `CoC7.FirearmSpecializationName` | Firearms | Огнестрельное оружие | Стрельба | то же |
| `CoC7.RangedSpecializationName` | Ranged | — | Дальний бой | отдельное свойство `ranged`; нельзя дублировать «Стрельбу», иначе навык получит оба свойства |
| `CoC7.LanguageSpecializationName` | Language | — | Язык | используется импортёром для разбора «Язык (Родной)» |
| `CoC7.SkillNameHandgun` … `SkillNameMachineGun` | Handgun … | — | Пистолет, Винтовка, Дробовик, Винтовка/Дробовик, Пистолет-пулемёт, Пулемёт | импортёр ищет навык по собранному имени «Стрельба (Пистолет)» |

### Примеры переведённых строк
| Ключ | Английский | Русский |
| --- | --- | --- |
| `CoC7.ChaosiumCanvasInterface.Buttons.Right` | Right Mouse Button | Правая кнопка мыши |
| `CoC7.Settings.CharacteristicsOrder.Name` | Characteristics Order | Порядок характеристик |
| `CoC7.RollAsModifier.Title` | Set as roll damage or heal type | Назначить броску тип урона или лечения |
| `CoC7.Errors.UnknownAttribute` | Unknown Attribute | Неизвестный атрибут |
| `TYPES.Item.experiencePackage` | Experience Package | Пакет опыта |
| `CoC7.IdeaCheck` | Idea Roll | Бросок Идеи |
| `CoC7.SkillHintPush` | Skill can be pushed | Навык можно продавить |
| `CoC7.MythosGain` | Mythos gain | Прирост Мифов |

### Как воспроизвести список
```bash
# что осталось без русского перевода
python3 - <<'PY'
import json
def flat(d,p=''):
    for k,v in d.items():
        n=p+k
        if isinstance(v,dict): yield from flat(v,n+'.')
        else: yield n,v
en=dict(flat(json.load(open('static/lang/en.json'))))
ru=dict(flat(json.load(open('static/lang/ru.json'))))
fix=dict(flat(json.load(open('coc7-ru-fixes/lang/ru.json'))))
cont=dict(flat(json.load(open('coc7-ru-content/lang/ru.json'))))
print([k for k in en if (k not in ru and k not in fix and k not in cont) or (ru.get(k)==en[k] and k not in fix and k not in cont)])
PY
```

## Сверка с официальным русским изданием

Названия навыков, характеристик, состояний и разделов листа приведены к **официальному русскому изданию
«Зов Ктулху», 7-я редакция (Мир Хобби / Hobby World)**. Проверенные источники:

- [Лист сыщика 1920-х](https://hobbygames.ru/download/rules/call_of_cthulhu_character_sheet_00.pdf)
- [Лист из «Стартового набора»](https://hobbygames.ru/download/rules/Zov_Ktulhu_gotovie_pers.pdf)
- [Готовые сыщики «Кошмары цифровой эпохи»](https://hobbygames.ru/download/rules/zov-ktulhu-characters.pdf)
- [Лист современного сыщика](https://hobbygames.ru/download/rules/Keepers_sovremennij_Character_Sheets.pdf.pdf)
- [Готовые сыщики «Двери во тьму»](https://hobbygames.ru/download/rules/Call_of_Chtulhu/Dveri_vo_Tmu_Personazhi.pdf)
- [Материалы игроков «Маски Ньярлатхотепа»](https://hobbygames.ru/download/rules/zk-maski-njarlathotepa-materiali-igrokov.pdf)

Регистр в скобках — строчный, как в издании: `CoC7.SkillNameHandgun` = «пистолет», `CoC7.SkillOwn` = «родной».
Значения этих ключей обязаны совпадать с частью в скобках у названий навыков в паках `coc7-ru-content`,
иначе мастер создания сыщика создаст дубль навыка.
