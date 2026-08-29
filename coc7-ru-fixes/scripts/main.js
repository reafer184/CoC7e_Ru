const MODULE_ID = "coc7-ru-fixes";

const TRANSLATION_FIXES = {
  CoC7: {
    AddArmor: "Добавить броню",
    ClearExperiencePackageName: "Сбросить пакет опыта",
    DeleteBookProgress: "Удалить прогресс изучения книги",
    ExperiencePackageSkill: "Навык из пакета опыта",
    SkillExperiencePackage: "Пакет опыта",
    ModifiedByActiveEffect: "Значение изменено активным эффектом и недоступно для прямого редактирования",

    ActorDataLinked: "Данные персонажа связаны",
    ActorDataNotLinked: "Данные персонажа не связаны",
    ActorIsSyntheticActor: "Это синтетический персонаж",
    ActorIsTokenHint: "Персонаж используется как токен",

    AddSanityLossEncounter: "Добавить событие потери рассудка",
    DeleteSanityLossEncounter: "Удалить событие потери рассудка",
    AddSanityLossImmunity: "Добавить невосприимчивость к потере рассудка",
    DeleteSanityLossImmunity: "Удалить невосприимчивость к потере рассудка",
    SanityLossImmunity: "Невосприимчивость к потере рассудка",

    BackgroundFlagsMythosExperienced: "Получено 5% навыка «Мифы Ктулху» за безумие",
    BackgroundFlagsMythosHardened: "Закалён Мифами Ктулху",

    CriticalWounds: "Тяжёлая рана",
    Dead: "Мёртв",
    Dying: "При смерти",
    Prone: "Сбит с ног",
    Unconscious: "Без сознания",

    AutoCreditValues: "Включить или выключить автоматический расчёт",
    DailySanIconOver: "Сбросить",
    NoSkill: "Навык не назначен",

    Reload: "ЛКМ/ПКМ: добавить или убрать 1 патрон<br>Shift + ЛКМ/ПКМ: перезарядить или разрядить оружие",

    SkillBase: "Базовое значение",
    SkillDetail: "Сведения о навыке",
    SkillExperience: "Опыт",
    SkillOccupation: "Профессия",
    SkillPersonal: "Личные интересы",
    Value: "Итог",

    TradeItem: "Передать или убрать предмет",
    OccupationSkill: "Профессиональный навык",
    ArchetypeSkill: "Навык архетипа",

    ToolTipAutoToggle:
      "<label>Переключатель автоматического расчёта</label><ul><li><strong>ЛКМ</strong>: переключить между автоматическим расчётом и ручным вводом</li></ul>",
    ToolTipDB:
      "<label>Бонус к урону</label><ul><li><strong>ЛКМ</strong>: немедленно бросить кубики</li></ul>"
  }
};

Hooks.once("ready", () => {
  if (game.i18n.lang !== "ru") return;

  foundry.utils.mergeObject(game.i18n.translations, TRANSLATION_FIXES, {
    inplace: true,
    overwrite: true
  });

  console.info(`${MODULE_ID} | Исправления русской локализации загружены.`);
});
