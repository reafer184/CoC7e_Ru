# Глоссарий перевода CoC7 (Foundry VTT) — обязателен к соблюдению

Базис: **официальное русское издание «Зов Ктулху», 7-я редакция (Мир Хобби / Hobby World)**.
Спорные места решаются в пользу печатного листа сыщика и официальных материалов; см. раздел «Источники».

## Характеристики и производные (сокращения — как на официальном листе)

| Английский | Русский | Сокращение |
| --- | --- | --- |
| Strength | Сила | СИЛ |
| Constitution | Выносливость | ВЫН |
| Size | Телосложение | ТЕЛ |
| Dexterity | Ловкость | ЛВК |
| Appearance | Наружность | НАР |
| Intelligence | Интеллект | ИНТ |
| Power | Мощь | МОЩ |
| Education | Образование | ОБР |
| Sanity | Рассудок | РАС |
| Hit Points | Пункты здоровья | ПЗ |
| Magic Points | Пункты магии | ПМ |
| Luck | Удача | — |
| Damage Bonus | Бонус к урону | БкУ |
| Build | Комплекция | Компл. |
| Move rate | Скорость | СКО |
| Idea / Know | Идея / Знания | — |

## Термины правил

Investigator → сыщик (не «исследователь»)
Keeper → Хранитель
Setup → Набор правил
Occupation → Род занятий (в интерфейсе мастера — «Профессия», где речь о наборе навыков)
Archetype → Архетип
Skill → Навык
Specialization → Специализация (в названии — в скобках со строчной буквы)
Credit Rating → Средства
Spending Level / Cash / Assets → Карманные деньги / Наличные / Активы
Cthulhu Mythos → Мифы Ктулху
Bout of Madness → приступ безумия
Temporary insanity → Временное безумие
Indefinite insanity → Бессрочное безумие
Phobia / Mania → фобия / мания
Major Wound → Серьёзная рана
Dying → При смерти
Unconscious → Без сознания
Prone → Сбит с ног
Status → Состояние
Bonus die / Penalty die → бонусная кость / штрафная кость
Push roll → Повторная проверка
Combined / Opposed roll → Совместная / Встречная проверка
Regular / Hard / Extreme success → Обычный / Трудный / Чрезвычайный успех
Critical success / Fumble / Failure → Критический успех / Крах / Провал
Development Phase → Фаза развития
Pulp / Pulp Cthulhu → Pulp Cthulhu (название линейки не переводится)
Spell → Заклинание
Casting cost → Стоимость сотворения

## Разделы биографии (как на листе)

Personal Description → Описание · Ideology/Beliefs → Идеалы и принципы · Significant People → Значимые люди ·
Meaningful Locations → Важные места · Treasured Possessions → Ценное имущество · Traits → Черты ·
Injuries & Scars → Травмы и шрамы · Encounters with Strange Entities → Встречи со сверхъестественным ·
Arcane Tomes, Spells & Artifacts → Магические книги, заклинания, артефакты · Backstory → Биография

## Навыки: закреплённые решения издания

Fighting → Ближний бой · Firearms → Стрельба · Throw → Метание · Dodge → Уклонение
Spot Hidden → **Внимание** · Listen → Слух · Fast Talk → **Красноречие** · Charm → Обаяние ·
Persuade → Убеждение · Intimidate → Запугивание
Track → **Чтение следов** · Natural World → **Естествознание** · Locksmith → **Взлом** ·
Mechanical Repair → **Механика** · Electrical Repair → **Электрика** · Demolitions → **Взрывчатка** ·
Library Use → **Работа в библиотеке** · Accounting → **Бухгалтерское дело** ·
Operate Heavy Machinery → Управление тяжёлыми машинами · Drive Auto → Вождение автомобиля ·
Navigate → Ориентирование · Art/Craft (Fine Art) → Искусство/ремесло (живопись) ·
Science (Engineering) → Наука (инженерия) · Science (Pharmacy) → Наука (фармакология) ·
Language (Any) → Язык (иностранный) · Language (Own) → Язык (родной)

Правило регистра: специализация в скобках — **строчными**: «Стрельба (пистолет)», «Ближний бой (драка)», «Наука (биология)».

Отклонения от печатной формы, вынужденные движком Foundry (документированы в translation-notes):
на листе печатается «Язык, иностр.», но система выделяет специализацию по скобкам, поэтому в модуле — «Язык (иностранный)»;
у «любых» навыков на листе специализация не указана, в модуле сохранено «(любое/любая/любой)», иначе документы неотличимы.

## Интерфейс Foundry

Token → Токен · Actor → Актёр · Item → Предмет · Roll Table → Таблица случайных результатов ·
Compendium → Компендиум · Chat message → Сообщение в чате · GM/Keeper → Хранитель · Scene → Сцена ·
Region → Регион · Combat → Бой · Weapon malfunction → Осечка · Impale → Пробивание ·
Chaosium Canvas Interface → Интерфейс Chaosium · Handout → Раздаточный материал

## Правила

1. Перевод строго на русский, стиль — как в игровых правилах Call of Cthulhu 7-й редакции: вежливый, нейтральный, без обращений на «ты».
2. Сохраняй ВСЕ подстановки в исходном виде: `{name}`, `{value}`, `{actor}`, `%s`, `<b>`, `<i>`, `<br>`, `<p>`, ссылки, переводы строк `\n`, HTML-теги и их атрибуты.
3. Названия настроек — краткие (до 5–6 слов); подсказки (hint) — полными предложениями с точкой.
4. Термины из глоссария — обязательны, без вариаций внутри одного файла.
5. Кнопки и подписи — без точки в конце. Сообщения об ошибках — с точкой.
6. Не переводить: `CoC7`, `Foundry VTT`, `Chaosium`, `Pulp Cthulhu`, имена файлов, коды.
7. Сокращения единиц: ft → фт, yd → ярд, lb → фнт.
8. Никаких пояснений, комментариев и англоязычных «хвостов» в переводе.

## Источники (официальные материалы Мир Хобби / Hobby World)

- [Лист сыщика 1920-х](https://hobbygames.ru/download/rules/call_of_cthulhu_character_sheet_00.pdf) — канонический список навыков, блоки листа, уровни успеха.
- [Лист сыщика из «Стартового набора»](https://hobbygames.ru/download/rules/Zov_Ktulhu_gotovie_pers.pdf) — вторая независимая сверка.
- [Готовые сыщики «Кошмары цифровой эпохи»](https://hobbygames.ru/download/rules/zov-ktulhu-characters.pdf) — сокращения характеристик, названия оружия, разделы биографии.
- [Лист современного сыщика](https://hobbygames.ru/download/rules/Keepers_sovremennij_Character_Sheets.pdf.pdf) — «Пункты здоровья», «Пункты магии», «Работа с компьютером», «Электроника».
- [Готовые сыщики «Двери во тьму»](https://hobbygames.ru/download/rules/Call_of_Chtulhu/Dveri_vo_Tmu_Personazhi.pdf) — «Взрывчатка», «Наука (криминалистика)», названия оружия.
- [Материалы игроков «Маски Ньярлатхотепа»](https://hobbygames.ru/download/rules/zk-maski-njarlathotepa-materiali-igrokov.pdf) — «бонусная кость», «штрафная кость», «бессрочное безумие».
- [Глоссарий имён и существ](https://hobbygames.ru/download/rules/CoC_Keeper_Bestiary.pdf) — официальные написания имён Мифов.

Неофициальные источники (помечены `medium`, использованы только там, где издания молчат): [«Как создать персонажа», перевод Hort](https://callofcthulhu.ru/files/creating_investigators_for_call_of_cthulhu_rpg.pdf) — Наука (астрономия/зоология), Ближний бой (цепная пила).
