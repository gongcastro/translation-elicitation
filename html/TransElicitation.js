/************************* 
 * Transelicitation Test *
 *************************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'TransElicitation';  // from the Builder filename that created this script
let expInfo = {'Code': '', 'Birth place (city, country)': '', 'Current residence (city, country)': '', 'If current residence is not where you were born: How long have you been living in the current place? (in months)': '', "Father's birth place (city, country)": '', 'In what language do you speak to you father?': '', 'In what language does you father speak to you?': '', "Mothers's birth place (city, country)": '', 'In what language do you speak to you mother?': '', 'Do you have any visual, hearing, or movement problems?': ['Yes', 'No'], 'What other languages can you use?': '', 'At what age did you start learning these languages? Please, use the same order as in previous question)': '0', 'What is your level of oral comprehension in English?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)'], 'What is your level of oral comprehension in Spanish?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)'], 'What is your level of oral comprehension in Catalan?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)'], 'What is your level of oral comprehension in your other language 1 (if any)?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)'], 'What is your level of oral comprehension in your other language 2 (if any)?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)'], 'What is your level of oral comprehension in your other language 3 (if any)?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)']};

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
flowScheduler.add(block_welcomeRoutineBegin());
flowScheduler.add(block_welcomeRoutineEachFrame());
flowScheduler.add(block_welcomeRoutineEnd());
flowScheduler.add(block_instructionsRoutineBegin());
flowScheduler.add(block_instructionsRoutineEachFrame());
flowScheduler.add(block_instructionsRoutineEnd());
const loop_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop_trialsLoopBegin, loop_trialsLoopScheduler);
flowScheduler.add(loop_trialsLoopScheduler);
flowScheduler.add(loop_trialsLoopEnd);
flowScheduler.add(block_farewellRoutineBegin());
flowScheduler.add(block_farewellRoutineEachFrame());
flowScheduler.add(block_farewellRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.1';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var block_welcomeClock;
var text_welcome;
var welcome_text;
var welcome_next;
var welcome_key;
var block_instructionsClock;
var instructions_title;
var instructions_text;
var instructions_next;
var instructions_key;
var block_trialClock;
var trial_fixation;
var trial_sound;
var trial_response_display;
var block_farewellClock;
var farewell_text;
var farewell_key;
var farewell_next;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "block_welcome"
  block_welcomeClock = new util.Clock();
  text_welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_welcome',
    text: 'Welcome!',
    font: 'Arial',
    units: undefined, 
    pos: [0.0, 0.1], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  welcome_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_text',
    text: 'Please, use headphones',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.1)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  welcome_next = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_next',
    text: "Press 'return' key >>",
    font: 'Arial',
    units: undefined, 
    pos: [0.5, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  welcome_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "block_instructions"
  block_instructionsClock = new util.Clock();
  instructions_title = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_title',
    text: 'Instructions',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: 'In each trial, you will first see a cross.\n\nThen, you will listen a word in Catalan.\n\nType its translation in English.\n\nBe fast, be accurate.\n\nYou have 5 seconds to answer.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  instructions_next = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_next',
    text: "Press 'return' to start! >>",
    font: 'Arial',
    units: undefined, 
    pos: [0.5, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  instructions_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "block_trial"
  block_trialClock = new util.Clock();
  trial_fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  trial_sound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  trial_sound.setVolume(1);
  trial_response_display = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_response_display',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "block_farewell"
  block_farewellClock = new util.Clock();
  farewell_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'farewell_text',
    text: 'Thank you!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  farewell_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  farewell_next = new visual.TextStim({
    win: psychoJS.window,
    name: 'farewell_next',
    text: "Press 'return' key >>",
    font: 'Arial',
    units: undefined, 
    pos: [0.5, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _welcome_key_allKeys;
var block_welcomeComponents;
function block_welcomeRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'block_welcome'-------
    t = 0;
    block_welcomeClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    welcome_key.keys = undefined;
    welcome_key.rt = undefined;
    _welcome_key_allKeys = [];
    // keep track of which components have finished
    block_welcomeComponents = [];
    block_welcomeComponents.push(text_welcome);
    block_welcomeComponents.push(welcome_text);
    block_welcomeComponents.push(welcome_next);
    block_welcomeComponents.push(welcome_key);
    
    for (const thisComponent of block_welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function block_welcomeRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'block_welcome'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = block_welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_welcome* updates
    if (t >= 0.0 && text_welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_welcome.tStart = t;  // (not accounting for frame time here)
      text_welcome.frameNStart = frameN;  // exact frame index
      
      text_welcome.setAutoDraw(true);
    }

    
    // *welcome_text* updates
    if (t >= 0.0 && welcome_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_text.tStart = t;  // (not accounting for frame time here)
      welcome_text.frameNStart = frameN;  // exact frame index
      
      welcome_text.setAutoDraw(true);
    }

    
    // *welcome_next* updates
    if (t >= 0.0 && welcome_next.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_next.tStart = t;  // (not accounting for frame time here)
      welcome_next.frameNStart = frameN;  // exact frame index
      
      welcome_next.setAutoDraw(true);
    }

    
    // *welcome_key* updates
    if (t >= 0.0 && welcome_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_key.tStart = t;  // (not accounting for frame time here)
      welcome_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_key.start(); }); // start on screen flip
    }

    if (welcome_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_key.getKeys({keyList: ['return'], waitRelease: false});
      _welcome_key_allKeys = _welcome_key_allKeys.concat(theseKeys);
      if (_welcome_key_allKeys.length > 0) {
        welcome_key.keys = _welcome_key_allKeys[_welcome_key_allKeys.length - 1].name;  // just the last key pressed
        welcome_key.rt = _welcome_key_allKeys[_welcome_key_allKeys.length - 1].rt;
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
    for (const thisComponent of block_welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function block_welcomeRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'block_welcome'-------
    for (const thisComponent of block_welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "block_welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _instructions_key_allKeys;
var block_instructionsComponents;
function block_instructionsRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'block_instructions'-------
    t = 0;
    block_instructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_key.keys = undefined;
    instructions_key.rt = undefined;
    _instructions_key_allKeys = [];
    // keep track of which components have finished
    block_instructionsComponents = [];
    block_instructionsComponents.push(instructions_title);
    block_instructionsComponents.push(instructions_text);
    block_instructionsComponents.push(instructions_next);
    block_instructionsComponents.push(instructions_key);
    
    for (const thisComponent of block_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function block_instructionsRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'block_instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = block_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_title* updates
    if (t >= 0.0 && instructions_title.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_title.tStart = t;  // (not accounting for frame time here)
      instructions_title.frameNStart = frameN;  // exact frame index
      
      instructions_title.setAutoDraw(true);
    }

    
    // *instructions_text* updates
    if (t >= 0.0 && instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_text.tStart = t;  // (not accounting for frame time here)
      instructions_text.frameNStart = frameN;  // exact frame index
      
      instructions_text.setAutoDraw(true);
    }

    
    // *instructions_next* updates
    if (t >= 0.0 && instructions_next.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_next.tStart = t;  // (not accounting for frame time here)
      instructions_next.frameNStart = frameN;  // exact frame index
      
      instructions_next.setAutoDraw(true);
    }

    
    // *instructions_key* updates
    if (t >= 0.0 && instructions_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_key.tStart = t;  // (not accounting for frame time here)
      instructions_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructions_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructions_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructions_key.clearEvents(); });
    }

    if (instructions_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructions_key.getKeys({keyList: ['return'], waitRelease: false});
      _instructions_key_allKeys = _instructions_key_allKeys.concat(theseKeys);
      if (_instructions_key_allKeys.length > 0) {
        instructions_key.keys = _instructions_key_allKeys[_instructions_key_allKeys.length - 1].name;  // just the last key pressed
        instructions_key.rt = _instructions_key_allKeys[_instructions_key_allKeys.length - 1].rt;
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
    for (const thisComponent of block_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function block_instructionsRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'block_instructions'-------
    for (const thisComponent of block_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "block_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var loop_trials;
var currentLoop;
function loop_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  loop_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Stimuli/trials.xlsx',
    seed: undefined, name: 'loop_trials'
  });
  psychoJS.experiment.addLoop(loop_trials); // add the loop to the experiment
  currentLoop = loop_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLoop_trial of loop_trials) {
    const snapshot = loop_trials.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(block_trialRoutineBegin(snapshot));
    thisScheduler.add(block_trialRoutineEachFrame(snapshot));
    thisScheduler.add(block_trialRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function loop_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(loop_trials);

  return Scheduler.Event.NEXT;
}


var block_trialComponents;
function block_trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'block_trial'-------
    t = 0;
    block_trialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    trial_sound = new sound.Sound({
    win: psychoJS.window,
    value: FileName,
    secs: -1,
    });
    trial_sound.setVolume(1);
    trial_response_display.setText('');
    // keep track of which components have finished
    block_trialComponents = [];
    block_trialComponents.push(trial_fixation);
    block_trialComponents.push(trial_sound);
    block_trialComponents.push(trial_response_display);
    
    for (const thisComponent of block_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function block_trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'block_trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = block_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trial_fixation* updates
    if (t >= 0.0 && trial_fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_fixation.tStart = t;  // (not accounting for frame time here)
      trial_fixation.frameNStart = frameN;  // exact frame index
      
      trial_fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_fixation.setAutoDraw(false);
    }
    // start/stop trial_sound
    if (t >= 1.0 && trial_sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_sound.tStart = t;  // (not accounting for frame time here)
      trial_sound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ trial_sound.play(); });  // screen flip
      trial_sound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (trial_sound.getDuration() + trial_sound.tStart)     && trial_sound.status === PsychoJS.Status.STARTED) {
      trial_sound.stop();  // stop the sound (if longer than duration)
      trial_sound.status = PsychoJS.Status.FINISHED;
    }
    
    // *trial_response_display* updates
    if (t >= 1.0 && trial_response_display.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_response_display.tStart = t;  // (not accounting for frame time here)
      trial_response_display.frameNStart = frameN;  // exact frame index
      
      trial_response_display.setAutoDraw(true);
    }

    frameRemains = 1.0 + 5.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_response_display.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_response_display.setAutoDraw(false);
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
    for (const thisComponent of block_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function block_trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'block_trial'-------
    for (const thisComponent of block_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    trial_sound.stop();  // ensure sound has stopped at end of routine
    // the Routine "block_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _farewell_key_allKeys;
var block_farewellComponents;
function block_farewellRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'block_farewell'-------
    t = 0;
    block_farewellClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    farewell_key.keys = undefined;
    farewell_key.rt = undefined;
    _farewell_key_allKeys = [];
    // keep track of which components have finished
    block_farewellComponents = [];
    block_farewellComponents.push(farewell_text);
    block_farewellComponents.push(farewell_key);
    block_farewellComponents.push(farewell_next);
    
    for (const thisComponent of block_farewellComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function block_farewellRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'block_farewell'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = block_farewellClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *farewell_text* updates
    if (t >= 0.0 && farewell_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      farewell_text.tStart = t;  // (not accounting for frame time here)
      farewell_text.frameNStart = frameN;  // exact frame index
      
      farewell_text.setAutoDraw(true);
    }

    
    // *farewell_key* updates
    if (t >= 0.0 && farewell_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      farewell_key.tStart = t;  // (not accounting for frame time here)
      farewell_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { farewell_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { farewell_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { farewell_key.clearEvents(); });
    }

    if (farewell_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = farewell_key.getKeys({keyList: ['space'], waitRelease: false});
      _farewell_key_allKeys = _farewell_key_allKeys.concat(theseKeys);
      if (_farewell_key_allKeys.length > 0) {
        farewell_key.keys = _farewell_key_allKeys[_farewell_key_allKeys.length - 1].name;  // just the last key pressed
        farewell_key.rt = _farewell_key_allKeys[_farewell_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *farewell_next* updates
    if (t >= 0.0 && farewell_next.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      farewell_next.tStart = t;  // (not accounting for frame time here)
      farewell_next.frameNStart = frameN;  // exact frame index
      
      farewell_next.setAutoDraw(true);
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
    for (const thisComponent of block_farewellComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function block_farewellRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'block_farewell'-------
    for (const thisComponent of block_farewellComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "block_farewell" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
