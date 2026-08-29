#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генерирует русские YAML-исходники паков модуля coc7-ru-content и
lang/ru.json (имена CoCID) на основе английских компендиумов системы CoC7.

Запуск: python3 tools/generate-ru-yaml.py <путь к compendiums.json> 
(рядом должен лежать tools/en.json — языковой файл системы).
После генерации собрать паки: node tools/build-packs.mjs"""
import json, os, copy, io, sys

# Путь к дампу английских компендиумов системы CoC7.
# Готовится так (в клоне CoC7-FoundryVTT):
#   python3 -c "import yaml,glob,json; print(json.dumps({f: [d for d in yaml.safe_load_all(open(f,encoding=chr(39)+'utf-8'+chr(39))) if d] for f in sorted(glob.glob('compendiums/*.yaml'))}, ensure_ascii=False))" > compendiums.json
# и передаётся первым аргументом:
#   python3 tools/generate-ru-yaml.py ../CoC7-FoundryVTT/compendiums.json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC_PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "compendiums.json")
SRC = json.load(open(SRC_PATH, encoding="utf-8"))
SRC = {("upstream/compendiums/" + os.path.basename(k)): v for k, v in SRC.items()}
OUT = os.path.join(ROOT, "compendiums")
os.makedirs(OUT, exist_ok=True)

def s(f):
    return copy.deepcopy(SRC["upstream/compendiums/" + f])

# ---------------------------------------------------------------- навыки
SKILLS = {
 "Accounting": "Бухгалтерия",
 "Animal Handling": "Обращение с животными",
 "Anthropology": "Антропология",
 "Appraise": "Оценка",
 "Archaeology": "Археология",
 "Art/Craft (Acting)": "Искусство/Ремесло (Актёрское мастерство)",
 "Art/Craft (Any)": "Искусство/Ремесло (Любое)",
 "Art/Craft (Fine Art)": "Искусство/Ремесло (Изобразительное искусство)",
 "Art/Craft (Forgery)": "Искусство/Ремесло (Подделка)",
 "Art/Craft (Photography)": "Искусство/Ремесло (Фотография)",
 "Charm": "Обаяние",
 "Civics": "Гражданское право",
 "Climb": "Лазание",
 "Computer Use": "Работа с компьютером",
 "Credit Rating": "Кредитоспособность",
 "Cthulhu Mythos": "Мифы Ктулху",
 "Demolitions": "Подрывное дело",
 "Disguise": "Маскировка",
 "Diving": "Подводное плавание",
 "Dodge": "Уклонение",
 "Drive Auto": "Вождение (Автомобиль)",
 "Drive Carriage": "Вождение (Экипаж)",
 "Drive Horse / Oxen": "Вождение (Лошади и волы)",
 "Drive Wagon / Coach": "Вождение (Повозка и дилижанс)",
 "Electrical Repair": "Ремонт электрики",
 "Electronics": "Электроника",
 "Empire": "Империя",
 "Fast Talk": "Заговаривание",
 "Fighting (Any)": "Ближний бой (Любой)",
 "Fighting (Axe)": "Ближний бой (Топор)",
 "Fighting (Brawl)": "Ближний бой (Драка)",
 "Fighting (Chainsaw)": "Ближний бой (Цепная пила)",
 "Fighting (Flail)": "Ближний бой (Цеп)",
 "Fighting (Garrote)": "Ближний бой (Гаррота)",
 "Fighting (Spear)": "Ближний бой (Копьё)",
 "Fighting (Sword)": "Ближний бой (Меч)",
 "Throw": "Метание",
 "Fighting (Whip)": "Ближний бой (Кнут)",
 "Firearms (Any)": "Стрельба (Любая)",
 "Firearms (Artillery)": "Стрельба (Артиллерия)",
 "Firearms (Bow)": "Стрельба (Лук)",
 "Firearms (Flamethrower)": "Стрельба (Огнемёт)",
 "Firearms (Handgun)": "Стрельба (Пистолет)",
 "Firearms (Heavy Weapons)": "Стрельба (Тяжёлое оружие)",
 "Firearms (Machine Gun)": "Стрельба (Пулемёт)",
 "Firearms (Rifle/Shotgun)": "Стрельба (Винтовка/Дробовик)",
 "Firearms (Submachine Gun)": "Стрельба (Пистолет-пулемёт)",
 "First Aid": "Первая помощь",
 "Gambling": "Азартные игры",
 "History": "История",
 "Hypnosis": "Гипноз",
 "Intimidate": "Запугивание",
 "Jump": "Прыжки",
 "Language (Any)": "Язык (Любой)",
 "Language (Own)": "Язык (Родной)",
 "Language (Czech)": "Язык (Чешский)",
 "Language (Dutch)": "Язык (Нидерландский)",
 "Language (English)": "Язык (Английский)",
 "Language (German)": "Язык (Немецкий)",
 "Language (Polish)": "Язык (Польский)",
 "Language (Russian)": "Язык (Русский)",
 "Language (Swahili)": "Язык (Суахили)",
 "Language (Yoruba)": "Язык (Йоруба)",
 "Language (Zulu)": "Язык (Зулу)",
 "Law": "Юриспруденция",
 "Library Use": "Работа с библиотекой",
 "Listen": "Слух",
 "Locksmith": "Взлом замков",
 "Lore (Any)": "Знание (Любое)",
 "Mechanical Repair": "Ремонт механики",
 "Medicine": "Медицина",
 "Natural World": "Природа",
 "Navigate": "Ориентирование",
 "Occult": "Оккультизм",
 "Operate Heavy Machinery": "Управление тяжёлой техникой",
 "Persuade": "Убеждение",
 "Pilot (Any)": "Пилотирование (Любое)",
 "Psychoanalysis": "Психоанализ",
 "Psychology": "Психология",
 "Read Lips": "Чтение по губам",
 "Ride": "Верховая езда",
 "Rope Use": "Работа с верёвкой",
 "Science (Any)": "Наука (Любая)",
 "Science (Astronomy)": "Наука (Астрономия)",
 "Science (Biology)": "Наука (Биология)",
 "Science (Botany)": "Наука (Ботаника)",
 "Science (Chemistry)": "Наука (Химия)",
 "Science (Cryptography)": "Наука (Криптография)",
 "Science (Engineering)": "Наука (Инженерное дело)",
 "Science (Forensics)": "Наука (Криминалистика)",
 "Science (Geology)": "Наука (Геология)",
 "Science (Mathematics)": "Наука (Математика)",
 "Science (Meteorology)": "Наука (Метеорология)",
 "Science (Pharmacy)": "Наука (Фармацевтика)",
 "Science (Physics)": "Наука (Физика)",
 "Science (Zoology)": "Наука (Зоология)",
 "Sleight of Hand": "Ловкость рук",
 "Spot Hidden": "Внимательность",
 "Stealth": "Скрытность",
 "Survival (Any)": "Выживание (Любое)",
 "Swim": "Плавание",
 "Track": "Выслеживание",
 "Trap": "Ловушки",
}

DESCS = {
 "<p>See the Call of Cthulhu - 7th Ed Core Rulebook</p>":
   "<p>См. базовую книгу правил «Зов Ктулху», 7-я редакция.</p>",
 "<p>See the Cthulhu Invictus</p>": "<p>См. «Cthulhu Invictus».</p>",
 "<p>See the Cthulhu by Gaslight</p>": "<p>См. «Cthulhu by Gaslight».</p>",
 "<p>See the Down Darker Trails Rulebook</p>": "<p>См. книгу правил «Down Darker Trails».</p>",
 "<p>Use in occupations / archetypes to prompt to select one Fighting skill</p>":
   "<p>Используется в профессиях и архетипах, чтобы предложить выбрать один навык ближнего боя.</p>",
 "<p>Use in occupations / archetypes to prompt to select one Firearms skill</p>":
   "<p>Используется в профессиях и архетипах, чтобы предложить выбрать один навык стрельбы.</p>",
}

# --------------------------------------------------------------- оружие
WEAPON_FOLDERS = {
 "Hand-to-Hand Weapons": "Оружие ближнего боя",
 "Handguns": "Пистолеты и револьверы",
 "Rifles": "Винтовки",
 "Shotguns": "Дробовики",
 "Submachine Guns": "Пистолеты-пулемёты",
 "Machine Guns": "Пулемёты",
}
WEAPONS = {
 "Bow": "Лук",
 "Brass Knuckles": "Кастет",
 "Bullwhip": "Кнут",
 "Burning Torch": "Горящий факел",
 "Blackjack": "Кожаная дубинка",
 "Club, Large": "Дубина, большая",
 "Club, Small": "Дубинка, малая",
 "Crossbow": "Арбалет",
 "Garrote": "Гаррота",
 "Hatchet/Sickle": "Топорик/Серп",
 "Knife, Large": "Нож, большой",
 "Knife, Medium": "Нож, средний",
 "Knife, Small": "Нож, малый",
 "Nunchaku": "Нунчаку",
 "Rock, Thrown": "Камень (метательный)",
 "Shuriken": "Сюрикэн",
 "Spear": "Копьё",
 "Spear, Thrown": "Копьё (метательное)",
 ".22 Short Automatic": "Самозарядный пистолет .22 Short",
 ".25 Derringer (1B)": "Дерринджер .25 (1 ствол)",
 ".32 or 7.65mm Revolver": "Револьвер .32 / 7,65 мм",
 ".32 or 7.65mm Automatic": "Самозарядный пистолет .32 / 7,65 мм",
 "Model P08 Luger": "Люгер P08",
 ".45 Revolver": "Револьвер .45",
 ".45 Automatic": "Самозарядный пистолет .45",
 ".22 Bolt-Action Rifle": "Винтовка .22 со скользящим затвором",
 ".30 Lever-Action Carbine": "Карабин .30 со скобой Генри",
 ".45 Martini-Henry Rifle": "Винтовка Мартини-Генри .45",
 "Col. Moran's Air Rifle": "Духовое ружьё полковника Морана",
 ".303 Lee-Enfield": "Ли-Энфилд .303",
 ".30-06 Bolt-Action Rifle": "Винтовка .30-06 со скользящим затвором",
 "Elephant Gun (2B)": "Слоновое ружьё (2 ствола)",
 "20-gauge Shotgun (2B)": "Дробовик 20-го калибра (2 ствола)",
 "16-gauge Shotgun (2B)": "Дробовик 16-го калибра (2 ствола)",
 "12-gauge Shotgun (2B)": "Дробовик 12-го калибра (2 ствола)",
 "12-gauge Shotgun (semi-auto)": "Дробовик 12-го калибра (самозарядный)",
 "12-gauge Shotgun (2B sawed off)": "Дробовик 12-го калибра (обрез, 2 ствола)",
 "Bergmann MP181/MP2811": "Бергманн MP18I/MP28II",
 "Thompson": "Томпсон",
 "Browning Auto Rifle M1918": "Автоматическая винтовка Браунинга M1918",
 ".30 Browning M1917A1": "Браунинг M1917A1 .30",
 "Bren Gun": "Пулемёт «Брен»",
 "Mark I Lewis Gun": "Пулемёт Льюиса Mark I",
 "Vickers .303": "Виккерс .303",
 "Punch": "Удар кулаком",
 "Death ray (prototype)": "Луч смерти (прототип)",
 "Experimental weapon": "Экспериментальное оружие",
}

# ------------------------------------------------------- фобии и мании
STATUS_FOLDERS = {"Phobias": "Фобии", "Manias": "Мании"}
STATUSES = {
 "Agathomania": ("Агатомания", "<p>Патологическая доброта.</p>"),
 "Algomania": ("Алгомания", "<p>Одержимость болью.</p>"),
 "Amenomania": ("Аменомания", "<p>Беспричинная, неуместная жизнерадостность.</p>"),
 "Bibliokleptomania": ("Библиоклептомания", "<p>Навязчивая тяга к воровству книг.</p>"),
 "Dikemania": ("Дикемания", "<p>Одержимость идеей торжества справедливости.</p>"),
 "Geliomania": ("Гелиомания", "<p>Неудержимая тяга к смеху.</p>"),
 "Klazomania": ("Клазомания", "<p>Неудержимая тяга к крику.</p>"),
 "Kleptomania": ("Клептомания", "<p>Неудержимая тяга к воровству.</p>"),
 "Nosomania": ("Нозомания", "<p>Убеждённость в том, что страдаешь выдуманной болезнью.</p>"),
 "Pseudomania": ("Псевдомания", "<p>Неудержимая тяга ко лжи.</p>"),
 "Acrophobia": ("Акрофобия", "<p>Боязнь высоты.</p>"),
 "Arachnophobia": ("Арахнофобия", "<p>Боязнь пауков.</p>"),
 "Bibliophobia": ("Библиофобия", "<p>Боязнь книг.</p>"),
 "Eisoptrophobia": ("Эйсоптрофобия", "<p>Боязнь зеркал.</p>"),
 "Hemaphobia": ("Гемофобия", "<p>Боязнь крови.</p>"),
 "Necrophobia": ("Некрофобия", "<p>Боязнь мертвецов и всего мёртвого.</p>"),
 "Odontophobia": ("Одонтофобия", "<p>Боязнь зубов.</p>"),
 "Pyrophobia": ("Пирофобия", "<p>Боязнь огня.</p>"),
 "Telephonophobia": ("Телефонофобия", "<p>Боязнь телефонов.</p>"),
 "Xenophobia": ("Ксенофобия", "<p>Боязнь незнакомцев и иностранцев.</p>"),
}

# ------------------------------------------------------------- таблицы
TABLE_NAMES = {
 "Table VII: Bouts of Madness - Real Time": "Таблица VII: приступы безумия — в реальном времени",
 "Table VIII: Bouts of Madness - Summary": "Таблица VIII: приступы безумия — итоговая",
 "Table IX: Sample Phobias": "Таблица IX: примеры фобий",
 "Table X: Sample Manias": "Таблица X: примеры маний",
 "Bouts of Madness Table (Realtime)": "Таблица приступов безумия (в реальном времени)",
}
TABLE_DESCS = {
 "See Keeper rulebook P160 for details": "Подробности см. в книге Хранителя, с. 160.",
 "See Keeper rulebook P161 for details": "Подробности см. в книге Хранителя, с. 161.",
 "See - Keeper Rulebook V7 - P157 for details": "Подробности см. в книге Хранителя, 7-я редакция, с. 157.",
 "See - Keeper Rulebook V7 - P159 for details": "Подробности см. в книге Хранителя, 7-я редакция, с. 159.",
}
MADNESS = {
 "Amnesia": ("Амнезия",
   "Сыщик не помнит ничего из того, что произошло с момента, когда он последний раз находился в безопасном месте. Ему кажется, что мгновение назад он завтракал, а теперь стоит лицом к лицу с чудовищем. Длится [[/r 1D10]] раундов."),
 "Psychosomatic Disability": ("Психосоматическое расстройство",
   "Сыщик на [[/r 1D10]] раундов теряет зрение, слух или способность владеть одной из конечностей — без физической причины."),
 "Violence": ("Вспышка ярости",
   "Багровая пелена ярости застилает сыщику глаза, и он на [[/r 1D10]] раундов срывается в неуправляемое буйство, обрушивая его на всё вокруг — и на врагов, и на союзников."),
 "Paranoia": ("Паранойя",
   "На [[/r 1D10]] раундов сыщика охватывает тяжёлая паранойя. Все против него! Никому нельзя верить! За ним следят, его уже предали, а всё, что он видит, — обман."),
 "Significant Person": ("Значимый человек",
   "Обратитесь к разделу предыстории «Значимые люди». Сыщик принимает кого-то из присутствующих за своего значимого человека и действует, исходя из характера этих отношений. Длится [[/r 1D10]] раундов."),
 "Faint": ("Обморок",
   "Сыщик теряет сознание и приходит в себя через [[/r 1D10]] раундов."),
 "Flee in Panic": ("Паническое бегство",
   "Сыщик стремится оказаться как можно дальше отсюда любым доступным способом — даже если для этого придётся забрать единственную машину и бросить остальных. Бежит [[/r 1D10]] раундов."),
 "Physical Hysterics or Emotional Outburst": ("Истерика или эмоциональный срыв",
   "Сыщик не способен действовать: он хохочет, рыдает, кричит и так далее — [[/r 1D10]] раундов."),
 "Phobia": ("Фобия",
   "Сыщик приобретает новую фобию — например, клаустрофобию (боязнь замкнутых пространств), демонофобию (боязнь духов и демонов) или катсаридафобию (боязнь тараканов). Даже если источника страха рядом нет, следующие [[/r 1D10]] раундов сыщику кажется, что он здесь, и все его действия получают штрафную кость до конца приступа."),
 "Mania": ("Мания",
   "Сыщик приобретает новую манию — например, аблутоманию (тягу к постоянному мытью), псевдоманию (неудержимую тягу ко лжи) или гельминтоманию (болезненную любовь к червям). Следующие [[/r 1D10]] раундов сыщик стремится ей потворствовать, и все его действия получают штрафную кость до конца приступа."),
 "Bout of madness": ("Приступ безумия",
   "См. таблицу приступов безумия, с. 159. Длительность — [[/r 1D10]] часов."),
}

# --------------------------------------------------- прочие документы
SETUP_NAME = "Пример набора правил (1920-е)"
SETUP_DESC = "<p>Набор правил по умолчанию для персонажа 1920-х годов.</p>"
BIO_SECTIONS = [
 "Описание внешности",
 "CoC7.CoCIDFlag.keys.rt..backstory-ideology-and-beliefs",
 "CoC7.CoCIDFlag.keys.rt..backstory-significant-people",
 "CoC7.CoCIDFlag.keys.rt..backstory-meaningful-locations",
 "CoC7.CoCIDFlag.keys.rt..backstory-treasured-possessions",
 "CoC7.CoCIDFlag.keys.rt..backstory-traits",
]
ARCH_NAME = "Миротворец"
ARCH_DESC = ("<p>Человек, умеющий решать проблемы и от природы способный находить «око бури» — "
 "видеть вопрос со всех сторон сразу. Миротворцем движет стремление к согласию: он старается "
 "сохранить равновесие между людьми или группами людей и удержать положение вещей таким, как оно есть. "
 "Он ищет решения и легко приспосабливается — иногда себе во вред, потому что ставит чужие нужды выше "
 "собственных. Его нередко называют «покладистым» или «мягкотелым», но в час беды он бывает "
 "стойким, хладнокровным и смелым.</p>")
ARCH_OCC = ("<p>Спортсмен, бармен или официантка, патрульный полицейский, дворецкий, преступник, "
 "выборный чиновник, рабочий, миссионер, медсестра, священник, секретарь, йог.</p>")
ARCH_TRAITS = "<p>хладнокровен в напряжённой обстановке, рассудителен, держится скромно, самоотвержен.</p>"
OCC_NAME = "Уличный торговец"
OCC_DESC = ("<p>Уличные торговцы — их также называют разносчиками и лоточниками — кочуют с места на место, "
 "обычно с тележкой или лотком, и продают прохожим всякую мелочь: изделия ручной работы, еду и закуски "
 "или другие недорогие товары. Они славятся тем, что выкрикивают названия своих товаров, зазывая "
 "покупателей, а острым словом и болтовнёй умеют поднять цену и продать больше.</p>"
 "<p>Целый день на улице означает, что торговец знает разные районы, привычки и перемещения местных "
 "жителей и служит магнитом для сплетен — а нередко и их источником.</p>"
 "<p><strong>Возможные связи:</strong> другие торговцы, местные полицейские, поставщики товара, "
 "дворецкие и прочая домашняя прислуга.</p>")
TALENT_NAME = "Пример таланта"
SPELL_NAME = "Тестовое заклинание"
SPELL_TIME = "10–15 минут"
SPELL_DESC = ("<p>Заставляет другого человека увидеть кошмар.</p>"
 "<p>Чародей тратит некоторое количество очков магии и теряет [[/r 1D3 - 1]] очков рассудка. "
 "Если тот, кому предназначен кошмар, в этот момент не спит, чародей должен потратить 1 ВЛИ, "
 "а произнесение заклинания занимает на пять минут больше.</p>"
 "<p>Другие чародеи, знающие это заклинание, тоже могут добавить очки магии; любой присутствующий "
 "может добавить одно очко магии.</p>"
 "<p>Кошмар начинается с того, что жертва сдаёт экзамен, к которому не готовилась, и продлевается "
 "на одну минуту за каждые шесть потраченных очков магии.</p><p></p>")
SPELL_PROMPTS = {
 "The target is awake": "Жертва не спит",
 "Number of magic points you are spending": "Сколько очков магии вы тратите",
 "Others that know the spell": "Другие, знающие заклинание",
 "Magic points": "Очки магии",
 "Other casters": "Прочие участники",
 "Nightmare duration: @minutes minutes": "Длительность кошмара: @minutes мин.",
}
EXP_WEAPON_DESC = ("<p>Описание оружия.</p>"
 "<p>Если включить свойство «Зона поражения», станут доступны три разных значения урона и дистанции.</p>"
 "<p>Если включить «Автоматический огонь», для оружия можно будет выбрать два навыка.</p>"
 "<p>Если включить «Особое», активируется поле особого описания.</p>"
 "<p>На вкладке боя красный фон значка означает, что для этого оружия не выбран навык.</p>"
 "<p>Откройте оружие и выберите нужный навык.</p>")
EXP_WEAPON_SPECIAL = ("<p>Здесь можно добавить особое описание или броски:</p>"
 "<p>Бросок 1: [[/r 2d17kh]]</p>")

# --------------------------------------------- таблицы предыстории (новые)
BACKSTORY_TABLES = [
 ("rt..backstory-ideology-and-beliefs", "Мировоззрение и убеждения", [
   ("Вера", "Сыщик искренне верует и не пропускает ни одной службы; вера объясняет ему всё, что происходит в мире."),
   ("Наука", "Только то, что можно измерить и проверить, достойно доверия. Суеверия — удел слабых умов."),
   ("Судьба", "Всё предначертано заранее. Спорить с судьбой бессмысленно, остаётся лишь достойно сыграть свою роль."),
   ("Деньги", "Деньги решают всё. Достаточно узнать цену человека — и станет ясно, чего он стоит."),
   ("Политика", "Сыщик горячо привержен своим политическим взглядам и не молчит о них в обществе."),
   ("Человечность", "Люди в глубине души добры; жестокость — следствие обстоятельств, а не природы."),
   ("Мизантропия", "Люди — стая зверей в приличной одежде. Доверять можно единицам."),
   ("Тайное знание", "Мир скрывает истину, и сыщик убеждён, что однажды доберётся до неё."),
   ("Долг", "Слово дано — слово держат. Обязательства перед семьёй, страной или делом важнее личных желаний."),
   ("Суеверия", "Разбитое зеркало, чёрная кошка, тринадцатый номер — сыщик соблюдает свои приметы неукоснительно."),
 ]),
 ("rt..backstory-significant-people", "Значимые люди", [
   ("Родитель", "Отец или мать — тот, чьё одобрение сыщик до сих пор пытается заслужить."),
   ("Наставник", "Учитель или старший коллега, открывший сыщику его настоящее призвание."),
   ("Возлюбленный", "Тот, кого сыщик любит — взаимно или безответно."),
   ("Друг детства", "Человек, знающий о сыщике всё, включая то, о чём он предпочёл бы забыть."),
   ("Брат или сестра", "Родство, замешанное на соперничестве и привязанности одновременно."),
   ("Ребёнок", "Сын, дочь, племянник или воспитанник, за которого сыщик в ответе."),
   ("Спасённый", "Человек, которому сыщик однажды спас жизнь — и который об этом не забыл."),
   ("Кумир", "Знаменитость или мастер своего дела, которому сыщик подражает, порой не будучи с ним знаком."),
   ("Соперник", "Тот, чьи успехи сыщик мерит своими, а поражения переживает как победу."),
   ("Пропавший", "Человек, исчезнувший без объяснений; сыщик всё ещё ищет ответ."),
 ]),
 ("rt..backstory-meaningful-locations", "Важные места", [
   ("Родной дом", "Дом, где сыщик вырос: скрип половиц узнаётся с первого шага."),
   ("Альма-матер", "Университет или школа, где сыщик впервые понял, чего хочет от жизни."),
   ("Библиотека", "Тихий читальный зал, где мысли наконец укладываются в порядок."),
   ("Церковь", "Место, куда сыщик приходит за утешением или за прощением."),
   ("Кладбище", "Здесь лежит тот, чью могилу сыщик навещает без свидетелей."),
   ("Бар", "Знакомый кабак, где бармен наливает раньше, чем сыщик успевает попросить."),
   ("Берег", "Пристань, пляж или берег реки, куда сыщик едет, чтобы подумать."),
   ("Место работы", "Кабинет, цех или редакция, ставшие для сыщика вторым домом."),
   ("Клуб", "Общество или клуб, членство в котором сыщик ценит выше жалованья."),
   ("Глухая окраина", "Место, где с сыщиком случилось нечто, о чём он никому не рассказывает."),
 ]),
 ("rt..backstory-treasured-possessions", "Дорогие вещи", [
   ("Инструмент ремесла", "Предмет, без которого сыщик не берётся за свою работу."),
   ("Оружие", "Ствол или клинок, доставшийся от родителя или с войны."),
   ("Книга", "Том, зачитанный до трещин в переплёте, с пометками на полях."),
   ("Фотография", "Снимок человека или места, которых больше нет."),
   ("Украшение", "Медальон, кольцо или часы, передающиеся в семье из рук в руки."),
   ("Дневник", "Записи, которые сыщик ведёт ежедневно и не показывает никому."),
   ("Автомобиль", "Машина, за которой сыщик ухаживает тщательнее, чем за собой."),
   ("Музыкальный инструмент", "Скрипка, гитара или губная гармоника — спутник в дороге."),
   ("Сувенир", "Безделушка, привезённая из далёкой поездки и напоминающая о ней."),
   ("Письмо", "Письмо, которое сыщик перечитывает и до сих пор не отправил ответ."),
 ]),
 ("rt..backstory-traits", "Черты характера", [
   ("Щедрость", "Сыщик легко расстаётся с деньгами и временем ради других."),
   ("Упрямство", "Отговорить сыщика от задуманного почти невозможно."),
   ("Обаяние", "Люди тянутся к сыщику, сами не понимая почему."),
   ("Вспыльчивость", "Терпение у сыщика короткое, а память на обиды долгая."),
   ("Любопытство", "Закрытая дверь для сыщика — приглашение."),
   ("Осторожность", "Сыщик проверяет выходы прежде, чем садится за стол."),
   ("Чувство юмора", "Даже в дурной час у сыщика найдётся уместная шутка."),
   ("Скрытность", "Сыщик говорит меньше, чем знает, и знает больше, чем кажется."),
   ("Верность", "Своих сыщик не бросает, чего бы это ни стоило."),
   ("Пагубная привычка", "Выпивка, карты, табак или что-то похуже — у сыщика есть слабость, и она берёт своё."),
 ]),
 ("rt..backstory-injuries-and-scars", "Травмы и шрамы", [
   ("Шрам на лице", "Тонкая белая линия от брови до подбородка — след давней драки."),
   ("Сломанный нос", "Нос, сросшийся криво: его так и не удосужились выправить."),
   ("Хромота", "Старый перелом ноги, который ноет перед непогодой."),
   ("Ожог", "Стянутая ожогом кожа на кисти или предплечье."),
   ("Отсутствующий палец", "Палец, потерянный из-за станка, обморожения или ножа."),
   ("Глухота на одно ухо", "Последствие взрыва или болезни: сыщик поворачивается здоровым ухом к говорящему."),
   ("Рубец от пули", "Затянувшийся след огнестрельного ранения, который сыщик неохотно объясняет."),
   ("Больная спина", "Травма, из-за которой долго стоять или носить тяжести мучительно."),
   ("Испорченное зрение", "Без очков дальше вытянутой руки всё расплывается."),
   ("Хирургический шрам", "Ровный след операции, спасшей сыщику жизнь."),
 ]),
]

def cocid(doc):
    return doc.get("flags", {}).get("CoC7", {}).get("cocidFlag", {}).get("id", "")

def relang(doc, priority=0):
    doc.pop("_id", None)  # id будет сгенерирован сборщиком из русского имени
    f = doc["flags"]["CoC7"]["cocidFlag"]
    f["lang"] = "ru"
    f["priority"] = priority
    return doc

# --------------------------------------------------------------- сборка
missing = []

def tr_skill(doc):
    en = doc["name"]
    if en not in SKILLS:
        missing.append("skill: " + en)
        return doc
    doc["name"] = SKILLS[en]
    d = doc.get("system", {}).get("description", {}).get("value")
    if d is not None:
        if d not in DESCS:
            missing.append("skill-desc: " + d)
        else:
            doc["system"]["description"]["value"] = DESCS[d]
    return relang(doc)

skills = [tr_skill(d) for d in s("en-skills.yaml")]

items = s("en-items.yaml")
by_cocid = {cocid(d): d for d in items}

setup = by_cocid["i.setup.s-setup"]
setup["name"] = SETUP_NAME
setup["system"]["description"]["value"] = SETUP_DESC
setup["system"]["bioSections"] = BIO_SECTIONS
setups = [relang(setup)]

arch = by_cocid["i.archetype.peacemaker"]
arch["name"] = ARCH_NAME
arch["system"]["description"]["value"] = ARCH_DESC
arch["system"]["suggestedOccupations"] = ARCH_OCC
arch["system"]["suggestedTraits"] = ARCH_TRAITS
archetypes = [relang(arch)]

occ = by_cocid["i.occupation.street-vendor"]
occ["name"] = OCC_NAME
occ["system"]["description"]["value"] = OCC_DESC
occupations = [relang(occ)]

talent = by_cocid["i.talent.example-talent"]
talent["name"] = TALENT_NAME
spell = by_cocid["i.spell.test-spell"]
spell["name"] = SPELL_NAME
spell["system"]["castingTime"] = SPELL_TIME
spell["system"]["description"]["value"] = SPELL_DESC
for cost in spell["system"].get("costList", []):
    cfg = cost.get("config")
    if not cfg:
        continue
    obj = json.loads(cfg)
    if "prompt" in obj:
        if obj["prompt"] not in SPELL_PROMPTS:
            missing.append("spell-prompt: " + obj["prompt"])
        else:
            obj["prompt"] = SPELL_PROMPTS[obj["prompt"]]
    cost["config"] = json.dumps(obj, ensure_ascii=False)
misc_items = [relang(talent), relang(spell)]

# --- оружие: вики-паки + примеры из en-items
weapons = []
folder_map = {}
for d in s("en-wiki-weapons.yaml"):
    if d.get("type") == "folder":
        ru = WEAPON_FOLDERS[d["name"]]
        newid = "RuWeapFolder%04d" % (len(folder_map) + 1)
        folder_map[d["_id"]] = newid
        d["_id"] = newid
        d["name"] = ru
        weapons.append(d)
    else:
        # Исправление ошибки upstream: у «Spear, Thrown» скопирован CoCID сюрикэна.
        if d["name"] == "Spear, Thrown" and cocid(d) == "i.weapon.shuriken":
            d["flags"]["CoC7"]["cocidFlag"]["id"] = "i.weapon.spear-thrown"
        if d["name"] not in WEAPONS:
            missing.append("weapon: " + d["name"])
        else:
            d["name"] = WEAPONS[d["name"]]
        if "folder" in d:
            d["folder"] = folder_map[d["folder"]]
        weapons.append(relang(d))
for key in ("i.weapon.brawl", "i.weapon.example-death-ray-prototype", "i.weapon.example-experimental-weapon"):
    d = by_cocid[key]
    d["name"] = WEAPONS[d["name"]]
    if key == "i.weapon.example-experimental-weapon":
        d["system"]["description"]["value"] = EXP_WEAPON_DESC
        d["system"]["description"]["special"] = EXP_WEAPON_SPECIAL
        d["system"]["skill"]["main"]["name"] = "Выберите навык, когда оружие окажется у владельца"
    weapons.append(relang(d))

# --- фобии и мании
statuses = []
sfolder = {}
for d in s("en-wiki-phobias-and-manias.yaml"):
    if d.get("type") == "folder":
        newid = "RuStatFolder%04d" % (len(sfolder) + 1)
        sfolder[d["_id"]] = newid
        d["_id"] = newid
        d["name"] = STATUS_FOLDERS[d["name"]]
        statuses.append(d)
    else:
        ru, desc = STATUSES[d["name"]]
        d["name"] = ru
        d["system"]["description"]["value"] = desc
        d["folder"] = sfolder[d["folder"]]
        statuses.append(relang(d))

# --- таблицы
tables = []
for f in ("en-sanity-tables-examples.yaml", "en-wiki-roll-tables.yaml"):
    for d in s(f):
        d.pop("_id", None)
        # Исправление ошибки upstream: у итоговой таблицы скопирован CoCID таблицы «в реальном времени».
        if d["name"] == "Table VIII: Bouts of Madness - Summary":
            d["flags"]["CoC7"]["cocidFlag"]["id"] = "rt..system-bouts-of-madness-summary"
        if d["name"] not in TABLE_NAMES:
            missing.append("table: " + d["name"])
        else:
            d["name"] = TABLE_NAMES[d["name"]]
        if d.get("description") in TABLE_DESCS:
            d["description"] = TABLE_DESCS[d["description"]]
        for r in d.get("results", []):
            r.pop("_id", None)
            r.pop("documentId", None)
            if r.get("type") == "pack":
                en_target = r.pop("text")
                if en_target in STATUSES:
                    r["documentCoCID"] = "i.status." + en_target.lower()
                    r["text"] = STATUSES[en_target][0]
                elif en_target in TABLE_NAMES:
                    src_cocid = {
                        "Table IX: Sample Phobias": "rt..system-sample-phobias",
                        "Table X: Sample Manias": "rt..system-sample-manias",
                        "Bouts of Madness Table (Realtime)": "rt..bouts-of-madness-table-realtime",
                    }[en_target]
                    r["documentCoCID"] = src_cocid
                    r["text"] = TABLE_NAMES[en_target]
                else:
                    missing.append("table-ref: " + en_target)
                    r["text"] = en_target
                r.pop("documentCollection", None)
            elif r.get("type") == "text":
                if r.get("name") in MADNESS:
                    ru_name, ru_desc = MADNESS[r["name"]]
                    r["name"], r["description"] = ru_name, ru_desc
                else:
                    missing.append("table-text: " + str(r.get("name")))
        tables.append(relang(d))

# новые таблицы предыстории
for cid, name, rows in BACKSTORY_TABLES:
    tables.append({
        "name": name,
        "img": "icons/svg/d20-grey.svg",
        "description": "Русскоязычная таблица модуля coc7-ru-content для шага «Предыстория» мастера создания сыщика.",
        "formula": "1d10",
        "results": [{"type": "text", "img": "icons/svg/d20-black.svg", "name": n, "description": t} for n, t in rows],
        "flags": {"CoC7": {"cocidFlag": {"id": cid, "lang": "ru", "priority": 0}}},
    })

# ------------------------------------------------------------- запись
def dump(name, docs):
    import yaml
    path = os.path.join(OUT, name + ".yaml")
    with io.open(path, "w", encoding="utf-8") as fh:
        fh.write("# Автогенерировано gen_ru_content.py, далее правится вручную.\n")
        for i, d in enumerate(docs):
            if i:
                fh.write("---\n")
            yaml.safe_dump(d, fh, allow_unicode=True, sort_keys=False, default_flow_style=False, width=10000)
    print("%-16s %3d документов -> %s" % (name, len(docs), path))

dump("ru-skills", skills)
dump("ru-occupations", occupations)
dump("ru-archetypes", archetypes)
dump("ru-setups", setups)
dump("ru-weapons", weapons)
dump("ru-statuses", statuses)
dump("ru-items", misc_items)
dump("ru-tables", tables)

if missing:
    print("\nНЕ ПЕРЕВЕДЕНО (%d):" % len(missing))
    for m in missing:
        print(" -", m)
    sys.exit(1)
print("\nВсе строки переведены.")

# словарь имён для lang/ru.json модуля coc7-ru-fixes
keys = {}
en = json.load(open(os.path.join(HERE, "en.json"), encoding="utf-8"))
for k, v in en.items():
    if k.startswith("CoC7.CoCIDFlag.keys.i.skill."):
        if v in SKILLS:
            keys[k] = SKILLS[v]
        else:
            print("нет перевода для ключа", k, v)
for cid, name, _ in BACKSTORY_TABLES:
    keys["CoC7.CoCIDFlag.keys." + cid] = name
json.dump(keys, open(os.path.join(ROOT, "lang", "ru.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2, sort_keys=True)
print("Ключей CoCIDFlag.keys:", len(keys))
