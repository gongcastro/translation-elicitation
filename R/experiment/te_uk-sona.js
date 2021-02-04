/**************************************** 
 * Translationelicitation_Eng-Sona Test *
 ****************************************/

import { PsychoJS } from 'https://pavlovia.org/lib/core-3.2.js';
import * as core from 'https://pavlovia.org/lib/core-3.2.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data-3.2.js';
import { Scheduler } from 'https://pavlovia.org/lib/util-3.2.js';
import * as util from 'https://pavlovia.org/lib/util-3.2.js';
import * as visual from 'https://pavlovia.org/lib/visual-3.2.js';
import { Sound } from 'https://pavlovia.org/lib/sound-3.2.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'norm',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'TranslationElicitation_eng-sona';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

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
flowScheduler.add(setupRoutineBegin);
flowScheduler.add(setupRoutineEachFrame);
flowScheduler.add(setupRoutineEnd);
flowScheduler.add(welcomeRoutineBegin);
flowScheduler.add(welcomeRoutineEachFrame);
flowScheduler.add(welcomeRoutineEnd);
flowScheduler.add(descriptionRoutineBegin);
flowScheduler.add(descriptionRoutineEachFrame);
flowScheduler.add(descriptionRoutineEnd);
flowScheduler.add(voluntaryRoutineBegin);
flowScheduler.add(voluntaryRoutineEachFrame);
flowScheduler.add(voluntaryRoutineEnd);
flowScheduler.add(contactRoutineBegin);
flowScheduler.add(contactRoutineEachFrame);
flowScheduler.add(contactRoutineEnd);
flowScheduler.add(confidentialityRoutineBegin);
flowScheduler.add(confidentialityRoutineEachFrame);
flowScheduler.add(confidentialityRoutineEnd);
flowScheduler.add(informationRoutineBegin);
flowScheduler.add(informationRoutineEachFrame);
flowScheduler.add(informationRoutineEnd);
flowScheduler.add(consentRoutineBegin);
flowScheduler.add(consentRoutineEachFrame);
flowScheduler.add(consentRoutineEnd);
flowScheduler.add(languageL1RoutineBegin);
flowScheduler.add(languageL1RoutineEachFrame);
flowScheduler.add(languageL1RoutineEnd);
flowScheduler.add(languageL2RoutineBegin);
flowScheduler.add(languageL2RoutineEachFrame);
flowScheduler.add(languageL2RoutineEnd);
flowScheduler.add(languageL2OralRoutineBegin);
flowScheduler.add(languageL2OralRoutineEachFrame);
flowScheduler.add(languageL2OralRoutineEnd);
flowScheduler.add(languageL2WrittenRoutineBegin);
flowScheduler.add(languageL2WrittenRoutineEachFrame);
flowScheduler.add(languageL2WrittenRoutineEnd);
flowScheduler.add(languageL3RoutineBegin);
flowScheduler.add(languageL3RoutineEachFrame);
flowScheduler.add(languageL3RoutineEnd);
flowScheduler.add(languageL3OralRoutineBegin);
flowScheduler.add(languageL3OralRoutineEachFrame);
flowScheduler.add(languageL3OralRoutineEnd);
flowScheduler.add(languageL3WrittenRoutineBegin);
flowScheduler.add(languageL3WrittenRoutineEachFrame);
flowScheduler.add(languageL3WrittenRoutineEnd);
flowScheduler.add(languageCatalanOralRoutineBegin);
flowScheduler.add(languageCatalanOralRoutineEachFrame);
flowScheduler.add(languageCatalanOralRoutineEnd);
flowScheduler.add(languageCatalanWrittenRoutineBegin);
flowScheduler.add(languageCatalanWrittenRoutineEachFrame);
flowScheduler.add(languageCatalanWrittenRoutineEnd);
flowScheduler.add(languageCatalanTimeRoutineBegin);
flowScheduler.add(languageCatalanTimeRoutineEachFrame);
flowScheduler.add(languageCatalanTimeRoutineEnd);
flowScheduler.add(languageSpanishOralRoutineBegin);
flowScheduler.add(languageSpanishOralRoutineEachFrame);
flowScheduler.add(languageSpanishOralRoutineEnd);
flowScheduler.add(languageSpanishWrittenRoutineBegin);
flowScheduler.add(languageSpanishWrittenRoutineEachFrame);
flowScheduler.add(languageSpanishWrittenRoutineEnd);
flowScheduler.add(languageSpanishTimeRoutineBegin);
flowScheduler.add(languageSpanishTimeRoutineEachFrame);
flowScheduler.add(languageSpanishTimeRoutineEnd);
flowScheduler.add(demoAgeRoutineBegin);
flowScheduler.add(demoAgeRoutineEachFrame);
flowScheduler.add(demoAgeRoutineEnd);
flowScheduler.add(demoSexRoutineBegin);
flowScheduler.add(demoSexRoutineEachFrame);
flowScheduler.add(demoSexRoutineEnd);
flowScheduler.add(demoEducationRoutineBegin);
flowScheduler.add(demoEducationRoutineEachFrame);
flowScheduler.add(demoEducationRoutineEnd);
flowScheduler.add(demoCityRoutineBegin);
flowScheduler.add(demoCityRoutineEachFrame);
flowScheduler.add(demoCityRoutineEnd);
flowScheduler.add(demoVisionRoutineBegin);
flowScheduler.add(demoVisionRoutineEachFrame);
flowScheduler.add(demoVisionRoutineEnd);
flowScheduler.add(demoLanguageRoutineBegin);
flowScheduler.add(demoLanguageRoutineEachFrame);
flowScheduler.add(demoLanguageRoutineEnd);
flowScheduler.add(setupLocationRoutineBegin);
flowScheduler.add(setupLocationRoutineEachFrame);
flowScheduler.add(setupLocationRoutineEnd);
flowScheduler.add(setupNoiseRoutineBegin);
flowScheduler.add(setupNoiseRoutineEachFrame);
flowScheduler.add(setupNoiseRoutineEnd);
flowScheduler.add(instructionsRoutineBegin);
flowScheduler.add(instructionsRoutineEachFrame);
flowScheduler.add(instructionsRoutineEnd);
flowScheduler.add(instructions2RoutineBegin);
flowScheduler.add(instructions2RoutineEachFrame);
flowScheduler.add(instructions2RoutineEnd);
const trialsPracticeCatalanLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsPracticeCatalanLoopBegin, trialsPracticeCatalanLoopScheduler);
flowScheduler.add(trialsPracticeCatalanLoopScheduler);
flowScheduler.add(trialsPracticeCatalanLoopEnd);
const trialsPracticeSpanishLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsPracticeSpanishLoopBegin, trialsPracticeSpanishLoopScheduler);
flowScheduler.add(trialsPracticeSpanishLoopScheduler);
flowScheduler.add(trialsPracticeSpanishLoopEnd);
flowScheduler.add(beginRoutineBegin);
flowScheduler.add(beginRoutineEachFrame);
flowScheduler.add(beginRoutineEnd);
const trialsCatalanLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsCatalanLoopBegin, trialsCatalanLoopScheduler);
flowScheduler.add(trialsCatalanLoopScheduler);
flowScheduler.add(trialsCatalanLoopEnd);
const trialsSpanishLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsSpanishLoopBegin, trialsSpanishLoopScheduler);
flowScheduler.add(trialsSpanishLoopScheduler);
flowScheduler.add(trialsSpanishLoopEnd);
flowScheduler.add(farewellRoutineBegin);
flowScheduler.add(farewellRoutineEachFrame);
flowScheduler.add(farewellRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls(('https://psy-oxford.sona-systems.com/webstudy_credit.aspx?experiment_id=766&credit_token=23c483c2523249e3bc0bc1ab27a99117&survey_code=' + expInfo['participant']), '');

  return Scheduler.Event.NEXT;
}

var setupClock;
var setupTextTitle;
var setupText;
var setupTextNext;
var letterKeysAllowed;
var welcomeClock;
var welcomeTextTitle;
var welcomeText;
var welcomeTextNext;
var descriptionClock;
var descriptionTextTitle;
var descriptionText;
var descriptionTextNext;
var voluntaryClock;
var voluntaryTextTitle;
var voluntaryText;
var voluntaryTextNext;
var contactClock;
var contactTextTitle;
var contactText;
var contactTextNext;
var confidentialityClock;
var confidentialityTextTitle;
var confidentialityText;
var confidentialityTextNext;
var informationClock;
var informationTextTitle;
var informationText;
var informationTextNext;
var consentClock;
var consentTextTitle;
var consentText;
var consentTextNext;
var consentKey;
var languageL1Clock;
var languageL1TextTitle;
var languageL1Text;
var languageL1TextNext;
var languageL1Key;
var languageL2Clock;
var languageL2TextTitle;
var languageL2Text;
var languageL2TextNext;
var languageL2TextInput;
var languageL2OralClock;
var languageL2OralTextTitle;
var languageL2OralText;
var languageL2OralTextNext;
var languageL2OralKey;
var languageL2WrittenClock;
var languageL2WrittenTextTitle;
var languageL2WrittenText;
var languageL2WrittenTextNext;
var languageL2WrittenKey;
var languageL3Clock;
var languageL3TextTitle;
var languageL3Text;
var languageL3TextNext;
var languageL3TextInput;
var languageL3OralClock;
var languageL3OralTextTitle;
var languageL3OralText;
var languageL3OralTextNext;
var languageL3OralKey;
var languageL3WrittenClock;
var languageL3WrittenTextTitle;
var languageL3WrittenText;
var languageL3WrittenTextNext;
var languageL3WrittenKey;
var languageCatalanOralClock;
var languageCatalanOralTextTitle;
var languageCatalanOralText;
var languageCatalanOralTextNext;
var languageCatalanOralKey;
var languageCatalanWrittenClock;
var languageCatalanWrittenTextTitle;
var languageCatalanWrittenText;
var languageCatalanWrittenTextNext;
var languageCatalanWrittenKey;
var languageCatalanTimeClock;
var languageCatalanTimeTextTitle;
var languageCatalanTimeText;
var languageCatalanTimeTextNext;
var languageCatalanTimeKey;
var languageSpanishOralClock;
var languageSpanishOralTextTitle;
var languageSpanishOralText;
var languageSpanishOralTextNext;
var languageSpanishOralKey;
var languageSpanishWrittenClock;
var languageSpanishWrittenTextTitle;
var languageSpanishWrittenText;
var languageSpanishWrittenTextNext;
var languageSpanishWrittenKey;
var languageSpanishTimeClock;
var languageSpanishTimeTextTitle;
var languageSpanishTimeText;
var languageSpanishTimeTextNext;
var languageSpanishTimeKey;
var demoAgeClock;
var demoAgeTextTitle;
var demoAgeText;
var demoAgeTextNext;
var demoAgeTextInput;
var demoSexClock;
var demoSexTextTitle;
var demoSexText;
var demoSexTextNext;
var demoSexKey;
var demoEducationClock;
var demoEducationTextTitle;
var demoEducationText;
var demoEducationTextNext;
var demoEducationKey;
var demoCityClock;
var demoCityTextTitle;
var demoCityText;
var demoCityTextNext;
var demoCityTextInput;
var demoVisionClock;
var demoVisionTextTitle;
var demoVisionText;
var demoVisionTextNext;
var demoVisionKey;
var demoLanguageClock;
var demoLanguageTextTitle;
var demoLanguageText;
var demoLanguageTextNext;
var demoLanguageKey;
var setupLocationClock;
var setupLocationTextTitle;
var setupLocationText;
var setupLocationTextNext;
var setupLocationKey;
var setupNoiseClock;
var setupNoiseTextTitle;
var setupNoiseText;
var setupNoiseTextNext;
var setupNoiseKey;
var instructionsClock;
var instructionsTextTitle;
var instructionsText;
var instructionsTextNext;
var instructionsKeys;
var instructions2Clock;
var instructions2TextTitle;
var instructions2Text;
var instructions2TextNext;
var fixationClock;
var fixationText;
var trialClock;
var trialText;
var trialSound;
var inputText;
var beginClock;
var beginText;
var beginNext;
var farewellClock;
var farewellText;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "setup"
  setupClock = new util.Clock();
  setupTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupTextTitle',
    text: 'SET UP',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  setupText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupText',
    text: 'If possible, use Chrome or Mozilla Firefox\n\nUse a computer or a laptop (not a tablet or a phone)\n\nUse headphones \n\nClose all tabs other than this one\n\nDo not switch tabs in the browser\n\nIf, for any reason, you restart the study (e.g. because you reloaded the website or an internet failure), let us know by sending an email to serene.siow@psy.ox.ac.uk.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  setupTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupTextNext',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  var letterKeysAllowed;
  letterKeysAllowed = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "return", "backspace", "escape", "space"];
  
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  welcomeTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcomeTextTitle',
    text: 'WELCOME',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  welcomeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcomeText',
    text: 'This is a study designed by researchers from the Universitat Pompeu Fabra (Barcelona, Spain) and the University of Oxford (Oxford, UK). The aim of the study is to investigate how toddlers and adults process foreign words. The audios you will listen to throughout this study were recorded in a baby-directed style.\n\nYou have been invited to participate as you are between 18 and 25 years old, and a English native speaker with no knowledge of Spanish or Catalan.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  welcomeTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcomeTextNext',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "description"
  descriptionClock = new util.Clock();
  descriptionTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'descriptionTextTitle',
    text: 'OVERVIEW',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  descriptionText = new visual.TextStim({
    win: psychoJS.window,
    name: 'descriptionText',
    text: 'Firstly, you will be asked to complete a BRIEF QUESTIONNAIRE (your language profile, level of education, etc.).\n\nIn the main STUDY, you will listen to a series of SPANISH or CATALAN words. Your task will be to GUESS the TRANSLATION of each word in ENGLISH and TYPE your answer using the computer keyboard.\n\nThis should take around 30 minutes.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  descriptionTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'descriptionTextNext',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "voluntary"
  voluntaryClock = new util.Clock();
  voluntaryTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'voluntaryTextTitle',
    text: 'DO I HAVE TO TAKE PART?',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  voluntaryText = new visual.TextStim({
    win: psychoJS.window,
    name: 'voluntaryText',
    text: 'Participation in this study is absolutely VOLUNTARY. If you do decide to take part, you may withdraw at any point for any reason by pressing the ESC button. However, we are only able to reimburse participants who complete the full task.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  voluntaryTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'voluntaryTextNext',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "contact"
  contactClock = new util.Clock();
  contactTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'contactTextTitle',
    text: 'CONTACT DETAILS',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  contactText = new visual.TextStim({
    win: psychoJS.window,
    name: 'contactText',
    text: 'If you have any questions about this study, please contact the researchers.\nEmail: serene.siow@psy.ox.ac.uk\n \nPrincipal Investigators: Núria Sebastian-Galles and Kim Plunkett\nResearchers: Gonzalo García-Castro and Serene Siow\n \nCenter for Brain and Cognition, Universitat Pompeu Fabra\nDepartment of Experimental Psychology, University of Oxford',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  contactTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'contactTextNext',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "confidentiality"
  confidentialityClock = new util.Clock();
  confidentialityTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'confidentialityTextTitle',
    text: 'HOW WILL MY DATA BE USED?',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  confidentialityText = new visual.TextStim({
    win: psychoJS.window,
    name: 'confidentialityText',
    text: 'Your answers will be completely ANONYMOUS, and we will take all reasonable measures to ensure that they remain confidential.\n \nYour DATA WILL BE STORED in a password-protected file and MAY BE USED in academic publications IN AN ANONYMISED FORM. Your IP address will NOT BE STORED. Research data will be stored for a minimum of three years after publication or public release.\n \nWe would also like your permission to use your anonymised data in future studies, and to SHARE data with other researchers (e.g. in online databases). Any personal information that could identify you will be REMOVED or REPLACED before files are SHARED with other researchers or results are MADE PUBLIC.\n \nThis project has received ethics clearance through the University of Oxford Central University Research Ethics Committee, R60939/RE005.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  confidentialityTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'confidentialityTextNext',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "information"
  informationClock = new util.Clock();
  informationTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'informationTextTitle',
    text: 'NEED MORE INFORMATION?',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  informationText = new visual.TextStim({
    win: psychoJS.window,
    name: 'informationText',
    text: 'If you have a concern about any aspect of this study, please speak to Serene Siow (serene.siow@psy.ox.ac.uk), and we will do our best to answer your query.\n\nIf you remain unhappy or wish to make a formal complaint, please contact the Chair of the Research Ethics Committee at the University of Oxford.\n \nChair, Medical Sciences Interdivisional Research Ethics Committee;\nEmail: ethics@medsci.ox.ac.uk',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  informationTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'informationTextNext',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  consentTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'consentTextTitle',
    text: 'INFORMED CONSENT',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  consentText = new visual.TextStim({
    win: psychoJS.window,
    name: 'consentText',
    text: 'BY PRESSING SPACE, I certify that I am 18 years of age or over. I agree to participate in the study described. I have made this decision based on the information I have read in the consent information. I have had the opportunity to receive any additional details I wanted about the study and understand that I may ask questions in the future. I understand that I may withdraw this consent at any time.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  consentTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'consentTextNext',
    text: 'Press SPACE to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  consentKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageL1"
  languageL1Clock = new util.Clock();
  languageL1TextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL1TextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageL1Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL1Text',
    text: 'What is your NATIVE language?\n\ne) English\ns) Spanish\nc) Catalan\no) Other',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageL1TextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL1TextNext',
    text: 'Press the corresponding letter >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageL1Key = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageL2"
  languageL2Clock = new util.Clock();
  languageL2TextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2TextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageL2Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2Text',
    text: 'Do you know any other SECOND LANGUAGE, different than the one you indicated before? If yes, type which one and press RETURN. If no, press RETURN without writing anything.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageL2TextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2TextNext',
    text: 'Press RETURN to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageL2TextInput = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2TextInput',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "languageL2Oral"
  languageL2OralClock = new util.Clock();
  languageL2OralTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2OralTextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageL2OralText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2OralText',
    text: 'On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in your SECOND LANGUAGE?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageL2OralTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2OralTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageL2OralKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageL2Written"
  languageL2WrittenClock = new util.Clock();
  languageL2WrittenTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2WrittenTextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageL2WrittenText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2WrittenText',
    text: 'On a scale of 1-5, how would you rate your WRITTEN proficiency in your SECOND LANGUAGE?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageL2WrittenTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL2WrittenTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageL2WrittenKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageL3"
  languageL3Clock = new util.Clock();
  languageL3TextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3TextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageL3Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3Text',
    text: 'Do you know any other THIRD LANGUAGE, different than the ones you indicated before? If yes, type which one(s) and press RETURN. If no, press RETURN leaving it blank.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageL3TextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3TextNext',
    text: 'Press RETURN to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageL3TextInput = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3TextInput',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "languageL3Oral"
  languageL3OralClock = new util.Clock();
  languageL3OralTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3OralTextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageL3OralText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3OralText',
    text: 'On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in your THIRD LANGUAGE?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native / I am native',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageL3OralTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3OralTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageL3OralKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageL3Written"
  languageL3WrittenClock = new util.Clock();
  languageL3WrittenTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3WrittenTextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageL3WrittenText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3WrittenText',
    text: 'On a scale of 1-5, how would you rate your WRITTEN proficiency in your THIRD LANGUAGE?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageL3WrittenTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageL3WrittenTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageL3WrittenKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageCatalanOral"
  languageCatalanOralClock = new util.Clock();
  languageCatalanOralTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanOralTextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageCatalanOralText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanOralText',
    text: 'On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in CATALAN?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageCatalanOralTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanOralTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageCatalanOralKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageCatalanWritten"
  languageCatalanWrittenClock = new util.Clock();
  languageCatalanWrittenTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanWrittenTextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageCatalanWrittenText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanWrittenText',
    text: 'On a scale of 1-5, how would you rate your WRITTEN proficiency in CATALAN?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageCatalanWrittenTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanWrittenTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageCatalanWrittenKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageCatalanTime"
  languageCatalanTimeClock = new util.Clock();
  languageCatalanTimeTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanTimeTextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageCatalanTimeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanTimeText',
    text: 'How long have you spent in any REGION where CATALAN is spoken (Catalonia, Valencia, Balearic Islands), including your childhood? Pick the option that best describes your situation:\n\n1) Never or less than 1 month\n2) Between 1 and 3 months\n3) I used to spend holidays there\n4) I lived there for less than 6 months\n5) I lived there for 6 months or longer',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageCatalanTimeTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageCatalanTimeTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageCatalanTimeKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageSpanishOral"
  languageSpanishOralClock = new util.Clock();
  languageSpanishOralTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishOralTextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageSpanishOralText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishOralText',
    text: 'On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in SPANISH?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageSpanishOralTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishOralTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageSpanishOralKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageSpanishWritten"
  languageSpanishWrittenClock = new util.Clock();
  languageSpanishWrittenTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishWrittenTextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageSpanishWrittenText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishWrittenText',
    text: 'On a scale of 1-5, how would you rate your WRITTEN proficiency in SPANISH?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageSpanishWrittenTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishWrittenTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageSpanishWrittenKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "languageSpanishTime"
  languageSpanishTimeClock = new util.Clock();
  languageSpanishTimeTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishTimeTextTitle',
    text: 'LANGUAGE QUESTIONNAIRE',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  languageSpanishTimeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishTimeText',
    text: 'How long have you spent in any REGION where SPANISH is spoken (Spain, South America), including your childhood? Pick the option that best describes your situation:\n\n1) Never or less than 1 month\n2) Between 1 and 3 months\n3) I used to spend holidays there\n4) I lived there for less than 6 months\n5) I lived there for 6 months or longer',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  languageSpanishTimeTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'languageSpanishTimeTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  languageSpanishTimeKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "demoAge"
  demoAgeClock = new util.Clock();
  demoAgeTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoAgeTextTitle',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  demoAgeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoAgeText',
    text: 'Please, type your age (in years) and then press RETURN:',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  demoAgeTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoAgeTextNext',
    text: 'Press RETURN to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  demoAgeTextInput = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoAgeTextInput',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "demoSex"
  demoSexClock = new util.Clock();
  demoSexTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoSexTextTitle',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  demoSexText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoSexText',
    text: 'Sex:\n\nf) Female\nm) Male\no) Other',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  demoSexTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoSexTextNext',
    text: 'Press the corresponding letter >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  demoSexKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "demoEducation"
  demoEducationClock = new util.Clock();
  demoEducationTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoEducationTextTitle',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  demoEducationText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoEducationText',
    text: 'What is your highest level of EDUCATIONAL ACHIEVEMENT?\n\n1) No qualifications\n2) Left school at 16 with GCSE or equivalent\n3) Left school at 18 with A-Levels or equivalent\n4) University degree or equivalent\n5) Vocational training',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  demoEducationTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoEducationTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  demoEducationKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "demoCity"
  demoCityClock = new util.Clock();
  demoCityTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoCityTextTitle',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  demoCityText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoCityText',
    text: 'What CITY do you live in? Type it and press RETURN to continue.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  demoCityTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoCityTextNext',
    text: 'Press RETURN to continue >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  demoCityTextInput = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoCityTextInput',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "demoVision"
  demoVisionClock = new util.Clock();
  demoVisionTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoVisionTextTitle',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  demoVisionText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoVisionText',
    text: 'Do you have normal or corrected-to-normal VISION?\n\ny) Yes \nn) No',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  demoVisionTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoVisionTextNext',
    text: 'Press the corresponding letter >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  demoVisionKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "demoLanguage"
  demoLanguageClock = new util.Clock();
  demoLanguageTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoLanguageTextTitle',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  demoLanguageText = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoLanguageText',
    text: 'Have you been diagnosed with any LANGUAGE (e.g., DYSLEXIA) OR HEARING IMPAIRMENT?\n\ny) Yes\nn) No',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  demoLanguageTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'demoLanguageTextNext',
    text: 'Press the corresponding letter >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  demoLanguageKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "setupLocation"
  setupLocationClock = new util.Clock();
  setupLocationTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupLocationTextTitle',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  setupLocationText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupLocationText',
    text: 'WHERE are you completing this study?\n\n1) At home\n2) At the library\n3) At a cafe or restaurant\n4) At a friend’s house\n5) At school\n6) At work\n7) Other',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  setupLocationTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupLocationTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  setupLocationKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "setupNoise"
  setupNoiseClock = new util.Clock();
  setupNoiseTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupNoiseTextTitle',
    text: 'DEMOGRAPHIC INFORMATION',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  setupNoiseText = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupNoiseText',
    text: 'How NOISY was the environment in which you completed the experiment? \n\n1) Very quiet (like a library)\n2) Somewhat quiet (like an office)\n3) Somewhat noisy (like being at the park)\n4) Very noisy (like being at a busy street)',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  setupNoiseTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'setupNoiseTextNext',
    text: 'Press the corresponding number >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  setupNoiseKey = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  instructionsTextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionsTextTitle',
    text: 'INSTRUCTIONS',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  instructionsText = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionsText',
    text: 'You will listen to some words through your headphones.\n\nWords are in Catalan or Spanish and were recorded in a baby-directed manner. You will have to GUESS and TYPE the TRANSLATION of each word IN ENGLISH.\n\nStart typing as soon as you come up with an answer. It is probable that you do not know it. Type the translation you think is most likely to be correct. You MUST type an answer FOR EACH WORD.\n\nYou can use BACKSPACE to correct any typing errors, as you would normally.\n\nAfter typing the word, press RETURN to continue to the next word.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  instructionsTextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionsTextNext',
    text: 'NEXT, YOU WILL COMPLETE 5 PRACTICE TRIALS\n\nPress SPACE to continue.',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.7)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  instructionsKeys = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions2"
  instructions2Clock = new util.Clock();
  instructions2TextTitle = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions2TextTitle',
    text: 'INSTRUCTIONS',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.8], height: 0.11,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  instructions2Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions2Text',
    text: 'You may adjust the volume during these trials to avoid having to do it during the main experiment. Make sure words are loud enough for you to hear them clearly.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  instructions2TextNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions2TextNext',
    text: 'Press SPACE to start 5 practice trials >',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixationText = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixationText',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  trialText = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trialSound = new Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  trialSound.setVolume(1);
  inputText = "";
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixationText = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixationText',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  trialText = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trialSound = new Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  trialSound.setVolume(1);
  inputText = "";
  
  // Initialize components for Routine "begin"
  beginClock = new util.Clock();
  beginText = new visual.TextStim({
    win: psychoJS.window,
    name: 'beginText',
    text: 'You have completed the PRACTICE trials.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  beginNext = new visual.TextStim({
    win: psychoJS.window,
    name: 'beginNext',
    text: 'Press SPACE to start >',
    font: 'Arial',
    units : undefined, 
    pos: [0.7, (- 0.8)], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixationText = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixationText',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  trialText = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trialSound = new Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  trialSound.setVolume(1);
  inputText = "";
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixationText = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixationText',
    text: '+',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  trialText = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialText',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trialSound = new Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  trialSound.setVolume(1);
  inputText = "";
  
  // Initialize components for Routine "farewell"
  farewellClock = new util.Clock();
  farewellText = new visual.TextStim({
    win: psychoJS.window,
    name: 'farewellText',
    text: 'Congratulations! You have finished.\n\nTHANKS A LOT FOR YOUR PARTICIPATION.\n\nIf you have any questions, get in touch with us at serene.siow@ox.ac.uk\n\nPress SPACE to be redirected to SONA.\n\nPlease, wait to be redirected to SONA, otherwise you may not receive your credit.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var setupComponents;
function setupRoutineBegin() {
  //------Prepare to start Routine 'setup'-------
  t = 0;
  setupClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // align text to the left
  setupText.setAlignHoriz("left");
  welcomeText.setAlignHoriz("left");
  descriptionText.setAlignHoriz("left");
  voluntaryText.setAlignHoriz("left");
  contactText.setAlignHoriz("left");
  confidentialityText.setAlignHoriz("left");
  informationText.setAlignHoriz("left");
  consentText.setAlignHoriz("left");
  languageL1Text.setAlignHoriz("left");
  languageL2Text.setAlignHoriz("left");
  languageL2OralText.setAlignHoriz("left");
  languageL2WrittenText.setAlignHoriz("left");
  languageL3Text.setAlignHoriz("left");
  languageL3OralText.setAlignHoriz("left");
  languageL3WrittenText.setAlignHoriz("left");
  languageCatalanOralText.setAlignHoriz("left");
  languageCatalanWrittenText.setAlignHoriz("left");
  languageSpanishOralText.setAlignHoriz("left");
  languageSpanishWrittenText.setAlignHoriz("left");
  languageSpanishTimeText.setAlignHoriz("left");
  demoAgeText.setAlignHoriz("left");
  demoSexText.setAlignHoriz("left");
  demoEducationText.setAlignHoriz("left");
  demoCityText.setAlignHoriz("left");
  demoVisionText.setAlignHoriz("left");
  demoLanguageText.setAlignHoriz("left");
  setupLocationText.setAlignHoriz("left");
  setupNoiseText.setAlignHoriz("left");
  instructionsText.setAlignHoriz("left");
  instructions2Text.setAlignHoriz("left");
  beginText.setAlignHoriz("left");
  farewellText.setAlignHoriz("left");
  
  // keep track of which components have finished
  setupComponents = [];
  setupComponents.push(setupTextTitle);
  setupComponents.push(setupText);
  setupComponents.push(setupTextNext);
  
  for (const thisComponent of setupComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var keys;
var n;
var continueRoutine;
function setupRoutineEachFrame() {
  //------Loop for each frame of Routine 'setup'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = setupClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *setupTextTitle* updates
  if (t >= 0.0 && setupTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    setupTextTitle.tStart = t;  // (not accounting for frame time here)
    setupTextTitle.frameNStart = frameN;  // exact frame index
    setupTextTitle.setAutoDraw(true);
  }

  
  // *setupText* updates
  if (t >= 0.0 && setupText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    setupText.tStart = t;  // (not accounting for frame time here)
    setupText.frameNStart = frameN;  // exact frame index
    setupText.setAutoDraw(true);
  }

  
  // *setupTextNext* updates
  if (t >= 0.0 && setupTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    setupTextNext.tStart = t;  // (not accounting for frame time here)
    setupTextNext.frameNStart = frameN;  // exact frame index
    setupTextNext.setAutoDraw(true);
  }

  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of setupComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function setupRoutineEnd() {
  //------Ending Routine 'setup'-------
  for (const thisComponent of setupComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "setup" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var welcomeComponents;
function welcomeRoutineBegin() {
  //------Prepare to start Routine 'welcome'-------
  t = 0;
  welcomeClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  welcomeComponents = [];
  welcomeComponents.push(welcomeTextTitle);
  welcomeComponents.push(welcomeText);
  welcomeComponents.push(welcomeTextNext);
  
  for (const thisComponent of welcomeComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function welcomeRoutineEachFrame() {
  //------Loop for each frame of Routine 'welcome'-------
  let continueRoutine = true; // until we're told otherwise
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

  
  // *welcomeTextNext* updates
  if (t >= 0.0 && welcomeTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    welcomeTextNext.tStart = t;  // (not accounting for frame time here)
    welcomeTextNext.frameNStart = frameN;  // exact frame index
    welcomeTextNext.setAutoDraw(true);
  }

  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
      psychoJS.quit('Has presionado ESC. El estudio ha terminado. ¡Gracias por participar!');
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of welcomeComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEnd() {
  //------Ending Routine 'welcome'-------
  for (const thisComponent of welcomeComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var descriptionComponents;
function descriptionRoutineBegin() {
  //------Prepare to start Routine 'description'-------
  t = 0;
  descriptionClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  descriptionComponents = [];
  descriptionComponents.push(descriptionTextTitle);
  descriptionComponents.push(descriptionText);
  descriptionComponents.push(descriptionTextNext);
  
  for (const thisComponent of descriptionComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function descriptionRoutineEachFrame() {
  //------Loop for each frame of Routine 'description'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = descriptionClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *descriptionTextTitle* updates
  if (t >= 0.0 && descriptionTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    descriptionTextTitle.tStart = t;  // (not accounting for frame time here)
    descriptionTextTitle.frameNStart = frameN;  // exact frame index
    descriptionTextTitle.setAutoDraw(true);
  }

  
  // *descriptionText* updates
  if (t >= 0.0 && descriptionText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    descriptionText.tStart = t;  // (not accounting for frame time here)
    descriptionText.frameNStart = frameN;  // exact frame index
    descriptionText.setAutoDraw(true);
  }

  
  // *descriptionTextNext* updates
  if (t >= 0.0 && descriptionTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    descriptionTextNext.tStart = t;  // (not accounting for frame time here)
    descriptionTextNext.frameNStart = frameN;  // exact frame index
    descriptionTextNext.setAutoDraw(true);
  }

  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of descriptionComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function descriptionRoutineEnd() {
  //------Ending Routine 'description'-------
  for (const thisComponent of descriptionComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "description" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var voluntaryComponents;
function voluntaryRoutineBegin() {
  //------Prepare to start Routine 'voluntary'-------
  t = 0;
  voluntaryClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  voluntaryComponents = [];
  voluntaryComponents.push(voluntaryTextTitle);
  voluntaryComponents.push(voluntaryText);
  voluntaryComponents.push(voluntaryTextNext);
  
  for (const thisComponent of voluntaryComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function voluntaryRoutineEachFrame() {
  //------Loop for each frame of Routine 'voluntary'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = voluntaryClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *voluntaryTextTitle* updates
  if (t >= 0.0 && voluntaryTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    voluntaryTextTitle.tStart = t;  // (not accounting for frame time here)
    voluntaryTextTitle.frameNStart = frameN;  // exact frame index
    voluntaryTextTitle.setAutoDraw(true);
  }

  
  // *voluntaryText* updates
  if (t >= 0.0 && voluntaryText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    voluntaryText.tStart = t;  // (not accounting for frame time here)
    voluntaryText.frameNStart = frameN;  // exact frame index
    voluntaryText.setAutoDraw(true);
  }

  
  // *voluntaryTextNext* updates
  if (t >= 0.0 && voluntaryTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    voluntaryTextNext.tStart = t;  // (not accounting for frame time here)
    voluntaryTextNext.frameNStart = frameN;  // exact frame index
    voluntaryTextNext.setAutoDraw(true);
  }

  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of voluntaryComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function voluntaryRoutineEnd() {
  //------Ending Routine 'voluntary'-------
  for (const thisComponent of voluntaryComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "voluntary" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var contactComponents;
function contactRoutineBegin() {
  //------Prepare to start Routine 'contact'-------
  t = 0;
  contactClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  contactComponents = [];
  contactComponents.push(contactTextTitle);
  contactComponents.push(contactText);
  contactComponents.push(contactTextNext);
  
  for (const thisComponent of contactComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function contactRoutineEachFrame() {
  //------Loop for each frame of Routine 'contact'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = contactClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *contactTextTitle* updates
  if (t >= 0.0 && contactTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    contactTextTitle.tStart = t;  // (not accounting for frame time here)
    contactTextTitle.frameNStart = frameN;  // exact frame index
    contactTextTitle.setAutoDraw(true);
  }

  
  // *contactText* updates
  if (t >= 0.0 && contactText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    contactText.tStart = t;  // (not accounting for frame time here)
    contactText.frameNStart = frameN;  // exact frame index
    contactText.setAutoDraw(true);
  }

  
  // *contactTextNext* updates
  if (t >= 0.0 && contactTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    contactTextNext.tStart = t;  // (not accounting for frame time here)
    contactTextNext.frameNStart = frameN;  // exact frame index
    contactTextNext.setAutoDraw(true);
  }

  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
    psychoJS.quit('Has presionado ESC. El estudio ha terminado. ¡Gracias por participar!');
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of contactComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function contactRoutineEnd() {
  //------Ending Routine 'contact'-------
  for (const thisComponent of contactComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "contact" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var confidentialityComponents;
function confidentialityRoutineBegin() {
  //------Prepare to start Routine 'confidentiality'-------
  t = 0;
  confidentialityClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  confidentialityComponents = [];
  confidentialityComponents.push(confidentialityTextTitle);
  confidentialityComponents.push(confidentialityText);
  confidentialityComponents.push(confidentialityTextNext);
  
  for (const thisComponent of confidentialityComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function confidentialityRoutineEachFrame() {
  //------Loop for each frame of Routine 'confidentiality'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = confidentialityClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *confidentialityTextTitle* updates
  if (t >= 0.0 && confidentialityTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    confidentialityTextTitle.tStart = t;  // (not accounting for frame time here)
    confidentialityTextTitle.frameNStart = frameN;  // exact frame index
    confidentialityTextTitle.setAutoDraw(true);
  }

  
  // *confidentialityText* updates
  if (t >= 0.0 && confidentialityText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    confidentialityText.tStart = t;  // (not accounting for frame time here)
    confidentialityText.frameNStart = frameN;  // exact frame index
    confidentialityText.setAutoDraw(true);
  }

  
  // *confidentialityTextNext* updates
  if (t >= 0.0 && confidentialityTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    confidentialityTextNext.tStart = t;  // (not accounting for frame time here)
    confidentialityTextNext.frameNStart = frameN;  // exact frame index
    confidentialityTextNext.setAutoDraw(true);
  }

  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of confidentialityComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function confidentialityRoutineEnd() {
  //------Ending Routine 'confidentiality'-------
  for (const thisComponent of confidentialityComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "confidentiality" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var informationComponents;
function informationRoutineBegin() {
  //------Prepare to start Routine 'information'-------
  t = 0;
  informationClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  informationComponents = [];
  informationComponents.push(informationTextTitle);
  informationComponents.push(informationText);
  informationComponents.push(informationTextNext);
  
  for (const thisComponent of informationComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function informationRoutineEachFrame() {
  //------Loop for each frame of Routine 'information'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = informationClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *informationTextTitle* updates
  if (t >= 0.0 && informationTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    informationTextTitle.tStart = t;  // (not accounting for frame time here)
    informationTextTitle.frameNStart = frameN;  // exact frame index
    informationTextTitle.setAutoDraw(true);
  }

  
  // *informationText* updates
  if (t >= 0.0 && informationText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    informationText.tStart = t;  // (not accounting for frame time here)
    informationText.frameNStart = frameN;  // exact frame index
    informationText.setAutoDraw(true);
  }

  
  // *informationTextNext* updates
  if (t >= 0.0 && informationTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    informationTextNext.tStart = t;  // (not accounting for frame time here)
    informationTextNext.frameNStart = frameN;  // exact frame index
    informationTextNext.setAutoDraw(true);
  }

  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of informationComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function informationRoutineEnd() {
  //------Ending Routine 'information'-------
  for (const thisComponent of informationComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "information" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var consentComponents;
function consentRoutineBegin() {
  //------Prepare to start Routine 'consent'-------
  t = 0;
  consentClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  consentKey.keys = undefined;
  consentKey.rt = undefined;
  // keep track of which components have finished
  consentComponents = [];
  consentComponents.push(consentTextTitle);
  consentComponents.push(consentText);
  consentComponents.push(consentTextNext);
  consentComponents.push(consentKey);
  
  for (const thisComponent of consentComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function consentRoutineEachFrame() {
  //------Loop for each frame of Routine 'consent'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = consentClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *consentTextTitle* updates
  if (t >= 0.0 && consentTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    consentTextTitle.tStart = t;  // (not accounting for frame time here)
    consentTextTitle.frameNStart = frameN;  // exact frame index
    consentTextTitle.setAutoDraw(true);
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

  
  // *consentKey* updates
  if (t >= 0.0 && consentKey.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    consentKey.tStart = t;  // (not accounting for frame time here)
    consentKey.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { consentKey.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { consentKey.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { consentKey.clearEvents(); });
  }

  if (consentKey.status === PsychoJS.Status.STARTED) {
    let theseKeys = consentKey.getKeys({keyList: ['space', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      consentKey.keys = theseKeys[0].name;  // just the last key pressed
      consentKey.rt = theseKeys[0].rt;
    }
  }
  
  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of consentComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function consentRoutineEnd() {
  //------Ending Routine 'consent'-------
  for (const thisComponent of consentComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('consentKey.keys', consentKey.keys);
  if (typeof consentKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('consentKey.rt', consentKey.rt);
      }
  
  consentKey.stop();
  // the Routine "consent" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageL1Components;
function languageL1RoutineBegin() {
  //------Prepare to start Routine 'languageL1'-------
  t = 0;
  languageL1Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  languageL1Key.keys = undefined;
  languageL1Key.rt = undefined;
  // keep track of which components have finished
  languageL1Components = [];
  languageL1Components.push(languageL1TextTitle);
  languageL1Components.push(languageL1Text);
  languageL1Components.push(languageL1TextNext);
  languageL1Components.push(languageL1Key);
  
  for (const thisComponent of languageL1Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var _pj;
function languageL1RoutineEachFrame() {
  //------Loop for each frame of Routine 'languageL1'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageL1Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageL1TextTitle* updates
  if (t >= 0.0 && languageL1TextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL1TextTitle.tStart = t;  // (not accounting for frame time here)
    languageL1TextTitle.frameNStart = frameN;  // exact frame index
    languageL1TextTitle.setAutoDraw(true);
  }

  
  // *languageL1Text* updates
  if (t >= 0.0 && languageL1Text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL1Text.tStart = t;  // (not accounting for frame time here)
    languageL1Text.frameNStart = frameN;  // exact frame index
    languageL1Text.setAutoDraw(true);
  }

  
  // *languageL1TextNext* updates
  if (t >= 0.0 && languageL1TextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL1TextNext.tStart = t;  // (not accounting for frame time here)
    languageL1TextNext.frameNStart = frameN;  // exact frame index
    languageL1TextNext.setAutoDraw(true);
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
    let theseKeys = languageL1Key.getKeys({keyList: ['e', 's', 'c', 'o', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      languageL1Key.keys = theseKeys[0].name;  // just the last key pressed
      languageL1Key.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageL1Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageL1RoutineEnd() {
  //------Ending Routine 'languageL1'-------
  for (const thisComponent of languageL1Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('languageL1Key.keys', languageL1Key.keys);
  if (typeof languageL1Key.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('languageL1Key.rt', languageL1Key.rt);
      routineTimer.reset();
      }
  
  languageL1Key.stop();
  // the Routine "languageL1" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var isAccented;
var languageL2Components;
function languageL2RoutineBegin() {
  //------Prepare to start Routine 'languageL2'-------
  t = 0;
  languageL2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  psychoJS.eventManager.clearEvents();
  inputText = "";
  isAccented = false;
  
  // keep track of which components have finished
  languageL2Components = [];
  languageL2Components.push(languageL2TextTitle);
  languageL2Components.push(languageL2Text);
  languageL2Components.push(languageL2TextNext);
  languageL2Components.push(languageL2TextInput);
  
  for (const thisComponent of languageL2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var i;
var languageL2value;
var languageL3value;
function languageL2RoutineEachFrame() {
  //------Loop for each frame of Routine 'languageL2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageL2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageL2TextTitle* updates
  if (t >= 0.0 && languageL2TextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL2TextTitle.tStart = t;  // (not accounting for frame time here)
    languageL2TextTitle.frameNStart = frameN;  // exact frame index
    languageL2TextTitle.setAutoDraw(true);
  }

  
  // *languageL2Text* updates
  if (t >= 0.0 && languageL2Text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL2Text.tStart = t;  // (not accounting for frame time here)
    languageL2Text.frameNStart = frameN;  // exact frame index
    languageL2Text.setAutoDraw(true);
  }

  
  // *languageL2TextNext* updates
  if (t >= 0.0 && languageL2TextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL2TextNext.tStart = t;  // (not accounting for frame time here)
    languageL2TextNext.frameNStart = frameN;  // exact frame index
    languageL2TextNext.setAutoDraw(true);
  }

  
  // *languageL2TextInput* updates
  if (t >= 0.0 && languageL2TextInput.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL2TextInput.tStart = t;  // (not accounting for frame time here)
    languageL2TextInput.frameNStart = frameN;  // exact frame index
    languageL2TextInput.setAutoDraw(true);
  }

  
  if (languageL2TextInput.status === PsychoJS.Status.STARTED){ // only update if being drawn
    languageL2TextInput.setText(('> ' + inputText));
  }
  keys = psychoJS.eventManager.getKeys({"keyList": letterKeysAllowed});
  i = 0;
  if (keys.length) {
      if ((keys[i] === "escape")) {
          psychoJS.experiment.addData("languageL2", inputText);
          psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation. Press RETURN to exit.");
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
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageL2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageL2RoutineEnd() {
  //------Ending Routine 'languageL2'-------
  for (const thisComponent of languageL2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  console.log(languageL2value);
  
  // the Routine "languageL2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageL2OralComponents;
function languageL2OralRoutineBegin() {
  //------Prepare to start Routine 'languageL2Oral'-------
  t = 0;
  languageL2OralClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  languageL2OralKey.keys = undefined;
  languageL2OralKey.rt = undefined;
  // keep track of which components have finished
  languageL2OralComponents = [];
  languageL2OralComponents.push(languageL2OralTextTitle);
  languageL2OralComponents.push(languageL2OralText);
  languageL2OralComponents.push(languageL2OralTextNext);
  languageL2OralComponents.push(languageL2OralKey);
  
  for (const thisComponent of languageL2OralComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function languageL2OralRoutineEachFrame() {
  //------Loop for each frame of Routine 'languageL2Oral'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageL2OralClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageL2OralTextTitle* updates
  if (t >= 0.0 && languageL2OralTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL2OralTextTitle.tStart = t;  // (not accounting for frame time here)
    languageL2OralTextTitle.frameNStart = frameN;  // exact frame index
    languageL2OralTextTitle.setAutoDraw(true);
  }

  
  // *languageL2OralText* updates
  if (t >= 0.0 && languageL2OralText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL2OralText.tStart = t;  // (not accounting for frame time here)
    languageL2OralText.frameNStart = frameN;  // exact frame index
    languageL2OralText.setAutoDraw(true);
  }

  
  // *languageL2OralTextNext* updates
  if (t >= 0.0 && languageL2OralTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL2OralTextNext.tStart = t;  // (not accounting for frame time here)
    languageL2OralTextNext.frameNStart = frameN;  // exact frame index
    languageL2OralTextNext.setAutoDraw(true);
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
    let theseKeys = languageL2OralKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      languageL2OralKey.keys = theseKeys[0].name;  // just the last key pressed
      languageL2OralKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  if ((languageL2value==="")) {
      continueRoutine = false;
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageL2OralComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageL2OralRoutineEnd() {
  //------Ending Routine 'languageL2Oral'-------
  for (const thisComponent of languageL2OralComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('languageL2OralKey.keys', languageL2OralKey.keys);
  if (typeof languageL2OralKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('languageL2OralKey.rt', languageL2OralKey.rt);
      routineTimer.reset();
      }
  
  languageL2OralKey.stop();
  // the Routine "languageL2Oral" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageL2WrittenComponents;
function languageL2WrittenRoutineBegin() {
  //------Prepare to start Routine 'languageL2Written'-------
  t = 0;
  languageL2WrittenClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  languageL2WrittenKey.keys = undefined;
  languageL2WrittenKey.rt = undefined;
  // keep track of which components have finished
  languageL2WrittenComponents = [];
  languageL2WrittenComponents.push(languageL2WrittenTextTitle);
  languageL2WrittenComponents.push(languageL2WrittenText);
  languageL2WrittenComponents.push(languageL2WrittenTextNext);
  languageL2WrittenComponents.push(languageL2WrittenKey);
  
  for (const thisComponent of languageL2WrittenComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function languageL2WrittenRoutineEachFrame() {
  //------Loop for each frame of Routine 'languageL2Written'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageL2WrittenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageL2WrittenTextTitle* updates
  if (t >= 0.0 && languageL2WrittenTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL2WrittenTextTitle.tStart = t;  // (not accounting for frame time here)
    languageL2WrittenTextTitle.frameNStart = frameN;  // exact frame index
    languageL2WrittenTextTitle.setAutoDraw(true);
  }

  
  // *languageL2WrittenText* updates
  if (t >= 0.0 && languageL2WrittenText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL2WrittenText.tStart = t;  // (not accounting for frame time here)
    languageL2WrittenText.frameNStart = frameN;  // exact frame index
    languageL2WrittenText.setAutoDraw(true);
  }

  
  // *languageL2WrittenTextNext* updates
  if (t >= 0.0 && languageL2WrittenTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL2WrittenTextNext.tStart = t;  // (not accounting for frame time here)
    languageL2WrittenTextNext.frameNStart = frameN;  // exact frame index
    languageL2WrittenTextNext.setAutoDraw(true);
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
    let theseKeys = languageL2WrittenKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      languageL2WrittenKey.keys = theseKeys[0].name;  // just the last key pressed
      languageL2WrittenKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  if ((languageL2value === "")) {
      continueRoutine = false;
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageL2WrittenComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageL2WrittenRoutineEnd() {
  //------Ending Routine 'languageL2Written'-------
  for (const thisComponent of languageL2WrittenComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('languageL2WrittenKey.keys', languageL2WrittenKey.keys);
  if (typeof languageL2WrittenKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('languageL2WrittenKey.rt', languageL2WrittenKey.rt);
      routineTimer.reset();
      }
  
  languageL2WrittenKey.stop();
  // the Routine "languageL2Written" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageL3Components;
function languageL3RoutineBegin() {
  //------Prepare to start Routine 'languageL3'-------
  t = 0;
  languageL3Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  psychoJS.eventManager.clearEvents();
  inputText = "";
  isAccented = false;
  
  // keep track of which components have finished
  languageL3Components = [];
  languageL3Components.push(languageL3TextTitle);
  languageL3Components.push(languageL3Text);
  languageL3Components.push(languageL3TextNext);
  languageL3Components.push(languageL3TextInput);
  
  for (const thisComponent of languageL3Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function languageL3RoutineEachFrame() {
  //------Loop for each frame of Routine 'languageL3'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageL3Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageL3TextTitle* updates
  if (t >= 0.0 && languageL3TextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL3TextTitle.tStart = t;  // (not accounting for frame time here)
    languageL3TextTitle.frameNStart = frameN;  // exact frame index
    languageL3TextTitle.setAutoDraw(true);
  }

  
  // *languageL3Text* updates
  if (t >= 0.0 && languageL3Text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL3Text.tStart = t;  // (not accounting for frame time here)
    languageL3Text.frameNStart = frameN;  // exact frame index
    languageL3Text.setAutoDraw(true);
  }

  
  // *languageL3TextNext* updates
  if (t >= 0.0 && languageL3TextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL3TextNext.tStart = t;  // (not accounting for frame time here)
    languageL3TextNext.frameNStart = frameN;  // exact frame index
    languageL3TextNext.setAutoDraw(true);
  }

  
  // *languageL3TextInput* updates
  if (t >= 0.0 && languageL3TextInput.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL3TextInput.tStart = t;  // (not accounting for frame time here)
    languageL3TextInput.frameNStart = frameN;  // exact frame index
    languageL3TextInput.setAutoDraw(true);
  }

  
  if (languageL3TextInput.status === PsychoJS.Status.STARTED){ // only update if being drawn
    languageL3TextInput.setText(('> ' + inputText));
  }
  if ((languageL2value === "")) {
      continueRoutine = false;
  }
  keys = psychoJS.eventManager.getKeys({"keyList": letterKeysAllowed});
  i = 0;
  if (keys.length) {
      if ((keys[i] === "escape")) {
          psychoJS.experiment.addData("languageL3", inputText);
          psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation. Press RETURN to exit.");
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
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageL3Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageL3RoutineEnd() {
  //------Ending Routine 'languageL3'-------
  for (const thisComponent of languageL3Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  console.log(languageL3value);
  
  // the Routine "languageL3" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageL3OralComponents;
function languageL3OralRoutineBegin() {
  //------Prepare to start Routine 'languageL3Oral'-------
  t = 0;
  languageL3OralClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  languageL3OralKey.keys = undefined;
  languageL3OralKey.rt = undefined;
  // keep track of which components have finished
  languageL3OralComponents = [];
  languageL3OralComponents.push(languageL3OralTextTitle);
  languageL3OralComponents.push(languageL3OralText);
  languageL3OralComponents.push(languageL3OralTextNext);
  languageL3OralComponents.push(languageL3OralKey);
  
  for (const thisComponent of languageL3OralComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function languageL3OralRoutineEachFrame() {
  //------Loop for each frame of Routine 'languageL3Oral'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageL3OralClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageL3OralTextTitle* updates
  if (t >= 0.0 && languageL3OralTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL3OralTextTitle.tStart = t;  // (not accounting for frame time here)
    languageL3OralTextTitle.frameNStart = frameN;  // exact frame index
    languageL3OralTextTitle.setAutoDraw(true);
  }

  
  // *languageL3OralText* updates
  if (t >= 0.0 && languageL3OralText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL3OralText.tStart = t;  // (not accounting for frame time here)
    languageL3OralText.frameNStart = frameN;  // exact frame index
    languageL3OralText.setAutoDraw(true);
  }

  
  // *languageL3OralTextNext* updates
  if (t >= 0.0 && languageL3OralTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL3OralTextNext.tStart = t;  // (not accounting for frame time here)
    languageL3OralTextNext.frameNStart = frameN;  // exact frame index
    languageL3OralTextNext.setAutoDraw(true);
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
    let theseKeys = languageL3OralKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      languageL3OralKey.keys = theseKeys[0].name;  // just the last key pressed
      languageL3OralKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  if ((languageL2value === "" || languageL3value === "")) {
      continueRoutine = false;
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageL3OralComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageL3OralRoutineEnd() {
  //------Ending Routine 'languageL3Oral'-------
  for (const thisComponent of languageL3OralComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('languageL3OralKey.keys', languageL3OralKey.keys);
  if (typeof languageL3OralKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('languageL3OralKey.rt', languageL3OralKey.rt);
      routineTimer.reset();
      }
  
  languageL3OralKey.stop();
  // the Routine "languageL3Oral" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageL3WrittenComponents;
function languageL3WrittenRoutineBegin() {
  //------Prepare to start Routine 'languageL3Written'-------
  t = 0;
  languageL3WrittenClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  languageL3WrittenKey.keys = undefined;
  languageL3WrittenKey.rt = undefined;
  // keep track of which components have finished
  languageL3WrittenComponents = [];
  languageL3WrittenComponents.push(languageL3WrittenTextTitle);
  languageL3WrittenComponents.push(languageL3WrittenText);
  languageL3WrittenComponents.push(languageL3WrittenTextNext);
  languageL3WrittenComponents.push(languageL3WrittenKey);
  
  for (const thisComponent of languageL3WrittenComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function languageL3WrittenRoutineEachFrame() {
  //------Loop for each frame of Routine 'languageL3Written'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageL3WrittenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageL3WrittenTextTitle* updates
  if (t >= 0.0 && languageL3WrittenTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL3WrittenTextTitle.tStart = t;  // (not accounting for frame time here)
    languageL3WrittenTextTitle.frameNStart = frameN;  // exact frame index
    languageL3WrittenTextTitle.setAutoDraw(true);
  }

  
  // *languageL3WrittenText* updates
  if (t >= 0.0 && languageL3WrittenText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL3WrittenText.tStart = t;  // (not accounting for frame time here)
    languageL3WrittenText.frameNStart = frameN;  // exact frame index
    languageL3WrittenText.setAutoDraw(true);
  }

  
  // *languageL3WrittenTextNext* updates
  if (t >= 0.0 && languageL3WrittenTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageL3WrittenTextNext.tStart = t;  // (not accounting for frame time here)
    languageL3WrittenTextNext.frameNStart = frameN;  // exact frame index
    languageL3WrittenTextNext.setAutoDraw(true);
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
    let theseKeys = languageL3WrittenKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      languageL3WrittenKey.keys = theseKeys[0].name;  // just the last key pressed
      languageL3WrittenKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  if ((languageL2value === "" || languageL3value=== "")) {
      continueRoutine = false;
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageL3WrittenComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageL3WrittenRoutineEnd() {
  //------Ending Routine 'languageL3Written'-------
  for (const thisComponent of languageL3WrittenComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('languageL3WrittenKey.keys', languageL3WrittenKey.keys);
  if (typeof languageL3WrittenKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('languageL3WrittenKey.rt', languageL3WrittenKey.rt);
      routineTimer.reset();
      }
  
  languageL3WrittenKey.stop();
  // the Routine "languageL3Written" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageCatalanOralComponents;
function languageCatalanOralRoutineBegin() {
  //------Prepare to start Routine 'languageCatalanOral'-------
  t = 0;
  languageCatalanOralClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  languageCatalanOralKey.keys = undefined;
  languageCatalanOralKey.rt = undefined;
  // keep track of which components have finished
  languageCatalanOralComponents = [];
  languageCatalanOralComponents.push(languageCatalanOralTextTitle);
  languageCatalanOralComponents.push(languageCatalanOralText);
  languageCatalanOralComponents.push(languageCatalanOralTextNext);
  languageCatalanOralComponents.push(languageCatalanOralKey);
  
  for (const thisComponent of languageCatalanOralComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function languageCatalanOralRoutineEachFrame() {
  //------Loop for each frame of Routine 'languageCatalanOral'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageCatalanOralClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageCatalanOralTextTitle* updates
  if (t >= 0.0 && languageCatalanOralTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageCatalanOralTextTitle.tStart = t;  // (not accounting for frame time here)
    languageCatalanOralTextTitle.frameNStart = frameN;  // exact frame index
    languageCatalanOralTextTitle.setAutoDraw(true);
  }

  
  // *languageCatalanOralText* updates
  if (t >= 0.0 && languageCatalanOralText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageCatalanOralText.tStart = t;  // (not accounting for frame time here)
    languageCatalanOralText.frameNStart = frameN;  // exact frame index
    languageCatalanOralText.setAutoDraw(true);
  }

  
  // *languageCatalanOralTextNext* updates
  if (t >= 0.0 && languageCatalanOralTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageCatalanOralTextNext.tStart = t;  // (not accounting for frame time here)
    languageCatalanOralTextNext.frameNStart = frameN;  // exact frame index
    languageCatalanOralTextNext.setAutoDraw(true);
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
    let theseKeys = languageCatalanOralKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      languageCatalanOralKey.keys = theseKeys[0].name;  // just the last key pressed
      languageCatalanOralKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // if Catalan is L2 or L3, skip
  if ((languageL2value==="CATALAN" || languageL3value==="CATALAN")) {
      continueRoutine = false;
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageCatalanOralComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageCatalanOralRoutineEnd() {
  //------Ending Routine 'languageCatalanOral'-------
  for (const thisComponent of languageCatalanOralComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('languageCatalanOralKey.keys', languageCatalanOralKey.keys);
  if (typeof languageCatalanOralKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('languageCatalanOralKey.rt', languageCatalanOralKey.rt);
      routineTimer.reset();
      }
  
  languageCatalanOralKey.stop();
  // the Routine "languageCatalanOral" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageCatalanWrittenComponents;
function languageCatalanWrittenRoutineBegin() {
  //------Prepare to start Routine 'languageCatalanWritten'-------
  t = 0;
  languageCatalanWrittenClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  languageCatalanWrittenKey.keys = undefined;
  languageCatalanWrittenKey.rt = undefined;
  // keep track of which components have finished
  languageCatalanWrittenComponents = [];
  languageCatalanWrittenComponents.push(languageCatalanWrittenTextTitle);
  languageCatalanWrittenComponents.push(languageCatalanWrittenText);
  languageCatalanWrittenComponents.push(languageCatalanWrittenTextNext);
  languageCatalanWrittenComponents.push(languageCatalanWrittenKey);
  
  for (const thisComponent of languageCatalanWrittenComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function languageCatalanWrittenRoutineEachFrame() {
  //------Loop for each frame of Routine 'languageCatalanWritten'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageCatalanWrittenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageCatalanWrittenTextTitle* updates
  if (t >= 0.0 && languageCatalanWrittenTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageCatalanWrittenTextTitle.tStart = t;  // (not accounting for frame time here)
    languageCatalanWrittenTextTitle.frameNStart = frameN;  // exact frame index
    languageCatalanWrittenTextTitle.setAutoDraw(true);
  }

  
  // *languageCatalanWrittenText* updates
  if (t >= 0.0 && languageCatalanWrittenText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageCatalanWrittenText.tStart = t;  // (not accounting for frame time here)
    languageCatalanWrittenText.frameNStart = frameN;  // exact frame index
    languageCatalanWrittenText.setAutoDraw(true);
  }

  
  // *languageCatalanWrittenTextNext* updates
  if (t >= 0.0 && languageCatalanWrittenTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageCatalanWrittenTextNext.tStart = t;  // (not accounting for frame time here)
    languageCatalanWrittenTextNext.frameNStart = frameN;  // exact frame index
    languageCatalanWrittenTextNext.setAutoDraw(true);
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
    let theseKeys = languageCatalanWrittenKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      languageCatalanWrittenKey.keys = theseKeys[0].name;  // just the last key pressed
      languageCatalanWrittenKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // if Catalan is L2 or L3, skip
  if ((languageL2value==="CATALAN" || languageL3value==="CATALAN")) {
      continueRoutine = false;
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageCatalanWrittenComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageCatalanWrittenRoutineEnd() {
  //------Ending Routine 'languageCatalanWritten'-------
  for (const thisComponent of languageCatalanWrittenComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('languageCatalanWrittenKey.keys', languageCatalanWrittenKey.keys);
  if (typeof languageCatalanWrittenKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('languageCatalanWrittenKey.rt', languageCatalanWrittenKey.rt);
      routineTimer.reset();
      }
  
  languageCatalanWrittenKey.stop();
  // the Routine "languageCatalanWritten" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageCatalanTimeComponents;
function languageCatalanTimeRoutineBegin() {
  //------Prepare to start Routine 'languageCatalanTime'-------
  t = 0;
  languageCatalanTimeClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  languageCatalanTimeKey.keys = undefined;
  languageCatalanTimeKey.rt = undefined;
  // keep track of which components have finished
  languageCatalanTimeComponents = [];
  languageCatalanTimeComponents.push(languageCatalanTimeTextTitle);
  languageCatalanTimeComponents.push(languageCatalanTimeText);
  languageCatalanTimeComponents.push(languageCatalanTimeTextNext);
  languageCatalanTimeComponents.push(languageCatalanTimeKey);
  
  for (const thisComponent of languageCatalanTimeComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function languageCatalanTimeRoutineEachFrame() {
  //------Loop for each frame of Routine 'languageCatalanTime'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageCatalanTimeClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageCatalanTimeTextTitle* updates
  if (t >= 0.0 && languageCatalanTimeTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageCatalanTimeTextTitle.tStart = t;  // (not accounting for frame time here)
    languageCatalanTimeTextTitle.frameNStart = frameN;  // exact frame index
    languageCatalanTimeTextTitle.setAutoDraw(true);
  }

  
  // *languageCatalanTimeText* updates
  if (t >= 0.0 && languageCatalanTimeText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageCatalanTimeText.tStart = t;  // (not accounting for frame time here)
    languageCatalanTimeText.frameNStart = frameN;  // exact frame index
    languageCatalanTimeText.setAutoDraw(true);
  }

  
  // *languageCatalanTimeTextNext* updates
  if (t >= 0.0 && languageCatalanTimeTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageCatalanTimeTextNext.tStart = t;  // (not accounting for frame time here)
    languageCatalanTimeTextNext.frameNStart = frameN;  // exact frame index
    languageCatalanTimeTextNext.setAutoDraw(true);
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
    let theseKeys = languageCatalanTimeKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      languageCatalanTimeKey.keys = theseKeys[0].name;  // just the last key pressed
      languageCatalanTimeKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // if Catalan is L2 or L3, skip
  if ((languageL2value==="CATALAN" || languageL3value==="CATALAN")) {
      continueRoutine = false;
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageCatalanTimeComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageCatalanTimeRoutineEnd() {
  //------Ending Routine 'languageCatalanTime'-------
  for (const thisComponent of languageCatalanTimeComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('languageCatalanTimeKey.keys', languageCatalanTimeKey.keys);
  if (typeof languageCatalanTimeKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('languageCatalanTimeKey.rt', languageCatalanTimeKey.rt);
      routineTimer.reset();
      }
  
  languageCatalanTimeKey.stop();
  // the Routine "languageCatalanTime" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageSpanishOralComponents;
function languageSpanishOralRoutineBegin() {
  //------Prepare to start Routine 'languageSpanishOral'-------
  t = 0;
  languageSpanishOralClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  languageSpanishOralKey.keys = undefined;
  languageSpanishOralKey.rt = undefined;
  // keep track of which components have finished
  languageSpanishOralComponents = [];
  languageSpanishOralComponents.push(languageSpanishOralTextTitle);
  languageSpanishOralComponents.push(languageSpanishOralText);
  languageSpanishOralComponents.push(languageSpanishOralTextNext);
  languageSpanishOralComponents.push(languageSpanishOralKey);
  
  for (const thisComponent of languageSpanishOralComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function languageSpanishOralRoutineEachFrame() {
  //------Loop for each frame of Routine 'languageSpanishOral'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageSpanishOralClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageSpanishOralTextTitle* updates
  if (t >= 0.0 && languageSpanishOralTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageSpanishOralTextTitle.tStart = t;  // (not accounting for frame time here)
    languageSpanishOralTextTitle.frameNStart = frameN;  // exact frame index
    languageSpanishOralTextTitle.setAutoDraw(true);
  }

  
  // *languageSpanishOralText* updates
  if (t >= 0.0 && languageSpanishOralText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageSpanishOralText.tStart = t;  // (not accounting for frame time here)
    languageSpanishOralText.frameNStart = frameN;  // exact frame index
    languageSpanishOralText.setAutoDraw(true);
  }

  
  // *languageSpanishOralTextNext* updates
  if (t >= 0.0 && languageSpanishOralTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageSpanishOralTextNext.tStart = t;  // (not accounting for frame time here)
    languageSpanishOralTextNext.frameNStart = frameN;  // exact frame index
    languageSpanishOralTextNext.setAutoDraw(true);
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
    let theseKeys = languageSpanishOralKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      languageSpanishOralKey.keys = theseKeys[0].name;  // just the last key pressed
      languageSpanishOralKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // if Spanish is L2 or L3, skip
  if ((languageL2value==="SPANISH" || languageL3value==="SPANISH")) {
      continueRoutine = false;
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
  if (((languageL2value === "SPANISH") || (languageL3value === "SPANISH"))) {
      continueRoutine = false;
  }
  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if (_pj.in_es6("escape", keys)) {
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageSpanishOralComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageSpanishOralRoutineEnd() {
  //------Ending Routine 'languageSpanishOral'-------
  for (const thisComponent of languageSpanishOralComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('languageSpanishOralKey.keys', languageSpanishOralKey.keys);
  if (typeof languageSpanishOralKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('languageSpanishOralKey.rt', languageSpanishOralKey.rt);
      routineTimer.reset();
      }
  
  languageSpanishOralKey.stop();
  // the Routine "languageSpanishOral" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageSpanishWrittenComponents;
function languageSpanishWrittenRoutineBegin() {
  //------Prepare to start Routine 'languageSpanishWritten'-------
  t = 0;
  languageSpanishWrittenClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  languageSpanishWrittenKey.keys = undefined;
  languageSpanishWrittenKey.rt = undefined;
  // keep track of which components have finished
  languageSpanishWrittenComponents = [];
  languageSpanishWrittenComponents.push(languageSpanishWrittenTextTitle);
  languageSpanishWrittenComponents.push(languageSpanishWrittenText);
  languageSpanishWrittenComponents.push(languageSpanishWrittenTextNext);
  languageSpanishWrittenComponents.push(languageSpanishWrittenKey);
  
  for (const thisComponent of languageSpanishWrittenComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function languageSpanishWrittenRoutineEachFrame() {
  //------Loop for each frame of Routine 'languageSpanishWritten'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageSpanishWrittenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageSpanishWrittenTextTitle* updates
  if (t >= 0.0 && languageSpanishWrittenTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageSpanishWrittenTextTitle.tStart = t;  // (not accounting for frame time here)
    languageSpanishWrittenTextTitle.frameNStart = frameN;  // exact frame index
    languageSpanishWrittenTextTitle.setAutoDraw(true);
  }

  
  // *languageSpanishWrittenText* updates
  if (t >= 0.0 && languageSpanishWrittenText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageSpanishWrittenText.tStart = t;  // (not accounting for frame time here)
    languageSpanishWrittenText.frameNStart = frameN;  // exact frame index
    languageSpanishWrittenText.setAutoDraw(true);
  }

  
  // *languageSpanishWrittenTextNext* updates
  if (t >= 0.0 && languageSpanishWrittenTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageSpanishWrittenTextNext.tStart = t;  // (not accounting for frame time here)
    languageSpanishWrittenTextNext.frameNStart = frameN;  // exact frame index
    languageSpanishWrittenTextNext.setAutoDraw(true);
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
    let theseKeys = languageSpanishWrittenKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      languageSpanishWrittenKey.keys = theseKeys[0].name;  // just the last key pressed
      languageSpanishWrittenKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // if Spanish is L2 or L3, skip
  if ((languageL2value==="SPANISH" || languageL3value==="SPANISH")) {
      continueRoutine = false;
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageSpanishWrittenComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageSpanishWrittenRoutineEnd() {
  //------Ending Routine 'languageSpanishWritten'-------
  for (const thisComponent of languageSpanishWrittenComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('languageSpanishWrittenKey.keys', languageSpanishWrittenKey.keys);
  if (typeof languageSpanishWrittenKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('languageSpanishWrittenKey.rt', languageSpanishWrittenKey.rt);
      routineTimer.reset();
      }
  
  languageSpanishWrittenKey.stop();
  // the Routine "languageSpanishWritten" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var languageSpanishTimeComponents;
function languageSpanishTimeRoutineBegin() {
  //------Prepare to start Routine 'languageSpanishTime'-------
  t = 0;
  languageSpanishTimeClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  languageSpanishTimeKey.keys = undefined;
  languageSpanishTimeKey.rt = undefined;
  // keep track of which components have finished
  languageSpanishTimeComponents = [];
  languageSpanishTimeComponents.push(languageSpanishTimeTextTitle);
  languageSpanishTimeComponents.push(languageSpanishTimeText);
  languageSpanishTimeComponents.push(languageSpanishTimeTextNext);
  languageSpanishTimeComponents.push(languageSpanishTimeKey);
  
  for (const thisComponent of languageSpanishTimeComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function languageSpanishTimeRoutineEachFrame() {
  //------Loop for each frame of Routine 'languageSpanishTime'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = languageSpanishTimeClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *languageSpanishTimeTextTitle* updates
  if (t >= 0.0 && languageSpanishTimeTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageSpanishTimeTextTitle.tStart = t;  // (not accounting for frame time here)
    languageSpanishTimeTextTitle.frameNStart = frameN;  // exact frame index
    languageSpanishTimeTextTitle.setAutoDraw(true);
  }

  
  // *languageSpanishTimeText* updates
  if (t >= 0.0 && languageSpanishTimeText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageSpanishTimeText.tStart = t;  // (not accounting for frame time here)
    languageSpanishTimeText.frameNStart = frameN;  // exact frame index
    languageSpanishTimeText.setAutoDraw(true);
  }

  
  // *languageSpanishTimeTextNext* updates
  if (t >= 0.0 && languageSpanishTimeTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    languageSpanishTimeTextNext.tStart = t;  // (not accounting for frame time here)
    languageSpanishTimeTextNext.frameNStart = frameN;  // exact frame index
    languageSpanishTimeTextNext.setAutoDraw(true);
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
    let theseKeys = languageSpanishTimeKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      languageSpanishTimeKey.keys = theseKeys[0].name;  // just the last key pressed
      languageSpanishTimeKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // if Spanish is L2 or L3, skip
  if ((languageL2value==="SPANISH" || languageL3value==="SPANISH")) {
      continueRoutine = false;
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of languageSpanishTimeComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function languageSpanishTimeRoutineEnd() {
  //------Ending Routine 'languageSpanishTime'-------
  for (const thisComponent of languageSpanishTimeComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('languageSpanishTimeKey.keys', languageSpanishTimeKey.keys);
  if (typeof languageSpanishTimeKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('languageSpanishTimeKey.rt', languageSpanishTimeKey.rt);
      routineTimer.reset();
      }
  
  languageSpanishTimeKey.stop();
  // the Routine "languageSpanishTime" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var demoAgeComponents;
function demoAgeRoutineBegin() {
  //------Prepare to start Routine 'demoAge'-------
  t = 0;
  demoAgeClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  psychoJS.eventManager.clearEvents();
  inputText = "";
  isAccented = false;
  // keep track of which components have finished
  demoAgeComponents = [];
  demoAgeComponents.push(demoAgeTextTitle);
  demoAgeComponents.push(demoAgeText);
  demoAgeComponents.push(demoAgeTextNext);
  demoAgeComponents.push(demoAgeTextInput);
  
  for (const thisComponent of demoAgeComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function demoAgeRoutineEachFrame() {
  //------Loop for each frame of Routine 'demoAge'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = demoAgeClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *demoAgeTextTitle* updates
  if (t >= 0.0 && demoAgeTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoAgeTextTitle.tStart = t;  // (not accounting for frame time here)
    demoAgeTextTitle.frameNStart = frameN;  // exact frame index
    demoAgeTextTitle.setAutoDraw(true);
  }

  
  // *demoAgeText* updates
  if (t >= 0.0 && demoAgeText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoAgeText.tStart = t;  // (not accounting for frame time here)
    demoAgeText.frameNStart = frameN;  // exact frame index
    demoAgeText.setAutoDraw(true);
  }

  
  // *demoAgeTextNext* updates
  if (t >= 0.0 && demoAgeTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoAgeTextNext.tStart = t;  // (not accounting for frame time here)
    demoAgeTextNext.frameNStart = frameN;  // exact frame index
    demoAgeTextNext.setAutoDraw(true);
  }

  
  // *demoAgeTextInput* updates
  if (t >= 0.0 && demoAgeTextInput.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoAgeTextInput.tStart = t;  // (not accounting for frame time here)
    demoAgeTextInput.frameNStart = frameN;  // exact frame index
    demoAgeTextInput.setAutoDraw(true);
  }

  
  if (demoAgeTextInput.status === PsychoJS.Status.STARTED){ // only update if being drawn
    demoAgeTextInput.setText(('> ' + inputText));
  }
  keys = psychoJS.eventManager.getKeys({keyList:['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'escape', 'return', 'backspace']});
  i = 0;
  if (keys.length) {
      if ((keys[i] === "escape")) {
          psychoJS.experiment.addData("age", inputText);
          psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
      } else if ((keys[i] === "return" && inputText !== "")) {
          psychoJS.experiment.addData("age", inputText);
          continueRoutine = false;
      } else if ((keys[i] === "return" && inputText==="")) {
          inputText = "";
      } else if ((keys[i] === "backspace")) {
          inputText = inputText.slice(0, (- 1));
      } else {
          inputText += keys[i].toUpperCase();
          psychoJS.experiment.addData("age", inputText);
          i = (i + 1);
          }
      }
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of demoAgeComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function demoAgeRoutineEnd() {
  //------Ending Routine 'demoAge'-------
  for (const thisComponent of demoAgeComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "demoAge" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var demoSexComponents;
function demoSexRoutineBegin() {
  //------Prepare to start Routine 'demoSex'-------
  t = 0;
  demoSexClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  demoSexKey.keys = undefined;
  demoSexKey.rt = undefined;
  // keep track of which components have finished
  demoSexComponents = [];
  demoSexComponents.push(demoSexTextTitle);
  demoSexComponents.push(demoSexText);
  demoSexComponents.push(demoSexTextNext);
  demoSexComponents.push(demoSexKey);
  
  for (const thisComponent of demoSexComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function demoSexRoutineEachFrame() {
  //------Loop for each frame of Routine 'demoSex'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = demoSexClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *demoSexTextTitle* updates
  if (t >= 0.0 && demoSexTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoSexTextTitle.tStart = t;  // (not accounting for frame time here)
    demoSexTextTitle.frameNStart = frameN;  // exact frame index
    demoSexTextTitle.setAutoDraw(true);
  }

  
  // *demoSexText* updates
  if (t >= 0.0 && demoSexText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoSexText.tStart = t;  // (not accounting for frame time here)
    demoSexText.frameNStart = frameN;  // exact frame index
    demoSexText.setAutoDraw(true);
  }

  
  // *demoSexTextNext* updates
  if (t >= 0.0 && demoSexTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoSexTextNext.tStart = t;  // (not accounting for frame time here)
    demoSexTextNext.frameNStart = frameN;  // exact frame index
    demoSexTextNext.setAutoDraw(true);
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
    let theseKeys = demoSexKey.getKeys({keyList: ['m', 'f', 'o', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      demoSexKey.keys = theseKeys[0].name;  // just the last key pressed
      demoSexKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of demoSexComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function demoSexRoutineEnd() {
  //------Ending Routine 'demoSex'-------
  for (const thisComponent of demoSexComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('demoSexKey.keys', demoSexKey.keys);
  if (typeof demoSexKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('demoSexKey.rt', demoSexKey.rt);
      routineTimer.reset();
      }
  
  demoSexKey.stop();
  // the Routine "demoSex" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var demoEducationComponents;
function demoEducationRoutineBegin() {
  //------Prepare to start Routine 'demoEducation'-------
  t = 0;
  demoEducationClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  demoEducationKey.keys = undefined;
  demoEducationKey.rt = undefined;
  // keep track of which components have finished
  demoEducationComponents = [];
  demoEducationComponents.push(demoEducationTextTitle);
  demoEducationComponents.push(demoEducationText);
  demoEducationComponents.push(demoEducationTextNext);
  demoEducationComponents.push(demoEducationKey);
  
  for (const thisComponent of demoEducationComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function demoEducationRoutineEachFrame() {
  //------Loop for each frame of Routine 'demoEducation'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = demoEducationClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *demoEducationTextTitle* updates
  if (t >= 0.0 && demoEducationTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoEducationTextTitle.tStart = t;  // (not accounting for frame time here)
    demoEducationTextTitle.frameNStart = frameN;  // exact frame index
    demoEducationTextTitle.setAutoDraw(true);
  }

  
  // *demoEducationText* updates
  if (t >= 0.0 && demoEducationText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoEducationText.tStart = t;  // (not accounting for frame time here)
    demoEducationText.frameNStart = frameN;  // exact frame index
    demoEducationText.setAutoDraw(true);
  }

  
  // *demoEducationTextNext* updates
  if (t >= 0.0 && demoEducationTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoEducationTextNext.tStart = t;  // (not accounting for frame time here)
    demoEducationTextNext.frameNStart = frameN;  // exact frame index
    demoEducationTextNext.setAutoDraw(true);
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
    let theseKeys = demoEducationKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      demoEducationKey.keys = theseKeys[0].name;  // just the last key pressed
      demoEducationKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of demoEducationComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function demoEducationRoutineEnd() {
  //------Ending Routine 'demoEducation'-------
  for (const thisComponent of demoEducationComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('demoEducationKey.keys', demoEducationKey.keys);
  if (typeof demoEducationKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('demoEducationKey.rt', demoEducationKey.rt);
      routineTimer.reset();
      }
  
  demoEducationKey.stop();
  // the Routine "demoEducation" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var demoCityComponents;
function demoCityRoutineBegin() {
  //------Prepare to start Routine 'demoCity'-------
  t = 0;
  demoCityClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  psychoJS.eventManager.clearEvents();
  inputText = "";
  isAccented = false;
  
  // keep track of which components have finished
  demoCityComponents = [];
  demoCityComponents.push(demoCityTextTitle);
  demoCityComponents.push(demoCityText);
  demoCityComponents.push(demoCityTextNext);
  demoCityComponents.push(demoCityTextInput);
  
  for (const thisComponent of demoCityComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function demoCityRoutineEachFrame() {
  //------Loop for each frame of Routine 'demoCity'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = demoCityClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *demoCityTextTitle* updates
  if (t >= 0.0 && demoCityTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoCityTextTitle.tStart = t;  // (not accounting for frame time here)
    demoCityTextTitle.frameNStart = frameN;  // exact frame index
    demoCityTextTitle.setAutoDraw(true);
  }

  
  // *demoCityText* updates
  if (t >= 0.0 && demoCityText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoCityText.tStart = t;  // (not accounting for frame time here)
    demoCityText.frameNStart = frameN;  // exact frame index
    demoCityText.setAutoDraw(true);
  }

  
  // *demoCityTextNext* updates
  if (t >= 0.0 && demoCityTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoCityTextNext.tStart = t;  // (not accounting for frame time here)
    demoCityTextNext.frameNStart = frameN;  // exact frame index
    demoCityTextNext.setAutoDraw(true);
  }

  
  // *demoCityTextInput* updates
  if (t >= 0.0 && demoCityTextInput.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoCityTextInput.tStart = t;  // (not accounting for frame time here)
    demoCityTextInput.frameNStart = frameN;  // exact frame index
    demoCityTextInput.setAutoDraw(true);
  }

  
  if (demoCityTextInput.status === PsychoJS.Status.STARTED){ // only update if being drawn
    demoCityTextInput.setText(('> ' + inputText));
  }
  keys = psychoJS.eventManager.getKeys({"keyList": letterKeysAllowed});
  i = 0;
  if (keys.length) {
      if ((keys[i] === "escape")) {
          psychoJS.experiment.addData("city", inputText);
          psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
      } else {
          if ((keys[i] === "return")) {
              if ((inputText !== "")) {
                  psychoJS.experiment.addData("city", inputText);
                  continueRoutine = false;
              }
          } else {
              if ((keys[i] === "backspace")) {
                  inputText = inputText.slice(0, (- 1));
              } else {
                  if ((keys[i] === "apostrophe")) {
                      textInput += "'";
                      psychoJS.experiment.addData("city", inputText);
                      i = (i + 1);
                  } else {
                      inputText += keys[i].toUpperCase();
                      psychoJS.experiment.addData("city", inputText);
                      i = (i + 1);
                  }
              }
          }
      }
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of demoCityComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function demoCityRoutineEnd() {
  //------Ending Routine 'demoCity'-------
  for (const thisComponent of demoCityComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "demoCity" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var demoVisionComponents;
function demoVisionRoutineBegin() {
  //------Prepare to start Routine 'demoVision'-------
  t = 0;
  demoVisionClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  demoVisionKey.keys = undefined;
  demoVisionKey.rt = undefined;
  // keep track of which components have finished
  demoVisionComponents = [];
  demoVisionComponents.push(demoVisionTextTitle);
  demoVisionComponents.push(demoVisionText);
  demoVisionComponents.push(demoVisionTextNext);
  demoVisionComponents.push(demoVisionKey);
  
  for (const thisComponent of demoVisionComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function demoVisionRoutineEachFrame() {
  //------Loop for each frame of Routine 'demoVision'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = demoVisionClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *demoVisionTextTitle* updates
  if (t >= 0.0 && demoVisionTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoVisionTextTitle.tStart = t;  // (not accounting for frame time here)
    demoVisionTextTitle.frameNStart = frameN;  // exact frame index
    demoVisionTextTitle.setAutoDraw(true);
  }

  
  // *demoVisionText* updates
  if (t >= 0.0 && demoVisionText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoVisionText.tStart = t;  // (not accounting for frame time here)
    demoVisionText.frameNStart = frameN;  // exact frame index
    demoVisionText.setAutoDraw(true);
  }

  
  // *demoVisionTextNext* updates
  if (t >= 0.0 && demoVisionTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoVisionTextNext.tStart = t;  // (not accounting for frame time here)
    demoVisionTextNext.frameNStart = frameN;  // exact frame index
    demoVisionTextNext.setAutoDraw(true);
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
    let theseKeys = demoVisionKey.getKeys({keyList: ['y', 'n', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      demoVisionKey.keys = theseKeys[0].name;  // just the last key pressed
      demoVisionKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of demoVisionComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function demoVisionRoutineEnd() {
  //------Ending Routine 'demoVision'-------
  for (const thisComponent of demoVisionComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('demoVisionKey.keys', demoVisionKey.keys);
  if (typeof demoVisionKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('demoVisionKey.rt', demoVisionKey.rt);
      routineTimer.reset();
      }
  
  demoVisionKey.stop();
  // the Routine "demoVision" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var demoLanguageComponents;
function demoLanguageRoutineBegin() {
  //------Prepare to start Routine 'demoLanguage'-------
  t = 0;
  demoLanguageClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  demoLanguageKey.keys = undefined;
  demoLanguageKey.rt = undefined;
  // keep track of which components have finished
  demoLanguageComponents = [];
  demoLanguageComponents.push(demoLanguageTextTitle);
  demoLanguageComponents.push(demoLanguageText);
  demoLanguageComponents.push(demoLanguageTextNext);
  demoLanguageComponents.push(demoLanguageKey);
  
  for (const thisComponent of demoLanguageComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function demoLanguageRoutineEachFrame() {
  //------Loop for each frame of Routine 'demoLanguage'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = demoLanguageClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *demoLanguageTextTitle* updates
  if (t >= 0.0 && demoLanguageTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoLanguageTextTitle.tStart = t;  // (not accounting for frame time here)
    demoLanguageTextTitle.frameNStart = frameN;  // exact frame index
    demoLanguageTextTitle.setAutoDraw(true);
  }

  
  // *demoLanguageText* updates
  if (t >= 0.0 && demoLanguageText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoLanguageText.tStart = t;  // (not accounting for frame time here)
    demoLanguageText.frameNStart = frameN;  // exact frame index
    demoLanguageText.setAutoDraw(true);
  }

  
  // *demoLanguageTextNext* updates
  if (t >= 0.0 && demoLanguageTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    demoLanguageTextNext.tStart = t;  // (not accounting for frame time here)
    demoLanguageTextNext.frameNStart = frameN;  // exact frame index
    demoLanguageTextNext.setAutoDraw(true);
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
    let theseKeys = demoLanguageKey.getKeys({keyList: ['y', 'n', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      demoLanguageKey.keys = theseKeys[0].name;  // just the last key pressed
      demoLanguageKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of demoLanguageComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function demoLanguageRoutineEnd() {
  //------Ending Routine 'demoLanguage'-------
  for (const thisComponent of demoLanguageComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('demoLanguageKey.keys', demoLanguageKey.keys);
  if (typeof demoLanguageKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('demoLanguageKey.rt', demoLanguageKey.rt);
      routineTimer.reset();
      }
  
  demoLanguageKey.stop();
  // the Routine "demoLanguage" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var setupLocationComponents;
function setupLocationRoutineBegin() {
  //------Prepare to start Routine 'setupLocation'-------
  t = 0;
  setupLocationClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  setupLocationKey.keys = undefined;
  setupLocationKey.rt = undefined;
  // keep track of which components have finished
  setupLocationComponents = [];
  setupLocationComponents.push(setupLocationTextTitle);
  setupLocationComponents.push(setupLocationText);
  setupLocationComponents.push(setupLocationTextNext);
  setupLocationComponents.push(setupLocationKey);
  
  for (const thisComponent of setupLocationComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function setupLocationRoutineEachFrame() {
  //------Loop for each frame of Routine 'setupLocation'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = setupLocationClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *setupLocationTextTitle* updates
  if (t >= 0.0 && setupLocationTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    setupLocationTextTitle.tStart = t;  // (not accounting for frame time here)
    setupLocationTextTitle.frameNStart = frameN;  // exact frame index
    setupLocationTextTitle.setAutoDraw(true);
  }

  
  // *setupLocationText* updates
  if (t >= 0.0 && setupLocationText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    setupLocationText.tStart = t;  // (not accounting for frame time here)
    setupLocationText.frameNStart = frameN;  // exact frame index
    setupLocationText.setAutoDraw(true);
  }

  
  // *setupLocationTextNext* updates
  if (t >= 0.0 && setupLocationTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    setupLocationTextNext.tStart = t;  // (not accounting for frame time here)
    setupLocationTextNext.frameNStart = frameN;  // exact frame index
    setupLocationTextNext.setAutoDraw(true);
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
    let theseKeys = setupLocationKey.getKeys({keyList: ['1', '2', '3', '4', '5', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      setupLocationKey.keys = theseKeys[0].name;  // just the last key pressed
      setupLocationKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of setupLocationComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function setupLocationRoutineEnd() {
  //------Ending Routine 'setupLocation'-------
  for (const thisComponent of setupLocationComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('setupLocationKey.keys', setupLocationKey.keys);
  if (typeof setupLocationKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('setupLocationKey.rt', setupLocationKey.rt);
      routineTimer.reset();
      }
  
  setupLocationKey.stop();
  // the Routine "setupLocation" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var setupNoiseComponents;
function setupNoiseRoutineBegin() {
  //------Prepare to start Routine 'setupNoise'-------
  t = 0;
  setupNoiseClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  setupNoiseKey.keys = undefined;
  setupNoiseKey.rt = undefined;
  // keep track of which components have finished
  setupNoiseComponents = [];
  setupNoiseComponents.push(setupNoiseTextTitle);
  setupNoiseComponents.push(setupNoiseText);
  setupNoiseComponents.push(setupNoiseTextNext);
  setupNoiseComponents.push(setupNoiseKey);
  
  for (const thisComponent of setupNoiseComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function setupNoiseRoutineEachFrame() {
  //------Loop for each frame of Routine 'setupNoise'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = setupNoiseClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *setupNoiseTextTitle* updates
  if (t >= 0.0 && setupNoiseTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    setupNoiseTextTitle.tStart = t;  // (not accounting for frame time here)
    setupNoiseTextTitle.frameNStart = frameN;  // exact frame index
    setupNoiseTextTitle.setAutoDraw(true);
  }

  
  // *setupNoiseText* updates
  if (t >= 0.0 && setupNoiseText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    setupNoiseText.tStart = t;  // (not accounting for frame time here)
    setupNoiseText.frameNStart = frameN;  // exact frame index
    setupNoiseText.setAutoDraw(true);
  }

  
  // *setupNoiseTextNext* updates
  if (t >= 0.0 && setupNoiseTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    setupNoiseTextNext.tStart = t;  // (not accounting for frame time here)
    setupNoiseTextNext.frameNStart = frameN;  // exact frame index
    setupNoiseTextNext.setAutoDraw(true);
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
    let theseKeys = setupNoiseKey.getKeys({keyList: ['1', '2', '3', '4', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      setupNoiseKey.keys = theseKeys[0].name;  // just the last key pressed
      setupNoiseKey.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
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
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of setupNoiseComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function setupNoiseRoutineEnd() {
  //------Ending Routine 'setupNoise'-------
  for (const thisComponent of setupNoiseComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('setupNoiseKey.keys', setupNoiseKey.keys);
  if (typeof setupNoiseKey.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('setupNoiseKey.rt', setupNoiseKey.rt);
      routineTimer.reset();
      }
  
  setupNoiseKey.stop();
  // the Routine "setupNoise" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instructionsComponents;
function instructionsRoutineBegin() {
  //------Prepare to start Routine 'instructions'-------
  t = 0;
  instructionsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instructionsKeys.keys = undefined;
  instructionsKeys.rt = undefined;
  // keep track of which components have finished
  instructionsComponents = [];
  instructionsComponents.push(instructionsTextTitle);
  instructionsComponents.push(instructionsText);
  instructionsComponents.push(instructionsTextNext);
  instructionsComponents.push(instructionsKeys);
  
  for (const thisComponent of instructionsComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instructionsRoutineEachFrame() {
  //------Loop for each frame of Routine 'instructions'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructionsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instructionsTextTitle* updates
  if (t >= 0.0 && instructionsTextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructionsTextTitle.tStart = t;  // (not accounting for frame time here)
    instructionsTextTitle.frameNStart = frameN;  // exact frame index
    instructionsTextTitle.setAutoDraw(true);
  }

  
  // *instructionsText* updates
  if (t >= 0.0 && instructionsText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructionsText.tStart = t;  // (not accounting for frame time here)
    instructionsText.frameNStart = frameN;  // exact frame index
    instructionsText.setAutoDraw(true);
  }

  
  // *instructionsTextNext* updates
  if (t >= 0.0 && instructionsTextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructionsTextNext.tStart = t;  // (not accounting for frame time here)
    instructionsTextNext.frameNStart = frameN;  // exact frame index
    instructionsTextNext.setAutoDraw(true);
  }

  
  // *instructionsKeys* updates
  if (t >= 0.0 && instructionsKeys.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructionsKeys.tStart = t;  // (not accounting for frame time here)
    instructionsKeys.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { instructionsKeys.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { instructionsKeys.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { instructionsKeys.clearEvents(); });
  }

  if (instructionsKeys.status === PsychoJS.Status.STARTED) {
    let theseKeys = instructionsKeys.getKeys({keyList: ['space', 'escape'], waitRelease: false});
    if (theseKeys.length > 0) {  // at least one key was pressed
      instructionsKeys.keys = theseKeys[0].name;  // just the last key pressed
      instructionsKeys.rt = theseKeys[0].rt;
    }
  }
  
  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instructionsComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEnd() {
  //------Ending Routine 'instructions'-------
  for (const thisComponent of instructionsComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('instructionsKeys.keys', instructionsKeys.keys);
  if (typeof instructionsKeys.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('instructionsKeys.rt', instructionsKeys.rt);
      }
  
  instructionsKeys.stop();
  // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instructions2Components;
function instructions2RoutineBegin() {
  //------Prepare to start Routine 'instructions2'-------
  t = 0;
  instructions2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  instructions2Components = [];
  instructions2Components.push(instructions2TextTitle);
  instructions2Components.push(instructions2Text);
  instructions2Components.push(instructions2TextNext);
  
  for (const thisComponent of instructions2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instructions2RoutineEachFrame() {
  //------Loop for each frame of Routine 'instructions2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructions2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instructions2TextTitle* updates
  if (t >= 0.0 && instructions2TextTitle.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructions2TextTitle.tStart = t;  // (not accounting for frame time here)
    instructions2TextTitle.frameNStart = frameN;  // exact frame index
    instructions2TextTitle.setAutoDraw(true);
  }

  
  // *instructions2Text* updates
  if (t >= 0.0 && instructions2Text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructions2Text.tStart = t;  // (not accounting for frame time here)
    instructions2Text.frameNStart = frameN;  // exact frame index
    instructions2Text.setAutoDraw(true);
  }

  
  // *instructions2TextNext* updates
  if (t >= 0.0 && instructions2TextNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructions2TextNext.tStart = t;  // (not accounting for frame time here)
    instructions2TextNext.frameNStart = frameN;  // exact frame index
    instructions2TextNext.setAutoDraw(true);
  }

  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instructions2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

var versions;
var versionRandom;
var trialsPracticeCatalanReps;
var trialsPracticeSpanishReps;
var trialsCatalanReps;
var trialsSpanishReps;
function instructions2RoutineEnd() {
  //------Ending Routine 'instructions2'-------
  for (const thisComponent of instructions2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
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
}

var trialsPracticeCatalan;
var currentLoop;
function trialsPracticeCatalanLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trialsPracticeCatalan = new TrialHandler({
    psychoJS: psychoJS,
    nReps: trialsPracticeCatalanReps, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Trials/01_trials_practice_catalan.xlsx',
    seed: undefined, name: 'trialsPracticeCatalan'});
  psychoJS.experiment.addLoop(trialsPracticeCatalan); // add the loop to the experiment
  currentLoop = trialsPracticeCatalan;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrialsPracticeCatalan of trialsPracticeCatalan) {
    thisScheduler.add(importConditions(trialsPracticeCatalan));
    thisScheduler.add(fixationRoutineBegin);
    thisScheduler.add(fixationRoutineEachFrame);
    thisScheduler.add(fixationRoutineEnd);
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsPracticeCatalanLoopEnd() {
  psychoJS.experiment.removeLoop(trialsPracticeCatalan);

  return Scheduler.Event.NEXT;
}

var trialsPracticeSpanish;
function trialsPracticeSpanishLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trialsPracticeSpanish = new TrialHandler({
    psychoJS: psychoJS,
    nReps: trialsPracticeSpanishReps, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Trials/01_trials_practice_spanish.xlsx',
    seed: undefined, name: 'trialsPracticeSpanish'});
  psychoJS.experiment.addLoop(trialsPracticeSpanish); // add the loop to the experiment
  currentLoop = trialsPracticeSpanish;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrialsPracticeSpanish of trialsPracticeSpanish) {
    thisScheduler.add(importConditions(trialsPracticeSpanish));
    thisScheduler.add(fixationRoutineBegin);
    thisScheduler.add(fixationRoutineEachFrame);
    thisScheduler.add(fixationRoutineEnd);
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsPracticeSpanishLoopEnd() {
  psychoJS.experiment.removeLoop(trialsPracticeSpanish);

  return Scheduler.Event.NEXT;
}

var trialsCatalan;
function trialsCatalanLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trialsCatalan = new TrialHandler({
    psychoJS: psychoJS,
    nReps: trialsCatalanReps, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Trials/02_trials_catalan.xlsx',
    seed: undefined, name: 'trialsCatalan'});
  psychoJS.experiment.addLoop(trialsCatalan); // add the loop to the experiment
  currentLoop = trialsCatalan;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrialsCatalan of trialsCatalan) {
    thisScheduler.add(importConditions(trialsCatalan));
    thisScheduler.add(fixationRoutineBegin);
    thisScheduler.add(fixationRoutineEachFrame);
    thisScheduler.add(fixationRoutineEnd);
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsCatalanLoopEnd() {
  psychoJS.experiment.removeLoop(trialsCatalan);

  return Scheduler.Event.NEXT;
}

var trialsSpanish;
function trialsSpanishLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trialsSpanish = new TrialHandler({
    psychoJS: psychoJS,
    nReps: trialsSpanishReps, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Trials/02_trials_spanish.xlsx',
    seed: undefined, name: 'trialsSpanish'});
  psychoJS.experiment.addLoop(trialsSpanish); // add the loop to the experiment
  currentLoop = trialsSpanish;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrialsSpanish of trialsSpanish) {
    thisScheduler.add(importConditions(trialsSpanish));
    thisScheduler.add(fixationRoutineBegin);
    thisScheduler.add(fixationRoutineEachFrame);
    thisScheduler.add(fixationRoutineEnd);
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsSpanishLoopEnd() {
  psychoJS.experiment.removeLoop(trialsSpanish);

  return Scheduler.Event.NEXT;
}

var fixationComponents;
function fixationRoutineBegin() {
  //------Prepare to start Routine 'fixation'-------
  t = 0;
  fixationClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  fixationComponents = [];
  fixationComponents.push(fixationText);
  
  for (const thisComponent of fixationComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function fixationRoutineEachFrame() {
  //------Loop for each frame of Routine 'fixation'-------
  let continueRoutine = true; // until we're told otherwise
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
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of fixationComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function fixationRoutineEnd() {
  //------Ending Routine 'fixation'-------
  for (const thisComponent of fixationComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var keysAllowed;
var debugText;
var error;
var keyPressTime;
var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  trialSound = new Sound({
    win: psychoJS.window,
    value: soundfile,
    secs: -1,
    });
  trialSound.setVolume(1);
  keysAllowed = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "apostrophe", "z", "x", "c", "v", "b", "n", "m", "escape", "space", "return", "backspace"];
  inputText = "";
  debugText = "";
  isAccented = false;
  error = false;
  keyPressTime = 0;
  trialText.setText("");
  
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(trialText);
  trialComponents.push(trialSound);
  
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
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
    trialText.setText(('> ' + inputText));
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
                  psychoJS.quit("You have pressed ESC. The study has finished. Thank you for you participation. Press RETURN to finish.");
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
          psychoJS.experiment.nextEntry();
          i = (i + 1);
      }
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  for (const thisComponent of trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  trialSound.stop();  // ensure sound has stopped at end of routine
  // the Routine "trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var beginComponents;
function beginRoutineBegin() {
  //------Prepare to start Routine 'begin'-------
  t = 0;
  beginClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  beginComponents = [];
  beginComponents.push(beginText);
  beginComponents.push(beginNext);
  
  for (const thisComponent of beginComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function beginRoutineEachFrame() {
  //------Loop for each frame of Routine 'begin'-------
  let continueRoutine = true; // until we're told otherwise
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

  
  // *beginNext* updates
  if (t >= 0.0 && beginNext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    beginNext.tStart = t;  // (not accounting for frame time here)
    beginNext.frameNStart = frameN;  // exact frame index
    beginNext.setAutoDraw(true);
  }

  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of beginComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function beginRoutineEnd() {
  //------Ending Routine 'begin'-------
  for (const thisComponent of beginComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "begin" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var farewellComponents;
function farewellRoutineBegin() {
  //------Prepare to start Routine 'farewell'-------
  t = 0;
  farewellClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  farewellComponents = [];
  farewellComponents.push(farewellText);
  
  for (const thisComponent of farewellComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function farewellRoutineEachFrame() {
  //------Loop for each frame of Routine 'farewell'-------
  let continueRoutine = true; // until we're told otherwise
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

  keys = psychoJS.eventManager.getKeys({"keyList": ["escape", "space", "return"]});
  n = keys.length;
  if ((keys.includes("escape"))) {
      psychoJS.quit("You have pressed ESC. The study has finished. Thank you for your participation! Press RETURN to exit.");
  } else if ((keys.includes("space", keys))) {
      continueRoutine = false;
    }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of farewellComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function farewellRoutineEnd() {
  //------Ending Routine 'farewell'-------
  for (const thisComponent of farewellComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "farewell" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
