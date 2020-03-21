#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.1),
    on Sat Mar 21 12:32:03 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020.1')


from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'sounddevice'
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.1'
expName = 'TransElicitation'  # from the Builder filename that created this script
expInfo = {'Code': '', 'Birth place (city, country)': '', 'Current residence (city, country)': '', 'If current residence is not where you were born: How long have you been living in the current place? (in months)': '', "Father's birth place (city, country)": '', 'In what language do you speak to you father?': '', 'In what language does you father speak to you?': '', "Mothers's birth place (city, country)": '', 'In what language do you speak to you mother?': '', 'Do you have any visual, hearing, or movement problems?': ['Yes', 'No'], 'What other languages can you use?': '', 'At what age did you start learning these languages? Please, use the same order as in previous question)': '0', 'What is your level of oral comprehension in English?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)'], 'What is your level of oral comprehension in Spanish?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)'], 'What is your level of oral comprehension in Catalan?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)'], 'What is your level of oral comprehension in your other language 1 (if any)?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)'], 'What is your level of oral comprehension in your other language 2 (if any)?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)'], 'What is your level of oral comprehension in your other language 3 (if any)?': ['1 (very little)', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10 (native proficiency)']}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'Data/%s_%s_%s' % (expName, data.getDateStr(format="%Y-%m-%d-%H%M"), expInfo['Code'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/GonzaloGGC/projects/TransElicitation/TransElicitation_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "block_welcome"
block_welcomeClock = core.Clock()
text_welcome = visual.TextStim(win=win, name='text_welcome',
    text='Welcome!',
    font='Arial',
    pos=(0.0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Please, use headphones',
    font='Arial',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
welcome_next = visual.TextStim(win=win, name='welcome_next',
    text="Press 'return' key >>",
    font='Arial',
    pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
welcome_key = keyboard.Keyboard()
expInfo['date'] = data.getDateStr(format="%Y-%m-%d-%H%M")
expInfo['experiment'] = 'TransElicitation'

globalClock = core.Clock()

print('Log')

# Initialize components for Routine "block_instructions"
block_instructionsClock = core.Clock()
instructions_title = visual.TextStim(win=win, name='instructions_title',
    text='Instructions',
    font='Arial',
    pos=(0, 0.4), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='In each trial, you will first see a cross.\n\nThen, you will listen a word in Catalan.\n\nType its translation in English.\n\nBe fast, be accurate.\n\nYou have 5 seconds to answer.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructions_next = visual.TextStim(win=win, name='instructions_next',
    text="Press 'return' to start! >>",
    font='Arial',
    pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instructions_key = keyboard.Keyboard()

# Initialize components for Routine "block_trial"
block_trialClock = core.Clock()
trial_fixation = visual.TextStim(win=win, name='trial_fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.20, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='trial_sound')
trial_sound.setVolume(1)
trial_response_display = visual.TextStim(win=win, name='trial_response_display',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
import string
allLetters = list(string.ascii_lowercase)

from psychopy import core
globalClock = core.Clock()

# Initialize components for Routine "block_farewell"
block_farewellClock = core.Clock()
farewell_text = visual.TextStim(win=win, name='farewell_text',
    text='Thank you!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
farewell_key = keyboard.Keyboard()
farewell_next = visual.TextStim(win=win, name='farewell_next',
    text="Press 'return' key >>",
    font='Arial',
    pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "block_welcome"-------
continueRoutine = True
# update component parameters for each repeat
welcome_key.keys = []
welcome_key.rt = []
_welcome_key_allKeys = []
# keep track of which components have finished
block_welcomeComponents = [text_welcome, welcome_text, welcome_next, welcome_key]
for thisComponent in block_welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
block_welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "block_welcome"-------
while continueRoutine:
    # get current time
    t = block_welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=block_welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome* updates
    if text_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome.frameNStart = frameN  # exact frame index
        text_welcome.tStart = t  # local t and not account for scr refresh
        text_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome, 'tStartRefresh')  # time at next scr refresh
        text_welcome.setAutoDraw(True)
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
    # *welcome_next* updates
    if welcome_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_next.frameNStart = frameN  # exact frame index
        welcome_next.tStart = t  # local t and not account for scr refresh
        welcome_next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_next, 'tStartRefresh')  # time at next scr refresh
        welcome_next.setAutoDraw(True)
    
    # *welcome_key* updates
    waitOnFlip = False
    if welcome_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_key.frameNStart = frameN  # exact frame index
        welcome_key.tStart = t  # local t and not account for scr refresh
        welcome_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_key, 'tStartRefresh')  # time at next scr refresh
        welcome_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_key.clock.reset)  # t=0 on next screen flip
    if welcome_key.status == STARTED and not waitOnFlip:
        theseKeys = welcome_key.getKeys(keyList=['return'], waitRelease=False)
        _welcome_key_allKeys.extend(theseKeys)
        if len(_welcome_key_allKeys):
            welcome_key.keys = _welcome_key_allKeys[-1].name  # just the last key pressed
            welcome_key.rt = _welcome_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block_welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "block_welcome"-------
for thisComponent in block_welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "block_welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "block_instructions"-------
continueRoutine = True
# update component parameters for each repeat
instructions_key.keys = []
instructions_key.rt = []
_instructions_key_allKeys = []
# keep track of which components have finished
block_instructionsComponents = [instructions_title, instructions_text, instructions_next, instructions_key]
for thisComponent in block_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
block_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "block_instructions"-------
while continueRoutine:
    # get current time
    t = block_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=block_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_title* updates
    if instructions_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_title.frameNStart = frameN  # exact frame index
        instructions_title.tStart = t  # local t and not account for scr refresh
        instructions_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_title, 'tStartRefresh')  # time at next scr refresh
        instructions_title.setAutoDraw(True)
    
    # *instructions_text* updates
    if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.tStart = t  # local t and not account for scr refresh
        instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
        instructions_text.setAutoDraw(True)
    
    # *instructions_next* updates
    if instructions_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_next.frameNStart = frameN  # exact frame index
        instructions_next.tStart = t  # local t and not account for scr refresh
        instructions_next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_next, 'tStartRefresh')  # time at next scr refresh
        instructions_next.setAutoDraw(True)
    
    # *instructions_key* updates
    waitOnFlip = False
    if instructions_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_key.frameNStart = frameN  # exact frame index
        instructions_key.tStart = t  # local t and not account for scr refresh
        instructions_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_key, 'tStartRefresh')  # time at next scr refresh
        instructions_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions_key.status == STARTED and not waitOnFlip:
        theseKeys = instructions_key.getKeys(keyList=['return'], waitRelease=False)
        _instructions_key_allKeys.extend(theseKeys)
        if len(_instructions_key_allKeys):
            instructions_key.keys = _instructions_key_allKeys[-1].name  # just the last key pressed
            instructions_key.rt = _instructions_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "block_instructions"-------
for thisComponent in block_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "block_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli/trials.xlsx'),
    seed=None, name='loop_trials')
thisExp.addLoop(loop_trials)  # add the loop to the experiment
thisLoop_trial = loop_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
if thisLoop_trial != None:
    for paramName in thisLoop_trial:
        exec('{} = thisLoop_trial[paramName]'.format(paramName))

for thisLoop_trial in loop_trials:
    currentLoop = loop_trials
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
    if thisLoop_trial != None:
        for paramName in thisLoop_trial:
            exec('{} = thisLoop_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    trial_sound.setSound(FileName, hamming=True)
    trial_sound.setVolume(1, log=False)
    trial_response_display.setText('')
    textFill = ''
    response = False
    trialClock = core.Clock()
    # keep track of which components have finished
    block_trialComponents = [trial_fixation, trial_sound, trial_response_display]
    for thisComponent in block_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block_trial"-------
    while continueRoutine:
        # get current time
        t = block_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_fixation* updates
        if trial_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_fixation.frameNStart = frameN  # exact frame index
            trial_fixation.tStart = t  # local t and not account for scr refresh
            trial_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation, 'tStartRefresh')  # time at next scr refresh
            trial_fixation.setAutoDraw(True)
        if trial_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                trial_fixation.tStop = t  # not accounting for scr refresh
                trial_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_fixation, 'tStopRefresh')  # time at next scr refresh
                trial_fixation.setAutoDraw(False)
        # start/stop trial_sound
        if trial_sound.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial_sound.frameNStart = frameN  # exact frame index
            trial_sound.tStart = t  # local t and not account for scr refresh
            trial_sound.tStartRefresh = tThisFlipGlobal  # on global time
            trial_sound.play(when=win)  # sync with win flip
        
        # *trial_response_display* updates
        if trial_response_display.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            trial_response_display.frameNStart = frameN  # exact frame index
            trial_response_display.tStart = t  # local t and not account for scr refresh
            trial_response_display.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_response_display, 'tStartRefresh')  # time at next scr refresh
            trial_response_display.setAutoDraw(True)
        if trial_response_display.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_response_display.tStartRefresh + 5.5-frameTolerance:
                # keep track of stop time/frame for later
                trial_response_display.tStop = t  # not accounting for scr refresh
                trial_response_display.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_response_display, 'tStopRefresh')  # time at next scr refresh
                trial_response_display.setAutoDraw(False)
        keys = event.getKeys()
        if 'escape' in keys:
            core.quit()  # So you can quit
        else:
            if keys and not response and trialClock.getTime() > 1.0:
                firstKeyRT = trialClock.getTime()
                if keys[0] == 'space':
                    textFill += ' '  # Adds a space instead of 'space'
                elif keys[0] in allLetters:
                    textFill+=keys[0]  # Adds character to text if in alphabet.
                trial_response_display.setText(textFill)  # Set new text on screen
            elif keys and response and trialClock.getTime() > 1.0:
                if keys[0] == 'space':
                    textFill += ' '  # Adds a space instead of 'space'
                elif keys[0] in allLetters:
                    textFill+=keys[0]  # Adds character to text if in alphabet.
                    trial_response_display.setText(textFill)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_trial"-------
    for thisComponent in block_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_trials.addData('trial_fixation.started', trial_fixation.tStartRefresh)
    loop_trials.addData('trial_fixation.stopped', trial_fixation.tStopRefresh)
    trial_sound.stop()  # ensure sound has stopped at end of routine
    loop_trials.addData('trial_sound.started', trial_sound.tStartRefresh)
    loop_trials.addData('trial_sound.stopped', trial_sound.tStopRefresh)
    loop_trials.addData('trial_response_display.started', trial_response_display.tStartRefresh)
    loop_trials.addData('trial_response_display.stopped', trial_response_display.tStopRefresh)
    thisExp.addData('keyPresses', textFill)
    thisExp.addData('firstKeyRT', firstKeyRT)
    
    textFill = ''
    # the Routine "block_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_trials'


# ------Prepare to start Routine "block_farewell"-------
continueRoutine = True
# update component parameters for each repeat
farewell_key.keys = []
farewell_key.rt = []
_farewell_key_allKeys = []
# keep track of which components have finished
block_farewellComponents = [farewell_text, farewell_key, farewell_next]
for thisComponent in block_farewellComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
block_farewellClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "block_farewell"-------
while continueRoutine:
    # get current time
    t = block_farewellClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=block_farewellClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *farewell_text* updates
    if farewell_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        farewell_text.frameNStart = frameN  # exact frame index
        farewell_text.tStart = t  # local t and not account for scr refresh
        farewell_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(farewell_text, 'tStartRefresh')  # time at next scr refresh
        farewell_text.setAutoDraw(True)
    
    # *farewell_key* updates
    waitOnFlip = False
    if farewell_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        farewell_key.frameNStart = frameN  # exact frame index
        farewell_key.tStart = t  # local t and not account for scr refresh
        farewell_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(farewell_key, 'tStartRefresh')  # time at next scr refresh
        farewell_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(farewell_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(farewell_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if farewell_key.status == STARTED and not waitOnFlip:
        theseKeys = farewell_key.getKeys(keyList=['space'], waitRelease=False)
        _farewell_key_allKeys.extend(theseKeys)
        if len(_farewell_key_allKeys):
            farewell_key.keys = _farewell_key_allKeys[-1].name  # just the last key pressed
            farewell_key.rt = _farewell_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *farewell_next* updates
    if farewell_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        farewell_next.frameNStart = frameN  # exact frame index
        farewell_next.tStart = t  # local t and not account for scr refresh
        farewell_next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(farewell_next, 'tStartRefresh')  # time at next scr refresh
        farewell_next.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block_farewellComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "block_farewell"-------
for thisComponent in block_farewellComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "block_farewell" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
