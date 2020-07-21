#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Fri May  8 15:26:29 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020.1.2')


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
psychopyVersion = '2020.1.2'
expName = 'TranslationElicitationSpaTest'  # from the Builder filename that created this script
expInfo = {'ProlificID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'Data/%s_%s_%s' % (expName, expInfo['date'], expInfo['participant'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/GonzaloGGC/Desktop/TranslationElicitationEngTest/TranslationElicitationEngTest_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.ERROR)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1200, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()
setupTextTitle = visual.TextStim(win=win, name='setupTextTitle',
    text='SET UP',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
setupText = visual.TextStim(win=win, name='setupText',
    text='If possible, use Chrome or Mozilla Firefox\n\nUse a computer or a laptop (not a tablet or a phone)\n\nUse headphones \n\nClose all tabs other than this one\n\nDo not switch tabs in the browser\n\nIf, for any reason, you restart the study (e.g. because you reloaded the website or an internet failure), let us know by sending an email to serene.siow@psy.ox.ac.uk.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
setupTextNext = visual.TextStim(win=win, name='setupTextNext',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
# generate participant ID
import random
participant = str(random.randint(10000, 100000))
expInfo['participant'] = participant
thisExp.addData('participant', participant)

letterKeysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'return', 'backspace', 'escape', 'space']

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcomeTextTitle = visual.TextStim(win=win, name='welcomeTextTitle',
    text='WELCOME',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcomeText = visual.TextStim(win=win, name='welcomeText',
    text='This is a study designed by researchers from the Universitat Pompeu Fabra (Barcelona, Spain) and the University of Oxford (Oxford, UK). The aim of the study is to investigate how toddlers and adults process foreign words. The audios you will listen to throughout this study were recorded in a baby-directed style.\n\nYou have been invited to participate as you are between 18 and 22 years old, and a English native speaker with no knowledge of Spanish or Catalan.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
welcomeTextNext = visual.TextStim(win=win, name='welcomeTextNext',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "description"
descriptionClock = core.Clock()
descriptionTextTitle = visual.TextStim(win=win, name='descriptionTextTitle',
    text='OVERVIEW',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
descriptionText = visual.TextStim(win=win, name='descriptionText',
    text='Firstly, you will be asked to complete a BRIEF QUESTIONNAIRE (your language profile, level of education, etc.).\n\nIn the main STUDY, you will listen to a series of SPANISH or CATALAN words. Your task will be to GUESS the TRANSLATION of each word in ENGLISH and TYPE your answer using the computer keyboard.\n\nThis should take around 30 minutes.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
descriptionTextNext = visual.TextStim(win=win, name='descriptionTextNext',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "voluntary"
voluntaryClock = core.Clock()
voluntaryTextTitle = visual.TextStim(win=win, name='voluntaryTextTitle',
    text='DO I HAVE TO TAKE PART?',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
voluntaryText = visual.TextStim(win=win, name='voluntaryText',
    text='Participation in this study is absolutely VOLUNTARY. If you do decide to take part, you may withdraw at any point for any reason by pressing the ESC button. However, we are only able to reimburse participants who complete the full task.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
voluntaryTextNext = visual.TextStim(win=win, name='voluntaryTextNext',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "contact"
contactClock = core.Clock()
contactTextTitle = visual.TextStim(win=win, name='contactTextTitle',
    text='CONTACT DETAILS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
contactText = visual.TextStim(win=win, name='contactText',
    text='If you have any questions about this study, please contact the researchers.\nEmail: serene.siow@psy.ox.ac.uk\n \nPrincipal Investigators: Núria Sebastian-Galles and Kim Plunkett\nResearchers: Gonzalo García-Castro and Serene Siow\n \nCenter for Brain and Cognition, Universitat Pompeu Fabra\nDepartment of Experimental Psychology, University of Oxford',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
contactTextNext = visual.TextStim(win=win, name='contactTextNext',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "confidentiality"
confidentialityClock = core.Clock()
confidentialityTextTitle = visual.TextStim(win=win, name='confidentialityTextTitle',
    text='HOW WILL MY DATA BE USED?',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
confidentialityText = visual.TextStim(win=win, name='confidentialityText',
    text='Your answers will be completely ANONYMOUS, and we will take all reasonable measures to ensure that they remain confidential.\n \nYour DATA WILL BE STORED in a password-protected file and MAY BE USED in academic publications IN AN ANONYMISED FORM. Your IP address will NOT BE STORED. Research data will be stored for a minimum of three years after publication or public release.\n \nWe would also like your permission to use your anonymised data in future studies, and to SHARE data with other researchers (e.g. in online databases). Any personal information that could identify you will be REMOVED or REPLACED before files are SHARED with other researchers or results are MADE PUBLIC.\n \nThis project has received ethics clearance through the University of Oxford Central University Research Ethics Committee, R60939/RE005.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
confidentialityTextNext = visual.TextStim(win=win, name='confidentialityTextNext',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "information"
informationClock = core.Clock()
informationTextTitle = visual.TextStim(win=win, name='informationTextTitle',
    text='NEED MORE INFORMATION?',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
informationText = visual.TextStim(win=win, name='informationText',
    text='If you have a concern about any aspect of this study, please speak to Serene Siow (serene.siow@ox.ac.uk), and we will do our best to answer your query.\n\nIf you remain unhappy or wish to make a formal complaint, please contact the Chair of the Research Ethics Committee at the University of Oxford.\n \nChair, Medical Sciences Interdivisional Research Ethics Committee;\nEmail: ethics@medsci.ox.ac.uk',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
informationTextNext = visual.TextStim(win=win, name='informationTextNext',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "consent"
consentClock = core.Clock()
consentTextTitle = visual.TextStim(win=win, name='consentTextTitle',
    text='INFORMED CONSENT',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
consentText = visual.TextStim(win=win, name='consentText',
    text='BY PRESSING SPACE, I certify that I am 18 years of age or over. I agree to participate in the study described. I have made this decision based on the information I have read in the consent information. I have had the opportunity to receive any additional details I wanted about the study and understand that I may ask questions in the future. I understand that I may withdraw this consent at any time.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
consentTextNext = visual.TextStim(win=win, name='consentTextNext',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
consentKey = keyboard.Keyboard()

# Initialize components for Routine "languageL1"
languageL1Clock = core.Clock()
languageL1TextTitle = visual.TextStim(win=win, name='languageL1TextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL1Text = visual.TextStim(win=win, name='languageL1Text',
    text='What is your NATIVE language?\n\ne) English\ns) Spanish\nc) Catalan\no) Other',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL1TextNext = visual.TextStim(win=win, name='languageL1TextNext',
    text='Press the corresponding letter >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL1Key = keyboard.Keyboard()

# Initialize components for Routine "languageL2"
languageL2Clock = core.Clock()
languageL2TextTitle = visual.TextStim(win=win, name='languageL2TextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL2Text = visual.TextStim(win=win, name='languageL2Text',
    text='Do you know any other SECOND LANGUAGE, different than the one you indicated before? If yes, type which one and press RETURN. If no, press RETURN without writing anything.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL2TextNext = visual.TextStim(win=win, name='languageL2TextNext',
    text='Press ENTER to continue >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL2TextInput = visual.TextStim(win=win, name='languageL2TextInput',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "languageL2Oral"
languageL2OralClock = core.Clock()
languageL2OralTextTitle = visual.TextStim(win=win, name='languageL2OralTextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL2OralText = visual.TextStim(win=win, name='languageL2OralText',
    text='On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in your SECOND LANGUAGE?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL2OralTextNext = visual.TextStim(win=win, name='languageL2OralTextNext',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL2OralKey = keyboard.Keyboard()

# Initialize components for Routine "languageL2Written"
languageL2WrittenClock = core.Clock()
languageL2WrittenTextTitle = visual.TextStim(win=win, name='languageL2WrittenTextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL2WrittenText = visual.TextStim(win=win, name='languageL2WrittenText',
    text='On a scale of 1-5, how would you rate your WRITTEN proficiency in your SECOND LANGUAGE?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL2WrittenTextNext = visual.TextStim(win=win, name='languageL2WrittenTextNext',
    text='Presiona el número correspondiente.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL2WrittenKey = keyboard.Keyboard()

# Initialize components for Routine "languageL3"
languageL3Clock = core.Clock()
languageL3TextTitle = visual.TextStim(win=win, name='languageL3TextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL3Text = visual.TextStim(win=win, name='languageL3Text',
    text='Do you know any other THIRD LANGUAGE, different than the ones you indicated before? If yes, type which one(s) and press RETURN. If no, press RETURN leaving it blank.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL3TextNext = visual.TextStim(win=win, name='languageL3TextNext',
    text='Press RETURN to continue >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL3TextInput = visual.TextStim(win=win, name='languageL3TextInput',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "languageL3Oral"
languageL3OralClock = core.Clock()
languageL3OralTextTitle = visual.TextStim(win=win, name='languageL3OralTextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL3OralText = visual.TextStim(win=win, name='languageL3OralText',
    text='On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in your THIRD LANGUAGE?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native / I am native',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL3OralTextNext = visual.TextStim(win=win, name='languageL3OralTextNext',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL3OralKey = keyboard.Keyboard()

# Initialize components for Routine "languageL3Written"
languageL3WrittenClock = core.Clock()
languageL3WrittenTextTitle = visual.TextStim(win=win, name='languageL3WrittenTextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL3WrittenText = visual.TextStim(win=win, name='languageL3WrittenText',
    text='On a scale of 1-5, how would you rate your WRITTEN proficiency in your THIRD LANGUAGE?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL3WrittenTextNext = visual.TextStim(win=win, name='languageL3WrittenTextNext',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL3WrittenKey = keyboard.Keyboard()

# Initialize components for Routine "languageCatalanOral"
languageCatalanOralClock = core.Clock()
languageCatalanOralTextTitle = visual.TextStim(win=win, name='languageCatalanOralTextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageCatalanOralText = visual.TextStim(win=win, name='languageCatalanOralText',
    text='On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in CATALAN?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageCatalanOralTextNext = visual.TextStim(win=win, name='languageCatalanOralTextNext',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageCatalanOralKey = keyboard.Keyboard()

# Initialize components for Routine "languageCatalanWritten"
languageCatalanWrittenClock = core.Clock()
languageCatalanWrittenTextTitle = visual.TextStim(win=win, name='languageCatalanWrittenTextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageCatalanWrittenText = visual.TextStim(win=win, name='languageCatalanWrittenText',
    text='On a scale of 1-5, how would you rate your WRITTEN proficiency in CATALAN?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageCatalanWrittenTextNext = visual.TextStim(win=win, name='languageCatalanWrittenTextNext',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageCatalanWrittenKey = keyboard.Keyboard()

# Initialize components for Routine "languageCatalanTime"
languageCatalanTimeClock = core.Clock()
languageCatalanTimeTextTitle = visual.TextStim(win=win, name='languageCatalanTimeTextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageCatalanTimeText = visual.TextStim(win=win, name='languageCatalanTimeText',
    text='How long have you spent in any REGION where CATALAN is spoken (Catalonia, Valencia, Balearic Islands), including your childhood? Pick the option that best describes your situation:\n\n1) Never or less than 1 month\n2) Between 1 and 3 months\n3) I used to spend holidays there\n4) I lived there for less than 6 months\n5) I lived there for 6 months or longer',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageCatalanTimeTextNext = visual.TextStim(win=win, name='languageCatalanTimeTextNext',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageCatalanTimeKey = keyboard.Keyboard()

# Initialize components for Routine "languageSpanishOral"
languageSpanishOralClock = core.Clock()
languageSpanishOralTextTitle = visual.TextStim(win=win, name='languageSpanishOralTextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageSpanishOralText = visual.TextStim(win=win, name='languageSpanishOralText',
    text='On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in SPANISH?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageSpanishOralTextNext = visual.TextStim(win=win, name='languageSpanishOralTextNext',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageSpanishOralKey = keyboard.Keyboard()

# Initialize components for Routine "languageSpanishWritten"
languageSpanishWrittenClock = core.Clock()
languageSpanishWrittenTextTitle = visual.TextStim(win=win, name='languageSpanishWrittenTextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageSpanishWrittenText = visual.TextStim(win=win, name='languageSpanishWrittenText',
    text='On a scale of 1-5, how would you rate your WRITTEN proficiency in SPANISH?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageSpanishWrittenTextNext = visual.TextStim(win=win, name='languageSpanishWrittenTextNext',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageSpanishWrittenKey = keyboard.Keyboard()

# Initialize components for Routine "languageSpanishTime"
languageSpanishTimeClock = core.Clock()
languageSpanishTimeTextTitle = visual.TextStim(win=win, name='languageSpanishTimeTextTitle',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageSpanishTimeText = visual.TextStim(win=win, name='languageSpanishTimeText',
    text='How long have you spent in any REGION where SPANISH is spoken (Spain, South America), including your childhood? Pick the option that best describes your situation:\n\n1) Never or less than 1 month\n2) Between 1 and 3 months\n3) I used to spend holidays there\n4) I lived there for less than 6 months\n5) I lived there for 6 months or longer',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageSpanishTimeTextNext = visual.TextStim(win=win, name='languageSpanishTimeTextNext',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageSpanishTimeKey = keyboard.Keyboard()

# Initialize components for Routine "demoAge"
demoAgeClock = core.Clock()
demoAgeTextTitle = visual.TextStim(win=win, name='demoAgeTextTitle',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
demoAgeText = visual.TextStim(win=win, name='demoAgeText',
    text='Please, type your age (in years) and then press RETURN:',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
demoAgeTextNext = visual.TextStim(win=win, name='demoAgeTextNext',
    text='Presiona ENTER para continuar.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
demoAgeTextInput = visual.TextStim(win=win, name='demoAgeTextInput',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demoSex"
demoSexClock = core.Clock()
demoSexTextTitle = visual.TextStim(win=win, name='demoSexTextTitle',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
demoSexText = visual.TextStim(win=win, name='demoSexText',
    text='Sex:\n\nf) Female\nm) Male\no) Other',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
demoSexTextNext = visual.TextStim(win=win, name='demoSexTextNext',
    text='Press the corresponding letter >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
demoSexKey = keyboard.Keyboard()

# Initialize components for Routine "demoEducation"
demoEducationClock = core.Clock()
demoEducationTextTitle = visual.TextStim(win=win, name='demoEducationTextTitle',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
demoEducationText = visual.TextStim(win=win, name='demoEducationText',
    text='What is your highest level of EDUCATIONAL ACHIEVEMENT?\n\n1) No qualifications\n2) Left school at 16 with GCSE or equivalent\n3) Left school at 18 with A-Levels or equivalent\n4) University degree or equivalent\n5) Vocational training',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
demoEducationTextNext = visual.TextStim(win=win, name='demoEducationTextNext',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
demoEducationKey = keyboard.Keyboard()

# Initialize components for Routine "demoCity"
demoCityClock = core.Clock()
demoCityTextTitle = visual.TextStim(win=win, name='demoCityTextTitle',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
demoCityText = visual.TextStim(win=win, name='demoCityText',
    text='What CITY do you live in? Type it and press RETURN to continue.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
demoCityTextNext = visual.TextStim(win=win, name='demoCityTextNext',
    text='Press RETURN to continue >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
demoCityTextInput = visual.TextStim(win=win, name='demoCityTextInput',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demoVision"
demoVisionClock = core.Clock()
demoVisionTextTitle = visual.TextStim(win=win, name='demoVisionTextTitle',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
demoVisionText = visual.TextStim(win=win, name='demoVisionText',
    text='Do you have normal or corrected-to-normal VISION?\n\ny) Yes \nn) No',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
demoVisionTextNext = visual.TextStim(win=win, name='demoVisionTextNext',
    text='Press the corresponding letter >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
demoVisionKey = keyboard.Keyboard()

# Initialize components for Routine "demoLanguage"
demoLanguageClock = core.Clock()
demoLanguageTextTitle = visual.TextStim(win=win, name='demoLanguageTextTitle',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
demoLanguageText = visual.TextStim(win=win, name='demoLanguageText',
    text='Have you been diagnosed with any LANGUAGE (e.g., DYSLEXIA) OR HEARING IMPAIRMENT?\n\ny) Yes\nn) No',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
demoLanguageTextNext = visual.TextStim(win=win, name='demoLanguageTextNext',
    text='Press the corresponding letter >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
demoLanguageKey = keyboard.Keyboard()

# Initialize components for Routine "setupLocation"
setupLocationClock = core.Clock()
setupLocationTextTitle = visual.TextStim(win=win, name='setupLocationTextTitle',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
setupLocationText = visual.TextStim(win=win, name='setupLocationText',
    text='WHERE are you completing this study?\n\n1) At home\n2) At the library\n3) At a cafe or restaurant\n4) At a friend’s house\n5) At school\n6) At work\n7) Other',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
setupLocationTextNext = visual.TextStim(win=win, name='setupLocationTextNext',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
setupLocationKey = keyboard.Keyboard()

# Initialize components for Routine "setupNoise"
setupNoiseClock = core.Clock()
setupNoiseTextTitle = visual.TextStim(win=win, name='setupNoiseTextTitle',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
setupNoiseText = visual.TextStim(win=win, name='setupNoiseText',
    text='How NOISY was the environment in which you completed the experiment? \n\n1) Very quiet (like a library)\n2) Somewhat quiet (like an office)\n3) Somewhat noisy (like being at the park)\n4) Very noisy (like being at a busy street)',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
setupNoiseTextNext = visual.TextStim(win=win, name='setupNoiseTextNext',
    text='Presiona el número correspondiente.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
setupNoiseKey = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsTextTitle = visual.TextStim(win=win, name='instructionsTextTitle',
    text='INSTRUCTIONS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructionsText = visual.TextStim(win=win, name='instructionsText',
    text='You will listen to some words through your headphones.\n\nWords are in CATALAN OR SPANISH, and were recorded in a baby-directed manner. You will have to guess and type the TRANSLATION OF EACH WORD IN ENGLISH.\n\nStart typing AS SOON as you come up with an answer. It is probable that you do not know it. Type the translation you think is most likely to be correct. You must type an answer FOR EACH WORD.\n\nYou can use BACKSPACE to CORRECT any typing errors, as you would normally.\n\nAfter typing the word, press ENTER to continue to the next word.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructionsTextNext = visual.TextStim(win=win, name='instructionsTextNext',
    text='NEXT, YOU WILL COMPLETE 5 PRACTICE TRIALS\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, -0.7), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instructionsKeys = keyboard.Keyboard()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instructions2TextTitle = visual.TextStim(win=win, name='instructions2TextTitle',
    text='INSTRUCTIONS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructions2Text = visual.TextStim(win=win, name='instructions2Text',
    text='You may adjust the volume during these trials to avoid having to do it during the main experiment. Make sure words are loud enough for you to hear them clearly.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructions2TextNext = visual.TextStim(win=win, name='instructions2TextNext',
    text='Press SPACE to start 5 practice trials >',
    font='Arial',
    pos=(0, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
import random


# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixationText = visual.TextStim(win=win, name='fixationText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialText = visual.TextStim(win=win, name='trialText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trialSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='trialSound')
trialSound.setVolume(1)
inputText = '';

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixationText = visual.TextStim(win=win, name='fixationText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialText = visual.TextStim(win=win, name='trialText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trialSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='trialSound')
trialSound.setVolume(1)
inputText = '';

# Initialize components for Routine "begin"
beginClock = core.Clock()
beginText = visual.TextStim(win=win, name='beginText',
    text='You have completed the PRACTICE trials.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
beginNext = visual.TextStim(win=win, name='beginNext',
    text='Press SPACE to start >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixationText = visual.TextStim(win=win, name='fixationText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialText = visual.TextStim(win=win, name='trialText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trialSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='trialSound')
trialSound.setVolume(1)
inputText = '';

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixationText = visual.TextStim(win=win, name='fixationText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialText = visual.TextStim(win=win, name='trialText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trialSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='trialSound')
trialSound.setVolume(1)
inputText = '';

# Initialize components for Routine "farewell"
farewellClock = core.Clock()
farewellText = visual.TextStim(win=win, name='farewellText',
    text='Congratulations! You have finished.\n\nTHANKS A LOT FOR YOUR PARTICIPATION.\n\nYour participant ID is:\n\n\nIf you have any questions, get in touch with us at serene.siow@ox.ac.uk',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
farewellTextNext = visual.TextStim(win=win, name='farewellTextNext',
    text='Press RETURN to exit.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
farewellTextID = visual.TextStim(win=win, name='farewellTextID',
    text=participant,
    font='Arial',
    pos=(0, 0.01), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# align text to the left
setupText.alignText = "left"
welcomeText.alignText = "left"
descriptionText.alignText = "left"
voluntaryText.alignText = "left"
contactText.alignText = "left"
confidentialityText.alignText = "left"
informationText.alignText = "left"
consentText.alignText = "left"
languageL1Text.alignText = "left"
languageL2Text.alignText = "left"
languageL2OralText.alignText = "left"
languageL2WrittenText.alignText = "left"
languageL3Text.alignText = "left"
languageL3OralText.alignText = "left"
languageL3WrittenText.alignText = "left"
languageCatalanOralText.alignText = "left"
languageCatalanWrittenText.alignText = "left"
demoAgeText.alignText = "left"
demoSexText.alignText = "left"
demoEducationText.alignText = "left"
demoCityText.alignText = "left"
demoVisionText.alignText = "left"
demoLanguageText.alignText = "left"
setupLocationText.alignText = "left"
setupNoiseText.alignText = "left"
instructionsText.alignText = "left"
instructions2Text.alignText = "left"
beginText.alignText = "left"
farewellText.alignText = "left"

# keep track of which components have finished
setupComponents = [setupTextTitle, setupText, setupTextNext]
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *setupTextTitle* updates
    if setupTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupTextTitle.frameNStart = frameN  # exact frame index
        setupTextTitle.tStart = t  # local t and not account for scr refresh
        setupTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupTextTitle, 'tStartRefresh')  # time at next scr refresh
        setupTextTitle.setAutoDraw(True)
    
    # *setupText* updates
    if setupText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupText.frameNStart = frameN  # exact frame index
        setupText.tStart = t  # local t and not account for scr refresh
        setupText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupText, 'tStartRefresh')  # time at next scr refresh
        setupText.setAutoDraw(True)
    
    # *setupTextNext* updates
    if setupTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupTextNext.frameNStart = frameN  # exact frame index
        setupTextNext.tStart = t  # local t and not account for scr refresh
        setupTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupTextNext, 'tStartRefresh')  # time at next scr refresh
        setupTextNext.setAutoDraw(True)
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
welcomeComponents = [welcomeTextTitle, welcomeText, welcomeTextNext]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeTextTitle* updates
    if welcomeTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeTextTitle.frameNStart = frameN  # exact frame index
        welcomeTextTitle.tStart = t  # local t and not account for scr refresh
        welcomeTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeTextTitle, 'tStartRefresh')  # time at next scr refresh
        welcomeTextTitle.setAutoDraw(True)
    
    # *welcomeText* updates
    if welcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeText.frameNStart = frameN  # exact frame index
        welcomeText.tStart = t  # local t and not account for scr refresh
        welcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeText, 'tStartRefresh')  # time at next scr refresh
        welcomeText.setAutoDraw(True)
    
    # *welcomeTextNext* updates
    if welcomeTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeTextNext.frameNStart = frameN  # exact frame index
        welcomeTextNext.tStart = t  # local t and not account for scr refresh
        welcomeTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeTextNext, 'tStartRefresh')  # time at next scr refresh
        welcomeTextNext.setAutoDraw(True)
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "description"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
descriptionComponents = [descriptionTextTitle, descriptionText, descriptionTextNext]
for thisComponent in descriptionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
descriptionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "description"-------
while continueRoutine:
    # get current time
    t = descriptionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=descriptionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *descriptionTextTitle* updates
    if descriptionTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionTextTitle.frameNStart = frameN  # exact frame index
        descriptionTextTitle.tStart = t  # local t and not account for scr refresh
        descriptionTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionTextTitle, 'tStartRefresh')  # time at next scr refresh
        descriptionTextTitle.setAutoDraw(True)
    
    # *descriptionText* updates
    if descriptionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionText.frameNStart = frameN  # exact frame index
        descriptionText.tStart = t  # local t and not account for scr refresh
        descriptionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionText, 'tStartRefresh')  # time at next scr refresh
        descriptionText.setAutoDraw(True)
    
    # *descriptionTextNext* updates
    if descriptionTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionTextNext.frameNStart = frameN  # exact frame index
        descriptionTextNext.tStart = t  # local t and not account for scr refresh
        descriptionTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionTextNext, 'tStartRefresh')  # time at next scr refresh
        descriptionTextNext.setAutoDraw(True)
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in descriptionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "description"-------
for thisComponent in descriptionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "description" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "voluntary"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
voluntaryComponents = [voluntaryTextTitle, voluntaryText, voluntaryTextNext]
for thisComponent in voluntaryComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
voluntaryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "voluntary"-------
while continueRoutine:
    # get current time
    t = voluntaryClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=voluntaryClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *voluntaryTextTitle* updates
    if voluntaryTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        voluntaryTextTitle.frameNStart = frameN  # exact frame index
        voluntaryTextTitle.tStart = t  # local t and not account for scr refresh
        voluntaryTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(voluntaryTextTitle, 'tStartRefresh')  # time at next scr refresh
        voluntaryTextTitle.setAutoDraw(True)
    
    # *voluntaryText* updates
    if voluntaryText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        voluntaryText.frameNStart = frameN  # exact frame index
        voluntaryText.tStart = t  # local t and not account for scr refresh
        voluntaryText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(voluntaryText, 'tStartRefresh')  # time at next scr refresh
        voluntaryText.setAutoDraw(True)
    
    # *voluntaryTextNext* updates
    if voluntaryTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        voluntaryTextNext.frameNStart = frameN  # exact frame index
        voluntaryTextNext.tStart = t  # local t and not account for scr refresh
        voluntaryTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(voluntaryTextNext, 'tStartRefresh')  # time at next scr refresh
        voluntaryTextNext.setAutoDraw(True)
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in voluntaryComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "voluntary"-------
for thisComponent in voluntaryComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "voluntary" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "contact"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
contactComponents = [contactTextTitle, contactText, contactTextNext]
for thisComponent in contactComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
contactClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "contact"-------
while continueRoutine:
    # get current time
    t = contactClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=contactClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *contactTextTitle* updates
    if contactTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        contactTextTitle.frameNStart = frameN  # exact frame index
        contactTextTitle.tStart = t  # local t and not account for scr refresh
        contactTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contactTextTitle, 'tStartRefresh')  # time at next scr refresh
        contactTextTitle.setAutoDraw(True)
    
    # *contactText* updates
    if contactText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        contactText.frameNStart = frameN  # exact frame index
        contactText.tStart = t  # local t and not account for scr refresh
        contactText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contactText, 'tStartRefresh')  # time at next scr refresh
        contactText.setAutoDraw(True)
    
    # *contactTextNext* updates
    if contactTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        contactTextNext.frameNStart = frameN  # exact frame index
        contactTextNext.tStart = t  # local t and not account for scr refresh
        contactTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contactTextNext, 'tStartRefresh')  # time at next scr refresh
        contactTextNext.setAutoDraw(True)
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in contactComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "contact"-------
for thisComponent in contactComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "contact" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "confidentiality"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
confidentialityComponents = [confidentialityTextTitle, confidentialityText, confidentialityTextNext]
for thisComponent in confidentialityComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
confidentialityClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "confidentiality"-------
while continueRoutine:
    # get current time
    t = confidentialityClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=confidentialityClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *confidentialityTextTitle* updates
    if confidentialityTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        confidentialityTextTitle.frameNStart = frameN  # exact frame index
        confidentialityTextTitle.tStart = t  # local t and not account for scr refresh
        confidentialityTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confidentialityTextTitle, 'tStartRefresh')  # time at next scr refresh
        confidentialityTextTitle.setAutoDraw(True)
    
    # *confidentialityText* updates
    if confidentialityText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        confidentialityText.frameNStart = frameN  # exact frame index
        confidentialityText.tStart = t  # local t and not account for scr refresh
        confidentialityText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confidentialityText, 'tStartRefresh')  # time at next scr refresh
        confidentialityText.setAutoDraw(True)
    
    # *confidentialityTextNext* updates
    if confidentialityTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        confidentialityTextNext.frameNStart = frameN  # exact frame index
        confidentialityTextNext.tStart = t  # local t and not account for scr refresh
        confidentialityTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confidentialityTextNext, 'tStartRefresh')  # time at next scr refresh
        confidentialityTextNext.setAutoDraw(True)
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in confidentialityComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "confidentiality"-------
for thisComponent in confidentialityComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "confidentiality" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "information"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
informationComponents = [informationTextTitle, informationText, informationTextNext]
for thisComponent in informationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
informationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "information"-------
while continueRoutine:
    # get current time
    t = informationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=informationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *informationTextTitle* updates
    if informationTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        informationTextTitle.frameNStart = frameN  # exact frame index
        informationTextTitle.tStart = t  # local t and not account for scr refresh
        informationTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(informationTextTitle, 'tStartRefresh')  # time at next scr refresh
        informationTextTitle.setAutoDraw(True)
    
    # *informationText* updates
    if informationText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        informationText.frameNStart = frameN  # exact frame index
        informationText.tStart = t  # local t and not account for scr refresh
        informationText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(informationText, 'tStartRefresh')  # time at next scr refresh
        informationText.setAutoDraw(True)
    
    # *informationTextNext* updates
    if informationTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        informationTextNext.frameNStart = frameN  # exact frame index
        informationTextNext.tStart = t  # local t and not account for scr refresh
        informationTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(informationTextNext, 'tStartRefresh')  # time at next scr refresh
        informationTextNext.setAutoDraw(True)
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in informationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "information"-------
for thisComponent in informationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "information" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "consent"-------
continueRoutine = True
# update component parameters for each repeat
consentKey.keys = []
consentKey.rt = []
_consentKey_allKeys = []
# keep track of which components have finished
consentComponents = [consentTextTitle, consentText, consentTextNext, consentKey]
for thisComponent in consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
consentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "consent"-------
while continueRoutine:
    # get current time
    t = consentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=consentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *consentTextTitle* updates
    if consentTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consentTextTitle.frameNStart = frameN  # exact frame index
        consentTextTitle.tStart = t  # local t and not account for scr refresh
        consentTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentTextTitle, 'tStartRefresh')  # time at next scr refresh
        consentTextTitle.setAutoDraw(True)
    
    # *consentText* updates
    if consentText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consentText.frameNStart = frameN  # exact frame index
        consentText.tStart = t  # local t and not account for scr refresh
        consentText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentText, 'tStartRefresh')  # time at next scr refresh
        consentText.setAutoDraw(True)
    
    # *consentTextNext* updates
    if consentTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consentTextNext.frameNStart = frameN  # exact frame index
        consentTextNext.tStart = t  # local t and not account for scr refresh
        consentTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentTextNext, 'tStartRefresh')  # time at next scr refresh
        consentTextNext.setAutoDraw(True)
    
    # *consentKey* updates
    waitOnFlip = False
    if consentKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consentKey.frameNStart = frameN  # exact frame index
        consentKey.tStart = t  # local t and not account for scr refresh
        consentKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentKey, 'tStartRefresh')  # time at next scr refresh
        consentKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(consentKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(consentKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if consentKey.status == STARTED and not waitOnFlip:
        theseKeys = consentKey.getKeys(keyList=['space', 'escape'], waitRelease=False)
        _consentKey_allKeys.extend(theseKeys)
        if len(_consentKey_allKeys):
            consentKey.keys = _consentKey_allKeys[-1].name  # just the last key pressed
            consentKey.rt = _consentKey_allKeys[-1].rt
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "consent"-------
for thisComponent in consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if consentKey.keys in ['', [], None]:  # No response was made
    consentKey.keys = None
thisExp.addData('consentKey.keys',consentKey.keys)
if consentKey.keys != None:  # we had a response
    thisExp.addData('consentKey.rt', consentKey.rt)
thisExp.nextEntry()
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageL1"-------
continueRoutine = True
# update component parameters for each repeat
languageL1Key.keys = []
languageL1Key.rt = []
_languageL1Key_allKeys = []
# keep track of which components have finished
languageL1Components = [languageL1TextTitle, languageL1Text, languageL1TextNext, languageL1Key]
for thisComponent in languageL1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageL1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageL1"-------
while continueRoutine:
    # get current time
    t = languageL1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageL1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageL1TextTitle* updates
    if languageL1TextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL1TextTitle.frameNStart = frameN  # exact frame index
        languageL1TextTitle.tStart = t  # local t and not account for scr refresh
        languageL1TextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL1TextTitle, 'tStartRefresh')  # time at next scr refresh
        languageL1TextTitle.setAutoDraw(True)
    
    # *languageL1Text* updates
    if languageL1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL1Text.frameNStart = frameN  # exact frame index
        languageL1Text.tStart = t  # local t and not account for scr refresh
        languageL1Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL1Text, 'tStartRefresh')  # time at next scr refresh
        languageL1Text.setAutoDraw(True)
    
    # *languageL1TextNext* updates
    if languageL1TextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL1TextNext.frameNStart = frameN  # exact frame index
        languageL1TextNext.tStart = t  # local t and not account for scr refresh
        languageL1TextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL1TextNext, 'tStartRefresh')  # time at next scr refresh
        languageL1TextNext.setAutoDraw(True)
    
    # *languageL1Key* updates
    waitOnFlip = False
    if languageL1Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL1Key.frameNStart = frameN  # exact frame index
        languageL1Key.tStart = t  # local t and not account for scr refresh
        languageL1Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL1Key, 'tStartRefresh')  # time at next scr refresh
        languageL1Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(languageL1Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(languageL1Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if languageL1Key.status == STARTED and not waitOnFlip:
        theseKeys = languageL1Key.getKeys(keyList=['e', 's', 'c', 'o', 'escape'], waitRelease=False)
        _languageL1Key_allKeys.extend(theseKeys)
        if len(_languageL1Key_allKeys):
            languageL1Key.keys = _languageL1Key_allKeys[-1].name  # just the last key pressed
            languageL1Key.rt = _languageL1Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageL1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageL1"-------
for thisComponent in languageL1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if languageL1Key.keys in ['', [], None]:  # No response was made
    languageL1Key.keys = None
thisExp.addData('languageL1Key.keys',languageL1Key.keys)
if languageL1Key.keys != None:  # we had a response
    thisExp.addData('languageL1Key.rt', languageL1Key.rt)
thisExp.nextEntry()
# the Routine "languageL1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageL2"-------
continueRoutine = True
# update component parameters for each repeat
psychopy.event.clearEvents()
inputText = ''
isAccented = False

# keep track of which components have finished
languageL2Components = [languageL2TextTitle, languageL2Text, languageL2TextNext, languageL2TextInput]
for thisComponent in languageL2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageL2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageL2"-------
while continueRoutine:
    # get current time
    t = languageL2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageL2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageL2TextTitle* updates
    if languageL2TextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2TextTitle.frameNStart = frameN  # exact frame index
        languageL2TextTitle.tStart = t  # local t and not account for scr refresh
        languageL2TextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2TextTitle, 'tStartRefresh')  # time at next scr refresh
        languageL2TextTitle.setAutoDraw(True)
    
    # *languageL2Text* updates
    if languageL2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2Text.frameNStart = frameN  # exact frame index
        languageL2Text.tStart = t  # local t and not account for scr refresh
        languageL2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2Text, 'tStartRefresh')  # time at next scr refresh
        languageL2Text.setAutoDraw(True)
    
    # *languageL2TextNext* updates
    if languageL2TextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2TextNext.frameNStart = frameN  # exact frame index
        languageL2TextNext.tStart = t  # local t and not account for scr refresh
        languageL2TextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2TextNext, 'tStartRefresh')  # time at next scr refresh
        languageL2TextNext.setAutoDraw(True)
    
    # *languageL2TextInput* updates
    if languageL2TextInput.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2TextInput.frameNStart = frameN  # exact frame index
        languageL2TextInput.tStart = t  # local t and not account for scr refresh
        languageL2TextInput.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2TextInput, 'tStartRefresh')  # time at next scr refresh
        languageL2TextInput.setAutoDraw(True)
    if languageL2TextInput.status == STARTED:  # only update if drawing
        languageL2TextInput.setText('> ' + inputText, log=False)
    keys = event.getKeys(keyList = letterKeysAllowed)
    i = 0 # index whether how many keys have been previously pressed
    
    if len(keys): # if any key has been pressed...
    
         # ... and ESCAPE is pressed, quit experiment
        if keys[i]=='escape':
            thisExp.addData('languageL2', inputText) # save data
            core.quit()
            # ... and RETURN is pressed, stop trial
        if (keys[i]=='return'):
            languageL2value = inputText
            if (inputText==''):
                languageL3value=''
            thisExp.addData('languageL2', inputText) # save data
            continueRoutine = False 
        # ... and BACKSPACE is pressed, delete last character
        elif (keys[i]=='backspace'):
            inputText = inputText[:-1]
        elif (keys[i]=='space'):
            inputText += ' ';
        # and 'apostrophe' is pressed, flag accent
        elif (keys[i]=='apostrophe'):
            inputText="'"
        else:
            # write key as it is (in capital letters)
            inputText += keys[i].upper()
            thisExp.addData('languageL2', inputText) # save data
            i = i + 1 # index another key press
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageL2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageL2"-------
for thisComponent in languageL2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
print(languageL2value)
# the Routine "languageL2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageL2Oral"-------
continueRoutine = True
# update component parameters for each repeat
languageL2OralKey.keys = []
languageL2OralKey.rt = []
_languageL2OralKey_allKeys = []
# keep track of which components have finished
languageL2OralComponents = [languageL2OralTextTitle, languageL2OralText, languageL2OralTextNext, languageL2OralKey]
for thisComponent in languageL2OralComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageL2OralClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageL2Oral"-------
while continueRoutine:
    # get current time
    t = languageL2OralClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageL2OralClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageL2OralTextTitle* updates
    if languageL2OralTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2OralTextTitle.frameNStart = frameN  # exact frame index
        languageL2OralTextTitle.tStart = t  # local t and not account for scr refresh
        languageL2OralTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2OralTextTitle, 'tStartRefresh')  # time at next scr refresh
        languageL2OralTextTitle.setAutoDraw(True)
    
    # *languageL2OralText* updates
    if languageL2OralText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2OralText.frameNStart = frameN  # exact frame index
        languageL2OralText.tStart = t  # local t and not account for scr refresh
        languageL2OralText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2OralText, 'tStartRefresh')  # time at next scr refresh
        languageL2OralText.setAutoDraw(True)
    
    # *languageL2OralTextNext* updates
    if languageL2OralTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2OralTextNext.frameNStart = frameN  # exact frame index
        languageL2OralTextNext.tStart = t  # local t and not account for scr refresh
        languageL2OralTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2OralTextNext, 'tStartRefresh')  # time at next scr refresh
        languageL2OralTextNext.setAutoDraw(True)
    
    # *languageL2OralKey* updates
    waitOnFlip = False
    if languageL2OralKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2OralKey.frameNStart = frameN  # exact frame index
        languageL2OralKey.tStart = t  # local t and not account for scr refresh
        languageL2OralKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2OralKey, 'tStartRefresh')  # time at next scr refresh
        languageL2OralKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(languageL2OralKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(languageL2OralKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if languageL2OralKey.status == STARTED and not waitOnFlip:
        theseKeys = languageL2OralKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _languageL2OralKey_allKeys.extend(theseKeys)
        if len(_languageL2OralKey_allKeys):
            languageL2OralKey.keys = _languageL2OralKey_allKeys[-1].name  # just the last key pressed
            languageL2OralKey.rt = _languageL2OralKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    if languageL2=='':
        continueRoutine = False
        
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageL2OralComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageL2Oral"-------
for thisComponent in languageL2OralComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if languageL2OralKey.keys in ['', [], None]:  # No response was made
    languageL2OralKey.keys = None
thisExp.addData('languageL2OralKey.keys',languageL2OralKey.keys)
if languageL2OralKey.keys != None:  # we had a response
    thisExp.addData('languageL2OralKey.rt', languageL2OralKey.rt)
thisExp.nextEntry()
# the Routine "languageL2Oral" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageL2Written"-------
continueRoutine = True
# update component parameters for each repeat
languageL2WrittenKey.keys = []
languageL2WrittenKey.rt = []
_languageL2WrittenKey_allKeys = []
# keep track of which components have finished
languageL2WrittenComponents = [languageL2WrittenTextTitle, languageL2WrittenText, languageL2WrittenTextNext, languageL2WrittenKey]
for thisComponent in languageL2WrittenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageL2WrittenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageL2Written"-------
while continueRoutine:
    # get current time
    t = languageL2WrittenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageL2WrittenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageL2WrittenTextTitle* updates
    if languageL2WrittenTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2WrittenTextTitle.frameNStart = frameN  # exact frame index
        languageL2WrittenTextTitle.tStart = t  # local t and not account for scr refresh
        languageL2WrittenTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2WrittenTextTitle, 'tStartRefresh')  # time at next scr refresh
        languageL2WrittenTextTitle.setAutoDraw(True)
    
    # *languageL2WrittenText* updates
    if languageL2WrittenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2WrittenText.frameNStart = frameN  # exact frame index
        languageL2WrittenText.tStart = t  # local t and not account for scr refresh
        languageL2WrittenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2WrittenText, 'tStartRefresh')  # time at next scr refresh
        languageL2WrittenText.setAutoDraw(True)
    
    # *languageL2WrittenTextNext* updates
    if languageL2WrittenTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2WrittenTextNext.frameNStart = frameN  # exact frame index
        languageL2WrittenTextNext.tStart = t  # local t and not account for scr refresh
        languageL2WrittenTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2WrittenTextNext, 'tStartRefresh')  # time at next scr refresh
        languageL2WrittenTextNext.setAutoDraw(True)
    
    # *languageL2WrittenKey* updates
    waitOnFlip = False
    if languageL2WrittenKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2WrittenKey.frameNStart = frameN  # exact frame index
        languageL2WrittenKey.tStart = t  # local t and not account for scr refresh
        languageL2WrittenKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2WrittenKey, 'tStartRefresh')  # time at next scr refresh
        languageL2WrittenKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(languageL2WrittenKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(languageL2WrittenKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if languageL2WrittenKey.status == STARTED and not waitOnFlip:
        theseKeys = languageL2WrittenKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _languageL2WrittenKey_allKeys.extend(theseKeys)
        if len(_languageL2WrittenKey_allKeys):
            languageL2WrittenKey.keys = _languageL2WrittenKey_allKeys[-1].name  # just the last key pressed
            languageL2WrittenKey.rt = _languageL2WrittenKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if languageL2=='':
        continueRoutine = False
        
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageL2WrittenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageL2Written"-------
for thisComponent in languageL2WrittenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if languageL2WrittenKey.keys in ['', [], None]:  # No response was made
    languageL2WrittenKey.keys = None
thisExp.addData('languageL2WrittenKey.keys',languageL2WrittenKey.keys)
if languageL2WrittenKey.keys != None:  # we had a response
    thisExp.addData('languageL2WrittenKey.rt', languageL2WrittenKey.rt)
thisExp.nextEntry()
# the Routine "languageL2Written" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageL3"-------
continueRoutine = True
# update component parameters for each repeat
psychopy.event.clearEvents()
inputText = ''
isAccented = False
# keep track of which components have finished
languageL3Components = [languageL3TextTitle, languageL3Text, languageL3TextNext, languageL3TextInput]
for thisComponent in languageL3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageL3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageL3"-------
while continueRoutine:
    # get current time
    t = languageL3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageL3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageL3TextTitle* updates
    if languageL3TextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3TextTitle.frameNStart = frameN  # exact frame index
        languageL3TextTitle.tStart = t  # local t and not account for scr refresh
        languageL3TextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3TextTitle, 'tStartRefresh')  # time at next scr refresh
        languageL3TextTitle.setAutoDraw(True)
    
    # *languageL3Text* updates
    if languageL3Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3Text.frameNStart = frameN  # exact frame index
        languageL3Text.tStart = t  # local t and not account for scr refresh
        languageL3Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3Text, 'tStartRefresh')  # time at next scr refresh
        languageL3Text.setAutoDraw(True)
    
    # *languageL3TextNext* updates
    if languageL3TextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3TextNext.frameNStart = frameN  # exact frame index
        languageL3TextNext.tStart = t  # local t and not account for scr refresh
        languageL3TextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3TextNext, 'tStartRefresh')  # time at next scr refresh
        languageL3TextNext.setAutoDraw(True)
    
    # *languageL3TextInput* updates
    if languageL3TextInput.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3TextInput.frameNStart = frameN  # exact frame index
        languageL3TextInput.tStart = t  # local t and not account for scr refresh
        languageL3TextInput.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3TextInput, 'tStartRefresh')  # time at next scr refresh
        languageL3TextInput.setAutoDraw(True)
    if languageL3TextInput.status == STARTED:  # only update if drawing
        languageL3TextInput.setText('> ' + inputText, log=False)
    if languageL2value=='':
        continueRoutine = False
    
    keys = event.getKeys(keyList = letterKeysAllowed)
    i = 0 # index whether how many keys have been previously pressed
    
    if len(keys): # if any key has been pressed...
    
         # ... and ESCAPE is pressed, quit experiment
        if keys[i]=='escape':
            thisExp.addData('languageL3', inputText) # save data
            core.quit()
            # ... and RETURN is pressed, stop trial
        elif (keys[i]=='return'):
            languageL3value = inputText
            thisExp.addData('languageL3', inputText) # save data
            continueRoutine = False
        # ... and SPACE is pressed, add space
        elif (keys[i]=='space'):
            inputText += ' '
        # ... and BACKSPACE is pressed, delete last character
        elif (keys[i]=='backspace'):
            inputText = inputText[:-1]
        # and 'apostrophe' is pressed, flag accent
        elif (keys[i]=='apostrophe'):
            inputText = "'"
        else:
            # write key as it is (in capital letters)
            inputText += keys[i].upper()
            thisExp.addData('languageL3', inputText) # save data
            i = i + 1 # index another key press
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageL3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageL3"-------
for thisComponent in languageL3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
print(languageL3value)
# the Routine "languageL3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageL3Oral"-------
continueRoutine = True
# update component parameters for each repeat
languageL3OralKey.keys = []
languageL3OralKey.rt = []
_languageL3OralKey_allKeys = []


# keep track of which components have finished
languageL3OralComponents = [languageL3OralTextTitle, languageL3OralText, languageL3OralTextNext, languageL3OralKey]
for thisComponent in languageL3OralComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageL3OralClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageL3Oral"-------
while continueRoutine:
    # get current time
    t = languageL3OralClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageL3OralClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageL3OralTextTitle* updates
    if languageL3OralTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3OralTextTitle.frameNStart = frameN  # exact frame index
        languageL3OralTextTitle.tStart = t  # local t and not account for scr refresh
        languageL3OralTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3OralTextTitle, 'tStartRefresh')  # time at next scr refresh
        languageL3OralTextTitle.setAutoDraw(True)
    
    # *languageL3OralText* updates
    if languageL3OralText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3OralText.frameNStart = frameN  # exact frame index
        languageL3OralText.tStart = t  # local t and not account for scr refresh
        languageL3OralText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3OralText, 'tStartRefresh')  # time at next scr refresh
        languageL3OralText.setAutoDraw(True)
    
    # *languageL3OralTextNext* updates
    if languageL3OralTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3OralTextNext.frameNStart = frameN  # exact frame index
        languageL3OralTextNext.tStart = t  # local t and not account for scr refresh
        languageL3OralTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3OralTextNext, 'tStartRefresh')  # time at next scr refresh
        languageL3OralTextNext.setAutoDraw(True)
    
    # *languageL3OralKey* updates
    waitOnFlip = False
    if languageL3OralKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3OralKey.frameNStart = frameN  # exact frame index
        languageL3OralKey.tStart = t  # local t and not account for scr refresh
        languageL3OralKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3OralKey, 'tStartRefresh')  # time at next scr refresh
        languageL3OralKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(languageL3OralKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(languageL3OralKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if languageL3OralKey.status == STARTED and not waitOnFlip:
        theseKeys = languageL3OralKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _languageL3OralKey_allKeys.extend(theseKeys)
        if len(_languageL3OralKey_allKeys):
            languageL3OralKey.keys = _languageL3OralKey_allKeys[-1].name  # just the last key pressed
            languageL3OralKey.rt = _languageL3OralKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    if languageL3value=='' or languageL2value=='':
        continueRoutine = False
        
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageL3OralComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageL3Oral"-------
for thisComponent in languageL3OralComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if languageL3OralKey.keys in ['', [], None]:  # No response was made
    languageL3OralKey.keys = None
thisExp.addData('languageL3OralKey.keys',languageL3OralKey.keys)
if languageL3OralKey.keys != None:  # we had a response
    thisExp.addData('languageL3OralKey.rt', languageL3OralKey.rt)
thisExp.nextEntry()
# the Routine "languageL3Oral" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageL3Written"-------
continueRoutine = True
# update component parameters for each repeat
languageL3WrittenKey.keys = []
languageL3WrittenKey.rt = []
_languageL3WrittenKey_allKeys = []
# keep track of which components have finished
languageL3WrittenComponents = [languageL3WrittenTextTitle, languageL3WrittenText, languageL3WrittenTextNext, languageL3WrittenKey]
for thisComponent in languageL3WrittenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageL3WrittenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageL3Written"-------
while continueRoutine:
    # get current time
    t = languageL3WrittenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageL3WrittenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageL3WrittenTextTitle* updates
    if languageL3WrittenTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3WrittenTextTitle.frameNStart = frameN  # exact frame index
        languageL3WrittenTextTitle.tStart = t  # local t and not account for scr refresh
        languageL3WrittenTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3WrittenTextTitle, 'tStartRefresh')  # time at next scr refresh
        languageL3WrittenTextTitle.setAutoDraw(True)
    
    # *languageL3WrittenText* updates
    if languageL3WrittenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3WrittenText.frameNStart = frameN  # exact frame index
        languageL3WrittenText.tStart = t  # local t and not account for scr refresh
        languageL3WrittenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3WrittenText, 'tStartRefresh')  # time at next scr refresh
        languageL3WrittenText.setAutoDraw(True)
    
    # *languageL3WrittenTextNext* updates
    if languageL3WrittenTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3WrittenTextNext.frameNStart = frameN  # exact frame index
        languageL3WrittenTextNext.tStart = t  # local t and not account for scr refresh
        languageL3WrittenTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3WrittenTextNext, 'tStartRefresh')  # time at next scr refresh
        languageL3WrittenTextNext.setAutoDraw(True)
    
    # *languageL3WrittenKey* updates
    waitOnFlip = False
    if languageL3WrittenKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3WrittenKey.frameNStart = frameN  # exact frame index
        languageL3WrittenKey.tStart = t  # local t and not account for scr refresh
        languageL3WrittenKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3WrittenKey, 'tStartRefresh')  # time at next scr refresh
        languageL3WrittenKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(languageL3WrittenKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(languageL3WrittenKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if languageL3WrittenKey.status == STARTED and not waitOnFlip:
        theseKeys = languageL3WrittenKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _languageL3WrittenKey_allKeys.extend(theseKeys)
        if len(_languageL3WrittenKey_allKeys):
            languageL3WrittenKey.keys = _languageL3WrittenKey_allKeys[-1].name  # just the last key pressed
            languageL3WrittenKey.rt = _languageL3WrittenKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    if languageL3=='':
        continueRoutine = False
    
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageL3WrittenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageL3Written"-------
for thisComponent in languageL3WrittenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if languageL3WrittenKey.keys in ['', [], None]:  # No response was made
    languageL3WrittenKey.keys = None
thisExp.addData('languageL3WrittenKey.keys',languageL3WrittenKey.keys)
if languageL3WrittenKey.keys != None:  # we had a response
    thisExp.addData('languageL3WrittenKey.rt', languageL3WrittenKey.rt)
thisExp.nextEntry()
# the Routine "languageL3Written" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageCatalanOral"-------
continueRoutine = True
# update component parameters for each repeat
languageCatalanOralKey.keys = []
languageCatalanOralKey.rt = []
_languageCatalanOralKey_allKeys = []
# keep track of which components have finished
languageCatalanOralComponents = [languageCatalanOralTextTitle, languageCatalanOralText, languageCatalanOralTextNext, languageCatalanOralKey]
for thisComponent in languageCatalanOralComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageCatalanOralClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageCatalanOral"-------
while continueRoutine:
    # get current time
    t = languageCatalanOralClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageCatalanOralClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageCatalanOralTextTitle* updates
    if languageCatalanOralTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanOralTextTitle.frameNStart = frameN  # exact frame index
        languageCatalanOralTextTitle.tStart = t  # local t and not account for scr refresh
        languageCatalanOralTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanOralTextTitle, 'tStartRefresh')  # time at next scr refresh
        languageCatalanOralTextTitle.setAutoDraw(True)
    
    # *languageCatalanOralText* updates
    if languageCatalanOralText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanOralText.frameNStart = frameN  # exact frame index
        languageCatalanOralText.tStart = t  # local t and not account for scr refresh
        languageCatalanOralText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanOralText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanOralText.setAutoDraw(True)
    
    # *languageCatalanOralTextNext* updates
    if languageCatalanOralTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanOralTextNext.frameNStart = frameN  # exact frame index
        languageCatalanOralTextNext.tStart = t  # local t and not account for scr refresh
        languageCatalanOralTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanOralTextNext, 'tStartRefresh')  # time at next scr refresh
        languageCatalanOralTextNext.setAutoDraw(True)
    
    # *languageCatalanOralKey* updates
    waitOnFlip = False
    if languageCatalanOralKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanOralKey.frameNStart = frameN  # exact frame index
        languageCatalanOralKey.tStart = t  # local t and not account for scr refresh
        languageCatalanOralKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanOralKey, 'tStartRefresh')  # time at next scr refresh
        languageCatalanOralKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(languageCatalanOralKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(languageCatalanOralKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if languageCatalanOralKey.status == STARTED and not waitOnFlip:
        theseKeys = languageCatalanOralKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _languageCatalanOralKey_allKeys.extend(theseKeys)
        if len(_languageCatalanOralKey_allKeys):
            languageCatalanOralKey.keys = _languageCatalanOralKey_allKeys[-1].name  # just the last key pressed
            languageCatalanOralKey.rt = _languageCatalanOralKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if Catalan is L2 or L3, skip
    if (languageL2value=="CATALAN" or languageL3value=="CATALAN"):
        continueRoutine = False
        
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageCatalanOralComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageCatalanOral"-------
for thisComponent in languageCatalanOralComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if languageCatalanOralKey.keys in ['', [], None]:  # No response was made
    languageCatalanOralKey.keys = None
thisExp.addData('languageCatalanOralKey.keys',languageCatalanOralKey.keys)
if languageCatalanOralKey.keys != None:  # we had a response
    thisExp.addData('languageCatalanOralKey.rt', languageCatalanOralKey.rt)
thisExp.nextEntry()
# the Routine "languageCatalanOral" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageCatalanWritten"-------
continueRoutine = True
# update component parameters for each repeat
languageCatalanWrittenKey.keys = []
languageCatalanWrittenKey.rt = []
_languageCatalanWrittenKey_allKeys = []
# keep track of which components have finished
languageCatalanWrittenComponents = [languageCatalanWrittenTextTitle, languageCatalanWrittenText, languageCatalanWrittenTextNext, languageCatalanWrittenKey]
for thisComponent in languageCatalanWrittenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageCatalanWrittenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageCatalanWritten"-------
while continueRoutine:
    # get current time
    t = languageCatalanWrittenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageCatalanWrittenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageCatalanWrittenTextTitle* updates
    if languageCatalanWrittenTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanWrittenTextTitle.frameNStart = frameN  # exact frame index
        languageCatalanWrittenTextTitle.tStart = t  # local t and not account for scr refresh
        languageCatalanWrittenTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanWrittenTextTitle, 'tStartRefresh')  # time at next scr refresh
        languageCatalanWrittenTextTitle.setAutoDraw(True)
    
    # *languageCatalanWrittenText* updates
    if languageCatalanWrittenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanWrittenText.frameNStart = frameN  # exact frame index
        languageCatalanWrittenText.tStart = t  # local t and not account for scr refresh
        languageCatalanWrittenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanWrittenText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanWrittenText.setAutoDraw(True)
    
    # *languageCatalanWrittenTextNext* updates
    if languageCatalanWrittenTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanWrittenTextNext.frameNStart = frameN  # exact frame index
        languageCatalanWrittenTextNext.tStart = t  # local t and not account for scr refresh
        languageCatalanWrittenTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanWrittenTextNext, 'tStartRefresh')  # time at next scr refresh
        languageCatalanWrittenTextNext.setAutoDraw(True)
    
    # *languageCatalanWrittenKey* updates
    waitOnFlip = False
    if languageCatalanWrittenKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanWrittenKey.frameNStart = frameN  # exact frame index
        languageCatalanWrittenKey.tStart = t  # local t and not account for scr refresh
        languageCatalanWrittenKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanWrittenKey, 'tStartRefresh')  # time at next scr refresh
        languageCatalanWrittenKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(languageCatalanWrittenKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(languageCatalanWrittenKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if languageCatalanWrittenKey.status == STARTED and not waitOnFlip:
        theseKeys = languageCatalanWrittenKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _languageCatalanWrittenKey_allKeys.extend(theseKeys)
        if len(_languageCatalanWrittenKey_allKeys):
            languageCatalanWrittenKey.keys = _languageCatalanWrittenKey_allKeys[-1].name  # just the last key pressed
            languageCatalanWrittenKey.rt = _languageCatalanWrittenKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if Catalan is L2 or L3, skip
    if (languageL2value=="CATALAN" or languageL3value=="CATALAN"):
        continueRoutine = False
        
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageCatalanWrittenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageCatalanWritten"-------
for thisComponent in languageCatalanWrittenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if languageCatalanWrittenKey.keys in ['', [], None]:  # No response was made
    languageCatalanWrittenKey.keys = None
thisExp.addData('languageCatalanWrittenKey.keys',languageCatalanWrittenKey.keys)
if languageCatalanWrittenKey.keys != None:  # we had a response
    thisExp.addData('languageCatalanWrittenKey.rt', languageCatalanWrittenKey.rt)
thisExp.nextEntry()
# the Routine "languageCatalanWritten" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageCatalanTime"-------
continueRoutine = True
# update component parameters for each repeat
languageCatalanTimeKey.keys = []
languageCatalanTimeKey.rt = []
_languageCatalanTimeKey_allKeys = []
# keep track of which components have finished
languageCatalanTimeComponents = [languageCatalanTimeTextTitle, languageCatalanTimeText, languageCatalanTimeTextNext, languageCatalanTimeKey]
for thisComponent in languageCatalanTimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageCatalanTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageCatalanTime"-------
while continueRoutine:
    # get current time
    t = languageCatalanTimeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageCatalanTimeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageCatalanTimeTextTitle* updates
    if languageCatalanTimeTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanTimeTextTitle.frameNStart = frameN  # exact frame index
        languageCatalanTimeTextTitle.tStart = t  # local t and not account for scr refresh
        languageCatalanTimeTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanTimeTextTitle, 'tStartRefresh')  # time at next scr refresh
        languageCatalanTimeTextTitle.setAutoDraw(True)
    
    # *languageCatalanTimeText* updates
    if languageCatalanTimeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanTimeText.frameNStart = frameN  # exact frame index
        languageCatalanTimeText.tStart = t  # local t and not account for scr refresh
        languageCatalanTimeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanTimeText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanTimeText.setAutoDraw(True)
    
    # *languageCatalanTimeTextNext* updates
    if languageCatalanTimeTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanTimeTextNext.frameNStart = frameN  # exact frame index
        languageCatalanTimeTextNext.tStart = t  # local t and not account for scr refresh
        languageCatalanTimeTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanTimeTextNext, 'tStartRefresh')  # time at next scr refresh
        languageCatalanTimeTextNext.setAutoDraw(True)
    
    # *languageCatalanTimeKey* updates
    waitOnFlip = False
    if languageCatalanTimeKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanTimeKey.frameNStart = frameN  # exact frame index
        languageCatalanTimeKey.tStart = t  # local t and not account for scr refresh
        languageCatalanTimeKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanTimeKey, 'tStartRefresh')  # time at next scr refresh
        languageCatalanTimeKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(languageCatalanTimeKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(languageCatalanTimeKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if languageCatalanTimeKey.status == STARTED and not waitOnFlip:
        theseKeys = languageCatalanTimeKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _languageCatalanTimeKey_allKeys.extend(theseKeys)
        if len(_languageCatalanTimeKey_allKeys):
            languageCatalanTimeKey.keys = _languageCatalanTimeKey_allKeys[-1].name  # just the last key pressed
            languageCatalanTimeKey.rt = _languageCatalanTimeKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if Catalan is L2 or L3, skip
    if (languageL2value=="CATALAN" or languageL3value=="CATALAN"):
        continueRoutine = False
        
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageCatalanTimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageCatalanTime"-------
for thisComponent in languageCatalanTimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if languageCatalanTimeKey.keys in ['', [], None]:  # No response was made
    languageCatalanTimeKey.keys = None
thisExp.addData('languageCatalanTimeKey.keys',languageCatalanTimeKey.keys)
if languageCatalanTimeKey.keys != None:  # we had a response
    thisExp.addData('languageCatalanTimeKey.rt', languageCatalanTimeKey.rt)
thisExp.nextEntry()
# the Routine "languageCatalanTime" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageSpanishOral"-------
continueRoutine = True
# update component parameters for each repeat
languageSpanishOralKey.keys = []
languageSpanishOralKey.rt = []
_languageSpanishOralKey_allKeys = []
# keep track of which components have finished
languageSpanishOralComponents = [languageSpanishOralTextTitle, languageSpanishOralText, languageSpanishOralTextNext, languageSpanishOralKey]
for thisComponent in languageSpanishOralComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageSpanishOralClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageSpanishOral"-------
while continueRoutine:
    # get current time
    t = languageSpanishOralClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageSpanishOralClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageSpanishOralTextTitle* updates
    if languageSpanishOralTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishOralTextTitle.frameNStart = frameN  # exact frame index
        languageSpanishOralTextTitle.tStart = t  # local t and not account for scr refresh
        languageSpanishOralTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishOralTextTitle, 'tStartRefresh')  # time at next scr refresh
        languageSpanishOralTextTitle.setAutoDraw(True)
    
    # *languageSpanishOralText* updates
    if languageSpanishOralText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishOralText.frameNStart = frameN  # exact frame index
        languageSpanishOralText.tStart = t  # local t and not account for scr refresh
        languageSpanishOralText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishOralText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishOralText.setAutoDraw(True)
    
    # *languageSpanishOralTextNext* updates
    if languageSpanishOralTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishOralTextNext.frameNStart = frameN  # exact frame index
        languageSpanishOralTextNext.tStart = t  # local t and not account for scr refresh
        languageSpanishOralTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishOralTextNext, 'tStartRefresh')  # time at next scr refresh
        languageSpanishOralTextNext.setAutoDraw(True)
    
    # *languageSpanishOralKey* updates
    waitOnFlip = False
    if languageSpanishOralKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishOralKey.frameNStart = frameN  # exact frame index
        languageSpanishOralKey.tStart = t  # local t and not account for scr refresh
        languageSpanishOralKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishOralKey, 'tStartRefresh')  # time at next scr refresh
        languageSpanishOralKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(languageSpanishOralKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(languageSpanishOralKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if languageSpanishOralKey.status == STARTED and not waitOnFlip:
        theseKeys = languageSpanishOralKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _languageSpanishOralKey_allKeys.extend(theseKeys)
        if len(_languageSpanishOralKey_allKeys):
            languageSpanishOralKey.keys = _languageSpanishOralKey_allKeys[-1].name  # just the last key pressed
            languageSpanishOralKey.rt = _languageSpanishOralKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if Spanish is L2 or L3, skip
    if (languageL2value=="SPANISH" or languageL3value=="SPANISH"):
        continueRoutine = False
    
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageSpanishOralComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageSpanishOral"-------
for thisComponent in languageSpanishOralComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if languageSpanishOralKey.keys in ['', [], None]:  # No response was made
    languageSpanishOralKey.keys = None
thisExp.addData('languageSpanishOralKey.keys',languageSpanishOralKey.keys)
if languageSpanishOralKey.keys != None:  # we had a response
    thisExp.addData('languageSpanishOralKey.rt', languageSpanishOralKey.rt)
thisExp.nextEntry()
# the Routine "languageSpanishOral" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageSpanishWritten"-------
continueRoutine = True
# update component parameters for each repeat
languageSpanishWrittenKey.keys = []
languageSpanishWrittenKey.rt = []
_languageSpanishWrittenKey_allKeys = []
# keep track of which components have finished
languageSpanishWrittenComponents = [languageSpanishWrittenTextTitle, languageSpanishWrittenText, languageSpanishWrittenTextNext, languageSpanishWrittenKey]
for thisComponent in languageSpanishWrittenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageSpanishWrittenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageSpanishWritten"-------
while continueRoutine:
    # get current time
    t = languageSpanishWrittenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageSpanishWrittenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageSpanishWrittenTextTitle* updates
    if languageSpanishWrittenTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishWrittenTextTitle.frameNStart = frameN  # exact frame index
        languageSpanishWrittenTextTitle.tStart = t  # local t and not account for scr refresh
        languageSpanishWrittenTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishWrittenTextTitle, 'tStartRefresh')  # time at next scr refresh
        languageSpanishWrittenTextTitle.setAutoDraw(True)
    
    # *languageSpanishWrittenText* updates
    if languageSpanishWrittenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishWrittenText.frameNStart = frameN  # exact frame index
        languageSpanishWrittenText.tStart = t  # local t and not account for scr refresh
        languageSpanishWrittenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishWrittenText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishWrittenText.setAutoDraw(True)
    
    # *languageSpanishWrittenTextNext* updates
    if languageSpanishWrittenTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishWrittenTextNext.frameNStart = frameN  # exact frame index
        languageSpanishWrittenTextNext.tStart = t  # local t and not account for scr refresh
        languageSpanishWrittenTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishWrittenTextNext, 'tStartRefresh')  # time at next scr refresh
        languageSpanishWrittenTextNext.setAutoDraw(True)
    
    # *languageSpanishWrittenKey* updates
    waitOnFlip = False
    if languageSpanishWrittenKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishWrittenKey.frameNStart = frameN  # exact frame index
        languageSpanishWrittenKey.tStart = t  # local t and not account for scr refresh
        languageSpanishWrittenKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishWrittenKey, 'tStartRefresh')  # time at next scr refresh
        languageSpanishWrittenKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(languageSpanishWrittenKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(languageSpanishWrittenKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if languageSpanishWrittenKey.status == STARTED and not waitOnFlip:
        theseKeys = languageSpanishWrittenKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _languageSpanishWrittenKey_allKeys.extend(theseKeys)
        if len(_languageSpanishWrittenKey_allKeys):
            languageSpanishWrittenKey.keys = _languageSpanishWrittenKey_allKeys[-1].name  # just the last key pressed
            languageSpanishWrittenKey.rt = _languageSpanishWrittenKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if Spanish is L2 or L3, skip
    if (languageL2value=="SPANISH" or languageL3value=="SPANISH"):
        continueRoutine = False
    
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageSpanishWrittenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageSpanishWritten"-------
for thisComponent in languageSpanishWrittenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if languageSpanishWrittenKey.keys in ['', [], None]:  # No response was made
    languageSpanishWrittenKey.keys = None
thisExp.addData('languageSpanishWrittenKey.keys',languageSpanishWrittenKey.keys)
if languageSpanishWrittenKey.keys != None:  # we had a response
    thisExp.addData('languageSpanishWrittenKey.rt', languageSpanishWrittenKey.rt)
thisExp.nextEntry()
# the Routine "languageSpanishWritten" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageSpanishTime"-------
continueRoutine = True
# update component parameters for each repeat
languageSpanishTimeKey.keys = []
languageSpanishTimeKey.rt = []
_languageSpanishTimeKey_allKeys = []
# keep track of which components have finished
languageSpanishTimeComponents = [languageSpanishTimeTextTitle, languageSpanishTimeText, languageSpanishTimeTextNext, languageSpanishTimeKey]
for thisComponent in languageSpanishTimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
languageSpanishTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "languageSpanishTime"-------
while continueRoutine:
    # get current time
    t = languageSpanishTimeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=languageSpanishTimeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *languageSpanishTimeTextTitle* updates
    if languageSpanishTimeTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishTimeTextTitle.frameNStart = frameN  # exact frame index
        languageSpanishTimeTextTitle.tStart = t  # local t and not account for scr refresh
        languageSpanishTimeTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishTimeTextTitle, 'tStartRefresh')  # time at next scr refresh
        languageSpanishTimeTextTitle.setAutoDraw(True)
    
    # *languageSpanishTimeText* updates
    if languageSpanishTimeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishTimeText.frameNStart = frameN  # exact frame index
        languageSpanishTimeText.tStart = t  # local t and not account for scr refresh
        languageSpanishTimeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishTimeText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishTimeText.setAutoDraw(True)
    
    # *languageSpanishTimeTextNext* updates
    if languageSpanishTimeTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishTimeTextNext.frameNStart = frameN  # exact frame index
        languageSpanishTimeTextNext.tStart = t  # local t and not account for scr refresh
        languageSpanishTimeTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishTimeTextNext, 'tStartRefresh')  # time at next scr refresh
        languageSpanishTimeTextNext.setAutoDraw(True)
    
    # *languageSpanishTimeKey* updates
    waitOnFlip = False
    if languageSpanishTimeKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishTimeKey.frameNStart = frameN  # exact frame index
        languageSpanishTimeKey.tStart = t  # local t and not account for scr refresh
        languageSpanishTimeKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishTimeKey, 'tStartRefresh')  # time at next scr refresh
        languageSpanishTimeKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(languageSpanishTimeKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(languageSpanishTimeKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if languageSpanishTimeKey.status == STARTED and not waitOnFlip:
        theseKeys = languageSpanishTimeKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _languageSpanishTimeKey_allKeys.extend(theseKeys)
        if len(_languageSpanishTimeKey_allKeys):
            languageSpanishTimeKey.keys = _languageSpanishTimeKey_allKeys[-1].name  # just the last key pressed
            languageSpanishTimeKey.rt = _languageSpanishTimeKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if Spanish is L2 or L3, skip
    if (languageL2value=="SPANISH" or languageL3value=="SPANISH"):
        continueRoutine = False
    
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in languageSpanishTimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "languageSpanishTime"-------
for thisComponent in languageSpanishTimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if languageSpanishTimeKey.keys in ['', [], None]:  # No response was made
    languageSpanishTimeKey.keys = None
thisExp.addData('languageSpanishTimeKey.keys',languageSpanishTimeKey.keys)
if languageSpanishTimeKey.keys != None:  # we had a response
    thisExp.addData('languageSpanishTimeKey.rt', languageSpanishTimeKey.rt)
thisExp.nextEntry()
# the Routine "languageSpanishTime" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoAge"-------
continueRoutine = True
# update component parameters for each repeat
psychopy.event.clearEvents()
inputText = ''
isAccented = False

# keep track of which components have finished
demoAgeComponents = [demoAgeTextTitle, demoAgeText, demoAgeTextNext, demoAgeTextInput]
for thisComponent in demoAgeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demoAgeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demoAge"-------
while continueRoutine:
    # get current time
    t = demoAgeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demoAgeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demoAgeTextTitle* updates
    if demoAgeTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoAgeTextTitle.frameNStart = frameN  # exact frame index
        demoAgeTextTitle.tStart = t  # local t and not account for scr refresh
        demoAgeTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoAgeTextTitle, 'tStartRefresh')  # time at next scr refresh
        demoAgeTextTitle.setAutoDraw(True)
    
    # *demoAgeText* updates
    if demoAgeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoAgeText.frameNStart = frameN  # exact frame index
        demoAgeText.tStart = t  # local t and not account for scr refresh
        demoAgeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoAgeText, 'tStartRefresh')  # time at next scr refresh
        demoAgeText.setAutoDraw(True)
    
    # *demoAgeTextNext* updates
    if demoAgeTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoAgeTextNext.frameNStart = frameN  # exact frame index
        demoAgeTextNext.tStart = t  # local t and not account for scr refresh
        demoAgeTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoAgeTextNext, 'tStartRefresh')  # time at next scr refresh
        demoAgeTextNext.setAutoDraw(True)
    
    # *demoAgeTextInput* updates
    if demoAgeTextInput.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoAgeTextInput.frameNStart = frameN  # exact frame index
        demoAgeTextInput.tStart = t  # local t and not account for scr refresh
        demoAgeTextInput.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoAgeTextInput, 'tStartRefresh')  # time at next scr refresh
        demoAgeTextInput.setAutoDraw(True)
    if demoAgeTextInput.status == STARTED:  # only update if drawing
        demoAgeTextInput.setText('> ' + inputText, log=False)
    keys = event.getKeys(keylist:['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'escape', 'backspace', 'return'])
    i = 0 # index whether how many keys have been previously pressed
    
    # Keys are mapped onto a Spanish keyboard
    
    if len(keys): # if any key has been pressed...
    
         # ... and ESCAPE is pressed, quit experiment
        if keys[i]=='escape':
            age = inputText
            thisExp.addData('age', inputText) # save data
            core.quit()
            # ... and RETURN is pressed, stop trial
        elif (keys[i]=='return'):
            if (inputText != ''):
                language2 = inputText
                thisExp.addData('age', inputText) # save data
                continueRoutine = False 
        # ... and BACKSPACE is pressed, delete last character
        elif (keys[i]=='backspace'):
            inputText = inputText[:-1]
        else:
            # write key as it is (in capital letters)
            inputText += keys[i].upper()
            thisExp.addData('age', inputText) # save data
            i = i + 1 # index another key press
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoAgeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoAge"-------
for thisComponent in demoAgeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
print(age)
# the Routine "demoAge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoSex"-------
continueRoutine = True
# update component parameters for each repeat
demoSexKey.keys = []
demoSexKey.rt = []
_demoSexKey_allKeys = []


# keep track of which components have finished
demoSexComponents = [demoSexTextTitle, demoSexText, demoSexTextNext, demoSexKey]
for thisComponent in demoSexComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demoSexClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demoSex"-------
while continueRoutine:
    # get current time
    t = demoSexClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demoSexClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demoSexTextTitle* updates
    if demoSexTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoSexTextTitle.frameNStart = frameN  # exact frame index
        demoSexTextTitle.tStart = t  # local t and not account for scr refresh
        demoSexTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoSexTextTitle, 'tStartRefresh')  # time at next scr refresh
        demoSexTextTitle.setAutoDraw(True)
    
    # *demoSexText* updates
    if demoSexText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoSexText.frameNStart = frameN  # exact frame index
        demoSexText.tStart = t  # local t and not account for scr refresh
        demoSexText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoSexText, 'tStartRefresh')  # time at next scr refresh
        demoSexText.setAutoDraw(True)
    
    # *demoSexTextNext* updates
    if demoSexTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoSexTextNext.frameNStart = frameN  # exact frame index
        demoSexTextNext.tStart = t  # local t and not account for scr refresh
        demoSexTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoSexTextNext, 'tStartRefresh')  # time at next scr refresh
        demoSexTextNext.setAutoDraw(True)
    
    # *demoSexKey* updates
    waitOnFlip = False
    if demoSexKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoSexKey.frameNStart = frameN  # exact frame index
        demoSexKey.tStart = t  # local t and not account for scr refresh
        demoSexKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoSexKey, 'tStartRefresh')  # time at next scr refresh
        demoSexKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demoSexKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demoSexKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demoSexKey.status == STARTED and not waitOnFlip:
        theseKeys = demoSexKey.getKeys(keyList=['m', 'f', 'o', 'escape'], waitRelease=False)
        _demoSexKey_allKeys.extend(theseKeys)
        if len(_demoSexKey_allKeys):
            demoSexKey.keys = _demoSexKey_allKeys[-1].name  # just the last key pressed
            demoSexKey.rt = _demoSexKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoSexComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoSex"-------
for thisComponent in demoSexComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if demoSexKey.keys in ['', [], None]:  # No response was made
    demoSexKey.keys = None
thisExp.addData('demoSexKey.keys',demoSexKey.keys)
if demoSexKey.keys != None:  # we had a response
    thisExp.addData('demoSexKey.rt', demoSexKey.rt)
thisExp.nextEntry()
# the Routine "demoSex" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoEducation"-------
continueRoutine = True
# update component parameters for each repeat
demoEducationKey.keys = []
demoEducationKey.rt = []
_demoEducationKey_allKeys = []


# keep track of which components have finished
demoEducationComponents = [demoEducationTextTitle, demoEducationText, demoEducationTextNext, demoEducationKey]
for thisComponent in demoEducationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demoEducationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demoEducation"-------
while continueRoutine:
    # get current time
    t = demoEducationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demoEducationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demoEducationTextTitle* updates
    if demoEducationTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoEducationTextTitle.frameNStart = frameN  # exact frame index
        demoEducationTextTitle.tStart = t  # local t and not account for scr refresh
        demoEducationTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoEducationTextTitle, 'tStartRefresh')  # time at next scr refresh
        demoEducationTextTitle.setAutoDraw(True)
    
    # *demoEducationText* updates
    if demoEducationText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoEducationText.frameNStart = frameN  # exact frame index
        demoEducationText.tStart = t  # local t and not account for scr refresh
        demoEducationText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoEducationText, 'tStartRefresh')  # time at next scr refresh
        demoEducationText.setAutoDraw(True)
    
    # *demoEducationTextNext* updates
    if demoEducationTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoEducationTextNext.frameNStart = frameN  # exact frame index
        demoEducationTextNext.tStart = t  # local t and not account for scr refresh
        demoEducationTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoEducationTextNext, 'tStartRefresh')  # time at next scr refresh
        demoEducationTextNext.setAutoDraw(True)
    
    # *demoEducationKey* updates
    waitOnFlip = False
    if demoEducationKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoEducationKey.frameNStart = frameN  # exact frame index
        demoEducationKey.tStart = t  # local t and not account for scr refresh
        demoEducationKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoEducationKey, 'tStartRefresh')  # time at next scr refresh
        demoEducationKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demoEducationKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demoEducationKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demoEducationKey.status == STARTED and not waitOnFlip:
        theseKeys = demoEducationKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _demoEducationKey_allKeys.extend(theseKeys)
        if len(_demoEducationKey_allKeys):
            demoEducationKey.keys = _demoEducationKey_allKeys[-1].name  # just the last key pressed
            demoEducationKey.rt = _demoEducationKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoEducationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoEducation"-------
for thisComponent in demoEducationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if demoEducationKey.keys in ['', [], None]:  # No response was made
    demoEducationKey.keys = None
thisExp.addData('demoEducationKey.keys',demoEducationKey.keys)
if demoEducationKey.keys != None:  # we had a response
    thisExp.addData('demoEducationKey.rt', demoEducationKey.rt)
thisExp.nextEntry()
# the Routine "demoEducation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoCity"-------
continueRoutine = True
# update component parameters for each repeat
psychopy.event.clearEvents()
inputText = ''
isAccented = False
# keep track of which components have finished
demoCityComponents = [demoCityTextTitle, demoCityText, demoCityTextNext, demoCityTextInput]
for thisComponent in demoCityComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demoCityClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demoCity"-------
while continueRoutine:
    # get current time
    t = demoCityClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demoCityClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demoCityTextTitle* updates
    if demoCityTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoCityTextTitle.frameNStart = frameN  # exact frame index
        demoCityTextTitle.tStart = t  # local t and not account for scr refresh
        demoCityTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoCityTextTitle, 'tStartRefresh')  # time at next scr refresh
        demoCityTextTitle.setAutoDraw(True)
    
    # *demoCityText* updates
    if demoCityText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoCityText.frameNStart = frameN  # exact frame index
        demoCityText.tStart = t  # local t and not account for scr refresh
        demoCityText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoCityText, 'tStartRefresh')  # time at next scr refresh
        demoCityText.setAutoDraw(True)
    
    # *demoCityTextNext* updates
    if demoCityTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoCityTextNext.frameNStart = frameN  # exact frame index
        demoCityTextNext.tStart = t  # local t and not account for scr refresh
        demoCityTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoCityTextNext, 'tStartRefresh')  # time at next scr refresh
        demoCityTextNext.setAutoDraw(True)
    
    # *demoCityTextInput* updates
    if demoCityTextInput.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoCityTextInput.frameNStart = frameN  # exact frame index
        demoCityTextInput.tStart = t  # local t and not account for scr refresh
        demoCityTextInput.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoCityTextInput, 'tStartRefresh')  # time at next scr refresh
        demoCityTextInput.setAutoDraw(True)
    if demoCityTextInput.status == STARTED:  # only update if drawing
        demoCityTextInput.setText('> ' + inputText, log=False)
    keys = event.getKeys(keyList = letterKeysAllowed)
    i = 0 # index whether how many keys have been previously pressed
    
    if len(keys): # if any key has been pressed...
    
         # ... and ESCAPE is pressed, quit experiment
        if keys[i]=='escape':
            thisExp.addData('city', inputText) # save data
            core.quit()
        # ... and RETURN is pressed, stop trial
        elif (keys[i]=='return'):
            if (inputText!=''):
                thisExp.addData('city', inputText) # save data
                continueRoutine = False
        # ... and BACKSPACE is pressed, delete last character
        elif (keys[i]=='backspace'):
            inputText = inputText[:-1]
        # and 'apostrophe' is pressed, flag accent
        elif (keys[i]=='apostrophe'):
            textInput += "'"
            thisExp.addData('city', inputText) # save data
            i = i + 1 # index another key press
    
        else:
            # write key as it is (in capital letters)
            inputText += keys[i].upper()
            thisExp.addData('city', inputText) # save data
            i = i + 1 # index another key press
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoCityComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoCity"-------
for thisComponent in demoCityComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "demoCity" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoVision"-------
continueRoutine = True
# update component parameters for each repeat
demoVisionKey.keys = []
demoVisionKey.rt = []
_demoVisionKey_allKeys = []


# keep track of which components have finished
demoVisionComponents = [demoVisionTextTitle, demoVisionText, demoVisionTextNext, demoVisionKey]
for thisComponent in demoVisionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demoVisionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demoVision"-------
while continueRoutine:
    # get current time
    t = demoVisionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demoVisionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demoVisionTextTitle* updates
    if demoVisionTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoVisionTextTitle.frameNStart = frameN  # exact frame index
        demoVisionTextTitle.tStart = t  # local t and not account for scr refresh
        demoVisionTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoVisionTextTitle, 'tStartRefresh')  # time at next scr refresh
        demoVisionTextTitle.setAutoDraw(True)
    
    # *demoVisionText* updates
    if demoVisionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoVisionText.frameNStart = frameN  # exact frame index
        demoVisionText.tStart = t  # local t and not account for scr refresh
        demoVisionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoVisionText, 'tStartRefresh')  # time at next scr refresh
        demoVisionText.setAutoDraw(True)
    
    # *demoVisionTextNext* updates
    if demoVisionTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoVisionTextNext.frameNStart = frameN  # exact frame index
        demoVisionTextNext.tStart = t  # local t and not account for scr refresh
        demoVisionTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoVisionTextNext, 'tStartRefresh')  # time at next scr refresh
        demoVisionTextNext.setAutoDraw(True)
    
    # *demoVisionKey* updates
    waitOnFlip = False
    if demoVisionKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoVisionKey.frameNStart = frameN  # exact frame index
        demoVisionKey.tStart = t  # local t and not account for scr refresh
        demoVisionKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoVisionKey, 'tStartRefresh')  # time at next scr refresh
        demoVisionKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demoVisionKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demoVisionKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demoVisionKey.status == STARTED and not waitOnFlip:
        theseKeys = demoVisionKey.getKeys(keyList=['y', 'n', 'escape'], waitRelease=False)
        _demoVisionKey_allKeys.extend(theseKeys)
        if len(_demoVisionKey_allKeys):
            demoVisionKey.keys = _demoVisionKey_allKeys[-1].name  # just the last key pressed
            demoVisionKey.rt = _demoVisionKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoVisionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoVision"-------
for thisComponent in demoVisionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if demoVisionKey.keys in ['', [], None]:  # No response was made
    demoVisionKey.keys = None
thisExp.addData('demoVisionKey.keys',demoVisionKey.keys)
if demoVisionKey.keys != None:  # we had a response
    thisExp.addData('demoVisionKey.rt', demoVisionKey.rt)
thisExp.nextEntry()
# the Routine "demoVision" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoLanguage"-------
continueRoutine = True
# update component parameters for each repeat
demoLanguageKey.keys = []
demoLanguageKey.rt = []
_demoLanguageKey_allKeys = []


# keep track of which components have finished
demoLanguageComponents = [demoLanguageTextTitle, demoLanguageText, demoLanguageTextNext, demoLanguageKey]
for thisComponent in demoLanguageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demoLanguageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demoLanguage"-------
while continueRoutine:
    # get current time
    t = demoLanguageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demoLanguageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demoLanguageTextTitle* updates
    if demoLanguageTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoLanguageTextTitle.frameNStart = frameN  # exact frame index
        demoLanguageTextTitle.tStart = t  # local t and not account for scr refresh
        demoLanguageTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoLanguageTextTitle, 'tStartRefresh')  # time at next scr refresh
        demoLanguageTextTitle.setAutoDraw(True)
    
    # *demoLanguageText* updates
    if demoLanguageText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoLanguageText.frameNStart = frameN  # exact frame index
        demoLanguageText.tStart = t  # local t and not account for scr refresh
        demoLanguageText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoLanguageText, 'tStartRefresh')  # time at next scr refresh
        demoLanguageText.setAutoDraw(True)
    
    # *demoLanguageTextNext* updates
    if demoLanguageTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoLanguageTextNext.frameNStart = frameN  # exact frame index
        demoLanguageTextNext.tStart = t  # local t and not account for scr refresh
        demoLanguageTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoLanguageTextNext, 'tStartRefresh')  # time at next scr refresh
        demoLanguageTextNext.setAutoDraw(True)
    
    # *demoLanguageKey* updates
    waitOnFlip = False
    if demoLanguageKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoLanguageKey.frameNStart = frameN  # exact frame index
        demoLanguageKey.tStart = t  # local t and not account for scr refresh
        demoLanguageKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoLanguageKey, 'tStartRefresh')  # time at next scr refresh
        demoLanguageKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demoLanguageKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demoLanguageKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demoLanguageKey.status == STARTED and not waitOnFlip:
        theseKeys = demoLanguageKey.getKeys(keyList=['y', 'n', 'escape'], waitRelease=False)
        _demoLanguageKey_allKeys.extend(theseKeys)
        if len(_demoLanguageKey_allKeys):
            demoLanguageKey.keys = _demoLanguageKey_allKeys[-1].name  # just the last key pressed
            demoLanguageKey.rt = _demoLanguageKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoLanguageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoLanguage"-------
for thisComponent in demoLanguageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if demoLanguageKey.keys in ['', [], None]:  # No response was made
    demoLanguageKey.keys = None
thisExp.addData('demoLanguageKey.keys',demoLanguageKey.keys)
if demoLanguageKey.keys != None:  # we had a response
    thisExp.addData('demoLanguageKey.rt', demoLanguageKey.rt)
thisExp.nextEntry()
# the Routine "demoLanguage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "setupLocation"-------
continueRoutine = True
# update component parameters for each repeat
setupLocationKey.keys = []
setupLocationKey.rt = []
_setupLocationKey_allKeys = []


# keep track of which components have finished
setupLocationComponents = [setupLocationTextTitle, setupLocationText, setupLocationTextNext, setupLocationKey]
for thisComponent in setupLocationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupLocationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setupLocation"-------
while continueRoutine:
    # get current time
    t = setupLocationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupLocationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *setupLocationTextTitle* updates
    if setupLocationTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupLocationTextTitle.frameNStart = frameN  # exact frame index
        setupLocationTextTitle.tStart = t  # local t and not account for scr refresh
        setupLocationTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupLocationTextTitle, 'tStartRefresh')  # time at next scr refresh
        setupLocationTextTitle.setAutoDraw(True)
    
    # *setupLocationText* updates
    if setupLocationText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupLocationText.frameNStart = frameN  # exact frame index
        setupLocationText.tStart = t  # local t and not account for scr refresh
        setupLocationText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupLocationText, 'tStartRefresh')  # time at next scr refresh
        setupLocationText.setAutoDraw(True)
    
    # *setupLocationTextNext* updates
    if setupLocationTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupLocationTextNext.frameNStart = frameN  # exact frame index
        setupLocationTextNext.tStart = t  # local t and not account for scr refresh
        setupLocationTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupLocationTextNext, 'tStartRefresh')  # time at next scr refresh
        setupLocationTextNext.setAutoDraw(True)
    
    # *setupLocationKey* updates
    waitOnFlip = False
    if setupLocationKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupLocationKey.frameNStart = frameN  # exact frame index
        setupLocationKey.tStart = t  # local t and not account for scr refresh
        setupLocationKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupLocationKey, 'tStartRefresh')  # time at next scr refresh
        setupLocationKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(setupLocationKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(setupLocationKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if setupLocationKey.status == STARTED and not waitOnFlip:
        theseKeys = setupLocationKey.getKeys(keyList=['1', '2', '3', '4', '5', 'escape'], waitRelease=False)
        _setupLocationKey_allKeys.extend(theseKeys)
        if len(_setupLocationKey_allKeys):
            setupLocationKey.keys = _setupLocationKey_allKeys[-1].name  # just the last key pressed
            setupLocationKey.rt = _setupLocationKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupLocationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setupLocation"-------
for thisComponent in setupLocationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if setupLocationKey.keys in ['', [], None]:  # No response was made
    setupLocationKey.keys = None
thisExp.addData('setupLocationKey.keys',setupLocationKey.keys)
if setupLocationKey.keys != None:  # we had a response
    thisExp.addData('setupLocationKey.rt', setupLocationKey.rt)
thisExp.nextEntry()
# the Routine "setupLocation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "setupNoise"-------
continueRoutine = True
# update component parameters for each repeat
setupNoiseKey.keys = []
setupNoiseKey.rt = []
_setupNoiseKey_allKeys = []


# keep track of which components have finished
setupNoiseComponents = [setupNoiseTextTitle, setupNoiseText, setupNoiseTextNext, setupNoiseKey]
for thisComponent in setupNoiseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupNoiseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setupNoise"-------
while continueRoutine:
    # get current time
    t = setupNoiseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupNoiseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *setupNoiseTextTitle* updates
    if setupNoiseTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupNoiseTextTitle.frameNStart = frameN  # exact frame index
        setupNoiseTextTitle.tStart = t  # local t and not account for scr refresh
        setupNoiseTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupNoiseTextTitle, 'tStartRefresh')  # time at next scr refresh
        setupNoiseTextTitle.setAutoDraw(True)
    
    # *setupNoiseText* updates
    if setupNoiseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupNoiseText.frameNStart = frameN  # exact frame index
        setupNoiseText.tStart = t  # local t and not account for scr refresh
        setupNoiseText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupNoiseText, 'tStartRefresh')  # time at next scr refresh
        setupNoiseText.setAutoDraw(True)
    
    # *setupNoiseTextNext* updates
    if setupNoiseTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupNoiseTextNext.frameNStart = frameN  # exact frame index
        setupNoiseTextNext.tStart = t  # local t and not account for scr refresh
        setupNoiseTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupNoiseTextNext, 'tStartRefresh')  # time at next scr refresh
        setupNoiseTextNext.setAutoDraw(True)
    
    # *setupNoiseKey* updates
    waitOnFlip = False
    if setupNoiseKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupNoiseKey.frameNStart = frameN  # exact frame index
        setupNoiseKey.tStart = t  # local t and not account for scr refresh
        setupNoiseKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupNoiseKey, 'tStartRefresh')  # time at next scr refresh
        setupNoiseKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(setupNoiseKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(setupNoiseKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if setupNoiseKey.status == STARTED and not waitOnFlip:
        theseKeys = setupNoiseKey.getKeys(keyList=['1', '2', '3', '4', 'escape'], waitRelease=False)
        _setupNoiseKey_allKeys.extend(theseKeys)
        if len(_setupNoiseKey_allKeys):
            setupNoiseKey.keys = _setupNoiseKey_allKeys[-1].name  # just the last key pressed
            setupNoiseKey.rt = _setupNoiseKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupNoiseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setupNoise"-------
for thisComponent in setupNoiseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if setupNoiseKey.keys in ['', [], None]:  # No response was made
    setupNoiseKey.keys = None
thisExp.addData('setupNoiseKey.keys',setupNoiseKey.keys)
if setupNoiseKey.keys != None:  # we had a response
    thisExp.addData('setupNoiseKey.rt', setupNoiseKey.rt)
thisExp.nextEntry()
# the Routine "setupNoise" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
instructionsKeys.keys = []
instructionsKeys.rt = []
_instructionsKeys_allKeys = []
# keep track of which components have finished
instructionsComponents = [instructionsTextTitle, instructionsText, instructionsTextNext, instructionsKeys]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionsTextTitle* updates
    if instructionsTextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionsTextTitle.frameNStart = frameN  # exact frame index
        instructionsTextTitle.tStart = t  # local t and not account for scr refresh
        instructionsTextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsTextTitle, 'tStartRefresh')  # time at next scr refresh
        instructionsTextTitle.setAutoDraw(True)
    
    # *instructionsText* updates
    if instructionsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionsText.frameNStart = frameN  # exact frame index
        instructionsText.tStart = t  # local t and not account for scr refresh
        instructionsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsText, 'tStartRefresh')  # time at next scr refresh
        instructionsText.setAutoDraw(True)
    
    # *instructionsTextNext* updates
    if instructionsTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionsTextNext.frameNStart = frameN  # exact frame index
        instructionsTextNext.tStart = t  # local t and not account for scr refresh
        instructionsTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsTextNext, 'tStartRefresh')  # time at next scr refresh
        instructionsTextNext.setAutoDraw(True)
    
    # *instructionsKeys* updates
    waitOnFlip = False
    if instructionsKeys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionsKeys.frameNStart = frameN  # exact frame index
        instructionsKeys.tStart = t  # local t and not account for scr refresh
        instructionsKeys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsKeys, 'tStartRefresh')  # time at next scr refresh
        instructionsKeys.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructionsKeys.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructionsKeys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructionsKeys.status == STARTED and not waitOnFlip:
        theseKeys = instructionsKeys.getKeys(keyList=['space', 'escape'], waitRelease=False)
        _instructionsKeys_allKeys.extend(theseKeys)
        if len(_instructionsKeys_allKeys):
            instructionsKeys.keys = _instructionsKeys_allKeys[-1].name  # just the last key pressed
            instructionsKeys.rt = _instructionsKeys_allKeys[-1].rt
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instructionsKeys.keys in ['', [], None]:  # No response was made
    instructionsKeys.keys = None
thisExp.addData('instructionsKeys.keys',instructionsKeys.keys)
if instructionsKeys.keys != None:  # we had a response
    thisExp.addData('instructionsKeys.rt', instructionsKeys.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions2"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
instructions2Components = [instructions2TextTitle, instructions2Text, instructions2TextNext]
for thisComponent in instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions2TextTitle* updates
    if instructions2TextTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2TextTitle.frameNStart = frameN  # exact frame index
        instructions2TextTitle.tStart = t  # local t and not account for scr refresh
        instructions2TextTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2TextTitle, 'tStartRefresh')  # time at next scr refresh
        instructions2TextTitle.setAutoDraw(True)
    
    # *instructions2Text* updates
    if instructions2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2Text.frameNStart = frameN  # exact frame index
        instructions2Text.tStart = t  # local t and not account for scr refresh
        instructions2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2Text, 'tStartRefresh')  # time at next scr refresh
        instructions2Text.setAutoDraw(True)
    
    # *instructions2TextNext* updates
    if instructions2TextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2TextNext.frameNStart = frameN  # exact frame index
        instructions2TextNext.tStart = t  # local t and not account for scr refresh
        instructions2TextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2TextNext, 'tStartRefresh')  # time at next scr refresh
        instructions2TextNext.setAutoDraw(True)
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# randomise testing language (between-participant)
versions = ['catalan', 'spanish']
versionRandom = random.sample(['catalan', 'spanish'])
if (versionRandom=="catalan"):
    trialsPracticeCatalanReps = 1
    trialsPracticeSpanishReps = 0
    trialsPatalanReps = 1
    trialsPpanishReps = 0
else:
    trialsPracticeCatalanReps = 0
    trialsPracticeSpanishReps = 1
    trialsCatalanReps = 0
    trialsSpanishReps = 1
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsPracticeCatalan = data.TrialHandler(nReps=trialsPracticeCatalanReps, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials/01_trials_practice_catalan.xlsx'),
    seed=None, name='trialsPracticeCatalan')
thisExp.addLoop(trialsPracticeCatalan)  # add the loop to the experiment
thisTrialsPracticeCatalan = trialsPracticeCatalan.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeCatalan.rgb)
if thisTrialsPracticeCatalan != None:
    for paramName in thisTrialsPracticeCatalan:
        exec('{} = thisTrialsPracticeCatalan[paramName]'.format(paramName))

for thisTrialsPracticeCatalan in trialsPracticeCatalan:
    currentLoop = trialsPracticeCatalan
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeCatalan.rgb)
    if thisTrialsPracticeCatalan != None:
        for paramName in thisTrialsPracticeCatalan:
            exec('{} = thisTrialsPracticeCatalan[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixationText]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixationText* updates
        if fixationText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixationText.frameNStart = frameN  # exact frame index
            fixationText.tStart = t  # local t and not account for scr refresh
            fixationText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationText, 'tStartRefresh')  # time at next scr refresh
            fixationText.setAutoDraw(True)
        if fixationText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixationText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixationText.tStop = t  # not accounting for scr refresh
                fixationText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixationText, 'tStopRefresh')  # time at next scr refresh
                fixationText.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    trialSound.setSound(soundfile, hamming=True)
    trialSound.setVolume(1, log=False)
    keysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'apostrophe', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'escape', 'space', 'return', 'backspace']
    inputText = ''
    debugText = ''
    isAccented = False
    error = False
    keyPressTime = 0
    trialText.setText = ''
    
    # keep track of which components have finished
    trialComponents = [trialText, trialSound]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialText* updates
        if trialText.status == NOT_STARTED and trialSound.status==FINISHED:
            # keep track of start time/frame for later
            trialText.frameNStart = frameN  # exact frame index
            trialText.tStart = t  # local t and not account for scr refresh
            trialText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialText, 'tStartRefresh')  # time at next scr refresh
            trialText.setAutoDraw(True)
        if trialText.status == STARTED:  # only update if drawing
            trialText.setText('> ' + inputText, log=False)
        # start/stop trialSound
        if trialSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialSound.frameNStart = frameN  # exact frame index
            trialSound.tStart = t  # local t and not account for scr refresh
            trialSound.tStartRefresh = tThisFlipGlobal  # on global time
            trialSound.play(when=win)  # sync with win flip
        keys = event.getKeys(keyList = keysAllowed)
        
        i = 0
        
        if trialSound.status==FINISHED: # if audio has finished...
        
            if len(keys): # if a key has been pressed...
            
                if 'return' in keys[i]: # and it's 'return'
                    thisExp.addData('trialOffset', t) # save time
                    thisExp.addData('keyPressTime', t) # save time
                    continueRoutine = False
                
                elif 'escape' in keys[i]: # and it's 'escape'...
                    thisExp.addData('trialOffset', t) # save time
                    core.quit()  # exit
                
                elif keys[i]=='space': # and it's 'space'...
                    inputText = inputText + ' ' # add a space
                
                elif keys[i] == 'backspace': # and it's 'backspace'
                    inputText = inputText[:-1]
                    keyPressTime = t # get time
                    error = True
                    inputText = inputText[:-1] # remove last character
                    
                elif 'apostrophe' in keys[i]: # and it's apostrophe
                    inputText += "'" # add apostrophe
                
                else:
                    inputText += keys[i].upper()
        
            # save data
                thisExp.addData('keyPressed', keys[i]) # save pressed key
                thisExp.addData('keyPressTime', t) # save time
                thisExp.addData('inputText', inputText) # save text
                thisExp.addData('error', error) # save time
                thisExp.nextEntry()
                i = i+1
        
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialSound.stop()  # ensure sound has stopped at end of routine
    trialsPracticeCatalan.addData('trialSound.started', trialSound.tStartRefresh)
    trialsPracticeCatalan.addData('trialSound.stopped', trialSound.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialsPracticeCatalanReps repeats of 'trialsPracticeCatalan'


# set up handler to look after randomisation of conditions etc
trialsPracticeSpanish = data.TrialHandler(nReps=trialsPracticeSpanishReps, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials/01_trials_practice_spanish.xlsx'),
    seed=None, name='trialsPracticeSpanish')
thisExp.addLoop(trialsPracticeSpanish)  # add the loop to the experiment
thisTrialsPracticeSpanish = trialsPracticeSpanish.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeSpanish.rgb)
if thisTrialsPracticeSpanish != None:
    for paramName in thisTrialsPracticeSpanish:
        exec('{} = thisTrialsPracticeSpanish[paramName]'.format(paramName))

for thisTrialsPracticeSpanish in trialsPracticeSpanish:
    currentLoop = trialsPracticeSpanish
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsPracticeSpanish.rgb)
    if thisTrialsPracticeSpanish != None:
        for paramName in thisTrialsPracticeSpanish:
            exec('{} = thisTrialsPracticeSpanish[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixationText]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixationText* updates
        if fixationText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixationText.frameNStart = frameN  # exact frame index
            fixationText.tStart = t  # local t and not account for scr refresh
            fixationText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationText, 'tStartRefresh')  # time at next scr refresh
            fixationText.setAutoDraw(True)
        if fixationText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixationText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixationText.tStop = t  # not accounting for scr refresh
                fixationText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixationText, 'tStopRefresh')  # time at next scr refresh
                fixationText.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    trialSound.setSound(soundfile, hamming=True)
    trialSound.setVolume(1, log=False)
    keysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'apostrophe', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'escape', 'space', 'return', 'backspace']
    inputText = ''
    debugText = ''
    isAccented = False
    error = False
    keyPressTime = 0
    trialText.setText = ''
    
    # keep track of which components have finished
    trialComponents = [trialText, trialSound]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialText* updates
        if trialText.status == NOT_STARTED and trialSound.status==FINISHED:
            # keep track of start time/frame for later
            trialText.frameNStart = frameN  # exact frame index
            trialText.tStart = t  # local t and not account for scr refresh
            trialText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialText, 'tStartRefresh')  # time at next scr refresh
            trialText.setAutoDraw(True)
        if trialText.status == STARTED:  # only update if drawing
            trialText.setText('> ' + inputText, log=False)
        # start/stop trialSound
        if trialSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialSound.frameNStart = frameN  # exact frame index
            trialSound.tStart = t  # local t and not account for scr refresh
            trialSound.tStartRefresh = tThisFlipGlobal  # on global time
            trialSound.play(when=win)  # sync with win flip
        keys = event.getKeys(keyList = keysAllowed)
        
        i = 0
        
        if trialSound.status==FINISHED: # if audio has finished...
        
            if len(keys): # if a key has been pressed...
            
                if 'return' in keys[i]: # and it's 'return'
                    thisExp.addData('trialOffset', t) # save time
                    thisExp.addData('keyPressTime', t) # save time
                    continueRoutine = False
                
                elif 'escape' in keys[i]: # and it's 'escape'...
                    thisExp.addData('trialOffset', t) # save time
                    core.quit()  # exit
                
                elif keys[i]=='space': # and it's 'space'...
                    inputText = inputText + ' ' # add a space
                
                elif keys[i] == 'backspace': # and it's 'backspace'
                    inputText = inputText[:-1]
                    keyPressTime = t # get time
                    error = True
                    inputText = inputText[:-1] # remove last character
                    
                elif 'apostrophe' in keys[i]: # and it's apostrophe
                    inputText += "'" # add apostrophe
                
                else:
                    inputText += keys[i].upper()
        
            # save data
                thisExp.addData('keyPressed', keys[i]) # save pressed key
                thisExp.addData('keyPressTime', t) # save time
                thisExp.addData('inputText', inputText) # save text
                thisExp.addData('error', error) # save time
                thisExp.nextEntry()
                i = i+1
        
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialSound.stop()  # ensure sound has stopped at end of routine
    trialsPracticeSpanish.addData('trialSound.started', trialSound.tStartRefresh)
    trialsPracticeSpanish.addData('trialSound.stopped', trialSound.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialsPracticeSpanishReps repeats of 'trialsPracticeSpanish'


# ------Prepare to start Routine "begin"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
beginComponents = [beginText, beginNext]
for thisComponent in beginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "begin"-------
while continueRoutine:
    # get current time
    t = beginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *beginText* updates
    if beginText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        beginText.frameNStart = frameN  # exact frame index
        beginText.tStart = t  # local t and not account for scr refresh
        beginText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(beginText, 'tStartRefresh')  # time at next scr refresh
        beginText.setAutoDraw(True)
    
    # *beginNext* updates
    if beginNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        beginNext.frameNStart = frameN  # exact frame index
        beginNext.tStart = t  # local t and not account for scr refresh
        beginNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(beginNext, 'tStartRefresh')  # time at next scr refresh
        beginNext.setAutoDraw(True)
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "begin"-------
for thisComponent in beginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialsCatalan = data.TrialHandler(nReps=trialsCatalanReps, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials/02_trials_catalan.xlsx'),
    seed=None, name='trialsCatalan')
thisExp.addLoop(trialsCatalan)  # add the loop to the experiment
thisTrialsCatalan = trialsCatalan.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsCatalan.rgb)
if thisTrialsCatalan != None:
    for paramName in thisTrialsCatalan:
        exec('{} = thisTrialsCatalan[paramName]'.format(paramName))

for thisTrialsCatalan in trialsCatalan:
    currentLoop = trialsCatalan
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsCatalan.rgb)
    if thisTrialsCatalan != None:
        for paramName in thisTrialsCatalan:
            exec('{} = thisTrialsCatalan[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixationText]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixationText* updates
        if fixationText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixationText.frameNStart = frameN  # exact frame index
            fixationText.tStart = t  # local t and not account for scr refresh
            fixationText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationText, 'tStartRefresh')  # time at next scr refresh
            fixationText.setAutoDraw(True)
        if fixationText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixationText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixationText.tStop = t  # not accounting for scr refresh
                fixationText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixationText, 'tStopRefresh')  # time at next scr refresh
                fixationText.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    trialSound.setSound(soundfile, hamming=True)
    trialSound.setVolume(1, log=False)
    keysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'apostrophe', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'escape', 'space', 'return', 'backspace']
    inputText = ''
    debugText = ''
    isAccented = False
    error = False
    keyPressTime = 0
    trialText.setText = ''
    
    # keep track of which components have finished
    trialComponents = [trialText, trialSound]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialText* updates
        if trialText.status == NOT_STARTED and trialSound.status==FINISHED:
            # keep track of start time/frame for later
            trialText.frameNStart = frameN  # exact frame index
            trialText.tStart = t  # local t and not account for scr refresh
            trialText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialText, 'tStartRefresh')  # time at next scr refresh
            trialText.setAutoDraw(True)
        if trialText.status == STARTED:  # only update if drawing
            trialText.setText('> ' + inputText, log=False)
        # start/stop trialSound
        if trialSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialSound.frameNStart = frameN  # exact frame index
            trialSound.tStart = t  # local t and not account for scr refresh
            trialSound.tStartRefresh = tThisFlipGlobal  # on global time
            trialSound.play(when=win)  # sync with win flip
        keys = event.getKeys(keyList = keysAllowed)
        
        i = 0
        
        if trialSound.status==FINISHED: # if audio has finished...
        
            if len(keys): # if a key has been pressed...
            
                if 'return' in keys[i]: # and it's 'return'
                    thisExp.addData('trialOffset', t) # save time
                    thisExp.addData('keyPressTime', t) # save time
                    continueRoutine = False
                
                elif 'escape' in keys[i]: # and it's 'escape'...
                    thisExp.addData('trialOffset', t) # save time
                    core.quit()  # exit
                
                elif keys[i]=='space': # and it's 'space'...
                    inputText = inputText + ' ' # add a space
                
                elif keys[i] == 'backspace': # and it's 'backspace'
                    inputText = inputText[:-1]
                    keyPressTime = t # get time
                    error = True
                    inputText = inputText[:-1] # remove last character
                    
                elif 'apostrophe' in keys[i]: # and it's apostrophe
                    inputText += "'" # add apostrophe
                
                else:
                    inputText += keys[i].upper()
        
            # save data
                thisExp.addData('keyPressed', keys[i]) # save pressed key
                thisExp.addData('keyPressTime', t) # save time
                thisExp.addData('inputText', inputText) # save text
                thisExp.addData('error', error) # save time
                thisExp.nextEntry()
                i = i+1
        
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialSound.stop()  # ensure sound has stopped at end of routine
    trialsCatalan.addData('trialSound.started', trialSound.tStartRefresh)
    trialsCatalan.addData('trialSound.stopped', trialSound.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialsCatalanReps repeats of 'trialsCatalan'


# set up handler to look after randomisation of conditions etc
trialsSpanish = data.TrialHandler(nReps=trialsSpanishReps, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials/02_trials_spanish.xlsx'),
    seed=None, name='trialsSpanish')
thisExp.addLoop(trialsSpanish)  # add the loop to the experiment
thisTrialsSpanish = trialsSpanish.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsSpanish.rgb)
if thisTrialsSpanish != None:
    for paramName in thisTrialsSpanish:
        exec('{} = thisTrialsSpanish[paramName]'.format(paramName))

for thisTrialsSpanish in trialsSpanish:
    currentLoop = trialsSpanish
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsSpanish.rgb)
    if thisTrialsSpanish != None:
        for paramName in thisTrialsSpanish:
            exec('{} = thisTrialsSpanish[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixationText]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixationText* updates
        if fixationText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixationText.frameNStart = frameN  # exact frame index
            fixationText.tStart = t  # local t and not account for scr refresh
            fixationText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationText, 'tStartRefresh')  # time at next scr refresh
            fixationText.setAutoDraw(True)
        if fixationText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixationText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixationText.tStop = t  # not accounting for scr refresh
                fixationText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixationText, 'tStopRefresh')  # time at next scr refresh
                fixationText.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    trialSound.setSound(soundfile, hamming=True)
    trialSound.setVolume(1, log=False)
    keysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'apostrophe', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'escape', 'space', 'return', 'backspace']
    inputText = ''
    debugText = ''
    isAccented = False
    error = False
    keyPressTime = 0
    trialText.setText = ''
    
    # keep track of which components have finished
    trialComponents = [trialText, trialSound]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trialText* updates
        if trialText.status == NOT_STARTED and trialSound.status==FINISHED:
            # keep track of start time/frame for later
            trialText.frameNStart = frameN  # exact frame index
            trialText.tStart = t  # local t and not account for scr refresh
            trialText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialText, 'tStartRefresh')  # time at next scr refresh
            trialText.setAutoDraw(True)
        if trialText.status == STARTED:  # only update if drawing
            trialText.setText('> ' + inputText, log=False)
        # start/stop trialSound
        if trialSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialSound.frameNStart = frameN  # exact frame index
            trialSound.tStart = t  # local t and not account for scr refresh
            trialSound.tStartRefresh = tThisFlipGlobal  # on global time
            trialSound.play(when=win)  # sync with win flip
        keys = event.getKeys(keyList = keysAllowed)
        
        i = 0
        
        if trialSound.status==FINISHED: # if audio has finished...
        
            if len(keys): # if a key has been pressed...
            
                if 'return' in keys[i]: # and it's 'return'
                    thisExp.addData('trialOffset', t) # save time
                    thisExp.addData('keyPressTime', t) # save time
                    continueRoutine = False
                
                elif 'escape' in keys[i]: # and it's 'escape'...
                    thisExp.addData('trialOffset', t) # save time
                    core.quit()  # exit
                
                elif keys[i]=='space': # and it's 'space'...
                    inputText = inputText + ' ' # add a space
                
                elif keys[i] == 'backspace': # and it's 'backspace'
                    inputText = inputText[:-1]
                    keyPressTime = t # get time
                    error = True
                    inputText = inputText[:-1] # remove last character
                    
                elif 'apostrophe' in keys[i]: # and it's apostrophe
                    inputText += "'" # add apostrophe
                
                else:
                    inputText += keys[i].upper()
        
            # save data
                thisExp.addData('keyPressed', keys[i]) # save pressed key
                thisExp.addData('keyPressTime', t) # save time
                thisExp.addData('inputText', inputText) # save text
                thisExp.addData('error', error) # save time
                thisExp.nextEntry()
                i = i+1
        
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialSound.stop()  # ensure sound has stopped at end of routine
    trialsSpanish.addData('trialSound.started', trialSound.tStartRefresh)
    trialsSpanish.addData('trialSound.stopped', trialSound.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed trialsSpanishReps repeats of 'trialsSpanish'


# ------Prepare to start Routine "farewell"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
farewellComponents = [farewellText, farewellTextNext, farewellTextID]
for thisComponent in farewellComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
farewellClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "farewell"-------
while continueRoutine:
    # get current time
    t = farewellClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=farewellClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *farewellText* updates
    if farewellText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        farewellText.frameNStart = frameN  # exact frame index
        farewellText.tStart = t  # local t and not account for scr refresh
        farewellText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(farewellText, 'tStartRefresh')  # time at next scr refresh
        farewellText.setAutoDraw(True)
    
    # *farewellTextNext* updates
    if farewellTextNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        farewellTextNext.frameNStart = frameN  # exact frame index
        farewellTextNext.tStart = t  # local t and not account for scr refresh
        farewellTextNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(farewellTextNext, 'tStartRefresh')  # time at next scr refresh
        farewellTextNext.setAutoDraw(True)
    
    # *farewellTextID* updates
    if farewellTextID.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        farewellTextID.frameNStart = frameN  # exact frame index
        farewellTextID.tStart = t  # local t and not account for scr refresh
        farewellTextID.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(farewellTextID, 'tStartRefresh')  # time at next scr refresh
        farewellTextID.setAutoDraw(True)
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in farewellComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "farewell"-------
for thisComponent in farewellComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "farewell" was not non-slip safe, so reset the non-slip timer
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
