/********************************************** 
 * Translationelicitation_Eng-Confidence Test *
 **********************************************/


// store info about the experiment session:
let expName = 'translationelicitation_eng-confidence';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([-1, -1, -1]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(setupRoutineBegin());
flowScheduler.add(setupRoutineEachFrame());
flowScheduler.add(setupRoutineEnd());
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(descriptionRoutineBegin());
flowScheduler.add(descriptionRoutineEachFrame());
flowScheduler.add(descriptionRoutineEnd());
flowScheduler.add(voluntaryRoutineBegin());
flowScheduler.add(voluntaryRoutineEachFrame());
flowScheduler.add(voluntaryRoutineEnd());
flowScheduler.add(contactRoutineBegin());
flowScheduler.add(contactRoutineEachFrame());
flowScheduler.add(contactRoutineEnd());
flowScheduler.add(confidentialityRoutineBegin());
flowScheduler.add(confidentialityRoutineEachFrame());
flowScheduler.add(confidentialityRoutineEnd());
flowScheduler.add(informationRoutineBegin());
flowScheduler.add(informationRoutineEachFrame());
flowScheduler.add(informationRoutineEnd());
flowScheduler.add(consentRoutineBegin());
flowScheduler.add(consentRoutineEachFrame());
flowScheduler.add(consentRoutineEnd());
flowScheduler.add(languageL1RoutineBegin());
flowScheduler.add(languageL1RoutineEachFrame());
flowScheduler.add(languageL1RoutineEnd());
flowScheduler.add(languageL2RoutineBegin());
flowScheduler.add(languageL2RoutineEachFrame());
flowScheduler.add(languageL2RoutineEnd());
flowScheduler.add(languageL2OralRoutineBegin());
flowScheduler.add(languageL2OralRoutineEachFrame());
flowScheduler.add(languageL2OralRoutineEnd());
flowScheduler.add(languageL2WrittenRoutineBegin());
flowScheduler.add(languageL2WrittenRoutineEachFrame());
flowScheduler.add(languageL2WrittenRoutineEnd());
flowScheduler.add(languageL3RoutineBegin());
flowScheduler.add(languageL3RoutineEachFrame());
flowScheduler.add(languageL3RoutineEnd());
flowScheduler.add(languageL3OralRoutineBegin());
flowScheduler.add(languageL3OralRoutineEachFrame());
flowScheduler.add(languageL3OralRoutineEnd());
flowScheduler.add(languageL3WrittenRoutineBegin());
flowScheduler.add(languageL3WrittenRoutineEachFrame());
flowScheduler.add(languageL3WrittenRoutineEnd());
flowScheduler.add(languageCatalanOralRoutineBegin());
flowScheduler.add(languageCatalanOralRoutineEachFrame());
flowScheduler.add(languageCatalanOralRoutineEnd());
flowScheduler.add(languageCatalanWrittenRoutineBegin());
flowScheduler.add(languageCatalanWrittenRoutineEachFrame());
flowScheduler.add(languageCatalanWrittenRoutineEnd());
flowScheduler.add(languageCatalanTimeRoutineBegin());
flowScheduler.add(languageCatalanTimeRoutineEachFrame());
flowScheduler.add(languageCatalanTimeRoutineEnd());
flowScheduler.add(languageSpanishOralRoutineBegin());
flowScheduler.add(languageSpanishOralRoutineEachFrame());
flowScheduler.add(languageSpanishOralRoutineEnd());
flowScheduler.add(languageSpanishWrittenRoutineBegin());
flowScheduler.add(languageSpanishWrittenRoutineEachFrame());
flowScheduler.add(languageSpanishWrittenRoutineEnd());
flowScheduler.add(languageSpanishTimeRoutineBegin());
flowScheduler.add(languageSpanishTimeRoutineEachFrame());
flowScheduler.add(languageSpanishTimeRoutineEnd());
flowScheduler.add(demoAgeRoutineBegin());
flowScheduler.add(demoAgeRoutineEachFrame());
flowScheduler.add(demoAgeRoutineEnd());
flowScheduler.add(demoSexRoutineBegin());
flowScheduler.add(demoSexRoutineEachFrame());
flowScheduler.add(demoSexRoutineEnd());
flowScheduler.add(demoEducationRoutineBegin());
flowScheduler.add(demoEducationRoutineEachFrame());
flowScheduler.add(demoEducationRoutineEnd());
flowScheduler.add(demoCityRoutineBegin());
flowScheduler.add(demoCityRoutineEachFrame());
flowScheduler.add(demoCityRoutineEnd());
flowScheduler.add(demoVisionRoutineBegin());
flowScheduler.add(demoVisionRoutineEachFrame());
flowScheduler.add(demoVisionRoutineEnd());
flowScheduler.add(demoLanguageRoutineBegin());
flowScheduler.add(demoLanguageRoutineEachFrame());
flowScheduler.add(demoLanguageRoutineEnd());
flowScheduler.add(setupLocationRoutineBegin());
flowScheduler.add(setupLocationRoutineEachFrame());
flowScheduler.add(setupLocationRoutineEnd());
flowScheduler.add(setupNoiseRoutineBegin());
flowScheduler.add(setupNoiseRoutineEachFrame());
flowScheduler.add(setupNoiseRoutineEnd());
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
flowScheduler.add(instructions2RoutineBegin());
flowScheduler.add(instructions2RoutineEachFrame());
flowScheduler.add(instructions2RoutineEnd());
const trialsPracticeCatalanLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsPracticeCatalanLoopBegin(trialsPracticeCatalanLoopScheduler));
flowScheduler.add(trialsPracticeCatalanLoopScheduler);
flowScheduler.add(trialsPracticeCatalanLoopEnd);
const trialsPracticeSpanishLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsPracticeSpanishLoopBegin(trialsPracticeSpanishLoopScheduler));
flowScheduler.add(trialsPracticeSpanishLoopScheduler);
flowScheduler.add(trialsPracticeSpanishLoopEnd);
flowScheduler.add(beginRoutineBegin());
flowScheduler.add(beginRoutineEachFrame());
flowScheduler.add(beginRoutineEnd());
const trialsCatalanLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsCatalanLoopBegin(trialsCatalanLoopScheduler));
flowScheduler.add(trialsCatalanLoopScheduler);
flowScheduler.add(trialsCatalanLoopEnd);
const trialsSpanishLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsSpanishLoopBegin(trialsSpanishLoopScheduler));
flowScheduler.add(trialsSpanishLoopScheduler);
flowScheduler.add(trialsSpanishLoopEnd);
flowScheduler.add(farewellRoutineBegin());
flowScheduler.add(farewellRoutineEachFrame());
flowScheduler.add(farewellRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Sounds/spa_gorrion.wav', 'path': 'Sounds/spa_gorrion.wav'},
    {'name': 'Sounds/spa_avestruz.wav', 'path': 'Sounds/spa_avestruz.wav'},
    {'name': 'Sounds/spa_ventana.wav', 'path': 'Sounds/spa_ventana.wav'},
    {'name': 'Sounds/spa_ladrillo.wav', 'path': 'Sounds/spa_ladrillo.wav'},
    {'name': 'Sounds/spa_pan.wav', 'path': 'Sounds/spa_pan.wav'},
    {'name': 'Sounds/cat_formiga.wav', 'path': 'Sounds/cat_formiga.wav'},
    {'name': 'Sounds/cat_orella.wav', 'path': 'Sounds/cat_orella.wav'},
    {'name': 'Sounds/cat_tobogan.wav', 'path': 'Sounds/cat_tobogan.wav'},
    {'name': 'Sounds/spa_boli.wav', 'path': 'Sounds/spa_boli.wav'},
    {'name': 'Sounds/cat_porta.wav', 'path': 'Sounds/cat_porta.wav'},
    {'name': 'Sounds/spa_platano.wav', 'path': 'Sounds/spa_platano.wav'},
    {'name': 'Trials/02_trials_spanish.xlsx', 'path': 'Trials/02_trials_spanish.xlsx'},
    {'name': 'Sounds/cat_zebra.wav', 'path': 'Sounds/cat_zebra.wav'},
    {'name': 'Sounds/spa_ensalada.wav', 'path': 'Sounds/spa_ensalada.wav'},
    {'name': 'Sounds/spa_coche.wav', 'path': 'Sounds/spa_coche.wav'},
    {'name': 'Sounds/cat_porc.wav', 'path': 'Sounds/cat_porc.wav'},
    {'name': 'Sounds/cat_sol.wav', 'path': 'Sounds/cat_sol.wav'},
    {'name': 'Sounds/spa_cereza.wav', 'path': 'Sounds/spa_cereza.wav'},
    {'name': 'Sounds/spa_biberon.wav', 'path': 'Sounds/spa_biberon.wav'},
    {'name': 'Sounds/spa_cesta.wav', 'path': 'Sounds/spa_cesta.wav'},
    {'name': 'Sounds/spa_pantalon.wav', 'path': 'Sounds/spa_pantalon.wav'},
    {'name': 'Sounds/spa_tambor.wav', 'path': 'Sounds/spa_tambor.wav'},
    {'name': 'Sounds/cat_moto.wav', 'path': 'Sounds/cat_moto.wav'},
    {'name': 'Sounds/spa_caja.wav', 'path': 'Sounds/spa_caja.wav'},
    {'name': 'Sounds/cat_cuc.wav', 'path': 'Sounds/cat_cuc.wav'},
    {'name': 'Sounds/spa_tomate.wav', 'path': 'Sounds/spa_tomate.wav'},
    {'name': 'Sounds/cat_cirera.wav', 'path': 'Sounds/cat_cirera.wav'},
    {'name': 'Sounds/spa_martillo.wav', 'path': 'Sounds/spa_martillo.wav'},
    {'name': 'Sounds/spa_camisa.wav', 'path': 'Sounds/spa_camisa.wav'},
    {'name': 'Sounds/cat_globus.wav', 'path': 'Sounds/cat_globus.wav'},
    {'name': 'Sounds/spa_pato.wav', 'path': 'Sounds/spa_pato.wav'},
    {'name': 'Sounds/spa_tigre.wav', 'path': 'Sounds/spa_tigre.wav'},
    {'name': 'Sounds/spa_mesa.wav', 'path': 'Sounds/spa_mesa.wav'},
    {'name': 'Sounds/cat_flor.wav', 'path': 'Sounds/cat_flor.wav'},
    {'name': 'Sounds/cat_ulleres.wav', 'path': 'Sounds/cat_ulleres.wav'},
    {'name': 'Sounds/spa_nariz.wav', 'path': 'Sounds/spa_nariz.wav'},
    {'name': 'Sounds/spa_naranja.wav', 'path': 'Sounds/spa_naranja.wav'},
    {'name': 'Sounds/cat_camisa.wav', 'path': 'Sounds/cat_camisa.wav'},
    {'name': 'Sounds/spa_cepillo.wav', 'path': 'Sounds/spa_cepillo.wav'},
    {'name': 'Sounds/spa_pajaro.wav', 'path': 'Sounds/spa_pajaro.wav'},
    {'name': 'Sounds/spa_jirafa.wav', 'path': 'Sounds/spa_jirafa.wav'},
    {'name': 'Sounds/spa_caballo.wav', 'path': 'Sounds/spa_caballo.wav'},
    {'name': 'Sounds/spa_arbol.wav', 'path': 'Sounds/spa_arbol.wav'},
    {'name': 'Sounds/cat_forquilla.wav', 'path': 'Sounds/cat_forquilla.wav'},
    {'name': 'Sounds/cat_amanida.wav', 'path': 'Sounds/cat_amanida.wav'},
    {'name': 'Sounds/cat_esponja.wav', 'path': 'Sounds/cat_esponja.wav'},
    {'name': 'Sounds/cat_abella.wav', 'path': 'Sounds/cat_abella.wav'},
    {'name': 'Sounds/spa_ola.wav', 'path': 'Sounds/spa_ola.wav'},
    {'name': 'Sounds/cat_ovella.wav', 'path': 'Sounds/cat_ovella.wav'},
    {'name': 'Trials/02_trials_catalan.xlsx', 'path': 'Trials/02_trials_catalan.xlsx'},
    {'name': 'Sounds/spa_buho.wav', 'path': 'Sounds/spa_buho.wav'},
    {'name': 'Sounds/spa_manzana.wav', 'path': 'Sounds/spa_manzana.wav'},
    {'name': 'Sounds/cat_caixa.wav', 'path': 'Sounds/cat_caixa.wav'},
    {'name': 'Sounds/spa_ombligo.wav', 'path': 'Sounds/spa_ombligo.wav'},
    {'name': 'Sounds/spa_puerta.wav', 'path': 'Sounds/spa_puerta.wav'},
    {'name': 'Sounds/cat_entrepa.wav', 'path': 'Sounds/cat_entrepa.wav'},
    {'name': 'Sounds/cat_dit.wav', 'path': 'Sounds/cat_dit.wav'},
    {'name': 'Sounds/cat_boca.wav', 'path': 'Sounds/cat_boca.wav'},
    {'name': 'Sounds/cat_girafa.wav', 'path': 'Sounds/cat_girafa.wav'},
    {'name': 'Sounds/spa_sol.wav', 'path': 'Sounds/spa_sol.wav'},
    {'name': 'Sounds/spa_burro.wav', 'path': 'Sounds/spa_burro.wav'},
    {'name': 'Sounds/cat_boto.wav', 'path': 'Sounds/cat_boto.wav'},
    {'name': 'Sounds/cat_aixeta.wav', 'path': 'Sounds/cat_aixeta.wav'},
    {'name': 'Sounds/cat_pa.wav', 'path': 'Sounds/cat_pa.wav'},
    {'name': 'Sounds/cat_bibero.wav', 'path': 'Sounds/cat_bibero.wav'},
    {'name': 'Sounds/cat_tren.wav', 'path': 'Sounds/cat_tren.wav'},
    {'name': 'Sounds/cat_bol.wav', 'path': 'Sounds/cat_bol.wav'},
    {'name': 'Sounds/cat_taronja.wav', 'path': 'Sounds/cat_taronja.wav'},
    {'name': 'Sounds/cat_fulla.wav', 'path': 'Sounds/cat_fulla.wav'},
    {'name': 'Sounds/spa_botella.wav', 'path': 'Sounds/spa_botella.wav'},
    {'name': 'Sounds/spa_cubo.wav', 'path': 'Sounds/spa_cubo.wav'},
    {'name': 'Sounds/cat_got.wav', 'path': 'Sounds/cat_got.wav'},
    {'name': 'Sounds/spa_hormiga.wav', 'path': 'Sounds/spa_hormiga.wav'},
    {'name': 'Sounds/cat_casa.wav', 'path': 'Sounds/cat_casa.wav'},
    {'name': 'Sounds/cat_nas.wav', 'path': 'Sounds/cat_nas.wav'},
    {'name': 'Sounds/spa_gallina.wav', 'path': 'Sounds/spa_gallina.wav'},
    {'name': 'Sounds/spa_libro.wav', 'path': 'Sounds/spa_libro.wav'},
    {'name': 'Sounds/cat_lleo.wav', 'path': 'Sounds/cat_lleo.wav'},
    {'name': 'Sounds/spa_moneda.wav', 'path': 'Sounds/spa_moneda.wav'},
    {'name': 'Sounds/cat_papallona.wav', 'path': 'Sounds/cat_papallona.wav'},
    {'name': 'Sounds/spa_estrella.wav', 'path': 'Sounds/spa_estrella.wav'},
    {'name': 'Sounds/spa_pollo.wav', 'path': 'Sounds/spa_pollo.wav'},
    {'name': 'Sounds/cat_plat.wav', 'path': 'Sounds/cat_plat.wav'},
    {'name': 'Sounds/spa_tenedor.wav', 'path': 'Sounds/spa_tenedor.wav'},
    {'name': 'Sounds/cat_estrella.wav', 'path': 'Sounds/cat_estrella.wav'},
    {'name': 'Sounds/spa_panal.wav', 'path': 'Sounds/spa_panal.wav'},
    {'name': 'Sounds/cat_galleda.wav', 'path': 'Sounds/cat_galleda.wav'},
    {'name': 'Sounds/spa_globo.wav', 'path': 'Sounds/spa_globo.wav'},
    {'name': 'Sounds/spa_leche.wav', 'path': 'Sounds/spa_leche.wav'},
    {'name': 'Sounds/cat_arbre.wav', 'path': 'Sounds/cat_arbre.wav'},
    {'name': 'Sounds/cat_berenar.wav', 'path': 'Sounds/cat_berenar.wav'},
    {'name': 'Sounds/cat_estruc.wav', 'path': 'Sounds/cat_estruc.wav'},
    {'name': 'Sounds/spa_muneca.wav', 'path': 'Sounds/spa_muneca.wav'},
    {'name': 'Sounds/spa_chocolate.wav', 'path': 'Sounds/spa_chocolate.wav'},
    {'name': 'Sounds/cat_gat.wav', 'path': 'Sounds/cat_gat.wav'},
    {'name': 'Sounds/spa_cerdo.wav', 'path': 'Sounds/spa_cerdo.wav'},
    {'name': 'Sounds/spa_frambuesa.wav', 'path': 'Sounds/spa_frambuesa.wav'},
    {'name': 'Sounds/cat_patata.wav', 'path': 'Sounds/cat_patata.wav'},
    {'name': 'Sounds/spa_corona.wav', 'path': 'Sounds/spa_corona.wav'},
    {'name': 'Sounds/cat_ma.wav', 'path': 'Sounds/cat_ma.wav'},
    {'name': 'Sounds/cat_mussol.wav', 'path': 'Sounds/cat_mussol.wav'},
    {'name': 'Sounds/cat_guitarra.wav', 'path': 'Sounds/cat_guitarra.wav'},
    {'name': 'Sounds/cat_ull.wav', 'path': 'Sounds/cat_ull.wav'},
    {'name': 'Sounds/spa_patata.wav', 'path': 'Sounds/spa_patata.wav'},
    {'name': 'Sounds/spa_mariposa.wav', 'path': 'Sounds/spa_mariposa.wav'},
    {'name': 'Sounds/spa_dedo.wav', 'path': 'Sounds/spa_dedo.wav'},
    {'name': 'Sounds/cat_raspall.wav', 'path': 'Sounds/cat_raspall.wav'},
    {'name': 'Sounds/spa_bol.wav', 'path': 'Sounds/spa_bol.wav'},
    {'name': 'Sounds/spa_grifo.wav', 'path': 'Sounds/spa_grifo.wav'},
    {'name': 'Sounds/spa_gorro.wav', 'path': 'Sounds/spa_gorro.wav'},
    {'name': 'Sounds/spa_bici.wav', 'path': 'Sounds/spa_bici.wav'},
    {'name': 'Sounds/spa_cuchara.wav', 'path': 'Sounds/spa_cuchara.wav'},
    {'name': 'Sounds/spa_boca.wav', 'path': 'Sounds/spa_boca.wav'},
    {'name': 'Sounds/spa_moto.wav', 'path': 'Sounds/spa_moto.wav'},
    {'name': 'Sounds/spa_osito.wav', 'path': 'Sounds/spa_osito.wav'},
    {'name': 'Sounds/cat_tisores.wav', 'path': 'Sounds/cat_tisores.wav'},
    {'name': 'Sounds/spa_lengua.wav', 'path': 'Sounds/spa_lengua.wav'},
    {'name': 'Sounds/spa_luna.wav', 'path': 'Sounds/spa_luna.wav'},
    {'name': 'Sounds/cat_pernil.wav', 'path': 'Sounds/cat_pernil.wav'},
    {'name': 'Sounds/spa_oveja.wav', 'path': 'Sounds/spa_oveja.wav'},
    {'name': 'Sounds/spa_sandwich.wav', 'path': 'Sounds/spa_sandwich.wav'},
    {'name': 'Sounds/spa_esponja.wav', 'path': 'Sounds/spa_esponja.wav'},
    {'name': 'Sounds/spa_cielo.wav', 'path': 'Sounds/spa_cielo.wav'},
    {'name': 'Sounds/cat_planta.wav', 'path': 'Sounds/cat_planta.wav'},
    {'name': 'Sounds/cat_bou.wav', 'path': 'Sounds/cat_bou.wav'},
    {'name': 'Sounds/cat_ampolla.wav', 'path': 'Sounds/cat_ampolla.wav'},
    {'name': 'Sounds/spa_mono.wav', 'path': 'Sounds/spa_mono.wav'},
    {'name': 'Sounds/cat_gerd.wav', 'path': 'Sounds/cat_gerd.wav'},
    {'name': 'Sounds/spa_pinguino.wav', 'path': 'Sounds/spa_pinguino.wav'},
    {'name': 'Sounds/spa_pez.wav', 'path': 'Sounds/spa_pez.wav'},
    {'name': 'Sounds/spa_boton.wav', 'path': 'Sounds/spa_boton.wav'},
    {'name': 'Sounds/cat_mico.wav', 'path': 'Sounds/cat_mico.wav'},
    {'name': 'Sounds/cat_bolet.wav', 'path': 'Sounds/cat_bolet.wav'},
    {'name': 'Sounds/spa_perro.wav', 'path': 'Sounds/spa_perro.wav'},
    {'name': 'Sounds/cat_lloro.wav', 'path': 'Sounds/cat_lloro.wav'},
    {'name': 'Sounds/cat_cama.wav', 'path': 'Sounds/cat_cama.wav'},
    {'name': 'Sounds/spa_gato.wav', 'path': 'Sounds/spa_gato.wav'},
    {'name': 'Sounds/cat_ungla.wav', 'path': 'Sounds/cat_ungla.wav'},
    {'name': 'Sounds/cat_cavall.wav', 'path': 'Sounds/cat_cavall.wav'},
    {'name': 'Sounds/cat_bici.wav', 'path': 'Sounds/cat_bici.wav'},
    {'name': 'Sounds/cat_mirall.wav', 'path': 'Sounds/cat_mirall.wav'},
    {'name': 'Sounds/spa_zanahoria.wav', 'path': 'Sounds/spa_zanahoria.wav'},
    {'name': 'Sounds/cat_tigre.wav', 'path': 'Sounds/cat_tigre.wav'},
    {'name': 'Sounds/spa_gafas.wav', 'path': 'Sounds/spa_gafas.wav'},
    {'name': 'Sounds/spa_tijeras.wav', 'path': 'Sounds/spa_tijeras.wav'},
    {'name': 'Sounds/spa_pelota.wav', 'path': 'Sounds/spa_pelota.wav'},
    {'name': 'Sounds/cat_jaqueta.wav', 'path': 'Sounds/cat_jaqueta.wav'},
    {'name': 'Sounds/cat_aigua.wav', 'path': 'Sounds/cat_aigua.wav'},
    {'name': 'Sounds/cat_peu.wav', 'path': 'Sounds/cat_peu.wav'},
    {'name': 'Sounds/spa_bocadillo.wav', 'path': 'Sounds/spa_bocadillo.wav'},
    {'name': 'Sounds/cat_colom.wav', 'path': 'Sounds/cat_colom.wav'},
    {'name': 'Sounds/spa_tobogan.wav', 'path': 'Sounds/spa_tobogan.wav'},
    {'name': 'Sounds/spa_barco.wav', 'path': 'Sounds/spa_barco.wav'},
    {'name': 'Sounds/spa_lapiz.wav', 'path': 'Sounds/spa_lapiz.wav'},
    {'name': 'Sounds/cat_llibre.wav', 'path': 'Sounds/cat_llibre.wav'},
    {'name': 'Sounds/spa_pastel.wav', 'path': 'Sounds/spa_pastel.wav'},
    {'name': 'Sounds/cat_cotxe.wav', 'path': 'Sounds/cat_cotxe.wav'},
    {'name': 'Sounds/spa_toro.wav', 'path': 'Sounds/spa_toro.wav'},
    {'name': 'Sounds/spa_pluma.wav', 'path': 'Sounds/spa_pluma.wav'},
    {'name': 'Sounds/cat_xocolata.wav', 'path': 'Sounds/cat_xocolata.wav'},
    {'name': 'Sounds/cat_tomaquet.wav', 'path': 'Sounds/cat_tomaquet.wav'},
    {'name': 'Sounds/cat_vaixell.wav', 'path': 'Sounds/cat_vaixell.wav'},
    {'name': 'Sounds/spa_caracol.wav', 'path': 'Sounds/spa_caracol.wav'},
    {'name': 'Sounds/cat_pollastre.wav', 'path': 'Sounds/cat_pollastre.wav'},
    {'name': 'Sounds/cat_onada.wav', 'path': 'Sounds/cat_onada.wav'},
    {'name': 'Trials/01_trials_practice_catalan.xlsx', 'path': 'Trials/01_trials_practice_catalan.xlsx'},
    {'name': 'Sounds/spa_gusano.wav', 'path': 'Sounds/spa_gusano.wav'},
    {'name': 'Sounds/spa_mano.wav', 'path': 'Sounds/spa_mano.wav'},
    {'name': 'Sounds/spa_pierna.wav', 'path': 'Sounds/spa_pierna.wav'},
    {'name': 'Sounds/spa_tren.wav', 'path': 'Sounds/spa_tren.wav'},
    {'name': 'Sounds/cat_moneda.wav', 'path': 'Sounds/cat_moneda.wav'},
    {'name': 'Sounds/cat_gorra.wav', 'path': 'Sounds/cat_gorra.wav'},
    {'name': 'Sounds/spa_chaqueta.wav', 'path': 'Sounds/spa_chaqueta.wav'},
    {'name': 'Sounds/spa_pie.wav', 'path': 'Sounds/spa_pie.wav'},
    {'name': 'Sounds/spa_plato.wav', 'path': 'Sounds/spa_plato.wav'},
    {'name': 'Sounds/cat_ploma.wav', 'path': 'Sounds/cat_ploma.wav'},
    {'name': 'Sounds/spa_loro.wav', 'path': 'Sounds/spa_loro.wav'},
    {'name': 'Sounds/cat_samarreta.wav', 'path': 'Sounds/cat_samarreta.wav'},
    {'name': 'Sounds/cat_bolquer.wav', 'path': 'Sounds/cat_bolquer.wav'},
    {'name': 'Sounds/spa_calcetin.wav', 'path': 'Sounds/spa_calcetin.wav'},
    {'name': 'Sounds/spa_brazo.wav', 'path': 'Sounds/spa_brazo.wav'},
    {'name': 'Sounds/spa_camiseta.wav', 'path': 'Sounds/spa_camiseta.wav'},
    {'name': 'Sounds/cat_galeta.wav', 'path': 'Sounds/cat_galeta.wav'},
    {'name': 'Sounds/cat_poma.wav', 'path': 'Sounds/cat_poma.wav'},
    {'name': 'Sounds/spa_cebra.wav', 'path': 'Sounds/spa_cebra.wav'},
    {'name': 'Trials/01_trials_practice_spanish.xlsx', 'path': 'Trials/01_trials_practice_spanish.xlsx'},
    {'name': 'Sounds/spa_galleta.wav', 'path': 'Sounds/spa_galleta.wav'},
    {'name': 'Sounds/spa_flor.wav', 'path': 'Sounds/spa_flor.wav'},
    {'name': 'Sounds/spa_guitarra.wav', 'path': 'Sounds/spa_guitarra.wav'},
    {'name': 'Sounds/cat_pingui.wav', 'path': 'Sounds/cat_pingui.wav'},
    {'name': 'Sounds/spa_leon.wav', 'path': 'Sounds/spa_leon.wav'},
    {'name': 'Sounds/cat_lluna.wav', 'path': 'Sounds/cat_lluna.wav'},
    {'name': 'Sounds/cat_corona.wav', 'path': 'Sounds/cat_corona.wav'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.ERROR);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.1.3';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.co/submissions/complete?cc=61C2960C', 'https://app.prolific.co/submissions/complete?cc=61C2960C');

  return Scheduler.Event.NEXT;
}


var setupClock;
var setupTitleText;
var setupText;
var setupNextText;
var setupNextKey;
var welcomeClock;
var welcomeTextTitle;
var welcomeText;
var welcomeNextText;
var welcomeNextKey;
var descriptionClock;
var descriptionTitleText;
var descriptionText;
var descriptionNextText;
var descriptionNextKey;
var voluntaryClock;
var voluntaryTitleText;
var voluntaryText;
var voluntaryNextText;
var voluntaryNextKey;
var contactClock;
var contactTitleText;
var contactText;
var contactNextText;
var contactNextKey;
var confidentialityClock;
var confidentialityTitleText;
var confidentialityText;
var confidentialityNextText;
var confidentialityNextKey;
var informationClock;
var informationTitleText;
var informationText;
var informationNextText;
var infomationNextKey;
var consentClock;
var consentTitleText;
var consentText;
var consentTextNext;
var consentNextKey;
var languageL1Clock;
var languageL1TitleText;
var languageL1Text;
var languageL1NextText;
var languageL1Key;
var languageL2Clock;
var languageL2TitleText;
var languageL2Text;
var languageL2NextText;
var languageL2InputText;
var languageL2OralClock;
var languageL2OralTitleText;
var languageL2OralText;
var languageL2OralNextText;
var languageL2OralKey;
var languageL2WrittenClock;
var languageL2WrittenTitleText;
var languageL2WrittenText;
var languageL2WrittenNextText;
var languageL2WrittenKey;
var languageL3Clock;
var languageL3TitleText;
var languageL3Text;
var languageL3NextText;
var languageL3InputText;
var languageL3OralClock;
var languageL3OralTitleText;
var languageL3OralText;
var languageL3OralNextText;
var languageL3OralKey;
var languageL3WrittenClock;
var languageL3WrittenTitleText;
var languageL3WrittenText;
var languageL3WrittenNextText;
var languageL3WrittenKey;
var languageCatalanOralClock;
var languageCatalanOralTitleText;
var languageCatalanOralText;
var languageCatalanOralNextText;
var languageCatalanOralKey;
var languageCatalanWrittenClock;
var languageCatalanWrittenTitleText;
var languageCatalanWrittenText;
var languageCatalanWrittenNextText;
var languageCatalanWrittenKey;
var languageCatalanTimeClock;
var languageCatalanTimeTitleText;
var languageCatalanTimeText;
var languageCatalanTimeNextText;
var languageCatalanTimeKey;
var languageSpanishOralClock;
var languageSpanishOralTitleText;
var languageSpanishOralText;
var languageSpanishOralNextText;
var languageSpanishOralKey;
var languageSpanishWrittenClock;
var languageSpanishTitleText;
var languageSpanishWrittenText;
var languageSpanishNextText;
var languageSpanishWrittenKey;
var languageSpanishTimeClock;
var languageSpanishTimeTitleText;
var languageSpanishTimeText;
var languageSpanishTimeNextText;
var languageSpanishTimeKey;
var demoAgeClock;
var demoAgeTitleText;
var demoAgeText;
var demoAgeNextText;
var demoAgeInputText;
var demoSexClock;
var demoSexTitleText;
var demoSexText;
var demoSexNextText;
var demoSexKey;
var demoEducationClock;
var demoEducationTitleText;
var demoEducationText;
var demoEducationNextText;
var demoEducationKey;
var demoCityClock;
var demoCityTitleText;
var demoCityText;
var demoCityNextText;
var demoCityInputText;
var demoVisionClock;
var demoVisionTitleText;
var demoVisionText;
var demoTextNextText;
var demoVisionKey;
var demoLanguageClock;
var demoLanguageTitleText;
var demoLanguageText;
var demoLanguageNextText;
var demoLanguageKey;
var setupLocationClock;
var setupLocationTitleText;
var setupLocationText;
var setupLocationNextText;
var setupLocationKey;
var setupNoiseClock;
var setupNoiseTitleText;
var setupNoiseText;
var setupNoiseNextText;
var setupNoiseKey;
var instructionsClock;
var instructionsTitleText;
var instructionsText;
var instructionsNextText;
var instructionsKey;
var instructions2Clock;
var instructions2TitleText;
var instructions2Text;
var isntructions2NextText;
var isntructions2Key;
var fixationClock;
var fixationText;
var trialClock;
var trialText;
var trialSound;
var beginClock;
var beginText;
var beginNextText;
var farewellClock;
var farewellText;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "setup"
  setupClock = new util.Clock();
  setupTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupTitleText',
    text: 'SETUP',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  setupText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupText',
    text: 'If possible, use Chrome or Mozilla Firefox\n\nUse a computer or a laptop (not a tablet or a phone)\n\nUse headphones \n\nClose all tabs other than this one\n\nDo not switch tabs in the browser\n\nIf, for any reason, you restart the study (e.g. because you reloaded the website or an internet failure), let us know by sending an email to serene.siow@psy.ox.ac.uk.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  setupNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupNextText',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  setupNextKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  
  
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  welcomeTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcomeTextTitle',
    text: 'WELCOME',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  welcomeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcomeText',
    text: 'This is a study designed by researchers from the Universitat Pompeu Fabra (Barcelona, Spain) and the University of Oxford (Oxford, UK). \n\nThe aim of the study is to investigate how toddlers and adults process foreign words. The audios you will listen to throughout this study were recorded in a baby-directed style.\n\nYou have been invited to participate as you are between 18 and 25 years old, and a English native speaker with no knowledge of Spanish or Catalan.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  welcomeNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcomeNextText',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  welcomeNextKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "description"
  descriptionClock = new util.Clock();
  descriptionTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'descriptionTitleText',
    text: 'OVERVIEW',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  descriptionText = new visual.TextStim({
    win: psychoJS.window,
    name: 'descriptionText',
    text: 'Firstly, you will be asked to complete a BRIEF QUESTIONNAIRE (your language profile, level of education, etc.).\n\nIn the main STUDY, you will listen to a series of SPANISH or CATALAN words. Your task will be to GUESS the TRANSLATION of each word in ENGLISH and TYPE your answer using the computer keyboard.\n\nThis should take around 30 minutes.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  descriptionNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'descriptionNextText',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  descriptionNextKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "voluntary"
  voluntaryClock = new util.Clock();
  voluntaryTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'voluntaryTitleText',
    text: 'DO I HAVE TO TAKE PART?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  voluntaryText = new visual.TextStim({
    win: psychoJS.window,
    name: 'voluntaryText',
    text: 'Participation in this study is absolutely VOLUNTARY. If you do decide to take part, you may withdraw at any point for any reason by pressing the ESC button. However, we are only able to reimburse participants who complete the full task.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  voluntaryNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'voluntaryNextText',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  voluntaryNextKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "contact"
  contactClock = new util.Clock();
  contactTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'contactTitleText',
    text: 'CONTACT DETAILS',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  contactText = new visual.TextStim({
    win: psychoJS.window,
    name: 'contactText',
    text: 'If you have any questions about this study, please contact the researchers.\n\nEmail: serene.siow@psy.ox.ac.uk\n\nPrincipal Investigators: Núria Sebastian-Galles and Kim Plunkett\n\nResearchers: Gonzalo García-Castro and Serene Siow\n\nCenter for Brain and Cognition, Universitat Pompeu Fabra\n\nDepartment of Experimental Psychology, University of Oxford',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  contactNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'contactNextText',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  contactNextKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "confidentiality"
  confidentialityClock = new util.Clock();
  confidentialityTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'confidentialityTitleText',
    text: 'HOW WILL MY DATA BE USED?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  confidentialityText = new visual.TextStim({
    win: psychoJS.window,
    name: 'confidentialityText',
    text: 'Your answers will be completely ANONYMOUS, and we will take all reasonable measures to ensure that they remain confidential.\n\nYour DATA WILL BE STORED in a password-protected file and MAY BE USED in academic publications IN AN ANONYMISED FORM. Your IP address will NOT BE STORED. Research data will be stored for a minimum of three years after publication or public release.\n\nWe would also like your permission to use your anonymised data in future studies, and to SHARE data with other researchers (e.g. in online databases). Any personal information that could identify you will be REMOVED or REPLACED before files are SHARED with other researchers or results are MADE PUBLIC.\n\nThis project has received ethics clearance through the University of Oxford Central University Research Ethics Committee, R60939/RE005.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  confidentialityNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'confidentialityNextText',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  confidentialityNextKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "information"
  informationClock = new util.Clock();
  informationTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'informationTitleText',
    text: 'NEED FOR INFORMATION?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  informationText = new visual.TextStim({
    win: psychoJS.window,
    name: 'informationText',
    text: 'If you have a concern about any aspect of this study, please speak to Serene Siow (serene.siow@psy.ox.ac.uk), and we will do our best to answer your query.\n\nIf you remain unhappy or wish to make a formal complaint, please contact the Chair of the Research Ethics Committee at the University of Oxford.\nChair, Medical Sciences Interdivisional Research Ethics Committee\nEmail: ethics@medsci.ox.ac.uk',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  informationNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'informationNextText',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  infomationNextKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  consentTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'consentTitleText',
    text: 'INFORMED CONSENT',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  consentText = new visual.TextStim({
    win: psychoJS.window,
    name: 'consentText',
    text: 'BY PRESSING SPACE, I certify that I am 18 years of age or over. I agree to participate in the study described. I have made this decision based on the information I have read in the consent information. I have had the opportunity to receive any additional details I wanted about the study and understand that I may ask questions in the future. I understand that I may withdraw this consent at any time.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  consentTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'consentTextNext',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  consentNextKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageL1"
  languageL1Clock = new util.Clock();
  languageL1TitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL1TitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageL1Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL1Text',
    text: 'What is your NATIVE language?\n\ne) English\ns) Spanish\nc) Catalan\no) Other',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageL1NextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL1NextText',
    text: 'Press the corresponding letter >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageL1Key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageL2"
  languageL2Clock = new util.Clock();
  languageL2TitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2TitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageL2Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2Text',
    text: 'Do you know any other SECOND LANGUAGE, different than the one you indicated before? If yes, type which one and press RETURN. If no, press RETURN without writing anything.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageL2NextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2NextText',
    text: 'Press RETURN to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageL2InputText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2InputText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "languageL2Oral"
  languageL2OralClock = new util.Clock();
  languageL2OralTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2OralTitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageL2OralText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2OralText',
    text: 'On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in your SECOND LANGUAGE?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageL2OralNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2OralNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageL2OralKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageL2Written"
  languageL2WrittenClock = new util.Clock();
  languageL2WrittenTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2WrittenTitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageL2WrittenText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2WrittenText',
    text: 'On a scale of 1-5, how would you rate your WRITTEN proficiency in your SECOND LANGUAGE?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageL2WrittenNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2WrittenNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageL2WrittenKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageL3"
  languageL3Clock = new util.Clock();
  languageL3TitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3TitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageL3Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3Text',
    text: 'Do you know any other THIRD LANGUAGE, different than the ones you indicated before? If yes, type which one(s) and press RETURN. If no, press RETURN leaving it blank.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageL3NextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3NextText',
    text: 'Press RETURN to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageL3InputText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3InputText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "languageL3Oral"
  languageL3OralClock = new util.Clock();
  languageL3OralTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3OralTitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageL3OralText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3OralText',
    text: 'On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in your THIRD LANGUAGE?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native / I am native',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageL3OralNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3OralNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageL3OralKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageL3Written"
  languageL3WrittenClock = new util.Clock();
  languageL3WrittenTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3WrittenTitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageL3WrittenText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3WrittenText',
    text: 'On a scale of 1-5, how would you rate your WRITTEN proficiency in your THIRD LANGUAGE?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageL3WrittenNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3WrittenNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageL3WrittenKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageCatalanOral"
  languageCatalanOralClock = new util.Clock();
  languageCatalanOralTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanOralTitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageCatalanOralText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanOralText',
    text: 'On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in CATALAN?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageCatalanOralNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanOralNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageCatalanOralKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageCatalanWritten"
  languageCatalanWrittenClock = new util.Clock();
  languageCatalanWrittenTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanWrittenTitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageCatalanWrittenText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanWrittenText',
    text: 'On a scale of 1-5, how would you rate your WRITTEN proficiency in CATALAN?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageCatalanWrittenNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanWrittenNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageCatalanWrittenKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageCatalanTime"
  languageCatalanTimeClock = new util.Clock();
  languageCatalanTimeTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanTimeTitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageCatalanTimeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanTimeText',
    text: 'How long have you spent in any REGION where CATALAN is spoken (Catalonia, Valencia, Balearic Islands), including your childhood? Pick the option that best describes your situation:\n\n1) Never or less than 1 month\n2) Between 1 and 3 months\n3) I used to spend holidays there\n4) I lived there for less than 6 months\n5) I lived there for 6 months or longer',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageCatalanTimeNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanTimeNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageCatalanTimeKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageSpanishOral"
  languageSpanishOralClock = new util.Clock();
  languageSpanishOralTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishOralTitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageSpanishOralText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishOralText',
    text: 'On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in SPANISH?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageSpanishOralNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishOralNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageSpanishOralKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageSpanishWritten"
  languageSpanishWrittenClock = new util.Clock();
  languageSpanishTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishTitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageSpanishWrittenText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishWrittenText',
    text: 'On a scale of 1-5, how would you rate your WRITTEN proficiency in SPANISH?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageSpanishNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageSpanishWrittenKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageSpanishTime"
  languageSpanishTimeClock = new util.Clock();
  languageSpanishTimeTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishTimeTitleText',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  languageSpanishTimeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishTimeText',
    text: 'How long have you spent in any REGION where SPANISH is spoken (Spain, South America), including your childhood? Pick the option that best describes your situation:\n\n1) Never or less than 1 month\n2) Between 1 and 3 months\n3) I used to spend holidays there\n4) I lived there for less than 6 months\n5) I lived there for 6 months or longer',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  languageSpanishTimeNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishTimeNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  languageSpanishTimeKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "demoAge"
  demoAgeClock = new util.Clock();
  demoAgeTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoAgeTitleText',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  demoAgeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoAgeText',
    text: 'Please, type your age (in years) and then press RETURN:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  demoAgeNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoAgeNextText',
    text: 'Press RETURN to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  demoAgeInputText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoAgeInputText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "demoSex"
  demoSexClock = new util.Clock();
  demoSexTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoSexTitleText',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  demoSexText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoSexText',
    text: 'Sex:\n\nf) Female\nm) Male\no) Other',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  demoSexNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoSexNextText',
    text: 'Press the corresponding letter >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  demoSexKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "demoEducation"
  demoEducationClock = new util.Clock();
  demoEducationTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoEducationTitleText',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  demoEducationText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoEducationText',
    text: 'What is your highest level of EDUCATIONAL ACHIEVEMENT?\n\n1) No qualifications\n2) Left school at 16 with GCSE or equivalent\n3) Left school at 18 with A-Levels or equivalent\n4) University degree or equivalent\n5) Vocational training',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  demoEducationNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoEducationNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  demoEducationKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "demoCity"
  demoCityClock = new util.Clock();
  demoCityTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoCityTitleText',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  demoCityText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoCityText',
    text: 'What CITY do you live in? Type it and press RETURN to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  demoCityNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoCityNextText',
    text: 'Press RETURN to continue >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  demoCityInputText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoCityInputText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "demoVision"
  demoVisionClock = new util.Clock();
  demoVisionTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoVisionTitleText',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  demoVisionText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoVisionText',
    text: 'Do you have normal or corrected-to-normal VISION?\n\ny) Yes\nn) No',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  demoTextNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoTextNextText',
    text: 'Press the corresponding letter >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  demoVisionKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "demoLanguage"
  demoLanguageClock = new util.Clock();
  demoLanguageTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoLanguageTitleText',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  demoLanguageText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoLanguageText',
    text: 'Have you been diagnosed with any LANGUAGE (e.g., DYSLEXIA) OR HEARING IMPAIRMENT?\n\ny) Yes\nn) No',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  demoLanguageNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoLanguageNextText',
    text: 'Press the corresponding letter >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  demoLanguageKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "setupLocation"
  setupLocationClock = new util.Clock();
  setupLocationTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupLocationTitleText',
    text: 'SETUP',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  setupLocationText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupLocationText',
    text: 'WHERE are you completing this study?\n\n1) At home\n2) At the library\n3) At a cafe or restaurant\n4) At a friend’s house\n5) At school\n6) At work\n7) Other',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  setupLocationNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupLocationNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  setupLocationKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "setupNoise"
  setupNoiseClock = new util.Clock();
  setupNoiseTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupNoiseTitleText',
    text: 'SETUP',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  setupNoiseText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupNoiseText',
    text: 'How NOISY was the environment in which you completed the experiment? \n\n1) Very quiet (like a library)\n2) Somewhat quiet (like an office)\n3) Somewhat noisy (like being at the park)\n4) Very noisy (like being at a busy street)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  setupNoiseNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupNoiseNextText',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  setupNoiseKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  instructionsTitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionsTitleText',
    text: 'INSTRUCTIONS',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  instructionsText = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionsText',
    text: 'You will listen to some words through your headphones.\n\nWords are in Catalan or Spanish and were recorded in a baby-directed manner. You will have to GUESS and TYPE the TRANSLATION of each word IN ENGLISH.\n\nStart typing as soon as you come up with an answer. It is probable that you do not know it. Type the translation you think is most likely to be correct. You MUST type an answer FOR EACH WORD.\n\nYou can use BACKSPACE to correct any typing errors, as you would normally.\n\nAfter typing the word, press RETURN to continue to the next word.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  instructionsNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionsNextText',
    text: 'NEXT, YOU WILL COMPLETE 5 PRACTICE TRIALS\n\nPress SPACE to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  instructionsKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions2"
  instructions2Clock = new util.Clock();
  instructions2TitleText = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions2TitleText',
    text: 'INSTRUCTIONS',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  instructions2Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions2Text',
    text: 'You may adjust the volume during these trials to avoid having to do it during the main experiment. Make sure words are loud enough for you to hear them clearly.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  isntructions2NextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'isntructions2NextText',
    text: 'Press SPACE to start 5 practice trials >',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -2.0 
  });
  
  isntructions2Key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixationText = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixationText',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  trialText = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  trialSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  trialSound.setVolume(1.0);
  // Initialize components for Routine "begin"
  beginClock = new util.Clock();
  beginText = new visual.TextStim({
    win: psychoJS.window,
    name: 'beginText',
    text: 'You have completed the PRACTICE trials',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  beginNextText = new visual.TextStim({
    win: psychoJS.window,
    name: 'beginNextText',
    text: 'Press SPACE to start >',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('yellow'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "farewell"
  farewellClock = new util.Clock();
  farewellText = new visual.TextStim({
    win: psychoJS.window,
    name: 'farewellText',
    text: 'Congratulations! You have finished.\n\nTHANKS A LOT FOR YOUR PARTICIPATION.\n\nIf you have any questions, get in touch with us at serene.siow@ox.ac.uk\n\nPress SPACE to be redirected to Prolific.\n\nPlease, wait to be redirected to Prolific, otherwise you may not receive your credit.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _setupNextKey_allKeys;
var setupComponents;
function setupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'setup'-------
    t = 0;
    setupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    setupNextKey.keys = undefined;
    setupNextKey.rt = undefined;
    _setupNextKey_allKeys = [];
    setupText.alignText = "left";
    welcomeText.alignText = "left";
    descriptionText.alignText = "left";
    voluntaryText.alignText = "left";
    contactText.alignText = "left";
    confidentialityText.alignText = "left";
    informationText.alignText = "left";
    consentText.alignText = "left";
    languageL1Text.alignText = "left";
    languageL2Text.alignText = "left";
    languageL2OralText.alignText = "left";
    languageL2WrittenText.alignText = "left";
    languageL3Text.alignText = "left";
    languageL3OralText.alignText = "left";
    languageL3WrittenText.alignText = "left";
    languageCatalanOralText.alignText = "left";
    languageCatalanWrittenText.alignText = "left";
    languageCatalanTimeText.alignText = "left";
    languageSpanishOralText.alignText = "left";
    languageSpanishWrittenText.alignText = "left";
    languageSpanishTimeText.alignText = "left";
    demoAgeText.alignText = "left";
    demoSexText.alignText = "left";
    demoEducationText.alignText = "left";
    demoCityText.alignText = "left";
    demoVisionText.alignText = "left";
    demoLanguageText.alignText = "left";
    setupLocationText.alignText = "left";
    setupNoiseText.alignText = "left";
    instructionsText.alignText = "left";
    instructions2Text.alignText = "left";
    
    // keep track of which components have finished
    setupComponents = [];
    setupComponents.push(setupTitleText);
    setupComponents.push(setupText);
    setupComponents.push(setupNextText);
    setupComponents.push(setupNextKey);
    
    setupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function setupRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'setup'-------
    // get current time
    t = setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *setupTitleText* updates
    if (t >= 0.0 && setupTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupTitleText.tStart = t;  // (not accounting for frame time here)
      setupTitleText.frameNStart = frameN;  // exact frame index
      
      setupTitleText.setAutoDraw(true);
    }

    
    // *setupText* updates
    if (t >= 0.0 && setupText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupText.tStart = t;  // (not accounting for frame time here)
      setupText.frameNStart = frameN;  // exact frame index
      
      setupText.setAutoDraw(true);
    }

    
    // *setupNextText* updates
    if (t >= 0.0 && setupNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupNextText.tStart = t;  // (not accounting for frame time here)
      setupNextText.frameNStart = frameN;  // exact frame index
      
      setupNextText.setAutoDraw(true);
    }

    
    // *setupNextKey* updates
    if (t >= 0.0 && setupNextKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupNextKey.tStart = t;  // (not accounting for frame time here)
      setupNextKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { setupNextKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { setupNextKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { setupNextKey.clearEvents(); });
    }

    if (setupNextKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = setupNextKey.getKeys({keyList: ['space'], waitRelease: false});
      _setupNextKey_allKeys = _setupNextKey_allKeys.concat(theseKeys);
      if (_setupNextKey_allKeys.length > 0) {
        setupNextKey.keys = _setupNextKey_allKeys[_setupNextKey_allKeys.length - 1].name;  // just the last key pressed
        setupNextKey.rt = _setupNextKey_allKeys[_setupNextKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    setupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function setupRoutineEnd() {
  return async function () {
    //------Ending Routine 'setup'-------
    setupComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    setupNextKey.stop();
    // the Routine "setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _welcomeNextKey_allKeys;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'welcome'-------
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    welcomeNextKey.keys = undefined;
    welcomeNextKey.rt = undefined;
    _welcomeNextKey_allKeys = [];
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(welcomeTextTitle);
    welcomeComponents.push(welcomeText);
    welcomeComponents.push(welcomeNextText);
    welcomeComponents.push(welcomeNextKey);
    
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'welcome'-------
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcomeTextTitle* updates
    if (t >= 0.0 && welcomeTextTitle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcomeTextTitle.tStart = t;  // (not accounting for frame time here)
      welcomeTextTitle.frameNStart = frameN;  // exact frame index
      
      welcomeTextTitle.setAutoDraw(true);
    }

    
    // *welcomeText* updates
    if (t >= 0.0 && welcomeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcomeText.tStart = t;  // (not accounting for frame time here)
      welcomeText.frameNStart = frameN;  // exact frame index
      
      welcomeText.setAutoDraw(true);
    }

    
    // *welcomeNextText* updates
    if (t >= 0.0 && welcomeNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcomeNextText.tStart = t;  // (not accounting for frame time here)
      welcomeNextText.frameNStart = frameN;  // exact frame index
      
      welcomeNextText.setAutoDraw(true);
    }

    
    // *welcomeNextKey* updates
    if (t >= 0.0 && welcomeNextKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcomeNextKey.tStart = t;  // (not accounting for frame time here)
      welcomeNextKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcomeNextKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcomeNextKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcomeNextKey.clearEvents(); });
    }

    if (welcomeNextKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcomeNextKey.getKeys({keyList: ['space'], waitRelease: false});
      _welcomeNextKey_allKeys = _welcomeNextKey_allKeys.concat(theseKeys);
      if (_welcomeNextKey_allKeys.length > 0) {
        welcomeNextKey.keys = _welcomeNextKey_allKeys[_welcomeNextKey_allKeys.length - 1].name;  // just the last key pressed
        welcomeNextKey.rt = _welcomeNextKey_allKeys[_welcomeNextKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd() {
  return async function () {
    //------Ending Routine 'welcome'-------
    welcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(welcomeNextKey.corr, level);
    }
    psychoJS.experiment.addData('welcomeNextKey.keys', welcomeNextKey.keys);
    if (typeof welcomeNextKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('welcomeNextKey.rt', welcomeNextKey.rt);
        routineTimer.reset();
        }
    
    welcomeNextKey.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _descriptionNextKey_allKeys;
var descriptionComponents;
function descriptionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'description'-------
    t = 0;
    descriptionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    descriptionNextKey.keys = undefined;
    descriptionNextKey.rt = undefined;
    _descriptionNextKey_allKeys = [];
    // keep track of which components have finished
    descriptionComponents = [];
    descriptionComponents.push(descriptionTitleText);
    descriptionComponents.push(descriptionText);
    descriptionComponents.push(descriptionNextText);
    descriptionComponents.push(descriptionNextKey);
    
    descriptionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function descriptionRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'description'-------
    // get current time
    t = descriptionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *descriptionTitleText* updates
    if (t >= 0.0 && descriptionTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      descriptionTitleText.tStart = t;  // (not accounting for frame time here)
      descriptionTitleText.frameNStart = frameN;  // exact frame index
      
      descriptionTitleText.setAutoDraw(true);
    }

    
    // *descriptionText* updates
    if (t >= 0.0 && descriptionText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      descriptionText.tStart = t;  // (not accounting for frame time here)
      descriptionText.frameNStart = frameN;  // exact frame index
      
      descriptionText.setAutoDraw(true);
    }

    
    // *descriptionNextText* updates
    if (t >= 0.0 && descriptionNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      descriptionNextText.tStart = t;  // (not accounting for frame time here)
      descriptionNextText.frameNStart = frameN;  // exact frame index
      
      descriptionNextText.setAutoDraw(true);
    }

    
    // *descriptionNextKey* updates
    if (t >= 0.0 && descriptionNextKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      descriptionNextKey.tStart = t;  // (not accounting for frame time here)
      descriptionNextKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { descriptionNextKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { descriptionNextKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { descriptionNextKey.clearEvents(); });
    }

    if (descriptionNextKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = descriptionNextKey.getKeys({keyList: ['space'], waitRelease: false});
      _descriptionNextKey_allKeys = _descriptionNextKey_allKeys.concat(theseKeys);
      if (_descriptionNextKey_allKeys.length > 0) {
        descriptionNextKey.keys = _descriptionNextKey_allKeys[_descriptionNextKey_allKeys.length - 1].name;  // just the last key pressed
        descriptionNextKey.rt = _descriptionNextKey_allKeys[_descriptionNextKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    descriptionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function descriptionRoutineEnd() {
  return async function () {
    //------Ending Routine 'description'-------
    descriptionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    descriptionNextKey.stop();
    // the Routine "description" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _voluntaryNextKey_allKeys;
var voluntaryComponents;
function voluntaryRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'voluntary'-------
    t = 0;
    voluntaryClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    voluntaryNextKey.keys = undefined;
    voluntaryNextKey.rt = undefined;
    _voluntaryNextKey_allKeys = [];
    // keep track of which components have finished
    voluntaryComponents = [];
    voluntaryComponents.push(voluntaryTitleText);
    voluntaryComponents.push(voluntaryText);
    voluntaryComponents.push(voluntaryNextText);
    voluntaryComponents.push(voluntaryNextKey);
    
    voluntaryComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function voluntaryRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'voluntary'-------
    // get current time
    t = voluntaryClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *voluntaryTitleText* updates
    if (t >= 0.0 && voluntaryTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      voluntaryTitleText.tStart = t;  // (not accounting for frame time here)
      voluntaryTitleText.frameNStart = frameN;  // exact frame index
      
      voluntaryTitleText.setAutoDraw(true);
    }

    
    // *voluntaryText* updates
    if (t >= 0.0 && voluntaryText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      voluntaryText.tStart = t;  // (not accounting for frame time here)
      voluntaryText.frameNStart = frameN;  // exact frame index
      
      voluntaryText.setAutoDraw(true);
    }

    
    // *voluntaryNextText* updates
    if (t >= 0.0 && voluntaryNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      voluntaryNextText.tStart = t;  // (not accounting for frame time here)
      voluntaryNextText.frameNStart = frameN;  // exact frame index
      
      voluntaryNextText.setAutoDraw(true);
    }

    
    // *voluntaryNextKey* updates
    if (t >= 0.0 && voluntaryNextKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      voluntaryNextKey.tStart = t;  // (not accounting for frame time here)
      voluntaryNextKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { voluntaryNextKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { voluntaryNextKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { voluntaryNextKey.clearEvents(); });
    }

    if (voluntaryNextKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = voluntaryNextKey.getKeys({keyList: ['space'], waitRelease: false});
      _voluntaryNextKey_allKeys = _voluntaryNextKey_allKeys.concat(theseKeys);
      if (_voluntaryNextKey_allKeys.length > 0) {
        voluntaryNextKey.keys = _voluntaryNextKey_allKeys[_voluntaryNextKey_allKeys.length - 1].name;  // just the last key pressed
        voluntaryNextKey.rt = _voluntaryNextKey_allKeys[_voluntaryNextKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    voluntaryComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function voluntaryRoutineEnd() {
  return async function () {
    //------Ending Routine 'voluntary'-------
    voluntaryComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    voluntaryNextKey.stop();
    // the Routine "voluntary" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _contactNextKey_allKeys;
var contactComponents;
function contactRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'contact'-------
    t = 0;
    contactClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    contactNextKey.keys = undefined;
    contactNextKey.rt = undefined;
    _contactNextKey_allKeys = [];
    // keep track of which components have finished
    contactComponents = [];
    contactComponents.push(contactTitleText);
    contactComponents.push(contactText);
    contactComponents.push(contactNextText);
    contactComponents.push(contactNextKey);
    
    contactComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function contactRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'contact'-------
    // get current time
    t = contactClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *contactTitleText* updates
    if (t >= 0.0 && contactTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contactTitleText.tStart = t;  // (not accounting for frame time here)
      contactTitleText.frameNStart = frameN;  // exact frame index
      
      contactTitleText.setAutoDraw(true);
    }

    
    // *contactText* updates
    if (t >= 0.0 && contactText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contactText.tStart = t;  // (not accounting for frame time here)
      contactText.frameNStart = frameN;  // exact frame index
      
      contactText.setAutoDraw(true);
    }

    
    // *contactNextText* updates
    if (t >= 0.0 && contactNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contactNextText.tStart = t;  // (not accounting for frame time here)
      contactNextText.frameNStart = frameN;  // exact frame index
      
      contactNextText.setAutoDraw(true);
    }

    
    // *contactNextKey* updates
    if (t >= 0.0 && contactNextKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contactNextKey.tStart = t;  // (not accounting for frame time here)
      contactNextKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { contactNextKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { contactNextKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { contactNextKey.clearEvents(); });
    }

    if (contactNextKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = contactNextKey.getKeys({keyList: ['space'], waitRelease: false});
      _contactNextKey_allKeys = _contactNextKey_allKeys.concat(theseKeys);
      if (_contactNextKey_allKeys.length > 0) {
        contactNextKey.keys = _contactNextKey_allKeys[_contactNextKey_allKeys.length - 1].name;  // just the last key pressed
        contactNextKey.rt = _contactNextKey_allKeys[_contactNextKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    contactComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function contactRoutineEnd() {
  return async function () {
    //------Ending Routine 'contact'-------
    contactComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    contactNextKey.stop();
    // the Routine "contact" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _confidentialityNextKey_allKeys;
var confidentialityComponents;
function confidentialityRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'confidentiality'-------
    t = 0;
    confidentialityClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    confidentialityNextKey.keys = undefined;
    confidentialityNextKey.rt = undefined;
    _confidentialityNextKey_allKeys = [];
    // keep track of which components have finished
    confidentialityComponents = [];
    confidentialityComponents.push(confidentialityTitleText);
    confidentialityComponents.push(confidentialityText);
    confidentialityComponents.push(confidentialityNextText);
    confidentialityComponents.push(confidentialityNextKey);
    
    confidentialityComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function confidentialityRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'confidentiality'-------
    // get current time
    t = confidentialityClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *confidentialityTitleText* updates
    if (t >= 0.0 && confidentialityTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confidentialityTitleText.tStart = t;  // (not accounting for frame time here)
      confidentialityTitleText.frameNStart = frameN;  // exact frame index
      
      confidentialityTitleText.setAutoDraw(true);
    }

    
    // *confidentialityText* updates
    if (t >= 0.0 && confidentialityText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confidentialityText.tStart = t;  // (not accounting for frame time here)
      confidentialityText.frameNStart = frameN;  // exact frame index
      
      confidentialityText.setAutoDraw(true);
    }

    
    // *confidentialityNextText* updates
    if (t >= 0.0 && confidentialityNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confidentialityNextText.tStart = t;  // (not accounting for frame time here)
      confidentialityNextText.frameNStart = frameN;  // exact frame index
      
      confidentialityNextText.setAutoDraw(true);
    }

    
    // *confidentialityNextKey* updates
    if (t >= 0.0 && confidentialityNextKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confidentialityNextKey.tStart = t;  // (not accounting for frame time here)
      confidentialityNextKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { confidentialityNextKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { confidentialityNextKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { confidentialityNextKey.clearEvents(); });
    }

    if (confidentialityNextKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = confidentialityNextKey.getKeys({keyList: ['space'], waitRelease: false});
      _confidentialityNextKey_allKeys = _confidentialityNextKey_allKeys.concat(theseKeys);
      if (_confidentialityNextKey_allKeys.length > 0) {
        confidentialityNextKey.keys = _confidentialityNextKey_allKeys[_confidentialityNextKey_allKeys.length - 1].name;  // just the last key pressed
        confidentialityNextKey.rt = _confidentialityNextKey_allKeys[_confidentialityNextKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    confidentialityComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function confidentialityRoutineEnd() {
  return async function () {
    //------Ending Routine 'confidentiality'-------
    confidentialityComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(confidentialityNextKey.corr, level);
    }
    psychoJS.experiment.addData('confidentialityNextKey.keys', confidentialityNextKey.keys);
    if (typeof confidentialityNextKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('confidentialityNextKey.rt', confidentialityNextKey.rt);
        routineTimer.reset();
        }
    
    confidentialityNextKey.stop();
    // the Routine "confidentiality" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _infomationNextKey_allKeys;
var informationComponents;
function informationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'information'-------
    t = 0;
    informationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    infomationNextKey.keys = undefined;
    infomationNextKey.rt = undefined;
    _infomationNextKey_allKeys = [];
    // keep track of which components have finished
    informationComponents = [];
    informationComponents.push(informationTitleText);
    informationComponents.push(informationText);
    informationComponents.push(informationNextText);
    informationComponents.push(infomationNextKey);
    
    informationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function informationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'information'-------
    // get current time
    t = informationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *informationTitleText* updates
    if (t >= 0.0 && informationTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      informationTitleText.tStart = t;  // (not accounting for frame time here)
      informationTitleText.frameNStart = frameN;  // exact frame index
      
      informationTitleText.setAutoDraw(true);
    }

    
    // *informationText* updates
    if (t >= 0.0 && informationText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      informationText.tStart = t;  // (not accounting for frame time here)
      informationText.frameNStart = frameN;  // exact frame index
      
      informationText.setAutoDraw(true);
    }

    
    // *informationNextText* updates
    if (t >= 0.0 && informationNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      informationNextText.tStart = t;  // (not accounting for frame time here)
      informationNextText.frameNStart = frameN;  // exact frame index
      
      informationNextText.setAutoDraw(true);
    }

    
    // *infomationNextKey* updates
    if (t >= 0.0 && infomationNextKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      infomationNextKey.tStart = t;  // (not accounting for frame time here)
      infomationNextKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { infomationNextKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { infomationNextKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { infomationNextKey.clearEvents(); });
    }

    if (infomationNextKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = infomationNextKey.getKeys({keyList: ['space'], waitRelease: false});
      _infomationNextKey_allKeys = _infomationNextKey_allKeys.concat(theseKeys);
      if (_infomationNextKey_allKeys.length > 0) {
        infomationNextKey.keys = _infomationNextKey_allKeys[_infomationNextKey_allKeys.length - 1].name;  // just the last key pressed
        infomationNextKey.rt = _infomationNextKey_allKeys[_infomationNextKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    informationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function informationRoutineEnd() {
  return async function () {
    //------Ending Routine 'information'-------
    informationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(infomationNextKey.corr, level);
    }
    psychoJS.experiment.addData('infomationNextKey.keys', infomationNextKey.keys);
    if (typeof infomationNextKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('infomationNextKey.rt', infomationNextKey.rt);
        routineTimer.reset();
        }
    
    infomationNextKey.stop();
    // the Routine "information" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _consentNextKey_allKeys;
var consentComponents;
function consentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'consent'-------
    t = 0;
    consentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    consentNextKey.keys = undefined;
    consentNextKey.rt = undefined;
    _consentNextKey_allKeys = [];
    // keep track of which components have finished
    consentComponents = [];
    consentComponents.push(consentTitleText);
    consentComponents.push(consentText);
    consentComponents.push(consentTextNext);
    consentComponents.push(consentNextKey);
    
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function consentRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'consent'-------
    // get current time
    t = consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *consentTitleText* updates
    if (t >= 0.0 && consentTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consentTitleText.tStart = t;  // (not accounting for frame time here)
      consentTitleText.frameNStart = frameN;  // exact frame index
      
      consentTitleText.setAutoDraw(true);
    }

    
    // *consentText* updates
    if (t >= 0.0 && consentText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consentText.tStart = t;  // (not accounting for frame time here)
      consentText.frameNStart = frameN;  // exact frame index
      
      consentText.setAutoDraw(true);
    }

    
    // *consentTextNext* updates
    if (t >= 0.0 && consentTextNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consentTextNext.tStart = t;  // (not accounting for frame time here)
      consentTextNext.frameNStart = frameN;  // exact frame index
      
      consentTextNext.setAutoDraw(true);
    }

    
    // *consentNextKey* updates
    if (t >= 0.0 && consentNextKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consentNextKey.tStart = t;  // (not accounting for frame time here)
      consentNextKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { consentNextKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { consentNextKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { consentNextKey.clearEvents(); });
    }

    if (consentNextKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = consentNextKey.getKeys({keyList: ['space'], waitRelease: false});
      _consentNextKey_allKeys = _consentNextKey_allKeys.concat(theseKeys);
      if (_consentNextKey_allKeys.length > 0) {
        consentNextKey.keys = _consentNextKey_allKeys[_consentNextKey_allKeys.length - 1].name;  // just the last key pressed
        consentNextKey.rt = _consentNextKey_allKeys[_consentNextKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentRoutineEnd() {
  return async function () {
    //------Ending Routine 'consent'-------
    consentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(consentNextKey.corr, level);
    }
    psychoJS.experiment.addData('consentNextKey.keys', consentNextKey.keys);
    if (typeof consentNextKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('consentNextKey.rt', consentNextKey.rt);
        routineTimer.reset();
        }
    
    consentNextKey.stop();
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _languageL1Key_allKeys;
var inputText;
var isAccented;
var languageL1Components;
function languageL1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageL1'-------
    t = 0;
    languageL1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    languageL1Key.keys = undefined;
    languageL1Key.rt = undefined;
    _languageL1Key_allKeys = [];
    psychopy.event.clearEvents();
    inputText = "";
    isAccented = false;
    
    // keep track of which components have finished
    languageL1Components = [];
    languageL1Components.push(languageL1TitleText);
    languageL1Components.push(languageL1Text);
    languageL1Components.push(languageL1NextText);
    languageL1Components.push(languageL1Key);
    
    languageL1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageL1RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageL1'-------
    // get current time
    t = languageL1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageL1TitleText* updates
    if (t >= 0.0 && languageL1TitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL1TitleText.tStart = t;  // (not accounting for frame time here)
      languageL1TitleText.frameNStart = frameN;  // exact frame index
      
      languageL1TitleText.setAutoDraw(true);
    }

    
    // *languageL1Text* updates
    if (t >= 0.0 && languageL1Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL1Text.tStart = t;  // (not accounting for frame time here)
      languageL1Text.frameNStart = frameN;  // exact frame index
      
      languageL1Text.setAutoDraw(true);
    }

    
    // *languageL1NextText* updates
    if (t >= 0.0 && languageL1NextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL1NextText.tStart = t;  // (not accounting for frame time here)
      languageL1NextText.frameNStart = frameN;  // exact frame index
      
      languageL1NextText.setAutoDraw(true);
    }

    
    // *languageL1Key* updates
    if (t >= 0.0 && languageL1Key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL1Key.tStart = t;  // (not accounting for frame time here)
      languageL1Key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { languageL1Key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { languageL1Key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { languageL1Key.clearEvents(); });
    }

    if (languageL1Key.status === PsychoJS.Status.STARTED) {
      let theseKeys = languageL1Key.getKeys({keyList: ['e', 's', 'c', 'o'], waitRelease: false});
      _languageL1Key_allKeys = _languageL1Key_allKeys.concat(theseKeys);
      if (_languageL1Key_allKeys.length > 0) {
        languageL1Key.keys = _languageL1Key_allKeys[_languageL1Key_allKeys.length - 1].name;  // just the last key pressed
        languageL1Key.rt = _languageL1Key_allKeys[_languageL1Key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageL1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageL1RoutineEnd() {
  return async function () {
    //------Ending Routine 'languageL1'-------
    languageL1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(languageL1Key.corr, level);
    }
    psychoJS.experiment.addData('languageL1Key.keys', languageL1Key.keys);
    if (typeof languageL1Key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('languageL1Key.rt', languageL1Key.rt);
        routineTimer.reset();
        }
    
    languageL1Key.stop();
    // the Routine "languageL1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var languageL2Components;
function languageL2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageL2'-------
    t = 0;
    languageL2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychopy.event.clearEvents();
    inputText = "";
    isAccented = false;
    
    // keep track of which components have finished
    languageL2Components = [];
    languageL2Components.push(languageL2TitleText);
    languageL2Components.push(languageL2Text);
    languageL2Components.push(languageL2NextText);
    languageL2Components.push(languageL2InputText);
    
    languageL2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var keys;
var i;
var languageL2value;
var languageL3value;
function languageL2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageL2'-------
    // get current time
    t = languageL2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageL2TitleText* updates
    if (t >= 0.0 && languageL2TitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2TitleText.tStart = t;  // (not accounting for frame time here)
      languageL2TitleText.frameNStart = frameN;  // exact frame index
      
      languageL2TitleText.setAutoDraw(true);
    }

    
    // *languageL2Text* updates
    if (t >= 0.0 && languageL2Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2Text.tStart = t;  // (not accounting for frame time here)
      languageL2Text.frameNStart = frameN;  // exact frame index
      
      languageL2Text.setAutoDraw(true);
    }

    
    // *languageL2NextText* updates
    if (t >= 0.0 && languageL2NextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2NextText.tStart = t;  // (not accounting for frame time here)
      languageL2NextText.frameNStart = frameN;  // exact frame index
      
      languageL2NextText.setAutoDraw(true);
    }

    
    // *languageL2InputText* updates
    if (t >= 0.0 && languageL2InputText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2InputText.tStart = t;  // (not accounting for frame time here)
      languageL2InputText.frameNStart = frameN;  // exact frame index
      
      languageL2InputText.setAutoDraw(true);
    }

    
    if (languageL2InputText.status === PsychoJS.Status.STARTED){ // only update if being drawn
      languageL2InputText.setText(("> " + inputText), false);
    }
    keys = psychoJS.eventManager.getKeys({"keyList": letterKeysAllowed});
    i = 0;
    if (keys.length) {
        if ((keys[i] === "escape")) {
            psychoJS.experiment.addData("languageL2", inputText);
            core.quit();
        }
        if ((keys[i] === "return")) {
            languageL2value = inputText;
            if ((inputText === "")) {
                languageL3value = "";
            }
            psychoJS.experiment.addData("languageL2", inputText);
            continueRoutine = false;
        } else {
            if ((keys[i] === "backspace")) {
                inputText = inputText.slice(0, (- 1));
            } else {
                if ((keys[i] === "space")) {
                    inputText += " ";
                } else {
                    if ((keys[i] === "apostrophe")) {
                        inputText = "'";
                    } else {
                        inputText += keys[i].toUpperCase();
                        psychoJS.experiment.addData("languageL2", inputText);
                        i = (i + 1);
                    }
                }
            }
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageL2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageL2RoutineEnd() {
  return async function () {
    //------Ending Routine 'languageL2'-------
    languageL2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    console.log(languageL2value);
    
    // the Routine "languageL2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _languageL2OralKey_allKeys;
var languageL2OralComponents;
function languageL2OralRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageL2Oral'-------
    t = 0;
    languageL2OralClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    languageL2OralKey.keys = undefined;
    languageL2OralKey.rt = undefined;
    _languageL2OralKey_allKeys = [];
    if ((languageL2value === "")) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    languageL2OralComponents = [];
    languageL2OralComponents.push(languageL2OralTitleText);
    languageL2OralComponents.push(languageL2OralText);
    languageL2OralComponents.push(languageL2OralNextText);
    languageL2OralComponents.push(languageL2OralKey);
    
    languageL2OralComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageL2OralRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageL2Oral'-------
    // get current time
    t = languageL2OralClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageL2OralTitleText* updates
    if (t >= 0.0 && languageL2OralTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2OralTitleText.tStart = t;  // (not accounting for frame time here)
      languageL2OralTitleText.frameNStart = frameN;  // exact frame index
      
      languageL2OralTitleText.setAutoDraw(true);
    }

    
    // *languageL2OralText* updates
    if (t >= 0.0 && languageL2OralText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2OralText.tStart = t;  // (not accounting for frame time here)
      languageL2OralText.frameNStart = frameN;  // exact frame index
      
      languageL2OralText.setAutoDraw(true);
    }

    
    // *languageL2OralNextText* updates
    if (t >= 0.0 && languageL2OralNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2OralNextText.tStart = t;  // (not accounting for frame time here)
      languageL2OralNextText.frameNStart = frameN;  // exact frame index
      
      languageL2OralNextText.setAutoDraw(true);
    }

    
    // *languageL2OralKey* updates
    if (t >= 0.0 && languageL2OralKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2OralKey.tStart = t;  // (not accounting for frame time here)
      languageL2OralKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { languageL2OralKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { languageL2OralKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { languageL2OralKey.clearEvents(); });
    }

    if (languageL2OralKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = languageL2OralKey.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _languageL2OralKey_allKeys = _languageL2OralKey_allKeys.concat(theseKeys);
      if (_languageL2OralKey_allKeys.length > 0) {
        languageL2OralKey.keys = _languageL2OralKey_allKeys[_languageL2OralKey_allKeys.length - 1].name;  // just the last key pressed
        languageL2OralKey.rt = _languageL2OralKey_allKeys[_languageL2OralKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageL2OralComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageL2OralRoutineEnd() {
  return async function () {
    //------Ending Routine 'languageL2Oral'-------
    languageL2OralComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(languageL2OralKey.corr, level);
    }
    psychoJS.experiment.addData('languageL2OralKey.keys', languageL2OralKey.keys);
    if (typeof languageL2OralKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('languageL2OralKey.rt', languageL2OralKey.rt);
        routineTimer.reset();
        }
    
    languageL2OralKey.stop();
    // the Routine "languageL2Oral" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _languageL2WrittenKey_allKeys;
var languageL2WrittenComponents;
function languageL2WrittenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageL2Written'-------
    t = 0;
    languageL2WrittenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    languageL2WrittenKey.keys = undefined;
    languageL2WrittenKey.rt = undefined;
    _languageL2WrittenKey_allKeys = [];
    if ((languageL2value === "")) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    languageL2WrittenComponents = [];
    languageL2WrittenComponents.push(languageL2WrittenTitleText);
    languageL2WrittenComponents.push(languageL2WrittenText);
    languageL2WrittenComponents.push(languageL2WrittenNextText);
    languageL2WrittenComponents.push(languageL2WrittenKey);
    
    languageL2WrittenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageL2WrittenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageL2Written'-------
    // get current time
    t = languageL2WrittenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageL2WrittenTitleText* updates
    if (t >= 0.0 && languageL2WrittenTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2WrittenTitleText.tStart = t;  // (not accounting for frame time here)
      languageL2WrittenTitleText.frameNStart = frameN;  // exact frame index
      
      languageL2WrittenTitleText.setAutoDraw(true);
    }

    
    // *languageL2WrittenText* updates
    if (t >= 0.0 && languageL2WrittenText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2WrittenText.tStart = t;  // (not accounting for frame time here)
      languageL2WrittenText.frameNStart = frameN;  // exact frame index
      
      languageL2WrittenText.setAutoDraw(true);
    }

    
    // *languageL2WrittenNextText* updates
    if (t >= 0.0 && languageL2WrittenNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2WrittenNextText.tStart = t;  // (not accounting for frame time here)
      languageL2WrittenNextText.frameNStart = frameN;  // exact frame index
      
      languageL2WrittenNextText.setAutoDraw(true);
    }

    
    // *languageL2WrittenKey* updates
    if (t >= 0.0 && languageL2WrittenKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL2WrittenKey.tStart = t;  // (not accounting for frame time here)
      languageL2WrittenKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { languageL2WrittenKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { languageL2WrittenKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { languageL2WrittenKey.clearEvents(); });
    }

    if (languageL2WrittenKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = languageL2WrittenKey.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _languageL2WrittenKey_allKeys = _languageL2WrittenKey_allKeys.concat(theseKeys);
      if (_languageL2WrittenKey_allKeys.length > 0) {
        languageL2WrittenKey.keys = _languageL2WrittenKey_allKeys[_languageL2WrittenKey_allKeys.length - 1].name;  // just the last key pressed
        languageL2WrittenKey.rt = _languageL2WrittenKey_allKeys[_languageL2WrittenKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageL2WrittenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageL2WrittenRoutineEnd() {
  return async function () {
    //------Ending Routine 'languageL2Written'-------
    languageL2WrittenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(languageL2WrittenKey.corr, level);
    }
    psychoJS.experiment.addData('languageL2WrittenKey.keys', languageL2WrittenKey.keys);
    if (typeof languageL2WrittenKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('languageL2WrittenKey.rt', languageL2WrittenKey.rt);
        routineTimer.reset();
        }
    
    languageL2WrittenKey.stop();
    // the Routine "languageL2Written" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var languageL3Components;
function languageL3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageL3'-------
    t = 0;
    languageL3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychopy.event.clearEvents();
    inputText = "";
    isAccented = false;
    
    // keep track of which components have finished
    languageL3Components = [];
    languageL3Components.push(languageL3TitleText);
    languageL3Components.push(languageL3Text);
    languageL3Components.push(languageL3NextText);
    languageL3Components.push(languageL3InputText);
    
    languageL3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageL3RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageL3'-------
    // get current time
    t = languageL3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageL3TitleText* updates
    if (t >= 0.0 && languageL3TitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3TitleText.tStart = t;  // (not accounting for frame time here)
      languageL3TitleText.frameNStart = frameN;  // exact frame index
      
      languageL3TitleText.setAutoDraw(true);
    }

    
    // *languageL3Text* updates
    if (t >= 0.0 && languageL3Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3Text.tStart = t;  // (not accounting for frame time here)
      languageL3Text.frameNStart = frameN;  // exact frame index
      
      languageL3Text.setAutoDraw(true);
    }

    
    // *languageL3NextText* updates
    if (t >= 0.0 && languageL3NextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3NextText.tStart = t;  // (not accounting for frame time here)
      languageL3NextText.frameNStart = frameN;  // exact frame index
      
      languageL3NextText.setAutoDraw(true);
    }

    
    // *languageL3InputText* updates
    if (t >= 0.0 && languageL3InputText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3InputText.tStart = t;  // (not accounting for frame time here)
      languageL3InputText.frameNStart = frameN;  // exact frame index
      
      languageL3InputText.setAutoDraw(true);
    }

    
    if (languageL3InputText.status === PsychoJS.Status.STARTED){ // only update if being drawn
      languageL3InputText.setText(("> " + inputText), false);
    }
    if ((languageL2value === "")) {
        continueRoutine = false;
    }
    keys = psychoJS.eventManager.getKeys({"keyList": letterKeysAllowed});
    i = 0;
    if (keys.length) {
        if ((keys[i] === "escape")) {
            psychoJS.experiment.addData("languageL3", inputText);
            core.quit();
        } else {
            if ((keys[i] === "return")) {
                languageL3value = inputText;
                psychoJS.experiment.addData("languageL3", inputText);
                continueRoutine = false;
            } else {
                if ((keys[i] === "space")) {
                    inputText += " ";
                } else {
                    if ((keys[i] === "backspace")) {
                        inputText = inputText.slice(0, (- 1));
                    } else {
                        if ((keys[i] === "apostrophe")) {
                            inputText = "'";
                        } else {
                            inputText += keys[i].toUpperCase();
                            psychoJS.experiment.addData("languageL3", inputText);
                            i = (i + 1);
                        }
                    }
                }
            }
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageL3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageL3RoutineEnd() {
  return async function () {
    //------Ending Routine 'languageL3'-------
    languageL3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    console.log(languageL3value);
    
    // the Routine "languageL3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _languageL3OralKey_allKeys;
var languageL3OralComponents;
function languageL3OralRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageL3Oral'-------
    t = 0;
    languageL3OralClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    languageL3OralKey.keys = undefined;
    languageL3OralKey.rt = undefined;
    _languageL3OralKey_allKeys = [];
    if ((languageL3value === "")) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    languageL3OralComponents = [];
    languageL3OralComponents.push(languageL3OralTitleText);
    languageL3OralComponents.push(languageL3OralText);
    languageL3OralComponents.push(languageL3OralNextText);
    languageL3OralComponents.push(languageL3OralKey);
    
    languageL3OralComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageL3OralRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageL3Oral'-------
    // get current time
    t = languageL3OralClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageL3OralTitleText* updates
    if (t >= 0.0 && languageL3OralTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3OralTitleText.tStart = t;  // (not accounting for frame time here)
      languageL3OralTitleText.frameNStart = frameN;  // exact frame index
      
      languageL3OralTitleText.setAutoDraw(true);
    }

    
    // *languageL3OralText* updates
    if (t >= 0.0 && languageL3OralText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3OralText.tStart = t;  // (not accounting for frame time here)
      languageL3OralText.frameNStart = frameN;  // exact frame index
      
      languageL3OralText.setAutoDraw(true);
    }

    
    // *languageL3OralNextText* updates
    if (t >= 0.0 && languageL3OralNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3OralNextText.tStart = t;  // (not accounting for frame time here)
      languageL3OralNextText.frameNStart = frameN;  // exact frame index
      
      languageL3OralNextText.setAutoDraw(true);
    }

    
    // *languageL3OralKey* updates
    if (t >= 0.0 && languageL3OralKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3OralKey.tStart = t;  // (not accounting for frame time here)
      languageL3OralKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { languageL3OralKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { languageL3OralKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { languageL3OralKey.clearEvents(); });
    }

    if (languageL3OralKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = languageL3OralKey.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _languageL3OralKey_allKeys = _languageL3OralKey_allKeys.concat(theseKeys);
      if (_languageL3OralKey_allKeys.length > 0) {
        languageL3OralKey.keys = _languageL3OralKey_allKeys[_languageL3OralKey_allKeys.length - 1].name;  // just the last key pressed
        languageL3OralKey.rt = _languageL3OralKey_allKeys[_languageL3OralKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageL3OralComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageL3OralRoutineEnd() {
  return async function () {
    //------Ending Routine 'languageL3Oral'-------
    languageL3OralComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(languageL3OralKey.corr, level);
    }
    psychoJS.experiment.addData('languageL3OralKey.keys', languageL3OralKey.keys);
    if (typeof languageL3OralKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('languageL3OralKey.rt', languageL3OralKey.rt);
        routineTimer.reset();
        }
    
    languageL3OralKey.stop();
    // the Routine "languageL3Oral" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _languageL3WrittenKey_allKeys;
var languageL3WrittenComponents;
function languageL3WrittenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageL3Written'-------
    t = 0;
    languageL3WrittenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    languageL3WrittenKey.keys = undefined;
    languageL3WrittenKey.rt = undefined;
    _languageL3WrittenKey_allKeys = [];
    if ((languageL3value === "")) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    languageL3WrittenComponents = [];
    languageL3WrittenComponents.push(languageL3WrittenTitleText);
    languageL3WrittenComponents.push(languageL3WrittenText);
    languageL3WrittenComponents.push(languageL3WrittenNextText);
    languageL3WrittenComponents.push(languageL3WrittenKey);
    
    languageL3WrittenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageL3WrittenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageL3Written'-------
    // get current time
    t = languageL3WrittenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageL3WrittenTitleText* updates
    if (t >= 0.0 && languageL3WrittenTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3WrittenTitleText.tStart = t;  // (not accounting for frame time here)
      languageL3WrittenTitleText.frameNStart = frameN;  // exact frame index
      
      languageL3WrittenTitleText.setAutoDraw(true);
    }

    
    // *languageL3WrittenText* updates
    if (t >= 0.0 && languageL3WrittenText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3WrittenText.tStart = t;  // (not accounting for frame time here)
      languageL3WrittenText.frameNStart = frameN;  // exact frame index
      
      languageL3WrittenText.setAutoDraw(true);
    }

    
    // *languageL3WrittenNextText* updates
    if (t >= 0.0 && languageL3WrittenNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3WrittenNextText.tStart = t;  // (not accounting for frame time here)
      languageL3WrittenNextText.frameNStart = frameN;  // exact frame index
      
      languageL3WrittenNextText.setAutoDraw(true);
    }

    
    // *languageL3WrittenKey* updates
    if (t >= 0.0 && languageL3WrittenKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageL3WrittenKey.tStart = t;  // (not accounting for frame time here)
      languageL3WrittenKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { languageL3WrittenKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { languageL3WrittenKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { languageL3WrittenKey.clearEvents(); });
    }

    if (languageL3WrittenKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = languageL3WrittenKey.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _languageL3WrittenKey_allKeys = _languageL3WrittenKey_allKeys.concat(theseKeys);
      if (_languageL3WrittenKey_allKeys.length > 0) {
        languageL3WrittenKey.keys = _languageL3WrittenKey_allKeys[_languageL3WrittenKey_allKeys.length - 1].name;  // just the last key pressed
        languageL3WrittenKey.rt = _languageL3WrittenKey_allKeys[_languageL3WrittenKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageL3WrittenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageL3WrittenRoutineEnd() {
  return async function () {
    //------Ending Routine 'languageL3Written'-------
    languageL3WrittenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(languageL3WrittenKey.corr, level);
    }
    psychoJS.experiment.addData('languageL3WrittenKey.keys', languageL3WrittenKey.keys);
    if (typeof languageL3WrittenKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('languageL3WrittenKey.rt', languageL3WrittenKey.rt);
        routineTimer.reset();
        }
    
    languageL3WrittenKey.stop();
    // the Routine "languageL3Written" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _languageCatalanOralKey_allKeys;
var _pj;
var n;
var languageCatalanOralComponents;
function languageCatalanOralRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageCatalanOral'-------
    t = 0;
    languageCatalanOralClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    languageCatalanOralKey.keys = undefined;
    languageCatalanOralKey.rt = undefined;
    _languageCatalanOralKey_allKeys = [];
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (((languageL2value === "CATALAN") || (languageL3value === "CATALAN"))) {
        continueRoutine = false;
    }
    keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
    n = keys.length;
    if (_pj.in_es6("escape", keys)) {
        core.quit();
    }
    
    // keep track of which components have finished
    languageCatalanOralComponents = [];
    languageCatalanOralComponents.push(languageCatalanOralTitleText);
    languageCatalanOralComponents.push(languageCatalanOralText);
    languageCatalanOralComponents.push(languageCatalanOralNextText);
    languageCatalanOralComponents.push(languageCatalanOralKey);
    
    languageCatalanOralComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageCatalanOralRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageCatalanOral'-------
    // get current time
    t = languageCatalanOralClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageCatalanOralTitleText* updates
    if (t >= 0.0 && languageCatalanOralTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanOralTitleText.tStart = t;  // (not accounting for frame time here)
      languageCatalanOralTitleText.frameNStart = frameN;  // exact frame index
      
      languageCatalanOralTitleText.setAutoDraw(true);
    }

    
    // *languageCatalanOralText* updates
    if (t >= 0.0 && languageCatalanOralText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanOralText.tStart = t;  // (not accounting for frame time here)
      languageCatalanOralText.frameNStart = frameN;  // exact frame index
      
      languageCatalanOralText.setAutoDraw(true);
    }

    
    // *languageCatalanOralNextText* updates
    if (t >= 0.0 && languageCatalanOralNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanOralNextText.tStart = t;  // (not accounting for frame time here)
      languageCatalanOralNextText.frameNStart = frameN;  // exact frame index
      
      languageCatalanOralNextText.setAutoDraw(true);
    }

    
    // *languageCatalanOralKey* updates
    if (t >= 0.0 && languageCatalanOralKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanOralKey.tStart = t;  // (not accounting for frame time here)
      languageCatalanOralKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { languageCatalanOralKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { languageCatalanOralKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { languageCatalanOralKey.clearEvents(); });
    }

    if (languageCatalanOralKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = languageCatalanOralKey.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _languageCatalanOralKey_allKeys = _languageCatalanOralKey_allKeys.concat(theseKeys);
      if (_languageCatalanOralKey_allKeys.length > 0) {
        languageCatalanOralKey.keys = _languageCatalanOralKey_allKeys[_languageCatalanOralKey_allKeys.length - 1].name;  // just the last key pressed
        languageCatalanOralKey.rt = _languageCatalanOralKey_allKeys[_languageCatalanOralKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageCatalanOralComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageCatalanOralRoutineEnd() {
  return async function () {
    //------Ending Routine 'languageCatalanOral'-------
    languageCatalanOralComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(languageCatalanOralKey.corr, level);
    }
    psychoJS.experiment.addData('languageCatalanOralKey.keys', languageCatalanOralKey.keys);
    if (typeof languageCatalanOralKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('languageCatalanOralKey.rt', languageCatalanOralKey.rt);
        routineTimer.reset();
        }
    
    languageCatalanOralKey.stop();
    // the Routine "languageCatalanOral" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _languageCatalanWrittenKey_allKeys;
var languageCatalanWrittenComponents;
function languageCatalanWrittenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageCatalanWritten'-------
    t = 0;
    languageCatalanWrittenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    languageCatalanWrittenKey.keys = undefined;
    languageCatalanWrittenKey.rt = undefined;
    _languageCatalanWrittenKey_allKeys = [];
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (((languageL2value === "CATALAN") || (languageL3value === "CATALAN"))) {
        continueRoutine = false;
    }
    keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
    n = keys.length;
    if (_pj.in_es6("escape", keys)) {
        core.quit();
    }
    
    // keep track of which components have finished
    languageCatalanWrittenComponents = [];
    languageCatalanWrittenComponents.push(languageCatalanWrittenTitleText);
    languageCatalanWrittenComponents.push(languageCatalanWrittenText);
    languageCatalanWrittenComponents.push(languageCatalanWrittenNextText);
    languageCatalanWrittenComponents.push(languageCatalanWrittenKey);
    
    languageCatalanWrittenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageCatalanWrittenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageCatalanWritten'-------
    // get current time
    t = languageCatalanWrittenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageCatalanWrittenTitleText* updates
    if (t >= 0.0 && languageCatalanWrittenTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanWrittenTitleText.tStart = t;  // (not accounting for frame time here)
      languageCatalanWrittenTitleText.frameNStart = frameN;  // exact frame index
      
      languageCatalanWrittenTitleText.setAutoDraw(true);
    }

    
    // *languageCatalanWrittenText* updates
    if (t >= 0.0 && languageCatalanWrittenText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanWrittenText.tStart = t;  // (not accounting for frame time here)
      languageCatalanWrittenText.frameNStart = frameN;  // exact frame index
      
      languageCatalanWrittenText.setAutoDraw(true);
    }

    
    // *languageCatalanWrittenNextText* updates
    if (t >= 0.0 && languageCatalanWrittenNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanWrittenNextText.tStart = t;  // (not accounting for frame time here)
      languageCatalanWrittenNextText.frameNStart = frameN;  // exact frame index
      
      languageCatalanWrittenNextText.setAutoDraw(true);
    }

    
    // *languageCatalanWrittenKey* updates
    if (t >= 0.0 && languageCatalanWrittenKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanWrittenKey.tStart = t;  // (not accounting for frame time here)
      languageCatalanWrittenKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { languageCatalanWrittenKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { languageCatalanWrittenKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { languageCatalanWrittenKey.clearEvents(); });
    }

    if (languageCatalanWrittenKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = languageCatalanWrittenKey.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _languageCatalanWrittenKey_allKeys = _languageCatalanWrittenKey_allKeys.concat(theseKeys);
      if (_languageCatalanWrittenKey_allKeys.length > 0) {
        languageCatalanWrittenKey.keys = _languageCatalanWrittenKey_allKeys[_languageCatalanWrittenKey_allKeys.length - 1].name;  // just the last key pressed
        languageCatalanWrittenKey.rt = _languageCatalanWrittenKey_allKeys[_languageCatalanWrittenKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageCatalanWrittenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageCatalanWrittenRoutineEnd() {
  return async function () {
    //------Ending Routine 'languageCatalanWritten'-------
    languageCatalanWrittenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(languageCatalanWrittenKey.corr, level);
    }
    psychoJS.experiment.addData('languageCatalanWrittenKey.keys', languageCatalanWrittenKey.keys);
    if (typeof languageCatalanWrittenKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('languageCatalanWrittenKey.rt', languageCatalanWrittenKey.rt);
        routineTimer.reset();
        }
    
    languageCatalanWrittenKey.stop();
    // the Routine "languageCatalanWritten" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _languageCatalanTimeKey_allKeys;
var languageCatalanTimeComponents;
function languageCatalanTimeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageCatalanTime'-------
    t = 0;
    languageCatalanTimeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    languageCatalanTimeKey.keys = undefined;
    languageCatalanTimeKey.rt = undefined;
    _languageCatalanTimeKey_allKeys = [];
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
    n = keys.length;
    if (_pj.in_es6("escape", keys)) {
        core.quit();
    }
    
    // keep track of which components have finished
    languageCatalanTimeComponents = [];
    languageCatalanTimeComponents.push(languageCatalanTimeTitleText);
    languageCatalanTimeComponents.push(languageCatalanTimeText);
    languageCatalanTimeComponents.push(languageCatalanTimeNextText);
    languageCatalanTimeComponents.push(languageCatalanTimeKey);
    
    languageCatalanTimeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageCatalanTimeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageCatalanTime'-------
    // get current time
    t = languageCatalanTimeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageCatalanTimeTitleText* updates
    if (t >= 0.0 && languageCatalanTimeTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanTimeTitleText.tStart = t;  // (not accounting for frame time here)
      languageCatalanTimeTitleText.frameNStart = frameN;  // exact frame index
      
      languageCatalanTimeTitleText.setAutoDraw(true);
    }

    
    // *languageCatalanTimeText* updates
    if (t >= 0.0 && languageCatalanTimeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanTimeText.tStart = t;  // (not accounting for frame time here)
      languageCatalanTimeText.frameNStart = frameN;  // exact frame index
      
      languageCatalanTimeText.setAutoDraw(true);
    }

    
    // *languageCatalanTimeNextText* updates
    if (t >= 0.0 && languageCatalanTimeNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanTimeNextText.tStart = t;  // (not accounting for frame time here)
      languageCatalanTimeNextText.frameNStart = frameN;  // exact frame index
      
      languageCatalanTimeNextText.setAutoDraw(true);
    }

    
    // *languageCatalanTimeKey* updates
    if (t >= 0.0 && languageCatalanTimeKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageCatalanTimeKey.tStart = t;  // (not accounting for frame time here)
      languageCatalanTimeKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { languageCatalanTimeKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { languageCatalanTimeKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { languageCatalanTimeKey.clearEvents(); });
    }

    if (languageCatalanTimeKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = languageCatalanTimeKey.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _languageCatalanTimeKey_allKeys = _languageCatalanTimeKey_allKeys.concat(theseKeys);
      if (_languageCatalanTimeKey_allKeys.length > 0) {
        languageCatalanTimeKey.keys = _languageCatalanTimeKey_allKeys[_languageCatalanTimeKey_allKeys.length - 1].name;  // just the last key pressed
        languageCatalanTimeKey.rt = _languageCatalanTimeKey_allKeys[_languageCatalanTimeKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageCatalanTimeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageCatalanTimeRoutineEnd() {
  return async function () {
    //------Ending Routine 'languageCatalanTime'-------
    languageCatalanTimeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(languageCatalanTimeKey.corr, level);
    }
    psychoJS.experiment.addData('languageCatalanTimeKey.keys', languageCatalanTimeKey.keys);
    if (typeof languageCatalanTimeKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('languageCatalanTimeKey.rt', languageCatalanTimeKey.rt);
        routineTimer.reset();
        }
    
    languageCatalanTimeKey.stop();
    // the Routine "languageCatalanTime" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _languageSpanishOralKey_allKeys;
var languageSpanishOralComponents;
function languageSpanishOralRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageSpanishOral'-------
    t = 0;
    languageSpanishOralClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    languageSpanishOralKey.keys = undefined;
    languageSpanishOralKey.rt = undefined;
    _languageSpanishOralKey_allKeys = [];
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (((languageL2value === "SPANISH") || (languageL3value === "SPANISH"))) {
        continueRoutine = false;
    }
    keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
    n = keys.length;
    if (_pj.in_es6("escape", keys)) {
        core.quit();
    }
    
    // keep track of which components have finished
    languageSpanishOralComponents = [];
    languageSpanishOralComponents.push(languageSpanishOralTitleText);
    languageSpanishOralComponents.push(languageSpanishOralText);
    languageSpanishOralComponents.push(languageSpanishOralNextText);
    languageSpanishOralComponents.push(languageSpanishOralKey);
    
    languageSpanishOralComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageSpanishOralRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageSpanishOral'-------
    // get current time
    t = languageSpanishOralClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageSpanishOralTitleText* updates
    if (t >= 0.0 && languageSpanishOralTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishOralTitleText.tStart = t;  // (not accounting for frame time here)
      languageSpanishOralTitleText.frameNStart = frameN;  // exact frame index
      
      languageSpanishOralTitleText.setAutoDraw(true);
    }

    
    // *languageSpanishOralText* updates
    if (t >= 0.0 && languageSpanishOralText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishOralText.tStart = t;  // (not accounting for frame time here)
      languageSpanishOralText.frameNStart = frameN;  // exact frame index
      
      languageSpanishOralText.setAutoDraw(true);
    }

    
    // *languageSpanishOralNextText* updates
    if (t >= 0.0 && languageSpanishOralNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishOralNextText.tStart = t;  // (not accounting for frame time here)
      languageSpanishOralNextText.frameNStart = frameN;  // exact frame index
      
      languageSpanishOralNextText.setAutoDraw(true);
    }

    
    // *languageSpanishOralKey* updates
    if (t >= 0.0 && languageSpanishOralKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishOralKey.tStart = t;  // (not accounting for frame time here)
      languageSpanishOralKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { languageSpanishOralKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { languageSpanishOralKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { languageSpanishOralKey.clearEvents(); });
    }

    if (languageSpanishOralKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = languageSpanishOralKey.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _languageSpanishOralKey_allKeys = _languageSpanishOralKey_allKeys.concat(theseKeys);
      if (_languageSpanishOralKey_allKeys.length > 0) {
        languageSpanishOralKey.keys = _languageSpanishOralKey_allKeys[_languageSpanishOralKey_allKeys.length - 1].name;  // just the last key pressed
        languageSpanishOralKey.rt = _languageSpanishOralKey_allKeys[_languageSpanishOralKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageSpanishOralComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageSpanishOralRoutineEnd() {
  return async function () {
    //------Ending Routine 'languageSpanishOral'-------
    languageSpanishOralComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(languageSpanishOralKey.corr, level);
    }
    psychoJS.experiment.addData('languageSpanishOralKey.keys', languageSpanishOralKey.keys);
    if (typeof languageSpanishOralKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('languageSpanishOralKey.rt', languageSpanishOralKey.rt);
        routineTimer.reset();
        }
    
    languageSpanishOralKey.stop();
    // the Routine "languageSpanishOral" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _languageSpanishWrittenKey_allKeys;
var languageSpanishWrittenComponents;
function languageSpanishWrittenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageSpanishWritten'-------
    t = 0;
    languageSpanishWrittenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    languageSpanishWrittenKey.keys = undefined;
    languageSpanishWrittenKey.rt = undefined;
    _languageSpanishWrittenKey_allKeys = [];
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (((languageL2value === "SPANISH") || (languageL3value === "SPANISH"))) {
        continueRoutine = false;
    }
    keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
    n = keys.length;
    if (_pj.in_es6("escape", keys)) {
        core.quit();
    }
    
    // keep track of which components have finished
    languageSpanishWrittenComponents = [];
    languageSpanishWrittenComponents.push(languageSpanishTitleText);
    languageSpanishWrittenComponents.push(languageSpanishWrittenText);
    languageSpanishWrittenComponents.push(languageSpanishNextText);
    languageSpanishWrittenComponents.push(languageSpanishWrittenKey);
    
    languageSpanishWrittenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageSpanishWrittenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageSpanishWritten'-------
    // get current time
    t = languageSpanishWrittenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageSpanishTitleText* updates
    if (t >= 0.0 && languageSpanishTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishTitleText.tStart = t;  // (not accounting for frame time here)
      languageSpanishTitleText.frameNStart = frameN;  // exact frame index
      
      languageSpanishTitleText.setAutoDraw(true);
    }

    
    // *languageSpanishWrittenText* updates
    if (t >= 0.0 && languageSpanishWrittenText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishWrittenText.tStart = t;  // (not accounting for frame time here)
      languageSpanishWrittenText.frameNStart = frameN;  // exact frame index
      
      languageSpanishWrittenText.setAutoDraw(true);
    }

    
    // *languageSpanishNextText* updates
    if (t >= 0.0 && languageSpanishNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishNextText.tStart = t;  // (not accounting for frame time here)
      languageSpanishNextText.frameNStart = frameN;  // exact frame index
      
      languageSpanishNextText.setAutoDraw(true);
    }

    
    // *languageSpanishWrittenKey* updates
    if (t >= 0.0 && languageSpanishWrittenKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishWrittenKey.tStart = t;  // (not accounting for frame time here)
      languageSpanishWrittenKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { languageSpanishWrittenKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { languageSpanishWrittenKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { languageSpanishWrittenKey.clearEvents(); });
    }

    if (languageSpanishWrittenKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = languageSpanishWrittenKey.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _languageSpanishWrittenKey_allKeys = _languageSpanishWrittenKey_allKeys.concat(theseKeys);
      if (_languageSpanishWrittenKey_allKeys.length > 0) {
        languageSpanishWrittenKey.keys = _languageSpanishWrittenKey_allKeys[_languageSpanishWrittenKey_allKeys.length - 1].name;  // just the last key pressed
        languageSpanishWrittenKey.rt = _languageSpanishWrittenKey_allKeys[_languageSpanishWrittenKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageSpanishWrittenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageSpanishWrittenRoutineEnd() {
  return async function () {
    //------Ending Routine 'languageSpanishWritten'-------
    languageSpanishWrittenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(languageSpanishWrittenKey.corr, level);
    }
    psychoJS.experiment.addData('languageSpanishWrittenKey.keys', languageSpanishWrittenKey.keys);
    if (typeof languageSpanishWrittenKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('languageSpanishWrittenKey.rt', languageSpanishWrittenKey.rt);
        routineTimer.reset();
        }
    
    languageSpanishWrittenKey.stop();
    // the Routine "languageSpanishWritten" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _languageSpanishTimeKey_allKeys;
var languageSpanishTimeComponents;
function languageSpanishTimeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'languageSpanishTime'-------
    t = 0;
    languageSpanishTimeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    languageSpanishTimeKey.keys = undefined;
    languageSpanishTimeKey.rt = undefined;
    _languageSpanishTimeKey_allKeys = [];
    // keep track of which components have finished
    languageSpanishTimeComponents = [];
    languageSpanishTimeComponents.push(languageSpanishTimeTitleText);
    languageSpanishTimeComponents.push(languageSpanishTimeText);
    languageSpanishTimeComponents.push(languageSpanishTimeNextText);
    languageSpanishTimeComponents.push(languageSpanishTimeKey);
    
    languageSpanishTimeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function languageSpanishTimeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'languageSpanishTime'-------
    // get current time
    t = languageSpanishTimeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *languageSpanishTimeTitleText* updates
    if (t >= 0.0 && languageSpanishTimeTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishTimeTitleText.tStart = t;  // (not accounting for frame time here)
      languageSpanishTimeTitleText.frameNStart = frameN;  // exact frame index
      
      languageSpanishTimeTitleText.setAutoDraw(true);
    }

    
    // *languageSpanishTimeText* updates
    if (t >= 0.0 && languageSpanishTimeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishTimeText.tStart = t;  // (not accounting for frame time here)
      languageSpanishTimeText.frameNStart = frameN;  // exact frame index
      
      languageSpanishTimeText.setAutoDraw(true);
    }

    
    // *languageSpanishTimeNextText* updates
    if (t >= 0.0 && languageSpanishTimeNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishTimeNextText.tStart = t;  // (not accounting for frame time here)
      languageSpanishTimeNextText.frameNStart = frameN;  // exact frame index
      
      languageSpanishTimeNextText.setAutoDraw(true);
    }

    
    // *languageSpanishTimeKey* updates
    if (t >= 0.0 && languageSpanishTimeKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      languageSpanishTimeKey.tStart = t;  // (not accounting for frame time here)
      languageSpanishTimeKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { languageSpanishTimeKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { languageSpanishTimeKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { languageSpanishTimeKey.clearEvents(); });
    }

    if (languageSpanishTimeKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = languageSpanishTimeKey.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _languageSpanishTimeKey_allKeys = _languageSpanishTimeKey_allKeys.concat(theseKeys);
      if (_languageSpanishTimeKey_allKeys.length > 0) {
        languageSpanishTimeKey.keys = _languageSpanishTimeKey_allKeys[_languageSpanishTimeKey_allKeys.length - 1].name;  // just the last key pressed
        languageSpanishTimeKey.rt = _languageSpanishTimeKey_allKeys[_languageSpanishTimeKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    languageSpanishTimeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function languageSpanishTimeRoutineEnd() {
  return async function () {
    //------Ending Routine 'languageSpanishTime'-------
    languageSpanishTimeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(languageSpanishTimeKey.corr, level);
    }
    psychoJS.experiment.addData('languageSpanishTimeKey.keys', languageSpanishTimeKey.keys);
    if (typeof languageSpanishTimeKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('languageSpanishTimeKey.rt', languageSpanishTimeKey.rt);
        routineTimer.reset();
        }
    
    languageSpanishTimeKey.stop();
    // the Routine "languageSpanishTime" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var demoAgeComponents;
function demoAgeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'demoAge'-------
    t = 0;
    demoAgeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychopy.event.clearEvents();
    inputText = "";
    isAccented = false;
    
    // keep track of which components have finished
    demoAgeComponents = [];
    demoAgeComponents.push(demoAgeTitleText);
    demoAgeComponents.push(demoAgeText);
    demoAgeComponents.push(demoAgeNextText);
    demoAgeComponents.push(demoAgeInputText);
    
    demoAgeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var age;
function demoAgeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'demoAge'-------
    // get current time
    t = demoAgeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demoAgeTitleText* updates
    if (t >= 0.0 && demoAgeTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoAgeTitleText.tStart = t;  // (not accounting for frame time here)
      demoAgeTitleText.frameNStart = frameN;  // exact frame index
      
      demoAgeTitleText.setAutoDraw(true);
    }

    
    // *demoAgeText* updates
    if (t >= 0.0 && demoAgeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoAgeText.tStart = t;  // (not accounting for frame time here)
      demoAgeText.frameNStart = frameN;  // exact frame index
      
      demoAgeText.setAutoDraw(true);
    }

    
    // *demoAgeNextText* updates
    if (t >= 0.0 && demoAgeNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoAgeNextText.tStart = t;  // (not accounting for frame time here)
      demoAgeNextText.frameNStart = frameN;  // exact frame index
      
      demoAgeNextText.setAutoDraw(true);
    }

    
    // *demoAgeInputText* updates
    if (t >= 0.0 && demoAgeInputText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoAgeInputText.tStart = t;  // (not accounting for frame time here)
      demoAgeInputText.frameNStart = frameN;  // exact frame index
      
      demoAgeInputText.setAutoDraw(true);
    }

    
    if (demoAgeInputText.status === PsychoJS.Status.STARTED){ // only update if being drawn
      demoAgeInputText.setText(("> " + inputText), false);
    }
    keys = psychoJS.eventManager.getKeys({"keyList": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "escape", "backspace", "return"]});
    i = 0;
    if (keys.length) {
        if ((keys[i] === "escape")) {
            age = inputText;
            psychoJS.experiment.addData("age", inputText);
            core.quit();
        } else {
            if ((keys[i] === "return")) {
                if ((inputText !== "")) {
                    language2 = inputText;
                    psychoJS.experiment.addData("age", inputText);
                    continueRoutine = false;
                }
            } else {
                if ((keys[i] === "backspace")) {
                    inputText = inputText.slice(0, (- 1));
                } else {
                    inputText += keys[i].toUpperCase();
                    psychoJS.experiment.addData("age", inputText);
                    i = (i + 1);
                }
            }
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    demoAgeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demoAgeRoutineEnd() {
  return async function () {
    //------Ending Routine 'demoAge'-------
    demoAgeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "demoAge" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _demoSexKey_allKeys;
var demoSexComponents;
function demoSexRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'demoSex'-------
    t = 0;
    demoSexClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    demoSexKey.keys = undefined;
    demoSexKey.rt = undefined;
    _demoSexKey_allKeys = [];
    // keep track of which components have finished
    demoSexComponents = [];
    demoSexComponents.push(demoSexTitleText);
    demoSexComponents.push(demoSexText);
    demoSexComponents.push(demoSexNextText);
    demoSexComponents.push(demoSexKey);
    
    demoSexComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function demoSexRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'demoSex'-------
    // get current time
    t = demoSexClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demoSexTitleText* updates
    if (t >= 0.0 && demoSexTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoSexTitleText.tStart = t;  // (not accounting for frame time here)
      demoSexTitleText.frameNStart = frameN;  // exact frame index
      
      demoSexTitleText.setAutoDraw(true);
    }

    
    // *demoSexText* updates
    if (t >= 0.0 && demoSexText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoSexText.tStart = t;  // (not accounting for frame time here)
      demoSexText.frameNStart = frameN;  // exact frame index
      
      demoSexText.setAutoDraw(true);
    }

    
    // *demoSexNextText* updates
    if (t >= 0.0 && demoSexNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoSexNextText.tStart = t;  // (not accounting for frame time here)
      demoSexNextText.frameNStart = frameN;  // exact frame index
      
      demoSexNextText.setAutoDraw(true);
    }

    
    // *demoSexKey* updates
    if (t >= 0.0 && demoSexKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoSexKey.tStart = t;  // (not accounting for frame time here)
      demoSexKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { demoSexKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { demoSexKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { demoSexKey.clearEvents(); });
    }

    if (demoSexKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = demoSexKey.getKeys({keyList: ['f', 'm', 'o'], waitRelease: false});
      _demoSexKey_allKeys = _demoSexKey_allKeys.concat(theseKeys);
      if (_demoSexKey_allKeys.length > 0) {
        demoSexKey.keys = _demoSexKey_allKeys[_demoSexKey_allKeys.length - 1].name;  // just the last key pressed
        demoSexKey.rt = _demoSexKey_allKeys[_demoSexKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    demoSexComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demoSexRoutineEnd() {
  return async function () {
    //------Ending Routine 'demoSex'-------
    demoSexComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(demoSexKey.corr, level);
    }
    psychoJS.experiment.addData('demoSexKey.keys', demoSexKey.keys);
    if (typeof demoSexKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('demoSexKey.rt', demoSexKey.rt);
        routineTimer.reset();
        }
    
    demoSexKey.stop();
    // the Routine "demoSex" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _demoEducationKey_allKeys;
var demoEducationComponents;
function demoEducationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'demoEducation'-------
    t = 0;
    demoEducationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    demoEducationKey.keys = undefined;
    demoEducationKey.rt = undefined;
    _demoEducationKey_allKeys = [];
    // keep track of which components have finished
    demoEducationComponents = [];
    demoEducationComponents.push(demoEducationTitleText);
    demoEducationComponents.push(demoEducationText);
    demoEducationComponents.push(demoEducationNextText);
    demoEducationComponents.push(demoEducationKey);
    
    demoEducationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function demoEducationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'demoEducation'-------
    // get current time
    t = demoEducationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demoEducationTitleText* updates
    if (t >= 0.0 && demoEducationTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoEducationTitleText.tStart = t;  // (not accounting for frame time here)
      demoEducationTitleText.frameNStart = frameN;  // exact frame index
      
      demoEducationTitleText.setAutoDraw(true);
    }

    
    // *demoEducationText* updates
    if (t >= 0.0 && demoEducationText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoEducationText.tStart = t;  // (not accounting for frame time here)
      demoEducationText.frameNStart = frameN;  // exact frame index
      
      demoEducationText.setAutoDraw(true);
    }

    
    // *demoEducationNextText* updates
    if (t >= 0.0 && demoEducationNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoEducationNextText.tStart = t;  // (not accounting for frame time here)
      demoEducationNextText.frameNStart = frameN;  // exact frame index
      
      demoEducationNextText.setAutoDraw(true);
    }

    
    // *demoEducationKey* updates
    if (t >= 0.0 && demoEducationKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoEducationKey.tStart = t;  // (not accounting for frame time here)
      demoEducationKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { demoEducationKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { demoEducationKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { demoEducationKey.clearEvents(); });
    }

    if (demoEducationKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = demoEducationKey.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _demoEducationKey_allKeys = _demoEducationKey_allKeys.concat(theseKeys);
      if (_demoEducationKey_allKeys.length > 0) {
        demoEducationKey.keys = _demoEducationKey_allKeys[_demoEducationKey_allKeys.length - 1].name;  // just the last key pressed
        demoEducationKey.rt = _demoEducationKey_allKeys[_demoEducationKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    demoEducationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demoEducationRoutineEnd() {
  return async function () {
    //------Ending Routine 'demoEducation'-------
    demoEducationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(demoEducationKey.corr, level);
    }
    psychoJS.experiment.addData('demoEducationKey.keys', demoEducationKey.keys);
    if (typeof demoEducationKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('demoEducationKey.rt', demoEducationKey.rt);
        routineTimer.reset();
        }
    
    demoEducationKey.stop();
    // the Routine "demoEducation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var demoCityComponents;
function demoCityRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'demoCity'-------
    t = 0;
    demoCityClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychopy.event.clearEvents();
    inputText = "";
    isAccented = false;
    
    // keep track of which components have finished
    demoCityComponents = [];
    demoCityComponents.push(demoCityTitleText);
    demoCityComponents.push(demoCityText);
    demoCityComponents.push(demoCityNextText);
    demoCityComponents.push(demoCityInputText);
    
    demoCityComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var city;
function demoCityRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'demoCity'-------
    // get current time
    t = demoCityClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demoCityTitleText* updates
    if (t >= 0.0 && demoCityTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoCityTitleText.tStart = t;  // (not accounting for frame time here)
      demoCityTitleText.frameNStart = frameN;  // exact frame index
      
      demoCityTitleText.setAutoDraw(true);
    }

    
    // *demoCityText* updates
    if (t >= 0.0 && demoCityText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoCityText.tStart = t;  // (not accounting for frame time here)
      demoCityText.frameNStart = frameN;  // exact frame index
      
      demoCityText.setAutoDraw(true);
    }

    
    // *demoCityNextText* updates
    if (t >= 0.0 && demoCityNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoCityNextText.tStart = t;  // (not accounting for frame time here)
      demoCityNextText.frameNStart = frameN;  // exact frame index
      
      demoCityNextText.setAutoDraw(true);
    }

    
    // *demoCityInputText* updates
    if (t >= 0.0 && demoCityInputText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoCityInputText.tStart = t;  // (not accounting for frame time here)
      demoCityInputText.frameNStart = frameN;  // exact frame index
      
      demoCityInputText.setAutoDraw(true);
    }

    
    if (demoCityInputText.status === PsychoJS.Status.STARTED){ // only update if being drawn
      demoCityInputText.setText(("> " + inputText), false);
    }
    keys = psychoJS.eventManager.getKeys({"keyList": letterKeysAllowed});
    i = 0;
    if (keys.length) {
        if ((keys[i] === "escape")) {
            psychoJS.experiment.addData("city", inputText);
            core.quit();
        }
        if ((keys[i] === "return")) {
            city = inputText;
            psychoJS.experiment.addData("city", inputText);
            continueRoutine = false;
        } else {
            if ((keys[i] === "backspace")) {
                inputText = inputText.slice(0, (- 1));
            } else {
                if ((keys[i] === "space")) {
                    inputText += " ";
                } else {
                    if ((keys[i] === "apostrophe")) {
                        inputText = "'";
                    } else {
                        inputText += keys[i].toUpperCase();
                        psychoJS.experiment.addData("city", inputText);
                        i = (i + 1);
                    }
                }
            }
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    demoCityComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demoCityRoutineEnd() {
  return async function () {
    //------Ending Routine 'demoCity'-------
    demoCityComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "demoCity" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _demoVisionKey_allKeys;
var demoVisionComponents;
function demoVisionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'demoVision'-------
    t = 0;
    demoVisionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    demoVisionKey.keys = undefined;
    demoVisionKey.rt = undefined;
    _demoVisionKey_allKeys = [];
    // keep track of which components have finished
    demoVisionComponents = [];
    demoVisionComponents.push(demoVisionTitleText);
    demoVisionComponents.push(demoVisionText);
    demoVisionComponents.push(demoTextNextText);
    demoVisionComponents.push(demoVisionKey);
    
    demoVisionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function demoVisionRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'demoVision'-------
    // get current time
    t = demoVisionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demoVisionTitleText* updates
    if (t >= 0.0 && demoVisionTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoVisionTitleText.tStart = t;  // (not accounting for frame time here)
      demoVisionTitleText.frameNStart = frameN;  // exact frame index
      
      demoVisionTitleText.setAutoDraw(true);
    }

    
    // *demoVisionText* updates
    if (t >= 0.0 && demoVisionText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoVisionText.tStart = t;  // (not accounting for frame time here)
      demoVisionText.frameNStart = frameN;  // exact frame index
      
      demoVisionText.setAutoDraw(true);
    }

    
    // *demoTextNextText* updates
    if (t >= 0.0 && demoTextNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoTextNextText.tStart = t;  // (not accounting for frame time here)
      demoTextNextText.frameNStart = frameN;  // exact frame index
      
      demoTextNextText.setAutoDraw(true);
    }

    
    // *demoVisionKey* updates
    if (t >= 0.0 && demoVisionKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoVisionKey.tStart = t;  // (not accounting for frame time here)
      demoVisionKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { demoVisionKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { demoVisionKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { demoVisionKey.clearEvents(); });
    }

    if (demoVisionKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = demoVisionKey.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _demoVisionKey_allKeys = _demoVisionKey_allKeys.concat(theseKeys);
      if (_demoVisionKey_allKeys.length > 0) {
        demoVisionKey.keys = _demoVisionKey_allKeys[_demoVisionKey_allKeys.length - 1].name;  // just the last key pressed
        demoVisionKey.rt = _demoVisionKey_allKeys[_demoVisionKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    demoVisionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demoVisionRoutineEnd() {
  return async function () {
    //------Ending Routine 'demoVision'-------
    demoVisionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(demoVisionKey.corr, level);
    }
    psychoJS.experiment.addData('demoVisionKey.keys', demoVisionKey.keys);
    if (typeof demoVisionKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('demoVisionKey.rt', demoVisionKey.rt);
        routineTimer.reset();
        }
    
    demoVisionKey.stop();
    // the Routine "demoVision" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _demoLanguageKey_allKeys;
var demoLanguageComponents;
function demoLanguageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'demoLanguage'-------
    t = 0;
    demoLanguageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    demoLanguageKey.keys = undefined;
    demoLanguageKey.rt = undefined;
    _demoLanguageKey_allKeys = [];
    // keep track of which components have finished
    demoLanguageComponents = [];
    demoLanguageComponents.push(demoLanguageTitleText);
    demoLanguageComponents.push(demoLanguageText);
    demoLanguageComponents.push(demoLanguageNextText);
    demoLanguageComponents.push(demoLanguageKey);
    
    demoLanguageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function demoLanguageRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'demoLanguage'-------
    // get current time
    t = demoLanguageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demoLanguageTitleText* updates
    if (t >= 0.0 && demoLanguageTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoLanguageTitleText.tStart = t;  // (not accounting for frame time here)
      demoLanguageTitleText.frameNStart = frameN;  // exact frame index
      
      demoLanguageTitleText.setAutoDraw(true);
    }

    
    // *demoLanguageText* updates
    if (t >= 0.0 && demoLanguageText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoLanguageText.tStart = t;  // (not accounting for frame time here)
      demoLanguageText.frameNStart = frameN;  // exact frame index
      
      demoLanguageText.setAutoDraw(true);
    }

    
    // *demoLanguageNextText* updates
    if (t >= 0.0 && demoLanguageNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoLanguageNextText.tStart = t;  // (not accounting for frame time here)
      demoLanguageNextText.frameNStart = frameN;  // exact frame index
      
      demoLanguageNextText.setAutoDraw(true);
    }

    
    // *demoLanguageKey* updates
    if (t >= 0.0 && demoLanguageKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demoLanguageKey.tStart = t;  // (not accounting for frame time here)
      demoLanguageKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { demoLanguageKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { demoLanguageKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { demoLanguageKey.clearEvents(); });
    }

    if (demoLanguageKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = demoLanguageKey.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _demoLanguageKey_allKeys = _demoLanguageKey_allKeys.concat(theseKeys);
      if (_demoLanguageKey_allKeys.length > 0) {
        demoLanguageKey.keys = _demoLanguageKey_allKeys[_demoLanguageKey_allKeys.length - 1].name;  // just the last key pressed
        demoLanguageKey.rt = _demoLanguageKey_allKeys[_demoLanguageKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    demoLanguageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demoLanguageRoutineEnd() {
  return async function () {
    //------Ending Routine 'demoLanguage'-------
    demoLanguageComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(demoLanguageKey.corr, level);
    }
    psychoJS.experiment.addData('demoLanguageKey.keys', demoLanguageKey.keys);
    if (typeof demoLanguageKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('demoLanguageKey.rt', demoLanguageKey.rt);
        routineTimer.reset();
        }
    
    demoLanguageKey.stop();
    // the Routine "demoLanguage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _setupLocationKey_allKeys;
var setupLocationComponents;
function setupLocationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'setupLocation'-------
    t = 0;
    setupLocationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    setupLocationKey.keys = undefined;
    setupLocationKey.rt = undefined;
    _setupLocationKey_allKeys = [];
    // keep track of which components have finished
    setupLocationComponents = [];
    setupLocationComponents.push(setupLocationTitleText);
    setupLocationComponents.push(setupLocationText);
    setupLocationComponents.push(setupLocationNextText);
    setupLocationComponents.push(setupLocationKey);
    
    setupLocationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function setupLocationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'setupLocation'-------
    // get current time
    t = setupLocationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *setupLocationTitleText* updates
    if (t >= 0.0 && setupLocationTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupLocationTitleText.tStart = t;  // (not accounting for frame time here)
      setupLocationTitleText.frameNStart = frameN;  // exact frame index
      
      setupLocationTitleText.setAutoDraw(true);
    }

    
    // *setupLocationText* updates
    if (t >= 0.0 && setupLocationText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupLocationText.tStart = t;  // (not accounting for frame time here)
      setupLocationText.frameNStart = frameN;  // exact frame index
      
      setupLocationText.setAutoDraw(true);
    }

    
    // *setupLocationNextText* updates
    if (t >= 0.0 && setupLocationNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupLocationNextText.tStart = t;  // (not accounting for frame time here)
      setupLocationNextText.frameNStart = frameN;  // exact frame index
      
      setupLocationNextText.setAutoDraw(true);
    }

    
    // *setupLocationKey* updates
    if (t >= 0.0 && setupLocationKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupLocationKey.tStart = t;  // (not accounting for frame time here)
      setupLocationKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { setupLocationKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { setupLocationKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { setupLocationKey.clearEvents(); });
    }

    if (setupLocationKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = setupLocationKey.getKeys({keyList: ['1', '2', '3', '4', '5', '6', '7'], waitRelease: false});
      _setupLocationKey_allKeys = _setupLocationKey_allKeys.concat(theseKeys);
      if (_setupLocationKey_allKeys.length > 0) {
        setupLocationKey.keys = _setupLocationKey_allKeys[_setupLocationKey_allKeys.length - 1].name;  // just the last key pressed
        setupLocationKey.rt = _setupLocationKey_allKeys[_setupLocationKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    setupLocationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function setupLocationRoutineEnd() {
  return async function () {
    //------Ending Routine 'setupLocation'-------
    setupLocationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(setupLocationKey.corr, level);
    }
    psychoJS.experiment.addData('setupLocationKey.keys', setupLocationKey.keys);
    if (typeof setupLocationKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('setupLocationKey.rt', setupLocationKey.rt);
        routineTimer.reset();
        }
    
    setupLocationKey.stop();
    // the Routine "setupLocation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _setupNoiseKey_allKeys;
var setupNoiseComponents;
function setupNoiseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'setupNoise'-------
    t = 0;
    setupNoiseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    setupNoiseKey.keys = undefined;
    setupNoiseKey.rt = undefined;
    _setupNoiseKey_allKeys = [];
    // keep track of which components have finished
    setupNoiseComponents = [];
    setupNoiseComponents.push(setupNoiseTitleText);
    setupNoiseComponents.push(setupNoiseText);
    setupNoiseComponents.push(setupNoiseNextText);
    setupNoiseComponents.push(setupNoiseKey);
    
    setupNoiseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function setupNoiseRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'setupNoise'-------
    // get current time
    t = setupNoiseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *setupNoiseTitleText* updates
    if (t >= 0.0 && setupNoiseTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupNoiseTitleText.tStart = t;  // (not accounting for frame time here)
      setupNoiseTitleText.frameNStart = frameN;  // exact frame index
      
      setupNoiseTitleText.setAutoDraw(true);
    }

    
    // *setupNoiseText* updates
    if (t >= 0.0 && setupNoiseText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupNoiseText.tStart = t;  // (not accounting for frame time here)
      setupNoiseText.frameNStart = frameN;  // exact frame index
      
      setupNoiseText.setAutoDraw(true);
    }

    
    // *setupNoiseNextText* updates
    if (t >= 0.0 && setupNoiseNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupNoiseNextText.tStart = t;  // (not accounting for frame time here)
      setupNoiseNextText.frameNStart = frameN;  // exact frame index
      
      setupNoiseNextText.setAutoDraw(true);
    }

    
    // *setupNoiseKey* updates
    if (t >= 0.0 && setupNoiseKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      setupNoiseKey.tStart = t;  // (not accounting for frame time here)
      setupNoiseKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { setupNoiseKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { setupNoiseKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { setupNoiseKey.clearEvents(); });
    }

    if (setupNoiseKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = setupNoiseKey.getKeys({keyList: ['1', '2', '3', '4'], waitRelease: false});
      _setupNoiseKey_allKeys = _setupNoiseKey_allKeys.concat(theseKeys);
      if (_setupNoiseKey_allKeys.length > 0) {
        setupNoiseKey.keys = _setupNoiseKey_allKeys[_setupNoiseKey_allKeys.length - 1].name;  // just the last key pressed
        setupNoiseKey.rt = _setupNoiseKey_allKeys[_setupNoiseKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    setupNoiseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function setupNoiseRoutineEnd() {
  return async function () {
    //------Ending Routine 'setupNoise'-------
    setupNoiseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(setupNoiseKey.corr, level);
    }
    psychoJS.experiment.addData('setupNoiseKey.keys', setupNoiseKey.keys);
    if (typeof setupNoiseKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('setupNoiseKey.rt', setupNoiseKey.rt);
        routineTimer.reset();
        }
    
    setupNoiseKey.stop();
    // the Routine "setupNoise" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _instructionsKey_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instructions'-------
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instructionsKey.keys = undefined;
    instructionsKey.rt = undefined;
    _instructionsKey_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instructionsTitleText);
    instructionsComponents.push(instructionsText);
    instructionsComponents.push(instructionsNextText);
    instructionsComponents.push(instructionsKey);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instructions'-------
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructionsTitleText* updates
    if (t >= 0.0 && instructionsTitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructionsTitleText.tStart = t;  // (not accounting for frame time here)
      instructionsTitleText.frameNStart = frameN;  // exact frame index
      
      instructionsTitleText.setAutoDraw(true);
    }

    
    // *instructionsText* updates
    if (t >= 0.0 && instructionsText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructionsText.tStart = t;  // (not accounting for frame time here)
      instructionsText.frameNStart = frameN;  // exact frame index
      
      instructionsText.setAutoDraw(true);
    }

    
    // *instructionsNextText* updates
    if (t >= 0.0 && instructionsNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructionsNextText.tStart = t;  // (not accounting for frame time here)
      instructionsNextText.frameNStart = frameN;  // exact frame index
      
      instructionsNextText.setAutoDraw(true);
    }

    
    // *instructionsKey* updates
    if (t >= 0.0 && instructionsKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructionsKey.tStart = t;  // (not accounting for frame time here)
      instructionsKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructionsKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructionsKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructionsKey.clearEvents(); });
    }

    if (instructionsKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructionsKey.getKeys({keyList: ['space'], waitRelease: false});
      _instructionsKey_allKeys = _instructionsKey_allKeys.concat(theseKeys);
      if (_instructionsKey_allKeys.length > 0) {
        instructionsKey.keys = _instructionsKey_allKeys[_instructionsKey_allKeys.length - 1].name;  // just the last key pressed
        instructionsKey.rt = _instructionsKey_allKeys[_instructionsKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd() {
  return async function () {
    //------Ending Routine 'instructions'-------
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instructionsKey.corr, level);
    }
    psychoJS.experiment.addData('instructionsKey.keys', instructionsKey.keys);
    if (typeof instructionsKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instructionsKey.rt', instructionsKey.rt);
        routineTimer.reset();
        }
    
    instructionsKey.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _isntructions2Key_allKeys;
var instructions2Components;
function instructions2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instructions2'-------
    t = 0;
    instructions2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    isntructions2Key.keys = undefined;
    isntructions2Key.rt = undefined;
    _isntructions2Key_allKeys = [];
    // keep track of which components have finished
    instructions2Components = [];
    instructions2Components.push(instructions2TitleText);
    instructions2Components.push(instructions2Text);
    instructions2Components.push(isntructions2NextText);
    instructions2Components.push(isntructions2Key);
    
    instructions2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instructions2'-------
    // get current time
    t = instructions2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions2TitleText* updates
    if (t >= 0.0 && instructions2TitleText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions2TitleText.tStart = t;  // (not accounting for frame time here)
      instructions2TitleText.frameNStart = frameN;  // exact frame index
      
      instructions2TitleText.setAutoDraw(true);
    }

    
    // *instructions2Text* updates
    if (t >= 0.0 && instructions2Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions2Text.tStart = t;  // (not accounting for frame time here)
      instructions2Text.frameNStart = frameN;  // exact frame index
      
      instructions2Text.setAutoDraw(true);
    }

    
    // *isntructions2NextText* updates
    if (t >= 0.0 && isntructions2NextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      isntructions2NextText.tStart = t;  // (not accounting for frame time here)
      isntructions2NextText.frameNStart = frameN;  // exact frame index
      
      isntructions2NextText.setAutoDraw(true);
    }

    
    // *isntructions2Key* updates
    if (t >= 0.0 && isntructions2Key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      isntructions2Key.tStart = t;  // (not accounting for frame time here)
      isntructions2Key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { isntructions2Key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { isntructions2Key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { isntructions2Key.clearEvents(); });
    }

    if (isntructions2Key.status === PsychoJS.Status.STARTED) {
      let theseKeys = isntructions2Key.getKeys({keyList: ['space'], waitRelease: false});
      _isntructions2Key_allKeys = _isntructions2Key_allKeys.concat(theseKeys);
      if (_isntructions2Key_allKeys.length > 0) {
        isntructions2Key.keys = _isntructions2Key_allKeys[_isntructions2Key_allKeys.length - 1].name;  // just the last key pressed
        isntructions2Key.rt = _isntructions2Key_allKeys[_isntructions2Key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructions2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var versions;
var versionRandom;
var trialsPracticeCatalanReps;
var trialsPracticeSpanishReps;
var trialsCatalanReps;
var trialsSpanishReps;
function instructions2RoutineEnd() {
  return async function () {
    //------Ending Routine 'instructions2'-------
    instructions2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(isntructions2Key.corr, level);
    }
    psychoJS.experiment.addData('isntructions2Key.keys', isntructions2Key.keys);
    if (typeof isntructions2Key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('isntructions2Key.rt', isntructions2Key.rt);
        routineTimer.reset();
        }
    
    isntructions2Key.stop();
    // randomise testing language (between-participant)
    versions = ['catalan', 'spanish'];
    versionRandom = versions[Math.floor(Math.random() *  versions.length)]; // ... randomly assign to Catalan or Spanish
    if (versionRandom==="catalan") {
        trialsPracticeCatalanReps = 1;
        trialsPracticeSpanishReps = 0;
        trialsCatalanReps = 1;
        trialsSpanishReps = 0;
        } else if (versionRandom==="spanish") {
            trialsPracticeCatalanReps = 0;
            trialsPracticeSpanishReps = 1;
            trialsCatalanReps = 0;
            trialsSpanishReps = 1;
            }
    
    // the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trialsPracticeCatalan;
var currentLoop;
function trialsPracticeCatalanLoopBegin(trialsPracticeCatalanLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsPracticeCatalan = new TrialHandler({
      psychoJS: psychoJS,
      nReps: trialsPracticeCatalanReps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Trials/01_trials_practice_catalan.xlsx',
      seed: undefined, name: 'trialsPracticeCatalan'
    });
    psychoJS.experiment.addLoop(trialsPracticeCatalan); // add the loop to the experiment
    currentLoop = trialsPracticeCatalan;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trialsPracticeCatalan.forEach(function() {
      const snapshot = trialsPracticeCatalan.getSnapshot();
    
      trialsPracticeCatalanLoopScheduler.add(importConditions(snapshot));
      trialsPracticeCatalanLoopScheduler.add(fixationRoutineBegin(snapshot));
      trialsPracticeCatalanLoopScheduler.add(fixationRoutineEachFrame());
      trialsPracticeCatalanLoopScheduler.add(fixationRoutineEnd());
      trialsPracticeCatalanLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsPracticeCatalanLoopScheduler.add(trialRoutineEachFrame());
      trialsPracticeCatalanLoopScheduler.add(trialRoutineEnd());
      trialsPracticeCatalanLoopScheduler.add(endLoopIteration(trialsPracticeCatalanLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsPracticeCatalanLoopEnd() {
  psychoJS.experiment.removeLoop(trialsPracticeCatalan);

  return Scheduler.Event.NEXT;
}


var trialsPracticeSpanish;
function trialsPracticeSpanishLoopBegin(trialsPracticeSpanishLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsPracticeSpanish = new TrialHandler({
      psychoJS: psychoJS,
      nReps: trialsPracticeSpanishReps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Trials/01_trials_practice_spanish.xlsx',
      seed: undefined, name: 'trialsPracticeSpanish'
    });
    psychoJS.experiment.addLoop(trialsPracticeSpanish); // add the loop to the experiment
    currentLoop = trialsPracticeSpanish;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trialsPracticeSpanish.forEach(function() {
      const snapshot = trialsPracticeSpanish.getSnapshot();
    
      trialsPracticeSpanishLoopScheduler.add(importConditions(snapshot));
      trialsPracticeSpanishLoopScheduler.add(fixationRoutineBegin(snapshot));
      trialsPracticeSpanishLoopScheduler.add(fixationRoutineEachFrame());
      trialsPracticeSpanishLoopScheduler.add(fixationRoutineEnd());
      trialsPracticeSpanishLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsPracticeSpanishLoopScheduler.add(trialRoutineEachFrame());
      trialsPracticeSpanishLoopScheduler.add(trialRoutineEnd());
      trialsPracticeSpanishLoopScheduler.add(endLoopIteration(trialsPracticeSpanishLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsPracticeSpanishLoopEnd() {
  psychoJS.experiment.removeLoop(trialsPracticeSpanish);

  return Scheduler.Event.NEXT;
}


var trialsCatalan;
function trialsCatalanLoopBegin(trialsCatalanLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsCatalan = new TrialHandler({
      psychoJS: psychoJS,
      nReps: trialsCatalanReps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Trials/02_trials_catalan.xlsx',
      seed: undefined, name: 'trialsCatalan'
    });
    psychoJS.experiment.addLoop(trialsCatalan); // add the loop to the experiment
    currentLoop = trialsCatalan;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trialsCatalan.forEach(function() {
      const snapshot = trialsCatalan.getSnapshot();
    
      trialsCatalanLoopScheduler.add(importConditions(snapshot));
      trialsCatalanLoopScheduler.add(fixationRoutineBegin(snapshot));
      trialsCatalanLoopScheduler.add(fixationRoutineEachFrame());
      trialsCatalanLoopScheduler.add(fixationRoutineEnd());
      trialsCatalanLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsCatalanLoopScheduler.add(trialRoutineEachFrame());
      trialsCatalanLoopScheduler.add(trialRoutineEnd());
      trialsCatalanLoopScheduler.add(endLoopIteration(trialsCatalanLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsCatalanLoopEnd() {
  psychoJS.experiment.removeLoop(trialsCatalan);

  return Scheduler.Event.NEXT;
}


var trialsSpanish;
function trialsSpanishLoopBegin(trialsSpanishLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialsSpanish = new TrialHandler({
      psychoJS: psychoJS,
      nReps: trialsSpanishReps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Trials/02_trials_spanish.xlsx',
      seed: undefined, name: 'trialsSpanish'
    });
    psychoJS.experiment.addLoop(trialsSpanish); // add the loop to the experiment
    currentLoop = trialsSpanish;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trialsSpanish.forEach(function() {
      const snapshot = trialsSpanish.getSnapshot();
    
      trialsSpanishLoopScheduler.add(importConditions(snapshot));
      trialsSpanishLoopScheduler.add(fixationRoutineBegin(snapshot));
      trialsSpanishLoopScheduler.add(fixationRoutineEachFrame());
      trialsSpanishLoopScheduler.add(fixationRoutineEnd());
      trialsSpanishLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsSpanishLoopScheduler.add(trialRoutineEachFrame());
      trialsSpanishLoopScheduler.add(trialRoutineEnd());
      trialsSpanishLoopScheduler.add(endLoopIteration(trialsSpanishLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsSpanishLoopEnd() {
  psychoJS.experiment.removeLoop(trialsSpanish);

  return Scheduler.Event.NEXT;
}


var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fixation'-------
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(fixationText);
    
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fixation'-------
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixationText* updates
    if (t >= 0.0 && fixationText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationText.tStart = t;  // (not accounting for frame time here)
      fixationText.frameNStart = frameN;  // exact frame index
      
      fixationText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixationText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixationText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd() {
  return async function () {
    //------Ending Routine 'fixation'-------
    fixationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var keysAllowed;
var debugText;
var error;
var keyPressTime;
var wordT;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    trialSound = new sound.Sound({
    win: psychoJS.window,
    value: soundfile,
    secs: -1,
    });
    trialSound.setVolume(1.0);
    keysAllowed = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "apostrophe", "z", "x", "c", "v", "b", "n", "m", "escape", "space", "return", "backspace"];
    inputText = "";
    debugText = "";
    isAccented = false;
    error = false;
    keyPressTime = 0;
    wordT = word;
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(trialText);
    trialComponents.push(trialSound);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trialText* updates
    if (((trialSound.status == FINISHED)) && trialText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialText.tStart = t;  // (not accounting for frame time here)
      trialText.frameNStart = frameN;  // exact frame index
      
      trialText.setAutoDraw(true);
    }

    
    if (trialText.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialText.setText(("> " + inputText), false);
    }
    // start/stop trialSound
    if (t >= 0.0 && trialSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialSound.tStart = t;  // (not accounting for frame time here)
      trialSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ trialSound.play(); });  // screen flip
      trialSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (trialSound.getDuration() + trialSound.tStart)     && trialSound.status === PsychoJS.Status.STARTED) {
      trialSound.stop();  // stop the sound (if longer than duration)
      trialSound.status = PsychoJS.Status.FINISHED;
    }
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys({"keyList": keysAllowed});
    i = 0;
    if ((trialSound.status === PsychoJS.Status.FINISHED)) {
        if (keys.length) {
            if (_pj.in_es6("return", keys[i])) {
                psychoJS.experiment.addData("trialOffset", t);
                psychoJS.experiment.addData("keyPressTime", t);
                continueRoutine = false;
            } else {
                if (_pj.in_es6("escape", keys[i])) {
                    psychoJS.experiment.addData("trialOffset", t);
                    core.quit();
                } else {
                    if ((keys[i] === "space")) {
                        inputText = (inputText + " ");
                    } else {
                        if ((keys[i] === "backspace")) {
                            inputText = inputText.slice(0, (- 1));
                            keyPressTime = t;
                            error = true;
                            inputText = inputText.slice(0, (- 1));
                        } else {
                            if (_pj.in_es6("apostrophe", keys[i])) {
                                inputText += "'";
                            } else {
                                inputText += keys[i].toUpperCase();
                            }
                        }
                    }
                }
            }
            psychoJS.experiment.addData("keyPressed", keys[i]);
            psychoJS.experiment.addData("keyPressTime", t);
            psychoJS.experiment.addData("inputText", inputText);
            psychoJS.experiment.addData("error", error);
            psychoJS.experiment.addData("wordT", wordT);
            psychoJS.experiment.nextEntry();
            i = (i + 1);
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    trialSound.stop();  // ensure sound has stopped at end of routine
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var beginComponents;
function beginRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'begin'-------
    t = 0;
    beginClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    beginComponents = [];
    beginComponents.push(beginText);
    beginComponents.push(beginNextText);
    
    beginComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function beginRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'begin'-------
    // get current time
    t = beginClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *beginText* updates
    if (t >= 0.0 && beginText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beginText.tStart = t;  // (not accounting for frame time here)
      beginText.frameNStart = frameN;  // exact frame index
      
      beginText.setAutoDraw(true);
    }

    
    // *beginNextText* updates
    if (t >= 0.0 && beginNextText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beginNextText.tStart = t;  // (not accounting for frame time here)
      beginNextText.frameNStart = frameN;  // exact frame index
      
      beginNextText.setAutoDraw(true);
    }

    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
    n = keys.length;
    if (_pj.in_es6("escape", keys)) {
        core.quit();
    } else {
        if (_pj.in_es6("space", keys)) {
            continueRoutine = false;
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    beginComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function beginRoutineEnd() {
  return async function () {
    //------Ending Routine 'begin'-------
    beginComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var farewellComponents;
function farewellRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'farewell'-------
    t = 0;
    farewellClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    farewellComponents = [];
    farewellComponents.push(farewellText);
    
    farewellComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function farewellRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'farewell'-------
    // get current time
    t = farewellClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *farewellText* updates
    if (t >= 0.0 && farewellText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      farewellText.tStart = t;  // (not accounting for frame time here)
      farewellText.frameNStart = frameN;  // exact frame index
      
      farewellText.setAutoDraw(true);
    }

    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
    n = keys.length;
    if (_pj.in_es6("escape", keys)) {
        core.quit();
    } else {
        if (_pj.in_es6("space", keys)) {
            continueRoutine = false;
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    farewellComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function farewellRoutineEnd() {
  return async function () {
    //------Ending Routine 'farewell'-------
    farewellComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "farewell" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
