# coc7-ru-content — заметки по переводу контента

Второй этап русификации: перевод самих CoCID-документов, а не строк интерфейса.
Плохой перевод навыка нельзя исправить словарём UI, потому что мастер создания
сыщика подставляет в интерфейс `item.name` документа, найденного по CoCID.

## Как работает переопределение

`coc7/apps/coc-id.js` → `#indexesFromCompendia` перебирает **все** паки мира
(включая модульные) и отбирает документы, у которых `flags.CoC7.cocidFlag.lang`
равен языку интерфейса или `en`. Затем `#filterByLanguage` выбрасывает
англоязычных кандидатов, если для того же CoCID есть документ на языке
интерфейса, а `#compareCoCIDPriority` сортирует остаток по `priority`.
Вывод: достаточно пака с `lang: ru` — рантайм-патчи не нужны. Приоритет у всех
документов модуля оставлен равным `0`, чтобы платный контент с более высоким
приоритетом мог перебить наш при необходимости.

## Принятая терминология

| Английский | Русский |
| --- | --- |
| Investigator | сыщик |
| Keeper | Хранитель |
| Setup | Набор правил |
| Archetype | Архетип |
| Occupation | Профессия |
| Credit Rating | Кредитоспособность |
| Cthulhu Mythos | Мифы Ктулху |
| Sanity | Рассудок |
| Bout of Madness | Приступ безумия |
| Phobia / Mania | Фобия / Мания |
| Status | Состояние |
| Backstory | Предыстория |
| Trait | Черта характера |
| Significant People | Значимые люди |
| Treasured Possessions | Дорогие вещи |
| penalty die | штрафная кость |
| POW | ВЛИ |
| Magic Points | Очки магии (ОМ) |

## Правило записи имён навыков

Сборщик системы разбирает имя навыка регулярным выражением `^(.+)\s*\((.+)\)$`:
часть до скобок становится `system.specialization`, часть в скобках —
`system.skillName`. Поэтому все специализации записаны в форме
«Специализация (Уточнение)» с заглавной буквы внутри скобок:
«Стрельба (Пистолет)» → специализация «Стрельба», навык «Пистолет».
Так лист персонажа корректно группирует навыки, а поиск «любого» навыка
(`Стрельба (Любая)`) продолжает работать.

## Навыки (103)

| CoCID | Английский | Русский |
| --- | --- | --- |
| `i.skill.accounting` | Accounting | Бухгалтерия |
| `i.skill.animal-handling` | Animal Handling | Обращение с животными |
| `i.skill.anthropology` | Anthropology | Антропология |
| `i.skill.appraise` | Appraise | Оценка |
| `i.skill.archaeology` | Archaeology | Археология |
| `i.skill.art-craft-acting` | Art/Craft (Acting) | Искусство/Ремесло (Актёрское мастерство) |
| `i.skill.art-craft-any` | Art/Craft (Any) | Искусство/Ремесло (Любое) |
| `i.skill.art-craft-fine-art` | Art/Craft (Fine Art) | Искусство/Ремесло (Изобразительное искусство) |
| `i.skill.art-craft-forgery` | Art/Craft (Forgery) | Искусство/Ремесло (Подделка) |
| `i.skill.art-craft-photography` | Art/Craft (Photography) | Искусство/Ремесло (Фотография) |
| `i.skill.charm` | Charm | Обаяние |
| `i.skill.civics` | Civics | Гражданское право |
| `i.skill.climb` | Climb | Лазание |
| `i.skill.computer-use` | Computer Use | Работа с компьютером |
| `i.skill.credit-rating` | Credit Rating | Кредитоспособность |
| `i.skill.cthulhu-mythos` | Cthulhu Mythos | Мифы Ктулху |
| `i.skill.demolitions` | Demolitions | Подрывное дело |
| `i.skill.disguise` | Disguise | Маскировка |
| `i.skill.diving` | Diving | Подводное плавание |
| `i.skill.dodge` | Dodge | Уклонение |
| `i.skill.drive-auto` | Drive Auto | Вождение (Автомобиль) |
| `i.skill.drive-carriage` | Drive Carriage | Вождение (Экипаж) |
| `i.skill.drive-horse-oxen` | Drive Horse / Oxen | Вождение (Лошади и волы) |
| `i.skill.drive-wagon-coach` | Drive Wagon / Coach | Вождение (Повозка и дилижанс) |
| `i.skill.electrical-repair` | Electrical Repair | Ремонт электрики |
| `i.skill.electronics` | Electronics | Электроника |
| `i.skill.empire` | Empire | Империя |
| `i.skill.fast-talk` | Fast Talk | Заговаривание |
| `i.skill.fighting-any` | Fighting (Any) | Ближний бой (Любой) |
| `i.skill.fighting-axe` | Fighting (Axe) | Ближний бой (Топор) |
| `i.skill.fighting-brawl` | Fighting (Brawl) | Ближний бой (Драка) |
| `i.skill.fighting-chainsaw` | Fighting (Chainsaw) | Ближний бой (Цепная пила) |
| `i.skill.fighting-flail` | Fighting (Flail) | Ближний бой (Цеп) |
| `i.skill.fighting-garrote` | Fighting (Garrote) | Ближний бой (Гаррота) |
| `i.skill.fighting-spear` | Fighting (Spear) | Ближний бой (Копьё) |
| `i.skill.fighting-sword` | Fighting (Sword) | Ближний бой (Меч) |
| `i.skill.throw` | Throw | Метание |
| `i.skill.fighting-whip` | Fighting (Whip) | Ближний бой (Кнут) |
| `i.skill.firearms-any` | Firearms (Any) | Стрельба (Любая) |
| `i.skill.firearms-artillery` | Firearms (Artillery) | Стрельба (Артиллерия) |
| `i.skill.firearms-bow` | Firearms (Bow) | Стрельба (Лук) |
| `i.skill.firearms-flamethrower` | Firearms (Flamethrower) | Стрельба (Огнемёт) |
| `i.skill.firearms-handgun` | Firearms (Handgun) | Стрельба (Пистолет) |
| `i.skill.firearms-heavy-weapons` | Firearms (Heavy Weapons) | Стрельба (Тяжёлое оружие) |
| `i.skill.firearms-machine-gun` | Firearms (Machine Gun) | Стрельба (Пулемёт) |
| `i.skill.firearms-rifle-shotgun` | Firearms (Rifle/Shotgun) | Стрельба (Винтовка/Дробовик) |
| `i.skill.firearms-submachine-gun` | Firearms (Submachine Gun) | Стрельба (Пистолет-пулемёт) |
| `i.skill.first-aid` | First Aid | Первая помощь |
| `i.skill.gambling` | Gambling | Азартные игры |
| `i.skill.history` | History | История |
| `i.skill.hypnosis` | Hypnosis | Гипноз |
| `i.skill.intimidate` | Intimidate | Запугивание |
| `i.skill.jump` | Jump | Прыжки |
| `i.skill.language-any` | Language (Any) | Язык (Любой) |
| `i.skill.language-own` | Language (Own) | Язык (Родной) |
| `i.skill.language-czech` | Language (Czech) | Язык (Чешский) |
| `i.skill.language-dutch` | Language (Dutch) | Язык (Нидерландский) |
| `i.skill.language-english` | Language (English) | Язык (Английский) |
| `i.skill.language-german` | Language (German) | Язык (Немецкий) |
| `i.skill.language-polish` | Language (Polish) | Язык (Польский) |
| `i.skill.language-russian` | Language (Russian) | Язык (Русский) |
| `i.skill.language-swahili` | Language (Swahili) | Язык (Суахили) |
| `i.skill.language-yoruba` | Language (Yoruba) | Язык (Йоруба) |
| `i.skill.language-zulu` | Language (Zulu) | Язык (Зулу) |
| `i.skill.law` | Law | Юриспруденция |
| `i.skill.library-use` | Library Use | Работа с библиотекой |
| `i.skill.listen` | Listen | Слух |
| `i.skill.locksmith` | Locksmith | Взлом замков |
| `i.skill.lore-any` | Lore (Any) | Знание (Любое) |
| `i.skill.mechanical-repair` | Mechanical Repair | Ремонт механики |
| `i.skill.medicine` | Medicine | Медицина |
| `i.skill.natural-world` | Natural World | Природа |
| `i.skill.navigate` | Navigate | Ориентирование |
| `i.skill.occult` | Occult | Оккультизм |
| `i.skill.operate-heavy-machinery` | Operate Heavy Machinery | Управление тяжёлой техникой |
| `i.skill.persuade` | Persuade | Убеждение |
| `i.skill.pilot-any` | Pilot (Any) | Пилотирование (Любое) |
| `i.skill.psychoanalysis` | Psychoanalysis | Психоанализ |
| `i.skill.psychology` | Psychology | Психология |
| `i.skill.read-lips` | Read Lips | Чтение по губам |
| `i.skill.ride` | Ride | Верховая езда |
| `i.skill.rope-use` | Rope Use | Работа с верёвкой |
| `i.skill.science-any` | Science (Any) | Наука (Любая) |
| `i.skill.science-astronomy` | Science (Astronomy) | Наука (Астрономия) |
| `i.skill.science-biology` | Science (Biology) | Наука (Биология) |
| `i.skill.science-botany` | Science (Botany) | Наука (Ботаника) |
| `i.skill.science-chemistry` | Science (Chemistry) | Наука (Химия) |
| `i.skill.science-cryptography` | Science (Cryptography) | Наука (Криптография) |
| `i.skill.science-engineering` | Science (Engineering) | Наука (Инженерное дело) |
| `i.skill.science-forensics` | Science (Forensics) | Наука (Криминалистика) |
| `i.skill.science-geology` | Science (Geology) | Наука (Геология) |
| `i.skill.science-mathematics` | Science (Mathematics) | Наука (Математика) |
| `i.skill.science-meteorology` | Science (Meteorology) | Наука (Метеорология) |
| `i.skill.science-pharmacy` | Science (Pharmacy) | Наука (Фармацевтика) |
| `i.skill.science-physics` | Science (Physics) | Наука (Физика) |
| `i.skill.science-zoology` | Science (Zoology) | Наука (Зоология) |
| `i.skill.sleight-of-hand` | Sleight of Hand | Ловкость рук |
| `i.skill.spot-hidden` | Spot Hidden | Внимательность |
| `i.skill.stealth` | Stealth | Скрытность |
| `i.skill.survival-any` | Survival (Any) | Выживание (Любое) |
| `i.skill.swim` | Swim | Плавание |
| `i.skill.track` | Track | Выслеживание |
| `i.skill.trap` | Trap | Ловушки |

## Описания навыков

| Английский | Русский |
| --- | --- |
| <p>See the Call of Cthulhu - 7th Ed Core Rulebook</p> | <p>См. базовую книгу правил «Зов Ктулху», 7-я редакция.</p> |
| <p>See the Cthulhu Invictus</p> | <p>См. «Cthulhu Invictus».</p> |
| <p>See the Cthulhu by Gaslight</p> | <p>См. «Cthulhu by Gaslight».</p> |
| <p>See the Down Darker Trails Rulebook</p> | <p>См. книгу правил «Down Darker Trails».</p> |
| <p>Use in occupations / archetypes to prompt to select one Fighting skill</p> | <p>Используется в профессиях и архетипах, чтобы предложить выбрать один навык ближнего боя.</p> |
| <p>Use in occupations / archetypes to prompt to select one Firearms skill</p> | <p>Используется в профессиях и архетипах, чтобы предложить выбрать один навык стрельбы.</p> |

## Фобии и мании (20)

| Английский | Русский | Описание |
| --- | --- | --- |
| Agathomania | Агатомания | Патологическая доброта. |
| Algomania | Алгомания | Одержимость болью. |
| Amenomania | Аменомания | Беспричинная, неуместная жизнерадостность. |
| Bibliokleptomania | Библиоклептомания | Навязчивая тяга к воровству книг. |
| Dikemania | Дикемания | Одержимость идеей торжества справедливости. |
| Geliomania | Гелиомания | Неудержимая тяга к смеху. |
| Klazomania | Клазомания | Неудержимая тяга к крику. |
| Kleptomania | Клептомания | Неудержимая тяга к воровству. |
| Nosomania | Нозомания | Убеждённость в том, что страдаешь выдуманной болезнью. |
| Pseudomania | Псевдомания | Неудержимая тяга ко лжи. |
| Acrophobia | Акрофобия | Боязнь высоты. |
| Arachnophobia | Арахнофобия | Боязнь пауков. |
| Bibliophobia | Библиофобия | Боязнь книг. |
| Eisoptrophobia | Эйсоптрофобия | Боязнь зеркал. |
| Hemaphobia | Гемофобия | Боязнь крови. |
| Necrophobia | Некрофобия | Боязнь мертвецов и всего мёртвого. |
| Odontophobia | Одонтофобия | Боязнь зубов. |
| Pyrophobia | Пирофобия | Боязнь огня. |
| Telephonophobia | Телефонофобия | Боязнь телефонов. |
| Xenophobia | Ксенофобия | Боязнь незнакомцев и иностранцев. |

| Папка | Перевод |
| --- | --- |
| Phobias | Фобии |
| Manias | Мании |

## Оружие (47)

| Английский | Русский |
| --- | --- |
| Bow | Лук |
| Brass Knuckles | Кастет |
| Bullwhip | Кнут |
| Burning Torch | Горящий факел |
| Blackjack | Кожаная дубинка |
| Club, Large | Дубина, большая |
| Club, Small | Дубинка, малая |
| Crossbow | Арбалет |
| Garrote | Гаррота |
| Hatchet/Sickle | Топорик/Серп |
| Knife, Large | Нож, большой |
| Knife, Medium | Нож, средний |
| Knife, Small | Нож, малый |
| Nunchaku | Нунчаку |
| Rock, Thrown | Камень (метательный) |
| Shuriken | Сюрикэн |
| Spear | Копьё |
| Spear, Thrown | Копьё (метательное) |
| .22 Short Automatic | Самозарядный пистолет .22 Short |
| .25 Derringer (1B) | Дерринджер .25 (1 ствол) |
| .32 or 7.65mm Revolver | Револьвер .32 / 7,65 мм |
| .32 or 7.65mm Automatic | Самозарядный пистолет .32 / 7,65 мм |
| Model P08 Luger | Люгер P08 |
| .45 Revolver | Револьвер .45 |
| .45 Automatic | Самозарядный пистолет .45 |
| .22 Bolt-Action Rifle | Винтовка .22 со скользящим затвором |
| .30 Lever-Action Carbine | Карабин .30 со скобой Генри |
| .45 Martini-Henry Rifle | Винтовка Мартини-Генри .45 |
| Col. Moran's Air Rifle | Духовое ружьё полковника Морана |
| .303 Lee-Enfield | Ли-Энфилд .303 |
| .30-06 Bolt-Action Rifle | Винтовка .30-06 со скользящим затвором |
| Elephant Gun (2B) | Слоновое ружьё (2 ствола) |
| 20-gauge Shotgun (2B) | Дробовик 20-го калибра (2 ствола) |
| 16-gauge Shotgun (2B) | Дробовик 16-го калибра (2 ствола) |
| 12-gauge Shotgun (2B) | Дробовик 12-го калибра (2 ствола) |
| 12-gauge Shotgun (semi-auto) | Дробовик 12-го калибра (самозарядный) |
| 12-gauge Shotgun (2B sawed off) | Дробовик 12-го калибра (обрез, 2 ствола) |
| Bergmann MP181/MP2811 | Бергманн MP18I/MP28II |
| Thompson | Томпсон |
| Browning Auto Rifle M1918 | Автоматическая винтовка Браунинга M1918 |
| .30 Browning M1917A1 | Браунинг M1917A1 .30 |
| Bren Gun | Пулемёт «Брен» |
| Mark I Lewis Gun | Пулемёт Льюиса Mark I |
| Vickers .303 | Виккерс .303 |
| Punch | Удар кулаком |
| Death ray (prototype) | Луч смерти (прототип) |
| Experimental weapon | Экспериментальное оружие |

| Папка | Перевод |
| --- | --- |
| Hand-to-Hand Weapons | Оружие ближнего боя |
| Handguns | Пистолеты и револьверы |
| Rifles | Винтовки |
| Shotguns | Дробовики |
| Submachine Guns | Пистолеты-пулемёты |
| Machine Guns | Пулемёты |

## Таблицы

| Английский | Русский |
| --- | --- |
| Table VII: Bouts of Madness - Real Time | Таблица VII: приступы безумия — в реальном времени |
| Table VIII: Bouts of Madness - Summary | Таблица VIII: приступы безумия — итоговая |
| Table IX: Sample Phobias | Таблица IX: примеры фобий |
| Table X: Sample Manias | Таблица X: примеры маний |
| Bouts of Madness Table (Realtime) | Таблица приступов безумия (в реальном времени) |

### Результаты таблицы приступов безумия

| Английский | Русский |
| --- | --- |
| Amnesia | Амнезия |
| Psychosomatic Disability | Психосоматическое расстройство |
| Violence | Вспышка ярости |
| Paranoia | Паранойя |
| Significant Person | Значимый человек |
| Faint | Обморок |
| Flee in Panic | Паническое бегство |
| Physical Hysterics or Emotional Outburst | Истерика или эмоциональный срыв |
| Phobia | Фобия |
| Mania | Мания |
| Bout of madness | Приступ безумия |

### Новые таблицы предыстории

Содержимое написано специально для модуля (не перевод книги правил), по 10
записей в каждой таблице, формула `1d10`.

| CoCID | Название |
| --- | --- |
| `rt..backstory-ideology-and-beliefs` | Мировоззрение и убеждения |
| `rt..backstory-significant-people` | Значимые люди |
| `rt..backstory-meaningful-locations` | Важные места |
| `rt..backstory-treasured-possessions` | Дорогие вещи |
| `rt..backstory-traits` | Черты характера |
| `rt..backstory-injuries-and-scars` | Травмы и шрамы |

## Секции биографии набора правил

| Английский | В русском наборе |
| --- | --- |
| Personal Description | `Описание внешности` |
| Ideology/Beliefs | `CoC7.CoCIDFlag.keys.rt..backstory-ideology-and-beliefs` |
| Significant People | `CoC7.CoCIDFlag.keys.rt..backstory-significant-people` |
| Meaningful Locations | `CoC7.CoCIDFlag.keys.rt..backstory-meaningful-locations` |
| Treasured Possessions | `CoC7.CoCIDFlag.keys.rt..backstory-treasured-possessions` |
| Traits | `CoC7.CoCIDFlag.keys.rt..backstory-traits` |

Пять секций из шести записаны ключами локализации `CoC7.CoCIDFlag.keys.rt..backstory-*`:
мастер создания сыщика распознаёт такой формат, локализует заголовок и
подставляет кнопку броска по одноимённой таблице.

## Исправленные опечатки CoCID системы

| Документ | CoCID в системе | CoCID в русском паке |
| --- | --- | --- |
| Spear, Thrown → Копьё (метательное) | `i.weapon.shuriken` | `i.weapon.spear-thrown` |
| Table VIII: Bouts of Madness - Summary → Таблица VIII | `rt..system-bouts-of-madness-real-time` | `rt..system-bouts-of-madness-summary` |

В системе у обоих документов CoCID продублирован с соседних (очевидная ошибка
копирования: два разных документа с одинаковым идентификатором). Без правки
сборка пака невозможна, поэтому для русских версий выданы отдельные CoCID.

## Имена для резервных проверок системы

`lang/ru.json` модуля содержит 109 ключей `CoC7.CoCIDFlag.keys.*`.
Они обязаны совпадать с именами документов в паках: система использует их как
резервный поиск, когда у предмета нет флага CoCID —
`actor.items.getName(game.i18n.localize('CoC7.CoCIDFlag.keys.i.skill.credit-rating'))`
в `models/actor/document-class.js` и `skill-system.js#isSpecificSkill`.
Файл генерируется тем же скриптом, что и YAML, поэтому расхождение исключено.

## Что не переводилось

- `en-examples.yaml` — демонстрационные НПС, существа и контейнеры.
- Игровые значения: `system.base`, `system.properties`, урон, дистанции,
  `malfunction`, `eras`, состав `system.items`/`skills`/`groups` — скопированы
  без изменений.
- Контент из платных книг: в системе его нет.
