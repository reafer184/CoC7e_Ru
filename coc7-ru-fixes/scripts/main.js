const MODULE_ID = "coc7-ru-fixes";

Hooks.once("ready", () => {
  if (game.i18n.lang !== "ru") return;
  console.info(`${MODULE_ID} | Russian Investigator localization fixes loaded.`);
});
