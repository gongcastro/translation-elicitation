#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on May 06, 2022, at 11:11
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.1.3')


from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'sounddevice'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'translationelicitation_eng-confidence'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\u155880\\Documents\\translationelicitation_eng-confidence\\translationelicitation_eng-confidence_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.ERROR)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1200, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1, -1, -1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "setup"
setupClock = core.Clock()
setupTitleText = visual.TextStim(win=win, name='setupTitleText',
    text='SETUP',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
setupText = visual.TextStim(win=win, name='setupText',
    text='If possible, use Chrome or Mozilla Firefox\n\nUse a computer or a laptop (not a tablet or a phone)\n\nUse headphones \n\nClose all tabs other than this one\n\nDo not switch tabs in the browser\n\nIf, for any reason, you restart the study (e.g. because you reloaded the website or an internet failure), let us know by sending an email to serene.siow@psy.ox.ac.uk.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
setupNextText = visual.TextStim(win=win, name='setupNextText',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
setupNextKey = keyboard.Keyboard()
letterKeysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'return', 'backspace', 'escape', 'space']
inputText = ''
languageL2 = ''
languageL3 = ''




# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcomeTextTitle = visual.TextStim(win=win, name='welcomeTextTitle',
    text='WELCOME',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcomeText = visual.TextStim(win=win, name='welcomeText',
    text='This is a study designed by researchers from the Universitat Pompeu Fabra (Barcelona, Spain) and the University of Oxford (Oxford, UK). \n\nThe aim of the study is to investigate how toddlers and adults process foreign words. The audios you will listen to throughout this study were recorded in a baby-directed style.\n\nYou have been invited to participate as you are between 18 and 25 years old, and a English native speaker with no knowledge of Spanish or Catalan.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
welcomeNextText = visual.TextStim(win=win, name='welcomeNextText',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
welcomeNextKey = keyboard.Keyboard()

# Initialize components for Routine "description"
descriptionClock = core.Clock()
descriptionTitleText = visual.TextStim(win=win, name='descriptionTitleText',
    text='OVERVIEW',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
descriptionText = visual.TextStim(win=win, name='descriptionText',
    text='Firstly, you will be asked to complete a BRIEF QUESTIONNAIRE (your language profile, level of education, etc.).\n\nIn the main STUDY, you will listen to a series of SPANISH or CATALAN words. Your task will be to GUESS the TRANSLATION of each word in ENGLISH and TYPE your answer using the computer keyboard.\n\nThis should take around 30 minutes.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
descriptionNextText = visual.TextStim(win=win, name='descriptionNextText',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
descriptionNextKey = keyboard.Keyboard()

# Initialize components for Routine "voluntary"
voluntaryClock = core.Clock()
voluntaryTitleText = visual.TextStim(win=win, name='voluntaryTitleText',
    text='DO I HAVE TO TAKE PART?',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
voluntaryText = visual.TextStim(win=win, name='voluntaryText',
    text='Participation in this study is absolutely VOLUNTARY. If you do decide to take part, you may withdraw at any point for any reason by pressing the ESC button. However, we are only able to reimburse participants who complete the full task.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
voluntaryNextText = visual.TextStim(win=win, name='voluntaryNextText',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
voluntaryNextKey = keyboard.Keyboard()

# Initialize components for Routine "contact"
contactClock = core.Clock()
contactTitleText = visual.TextStim(win=win, name='contactTitleText',
    text='CONTACT DETAILS',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
contactText = visual.TextStim(win=win, name='contactText',
    text='If you have any questions about this study, please contact the researchers.\n\nEmail: serene.siow@psy.ox.ac.uk\n\nPrincipal Investigators: Núria Sebastian-Galles and Kim Plunkett\n\nResearchers: Gonzalo García-Castro and Serene Siow\n\nCenter for Brain and Cognition, Universitat Pompeu Fabra\n\nDepartment of Experimental Psychology, University of Oxford',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
contactNextText = visual.TextStim(win=win, name='contactNextText',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
contactNextKey = keyboard.Keyboard()

# Initialize components for Routine "confidentiality"
confidentialityClock = core.Clock()
confidentialityTitleText = visual.TextStim(win=win, name='confidentialityTitleText',
    text='HOW WILL MY DATA BE USED?',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
confidentialityText = visual.TextStim(win=win, name='confidentialityText',
    text='Your answers will be completely ANONYMOUS, and we will take all reasonable measures to ensure that they remain confidential.\n\nYour DATA WILL BE STORED in a password-protected file and MAY BE USED in academic publications IN AN ANONYMISED FORM. Your IP address will NOT BE STORED. Research data will be stored for a minimum of three years after publication or public release.\n\nWe would also like your permission to use your anonymised data in future studies, and to SHARE data with other researchers (e.g. in online databases). Any personal information that could identify you will be REMOVED or REPLACED before files are SHARED with other researchers or results are MADE PUBLIC.\n\nThis project has received ethics clearance through the University of Oxford Central University Research Ethics Committee, R60939/RE005.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
confidentialityNextText = visual.TextStim(win=win, name='confidentialityNextText',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
confidentialityNextKey = keyboard.Keyboard()

# Initialize components for Routine "information"
informationClock = core.Clock()
informationTitleText = visual.TextStim(win=win, name='informationTitleText',
    text='NEED FOR INFORMATION?',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
informationText = visual.TextStim(win=win, name='informationText',
    text='If you have a concern about any aspect of this study, please speak to Serene Siow (serene.siow@psy.ox.ac.uk), and we will do our best to answer your query.\n\nIf you remain unhappy or wish to make a formal complaint, please contact the Chair of the Research Ethics Committee at the University of Oxford.\nChair, Medical Sciences Interdivisional Research Ethics Committee\nEmail: ethics@medsci.ox.ac.uk',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
informationNextText = visual.TextStim(win=win, name='informationNextText',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
infomationNextKey = keyboard.Keyboard()

# Initialize components for Routine "consent"
consentClock = core.Clock()
consentTitleText = visual.TextStim(win=win, name='consentTitleText',
    text='INFORMED CONSENT',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
consentText = visual.TextStim(win=win, name='consentText',
    text='BY PRESSING SPACE, I certify that I am 18 years of age or over. I agree to participate in the study described. I have made this decision based on the information I have read in the consent information. I have had the opportunity to receive any additional details I wanted about the study and understand that I may ask questions in the future. I understand that I may withdraw this consent at any time.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
consentTextNext = visual.TextStim(win=win, name='consentTextNext',
    text='Press SPACE to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
consentNextKey = keyboard.Keyboard()

# Initialize components for Routine "languageL1"
languageL1Clock = core.Clock()
languageL1TitleText = visual.TextStim(win=win, name='languageL1TitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageL1Text = visual.TextStim(win=win, name='languageL1Text',
    text='What is your NATIVE language?\n\ne) English\ns) Spanish\nc) Catalan\no) Other',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageL1NextText = visual.TextStim(win=win, name='languageL1NextText',
    text='Press the corresponding letter >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageL1Key = keyboard.Keyboard()

# Initialize components for Routine "languageL2"
languageL2Clock = core.Clock()
languageL2TitleText = visual.TextStim(win=win, name='languageL2TitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageL2Text = visual.TextStim(win=win, name='languageL2Text',
    text='Do you know any other SECOND LANGUAGE, different than the one you indicated before? If yes, type which one and press RETURN. If no, press RETURN without writing anything.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageL2NextText = visual.TextStim(win=win, name='languageL2NextText',
    text='Press RETURN to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageL2InputText = visual.TextStim(win=win, name='languageL2InputText',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "languageL2Oral"
languageL2OralClock = core.Clock()
languageL2OralTitleText = visual.TextStim(win=win, name='languageL2OralTitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageL2OralText = visual.TextStim(win=win, name='languageL2OralText',
    text='On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in your SECOND LANGUAGE?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageL2OralNextText = visual.TextStim(win=win, name='languageL2OralNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageL2OralKey = keyboard.Keyboard()

# Initialize components for Routine "languageL2Written"
languageL2WrittenClock = core.Clock()
languageL2WrittenTitleText = visual.TextStim(win=win, name='languageL2WrittenTitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageL2WrittenText = visual.TextStim(win=win, name='languageL2WrittenText',
    text='On a scale of 1-5, how would you rate your WRITTEN proficiency in your SECOND LANGUAGE?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageL2WrittenNextText = visual.TextStim(win=win, name='languageL2WrittenNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageL2WrittenKey = keyboard.Keyboard()

# Initialize components for Routine "languageL3"
languageL3Clock = core.Clock()
languageL3TitleText = visual.TextStim(win=win, name='languageL3TitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageL3Text = visual.TextStim(win=win, name='languageL3Text',
    text='Do you know any other THIRD LANGUAGE, different than the ones you indicated before? If yes, type which one(s) and press RETURN. If no, press RETURN leaving it blank.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageL3NextText = visual.TextStim(win=win, name='languageL3NextText',
    text='Press RETURN to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageL3InputText = visual.TextStim(win=win, name='languageL3InputText',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "languageL3Oral"
languageL3OralClock = core.Clock()
languageL3OralTitleText = visual.TextStim(win=win, name='languageL3OralTitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageL3OralText = visual.TextStim(win=win, name='languageL3OralText',
    text='On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in your THIRD LANGUAGE?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native / I am native',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageL3OralNextText = visual.TextStim(win=win, name='languageL3OralNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageL3OralKey = keyboard.Keyboard()

# Initialize components for Routine "languageL3Written"
languageL3WrittenClock = core.Clock()
languageL3WrittenTitleText = visual.TextStim(win=win, name='languageL3WrittenTitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageL3WrittenText = visual.TextStim(win=win, name='languageL3WrittenText',
    text='On a scale of 1-5, how would you rate your WRITTEN proficiency in your THIRD LANGUAGE?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageL3WrittenNextText = visual.TextStim(win=win, name='languageL3WrittenNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageL3WrittenKey = keyboard.Keyboard()

# Initialize components for Routine "languageCatalanOral"
languageCatalanOralClock = core.Clock()
languageCatalanOralTitleText = visual.TextStim(win=win, name='languageCatalanOralTitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageCatalanOralText = visual.TextStim(win=win, name='languageCatalanOralText',
    text='On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in CATALAN?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageCatalanOralNextText = visual.TextStim(win=win, name='languageCatalanOralNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageCatalanOralKey = keyboard.Keyboard()

# Initialize components for Routine "languageCatalanWritten"
languageCatalanWrittenClock = core.Clock()
languageCatalanWrittenTitleText = visual.TextStim(win=win, name='languageCatalanWrittenTitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageCatalanWrittenText = visual.TextStim(win=win, name='languageCatalanWrittenText',
    text='On a scale of 1-5, how would you rate your WRITTEN proficiency in CATALAN?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageCatalanWrittenNextText = visual.TextStim(win=win, name='languageCatalanWrittenNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageCatalanWrittenKey = keyboard.Keyboard()

# Initialize components for Routine "languageCatalanTime"
languageCatalanTimeClock = core.Clock()
languageCatalanTimeTitleText = visual.TextStim(win=win, name='languageCatalanTimeTitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageCatalanTimeText = visual.TextStim(win=win, name='languageCatalanTimeText',
    text='How long have you spent in any REGION where CATALAN is spoken (Catalonia, Valencia, Balearic Islands), including your childhood? Pick the option that best describes your situation:\n\n1) Never or less than 1 month\n2) Between 1 and 3 months\n3) I used to spend holidays there\n4) I lived there for less than 6 months\n5) I lived there for 6 months or longer',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageCatalanTimeNextText = visual.TextStim(win=win, name='languageCatalanTimeNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageCatalanTimeKey = keyboard.Keyboard()

# Initialize components for Routine "languageSpanishOral"
languageSpanishOralClock = core.Clock()
languageSpanishOralTitleText = visual.TextStim(win=win, name='languageSpanishOralTitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageSpanishOralText = visual.TextStim(win=win, name='languageSpanishOralText',
    text='On a scale of 1-5, how would you rate your ORAL COMPREHENSION proficiency in SPANISH?\n\n1) I do not understand anything\n2) I understand some words\n3) I can get what a conversation or sentence is about\n4) I understand almost everything\n5) Like a native /  I am native',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageSpanishOralNextText = visual.TextStim(win=win, name='languageSpanishOralNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageSpanishOralKey = keyboard.Keyboard()

# Initialize components for Routine "languageSpanishWritten"
languageSpanishWrittenClock = core.Clock()
languageSpanishTitleText = visual.TextStim(win=win, name='languageSpanishTitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageSpanishWrittenText = visual.TextStim(win=win, name='languageSpanishWrittenText',
    text='On a scale of 1-5, how would you rate your WRITTEN proficiency in SPANISH?\n\n1) I have never received any training in the orthography of this language\n2) I make a lot of orthographic mistakes\n3) I make many orthographic mistakes\n4) I make some orthographic mistakes\n5) I do not make any orthographic mistakes',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageSpanishNextText = visual.TextStim(win=win, name='languageSpanishNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageSpanishWrittenKey = keyboard.Keyboard()

# Initialize components for Routine "languageSpanishTime"
languageSpanishTimeClock = core.Clock()
languageSpanishTimeTitleText = visual.TextStim(win=win, name='languageSpanishTimeTitleText',
    text='LANGUAGE QUESTIONNAIRE',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
languageSpanishTimeText = visual.TextStim(win=win, name='languageSpanishTimeText',
    text='How long have you spent in any REGION where SPANISH is spoken (Spain, South America), including your childhood? Pick the option that best describes your situation:\n\n1) Never or less than 1 month\n2) Between 1 and 3 months\n3) I used to spend holidays there\n4) I lived there for less than 6 months\n5) I lived there for 6 months or longer',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
languageSpanishTimeNextText = visual.TextStim(win=win, name='languageSpanishTimeNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
languageSpanishTimeKey = keyboard.Keyboard()

# Initialize components for Routine "demoAge"
demoAgeClock = core.Clock()
demoAgeTitleText = visual.TextStim(win=win, name='demoAgeTitleText',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
demoAgeText = visual.TextStim(win=win, name='demoAgeText',
    text='Please, type your age (in years) and then press RETURN:',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demoAgeNextText = visual.TextStim(win=win, name='demoAgeNextText',
    text='Press RETURN to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
demoAgeInputText = visual.TextStim(win=win, name='demoAgeInputText',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demoSex"
demoSexClock = core.Clock()
demoSexTitleText = visual.TextStim(win=win, name='demoSexTitleText',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
demoSexText = visual.TextStim(win=win, name='demoSexText',
    text='Sex:\n\nf) Female\nm) Male\no) Other',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demoSexNextText = visual.TextStim(win=win, name='demoSexNextText',
    text='Press the corresponding letter >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
demoSexKey = keyboard.Keyboard()

# Initialize components for Routine "demoEducation"
demoEducationClock = core.Clock()
demoEducationTitleText = visual.TextStim(win=win, name='demoEducationTitleText',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
demoEducationText = visual.TextStim(win=win, name='demoEducationText',
    text='What is your highest level of EDUCATIONAL ACHIEVEMENT?\n\n1) No qualifications\n2) Left school at 16 with GCSE or equivalent\n3) Left school at 18 with A-Levels or equivalent\n4) University degree or equivalent\n5) Vocational training',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demoEducationNextText = visual.TextStim(win=win, name='demoEducationNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
demoEducationKey = keyboard.Keyboard()

# Initialize components for Routine "demoCity"
demoCityClock = core.Clock()
demoCityTitleText = visual.TextStim(win=win, name='demoCityTitleText',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
demoCityText = visual.TextStim(win=win, name='demoCityText',
    text='What CITY do you live in? Type it and press RETURN to continue.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demoCityNextText = visual.TextStim(win=win, name='demoCityNextText',
    text='Press RETURN to continue >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
demoCityInputText = visual.TextStim(win=win, name='demoCityInputText',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demoVision"
demoVisionClock = core.Clock()
demoVisionTitleText = visual.TextStim(win=win, name='demoVisionTitleText',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
demoVisionText = visual.TextStim(win=win, name='demoVisionText',
    text='Do you have normal or corrected-to-normal VISION?\n\ny) Yes\nn) No',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demoTextNextText = visual.TextStim(win=win, name='demoTextNextText',
    text='Press the corresponding letter >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
demoVisionKey = keyboard.Keyboard()

# Initialize components for Routine "demoLanguage"
demoLanguageClock = core.Clock()
demoLanguageTitleText = visual.TextStim(win=win, name='demoLanguageTitleText',
    text='DEMOGRAPHIC INFORMATION',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
demoLanguageText = visual.TextStim(win=win, name='demoLanguageText',
    text='Have you been diagnosed with any LANGUAGE (e.g., DYSLEXIA) OR HEARING IMPAIRMENT?\n\ny) Yes\nn) No',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
demoLanguageNextText = visual.TextStim(win=win, name='demoLanguageNextText',
    text='Press the corresponding letter >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
demoLanguageKey = keyboard.Keyboard()

# Initialize components for Routine "setupLocation"
setupLocationClock = core.Clock()
setupLocationTitleText = visual.TextStim(win=win, name='setupLocationTitleText',
    text='SETUP',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
setupLocationText = visual.TextStim(win=win, name='setupLocationText',
    text='WHERE are you completing this study?\n\n1) At home\n2) At the library\n3) At a cafe or restaurant\n4) At a friend’s house\n5) At school\n6) At work\n7) Other',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
setupLocationNextText = visual.TextStim(win=win, name='setupLocationNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
setupLocationKey = keyboard.Keyboard()

# Initialize components for Routine "setupNoise"
setupNoiseClock = core.Clock()
setupNoiseTitleText = visual.TextStim(win=win, name='setupNoiseTitleText',
    text='SETUP',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
setupNoiseText = visual.TextStim(win=win, name='setupNoiseText',
    text='How NOISY was the environment in which you completed the experiment? \n\n1) Very quiet (like a library)\n2) Somewhat quiet (like an office)\n3) Somewhat noisy (like being at the park)\n4) Very noisy (like being at a busy street)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
setupNoiseNextText = visual.TextStim(win=win, name='setupNoiseNextText',
    text='Press the corresponding number >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
setupNoiseKey = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsTitleText = visual.TextStim(win=win, name='instructionsTitleText',
    text='INSTRUCTIONS',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructionsText = visual.TextStim(win=win, name='instructionsText',
    text='You will listen to some words through your headphones.\n\nWords are in Catalan or Spanish and were recorded in a baby-directed manner. You will have to GUESS and TYPE the TRANSLATION of each word IN ENGLISH.\n\nStart typing as soon as you come up with an answer. It is probable that you do not know it. Type the translation you think is most likely to be correct. You MUST type an answer FOR EACH WORD.\n\nYou can use BACKSPACE to correct any typing errors, as you would normally.\n\nAfter typing the word, press RETURN to continue to the next word.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructionsNextText = visual.TextStim(win=win, name='instructionsNextText',
    text='NEXT, YOU WILL COMPLETE 5 PRACTICE TRIALS\n\nPress SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
instructionsKey = keyboard.Keyboard()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instructions2TitleText = visual.TextStim(win=win, name='instructions2TitleText',
    text='INSTRUCTIONS',
    font='Arial',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions2Text = visual.TextStim(win=win, name='instructions2Text',
    text='You may adjust the volume during these trials to avoid having to do it during the main experiment. Make sure words are loud enough for you to hear them clearly.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
isntructions2NextText = visual.TextStim(win=win, name='isntructions2NextText',
    text='Press SPACE to start 5 practice trials >',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
isntructions2Key = keyboard.Keyboard()
import random

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixationText = visual.TextStim(win=win, name='fixationText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialText = visual.TextStim(win=win, name='trialText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trialSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='trialSound')
trialSound.setVolume(1.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixationText = visual.TextStim(win=win, name='fixationText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialText = visual.TextStim(win=win, name='trialText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trialSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='trialSound')
trialSound.setVolume(1.0)

# Initialize components for Routine "begin"
beginClock = core.Clock()
beginText = visual.TextStim(win=win, name='beginText',
    text='You have completed the PRACTICE trials',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
beginNextText = visual.TextStim(win=win, name='beginNextText',
    text='Press SPACE to start >',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixationText = visual.TextStim(win=win, name='fixationText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialText = visual.TextStim(win=win, name='trialText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trialSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='trialSound')
trialSound.setVolume(1.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixationText = visual.TextStim(win=win, name='fixationText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialText = visual.TextStim(win=win, name='trialText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trialSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='trialSound')
trialSound.setVolume(1.0)

# Initialize components for Routine "farewell"
farewellClock = core.Clock()
farewellText = visual.TextStim(win=win, name='farewellText',
    text='Congratulations! You have finished.\n\nTHANKS A LOT FOR YOUR PARTICIPATION.\n\nIf you have any questions, get in touch with us at serene.siow@ox.ac.uk\n\nPress SPACE to be redirected to Prolific.\n\nPlease, wait to be redirected to Prolific, otherwise you may not receive your credit.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
setupNextKey.keys = []
setupNextKey.rt = []
_setupNextKey_allKeys = []
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
languageCatalanTimeText.alignText = "left"
languageSpanishOralText.alignText = "left"
languageSpanishWrittenText.alignText = "left"
languageSpanishTimeText.alignText = "left"
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


# keep track of which components have finished
setupComponents = [setupTitleText, setupText, setupNextText, setupNextKey]
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
    
    # *setupTitleText* updates
    if setupTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupTitleText.frameNStart = frameN  # exact frame index
        setupTitleText.tStart = t  # local t and not account for scr refresh
        setupTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupTitleText, 'tStartRefresh')  # time at next scr refresh
        setupTitleText.setAutoDraw(True)
    
    # *setupText* updates
    if setupText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupText.frameNStart = frameN  # exact frame index
        setupText.tStart = t  # local t and not account for scr refresh
        setupText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupText, 'tStartRefresh')  # time at next scr refresh
        setupText.setAutoDraw(True)
    
    # *setupNextText* updates
    if setupNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupNextText.frameNStart = frameN  # exact frame index
        setupNextText.tStart = t  # local t and not account for scr refresh
        setupNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupNextText, 'tStartRefresh')  # time at next scr refresh
        setupNextText.setAutoDraw(True)
    
    # *setupNextKey* updates
    waitOnFlip = False
    if setupNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupNextKey.frameNStart = frameN  # exact frame index
        setupNextKey.tStart = t  # local t and not account for scr refresh
        setupNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupNextKey, 'tStartRefresh')  # time at next scr refresh
        setupNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(setupNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(setupNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if setupNextKey.status == STARTED and not waitOnFlip:
        theseKeys = setupNextKey.getKeys(keyList=['space'], waitRelease=False)
        _setupNextKey_allKeys.extend(theseKeys)
        if len(_setupNextKey_allKeys):
            setupNextKey.keys = _setupNextKey_allKeys[-1].name  # just the last key pressed
            setupNextKey.rt = _setupNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
welcomeNextKey.keys = []
welcomeNextKey.rt = []
_welcomeNextKey_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcomeTextTitle, welcomeText, welcomeNextText, welcomeNextKey]
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
    
    # *welcomeNextText* updates
    if welcomeNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeNextText.frameNStart = frameN  # exact frame index
        welcomeNextText.tStart = t  # local t and not account for scr refresh
        welcomeNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeNextText, 'tStartRefresh')  # time at next scr refresh
        welcomeNextText.setAutoDraw(True)
    
    # *welcomeNextKey* updates
    waitOnFlip = False
    if welcomeNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeNextKey.frameNStart = frameN  # exact frame index
        welcomeNextKey.tStart = t  # local t and not account for scr refresh
        welcomeNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeNextKey, 'tStartRefresh')  # time at next scr refresh
        welcomeNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcomeNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcomeNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcomeNextKey.status == STARTED and not waitOnFlip:
        theseKeys = welcomeNextKey.getKeys(keyList=['space'], waitRelease=False)
        _welcomeNextKey_allKeys.extend(theseKeys)
        if len(_welcomeNextKey_allKeys):
            welcomeNextKey.keys = _welcomeNextKey_allKeys[-1].name  # just the last key pressed
            welcomeNextKey.rt = _welcomeNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
# check responses
if welcomeNextKey.keys in ['', [], None]:  # No response was made
    welcomeNextKey.keys = None
thisExp.addData('welcomeNextKey.keys',welcomeNextKey.keys)
if welcomeNextKey.keys != None:  # we had a response
    thisExp.addData('welcomeNextKey.rt', welcomeNextKey.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "description"-------
continueRoutine = True
# update component parameters for each repeat
descriptionNextKey.keys = []
descriptionNextKey.rt = []
_descriptionNextKey_allKeys = []
# keep track of which components have finished
descriptionComponents = [descriptionTitleText, descriptionText, descriptionNextText, descriptionNextKey]
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
    
    # *descriptionTitleText* updates
    if descriptionTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionTitleText.frameNStart = frameN  # exact frame index
        descriptionTitleText.tStart = t  # local t and not account for scr refresh
        descriptionTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionTitleText, 'tStartRefresh')  # time at next scr refresh
        descriptionTitleText.setAutoDraw(True)
    
    # *descriptionText* updates
    if descriptionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionText.frameNStart = frameN  # exact frame index
        descriptionText.tStart = t  # local t and not account for scr refresh
        descriptionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionText, 'tStartRefresh')  # time at next scr refresh
        descriptionText.setAutoDraw(True)
    
    # *descriptionNextText* updates
    if descriptionNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionNextText.frameNStart = frameN  # exact frame index
        descriptionNextText.tStart = t  # local t and not account for scr refresh
        descriptionNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionNextText, 'tStartRefresh')  # time at next scr refresh
        descriptionNextText.setAutoDraw(True)
    
    # *descriptionNextKey* updates
    waitOnFlip = False
    if descriptionNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        descriptionNextKey.frameNStart = frameN  # exact frame index
        descriptionNextKey.tStart = t  # local t and not account for scr refresh
        descriptionNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(descriptionNextKey, 'tStartRefresh')  # time at next scr refresh
        descriptionNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(descriptionNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(descriptionNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if descriptionNextKey.status == STARTED and not waitOnFlip:
        theseKeys = descriptionNextKey.getKeys(keyList=['space'], waitRelease=False)
        _descriptionNextKey_allKeys.extend(theseKeys)
        if len(_descriptionNextKey_allKeys):
            descriptionNextKey.keys = _descriptionNextKey_allKeys[-1].name  # just the last key pressed
            descriptionNextKey.rt = _descriptionNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
voluntaryNextKey.keys = []
voluntaryNextKey.rt = []
_voluntaryNextKey_allKeys = []
# keep track of which components have finished
voluntaryComponents = [voluntaryTitleText, voluntaryText, voluntaryNextText, voluntaryNextKey]
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
    
    # *voluntaryTitleText* updates
    if voluntaryTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        voluntaryTitleText.frameNStart = frameN  # exact frame index
        voluntaryTitleText.tStart = t  # local t and not account for scr refresh
        voluntaryTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(voluntaryTitleText, 'tStartRefresh')  # time at next scr refresh
        voluntaryTitleText.setAutoDraw(True)
    
    # *voluntaryText* updates
    if voluntaryText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        voluntaryText.frameNStart = frameN  # exact frame index
        voluntaryText.tStart = t  # local t and not account for scr refresh
        voluntaryText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(voluntaryText, 'tStartRefresh')  # time at next scr refresh
        voluntaryText.setAutoDraw(True)
    
    # *voluntaryNextText* updates
    if voluntaryNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        voluntaryNextText.frameNStart = frameN  # exact frame index
        voluntaryNextText.tStart = t  # local t and not account for scr refresh
        voluntaryNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(voluntaryNextText, 'tStartRefresh')  # time at next scr refresh
        voluntaryNextText.setAutoDraw(True)
    
    # *voluntaryNextKey* updates
    waitOnFlip = False
    if voluntaryNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        voluntaryNextKey.frameNStart = frameN  # exact frame index
        voluntaryNextKey.tStart = t  # local t and not account for scr refresh
        voluntaryNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(voluntaryNextKey, 'tStartRefresh')  # time at next scr refresh
        voluntaryNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(voluntaryNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(voluntaryNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if voluntaryNextKey.status == STARTED and not waitOnFlip:
        theseKeys = voluntaryNextKey.getKeys(keyList=['space'], waitRelease=False)
        _voluntaryNextKey_allKeys.extend(theseKeys)
        if len(_voluntaryNextKey_allKeys):
            voluntaryNextKey.keys = _voluntaryNextKey_allKeys[-1].name  # just the last key pressed
            voluntaryNextKey.rt = _voluntaryNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
contactNextKey.keys = []
contactNextKey.rt = []
_contactNextKey_allKeys = []
# keep track of which components have finished
contactComponents = [contactTitleText, contactText, contactNextText, contactNextKey]
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
    
    # *contactTitleText* updates
    if contactTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        contactTitleText.frameNStart = frameN  # exact frame index
        contactTitleText.tStart = t  # local t and not account for scr refresh
        contactTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contactTitleText, 'tStartRefresh')  # time at next scr refresh
        contactTitleText.setAutoDraw(True)
    
    # *contactText* updates
    if contactText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        contactText.frameNStart = frameN  # exact frame index
        contactText.tStart = t  # local t and not account for scr refresh
        contactText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contactText, 'tStartRefresh')  # time at next scr refresh
        contactText.setAutoDraw(True)
    
    # *contactNextText* updates
    if contactNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        contactNextText.frameNStart = frameN  # exact frame index
        contactNextText.tStart = t  # local t and not account for scr refresh
        contactNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contactNextText, 'tStartRefresh')  # time at next scr refresh
        contactNextText.setAutoDraw(True)
    
    # *contactNextKey* updates
    waitOnFlip = False
    if contactNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        contactNextKey.frameNStart = frameN  # exact frame index
        contactNextKey.tStart = t  # local t and not account for scr refresh
        contactNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contactNextKey, 'tStartRefresh')  # time at next scr refresh
        contactNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(contactNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(contactNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if contactNextKey.status == STARTED and not waitOnFlip:
        theseKeys = contactNextKey.getKeys(keyList=['space'], waitRelease=False)
        _contactNextKey_allKeys.extend(theseKeys)
        if len(_contactNextKey_allKeys):
            contactNextKey.keys = _contactNextKey_allKeys[-1].name  # just the last key pressed
            contactNextKey.rt = _contactNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
confidentialityNextKey.keys = []
confidentialityNextKey.rt = []
_confidentialityNextKey_allKeys = []
# keep track of which components have finished
confidentialityComponents = [confidentialityTitleText, confidentialityText, confidentialityNextText, confidentialityNextKey]
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
    
    # *confidentialityTitleText* updates
    if confidentialityTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        confidentialityTitleText.frameNStart = frameN  # exact frame index
        confidentialityTitleText.tStart = t  # local t and not account for scr refresh
        confidentialityTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confidentialityTitleText, 'tStartRefresh')  # time at next scr refresh
        confidentialityTitleText.setAutoDraw(True)
    
    # *confidentialityText* updates
    if confidentialityText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        confidentialityText.frameNStart = frameN  # exact frame index
        confidentialityText.tStart = t  # local t and not account for scr refresh
        confidentialityText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confidentialityText, 'tStartRefresh')  # time at next scr refresh
        confidentialityText.setAutoDraw(True)
    
    # *confidentialityNextText* updates
    if confidentialityNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        confidentialityNextText.frameNStart = frameN  # exact frame index
        confidentialityNextText.tStart = t  # local t and not account for scr refresh
        confidentialityNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confidentialityNextText, 'tStartRefresh')  # time at next scr refresh
        confidentialityNextText.setAutoDraw(True)
    
    # *confidentialityNextKey* updates
    waitOnFlip = False
    if confidentialityNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        confidentialityNextKey.frameNStart = frameN  # exact frame index
        confidentialityNextKey.tStart = t  # local t and not account for scr refresh
        confidentialityNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(confidentialityNextKey, 'tStartRefresh')  # time at next scr refresh
        confidentialityNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(confidentialityNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(confidentialityNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if confidentialityNextKey.status == STARTED and not waitOnFlip:
        theseKeys = confidentialityNextKey.getKeys(keyList=['space'], waitRelease=False)
        _confidentialityNextKey_allKeys.extend(theseKeys)
        if len(_confidentialityNextKey_allKeys):
            confidentialityNextKey.keys = _confidentialityNextKey_allKeys[-1].name  # just the last key pressed
            confidentialityNextKey.rt = _confidentialityNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
# check responses
if confidentialityNextKey.keys in ['', [], None]:  # No response was made
    confidentialityNextKey.keys = None
thisExp.addData('confidentialityNextKey.keys',confidentialityNextKey.keys)
if confidentialityNextKey.keys != None:  # we had a response
    thisExp.addData('confidentialityNextKey.rt', confidentialityNextKey.rt)
thisExp.nextEntry()
# the Routine "confidentiality" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "information"-------
continueRoutine = True
# update component parameters for each repeat
infomationNextKey.keys = []
infomationNextKey.rt = []
_infomationNextKey_allKeys = []
# keep track of which components have finished
informationComponents = [informationTitleText, informationText, informationNextText, infomationNextKey]
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
    
    # *informationTitleText* updates
    if informationTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        informationTitleText.frameNStart = frameN  # exact frame index
        informationTitleText.tStart = t  # local t and not account for scr refresh
        informationTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(informationTitleText, 'tStartRefresh')  # time at next scr refresh
        informationTitleText.setAutoDraw(True)
    
    # *informationText* updates
    if informationText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        informationText.frameNStart = frameN  # exact frame index
        informationText.tStart = t  # local t and not account for scr refresh
        informationText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(informationText, 'tStartRefresh')  # time at next scr refresh
        informationText.setAutoDraw(True)
    
    # *informationNextText* updates
    if informationNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        informationNextText.frameNStart = frameN  # exact frame index
        informationNextText.tStart = t  # local t and not account for scr refresh
        informationNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(informationNextText, 'tStartRefresh')  # time at next scr refresh
        informationNextText.setAutoDraw(True)
    
    # *infomationNextKey* updates
    waitOnFlip = False
    if infomationNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        infomationNextKey.frameNStart = frameN  # exact frame index
        infomationNextKey.tStart = t  # local t and not account for scr refresh
        infomationNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(infomationNextKey, 'tStartRefresh')  # time at next scr refresh
        infomationNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(infomationNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(infomationNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if infomationNextKey.status == STARTED and not waitOnFlip:
        theseKeys = infomationNextKey.getKeys(keyList=['space'], waitRelease=False)
        _infomationNextKey_allKeys.extend(theseKeys)
        if len(_infomationNextKey_allKeys):
            infomationNextKey.keys = _infomationNextKey_allKeys[-1].name  # just the last key pressed
            infomationNextKey.rt = _infomationNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
# check responses
if infomationNextKey.keys in ['', [], None]:  # No response was made
    infomationNextKey.keys = None
thisExp.addData('infomationNextKey.keys',infomationNextKey.keys)
if infomationNextKey.keys != None:  # we had a response
    thisExp.addData('infomationNextKey.rt', infomationNextKey.rt)
thisExp.nextEntry()
# the Routine "information" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "consent"-------
continueRoutine = True
# update component parameters for each repeat
consentNextKey.keys = []
consentNextKey.rt = []
_consentNextKey_allKeys = []
# keep track of which components have finished
consentComponents = [consentTitleText, consentText, consentTextNext, consentNextKey]
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
    
    # *consentTitleText* updates
    if consentTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consentTitleText.frameNStart = frameN  # exact frame index
        consentTitleText.tStart = t  # local t and not account for scr refresh
        consentTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentTitleText, 'tStartRefresh')  # time at next scr refresh
        consentTitleText.setAutoDraw(True)
    
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
    
    # *consentNextKey* updates
    waitOnFlip = False
    if consentNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consentNextKey.frameNStart = frameN  # exact frame index
        consentNextKey.tStart = t  # local t and not account for scr refresh
        consentNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consentNextKey, 'tStartRefresh')  # time at next scr refresh
        consentNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(consentNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(consentNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if consentNextKey.status == STARTED and not waitOnFlip:
        theseKeys = consentNextKey.getKeys(keyList=['space'], waitRelease=False)
        _consentNextKey_allKeys.extend(theseKeys)
        if len(_consentNextKey_allKeys):
            consentNextKey.keys = _consentNextKey_allKeys[-1].name  # just the last key pressed
            consentNextKey.rt = _consentNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
if consentNextKey.keys in ['', [], None]:  # No response was made
    consentNextKey.keys = None
thisExp.addData('consentNextKey.keys',consentNextKey.keys)
if consentNextKey.keys != None:  # we had a response
    thisExp.addData('consentNextKey.rt', consentNextKey.rt)
thisExp.addData('consentNextKey.started', consentNextKey.tStartRefresh)
thisExp.addData('consentNextKey.stopped', consentNextKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageL1"-------
continueRoutine = True
# update component parameters for each repeat
languageL1Key.keys = []
languageL1Key.rt = []
_languageL1Key_allKeys = []
psychopy.event.clearEvents()
inputText = ''
isAccented = False
# keep track of which components have finished
languageL1Components = [languageL1TitleText, languageL1Text, languageL1NextText, languageL1Key]
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
    
    # *languageL1TitleText* updates
    if languageL1TitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL1TitleText.frameNStart = frameN  # exact frame index
        languageL1TitleText.tStart = t  # local t and not account for scr refresh
        languageL1TitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL1TitleText, 'tStartRefresh')  # time at next scr refresh
        languageL1TitleText.setAutoDraw(True)
    
    # *languageL1Text* updates
    if languageL1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL1Text.frameNStart = frameN  # exact frame index
        languageL1Text.tStart = t  # local t and not account for scr refresh
        languageL1Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL1Text, 'tStartRefresh')  # time at next scr refresh
        languageL1Text.setAutoDraw(True)
    
    # *languageL1NextText* updates
    if languageL1NextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL1NextText.frameNStart = frameN  # exact frame index
        languageL1NextText.tStart = t  # local t and not account for scr refresh
        languageL1NextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL1NextText, 'tStartRefresh')  # time at next scr refresh
        languageL1NextText.setAutoDraw(True)
    
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
        theseKeys = languageL1Key.getKeys(keyList=['e', 's', 'c', 'o'], waitRelease=False)
        _languageL1Key_allKeys.extend(theseKeys)
        if len(_languageL1Key_allKeys):
            languageL1Key.keys = _languageL1Key_allKeys[-1].name  # just the last key pressed
            languageL1Key.rt = _languageL1Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
languageL2Components = [languageL2TitleText, languageL2Text, languageL2NextText, languageL2InputText]
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
    
    # *languageL2TitleText* updates
    if languageL2TitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2TitleText.frameNStart = frameN  # exact frame index
        languageL2TitleText.tStart = t  # local t and not account for scr refresh
        languageL2TitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2TitleText, 'tStartRefresh')  # time at next scr refresh
        languageL2TitleText.setAutoDraw(True)
    
    # *languageL2Text* updates
    if languageL2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2Text.frameNStart = frameN  # exact frame index
        languageL2Text.tStart = t  # local t and not account for scr refresh
        languageL2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2Text, 'tStartRefresh')  # time at next scr refresh
        languageL2Text.setAutoDraw(True)
    
    # *languageL2NextText* updates
    if languageL2NextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2NextText.frameNStart = frameN  # exact frame index
        languageL2NextText.tStart = t  # local t and not account for scr refresh
        languageL2NextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2NextText, 'tStartRefresh')  # time at next scr refresh
        languageL2NextText.setAutoDraw(True)
    
    # *languageL2InputText* updates
    if languageL2InputText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2InputText.frameNStart = frameN  # exact frame index
        languageL2InputText.tStart = t  # local t and not account for scr refresh
        languageL2InputText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2InputText, 'tStartRefresh')  # time at next scr refresh
        languageL2InputText.setAutoDraw(True)
    if languageL2InputText.status == STARTED:  # only update if drawing
        languageL2InputText.setText('> ' + inputText, log=False)
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
thisExp.addData('languageL2Text.started', languageL2Text.tStartRefresh)
thisExp.addData('languageL2Text.stopped', languageL2Text.tStopRefresh)
thisExp.addData('languageL2InputText.started', languageL2InputText.tStartRefresh)
thisExp.addData('languageL2InputText.stopped', languageL2InputText.tStopRefresh)
print(languageL2value)
# the Routine "languageL2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageL2Oral"-------
continueRoutine = True
# update component parameters for each repeat
languageL2OralKey.keys = []
languageL2OralKey.rt = []
_languageL2OralKey_allKeys = []
if languageL2value=='':
    continueRoutine = False
# keep track of which components have finished
languageL2OralComponents = [languageL2OralTitleText, languageL2OralText, languageL2OralNextText, languageL2OralKey]
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
    
    # *languageL2OralTitleText* updates
    if languageL2OralTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2OralTitleText.frameNStart = frameN  # exact frame index
        languageL2OralTitleText.tStart = t  # local t and not account for scr refresh
        languageL2OralTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2OralTitleText, 'tStartRefresh')  # time at next scr refresh
        languageL2OralTitleText.setAutoDraw(True)
    
    # *languageL2OralText* updates
    if languageL2OralText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2OralText.frameNStart = frameN  # exact frame index
        languageL2OralText.tStart = t  # local t and not account for scr refresh
        languageL2OralText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2OralText, 'tStartRefresh')  # time at next scr refresh
        languageL2OralText.setAutoDraw(True)
    
    # *languageL2OralNextText* updates
    if languageL2OralNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2OralNextText.frameNStart = frameN  # exact frame index
        languageL2OralNextText.tStart = t  # local t and not account for scr refresh
        languageL2OralNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2OralNextText, 'tStartRefresh')  # time at next scr refresh
        languageL2OralNextText.setAutoDraw(True)
    
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
        theseKeys = languageL2OralKey.getKeys(keyList=['1','2','3','4', '5'], waitRelease=False)
        _languageL2OralKey_allKeys.extend(theseKeys)
        if len(_languageL2OralKey_allKeys):
            languageL2OralKey.keys = _languageL2OralKey_allKeys[-1].name  # just the last key pressed
            languageL2OralKey.rt = _languageL2OralKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
if languageL2value=='':
    continueRoutine = False
# keep track of which components have finished
languageL2WrittenComponents = [languageL2WrittenTitleText, languageL2WrittenText, languageL2WrittenNextText, languageL2WrittenKey]
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
    
    # *languageL2WrittenTitleText* updates
    if languageL2WrittenTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2WrittenTitleText.frameNStart = frameN  # exact frame index
        languageL2WrittenTitleText.tStart = t  # local t and not account for scr refresh
        languageL2WrittenTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2WrittenTitleText, 'tStartRefresh')  # time at next scr refresh
        languageL2WrittenTitleText.setAutoDraw(True)
    
    # *languageL2WrittenText* updates
    if languageL2WrittenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2WrittenText.frameNStart = frameN  # exact frame index
        languageL2WrittenText.tStart = t  # local t and not account for scr refresh
        languageL2WrittenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2WrittenText, 'tStartRefresh')  # time at next scr refresh
        languageL2WrittenText.setAutoDraw(True)
    
    # *languageL2WrittenNextText* updates
    if languageL2WrittenNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL2WrittenNextText.frameNStart = frameN  # exact frame index
        languageL2WrittenNextText.tStart = t  # local t and not account for scr refresh
        languageL2WrittenNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL2WrittenNextText, 'tStartRefresh')  # time at next scr refresh
        languageL2WrittenNextText.setAutoDraw(True)
    
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
        theseKeys = languageL2WrittenKey.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _languageL2WrittenKey_allKeys.extend(theseKeys)
        if len(_languageL2WrittenKey_allKeys):
            languageL2WrittenKey.keys = _languageL2WrittenKey_allKeys[-1].name  # just the last key pressed
            languageL2WrittenKey.rt = _languageL2WrittenKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
languageL3Components = [languageL3TitleText, languageL3Text, languageL3NextText, languageL3InputText]
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
    
    # *languageL3TitleText* updates
    if languageL3TitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3TitleText.frameNStart = frameN  # exact frame index
        languageL3TitleText.tStart = t  # local t and not account for scr refresh
        languageL3TitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3TitleText, 'tStartRefresh')  # time at next scr refresh
        languageL3TitleText.setAutoDraw(True)
    
    # *languageL3Text* updates
    if languageL3Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3Text.frameNStart = frameN  # exact frame index
        languageL3Text.tStart = t  # local t and not account for scr refresh
        languageL3Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3Text, 'tStartRefresh')  # time at next scr refresh
        languageL3Text.setAutoDraw(True)
    
    # *languageL3NextText* updates
    if languageL3NextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3NextText.frameNStart = frameN  # exact frame index
        languageL3NextText.tStart = t  # local t and not account for scr refresh
        languageL3NextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3NextText, 'tStartRefresh')  # time at next scr refresh
        languageL3NextText.setAutoDraw(True)
    
    # *languageL3InputText* updates
    if languageL3InputText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3InputText.frameNStart = frameN  # exact frame index
        languageL3InputText.tStart = t  # local t and not account for scr refresh
        languageL3InputText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3InputText, 'tStartRefresh')  # time at next scr refresh
        languageL3InputText.setAutoDraw(True)
    if languageL3InputText.status == STARTED:  # only update if drawing
        languageL3InputText.setText('> ' + inputText, log=False)
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
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
thisExp.addData('languageL3TitleText.started', languageL3TitleText.tStartRefresh)
thisExp.addData('languageL3TitleText.stopped', languageL3TitleText.tStopRefresh)
print(languageL3value)
# the Routine "languageL3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageL3Oral"-------
continueRoutine = True
# update component parameters for each repeat
languageL3OralKey.keys = []
languageL3OralKey.rt = []
_languageL3OralKey_allKeys = []
if languageL3value=='':
    continueRoutine = False
# keep track of which components have finished
languageL3OralComponents = [languageL3OralTitleText, languageL3OralText, languageL3OralNextText, languageL3OralKey]
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
    
    # *languageL3OralTitleText* updates
    if languageL3OralTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3OralTitleText.frameNStart = frameN  # exact frame index
        languageL3OralTitleText.tStart = t  # local t and not account for scr refresh
        languageL3OralTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3OralTitleText, 'tStartRefresh')  # time at next scr refresh
        languageL3OralTitleText.setAutoDraw(True)
    
    # *languageL3OralText* updates
    if languageL3OralText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3OralText.frameNStart = frameN  # exact frame index
        languageL3OralText.tStart = t  # local t and not account for scr refresh
        languageL3OralText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3OralText, 'tStartRefresh')  # time at next scr refresh
        languageL3OralText.setAutoDraw(True)
    
    # *languageL3OralNextText* updates
    if languageL3OralNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3OralNextText.frameNStart = frameN  # exact frame index
        languageL3OralNextText.tStart = t  # local t and not account for scr refresh
        languageL3OralNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3OralNextText, 'tStartRefresh')  # time at next scr refresh
        languageL3OralNextText.setAutoDraw(True)
    
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
        theseKeys = languageL3OralKey.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _languageL3OralKey_allKeys.extend(theseKeys)
        if len(_languageL3OralKey_allKeys):
            languageL3OralKey.keys = _languageL3OralKey_allKeys[-1].name  # just the last key pressed
            languageL3OralKey.rt = _languageL3OralKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
if languageL3value=='':
    continueRoutine = False
# keep track of which components have finished
languageL3WrittenComponents = [languageL3WrittenTitleText, languageL3WrittenText, languageL3WrittenNextText, languageL3WrittenKey]
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
    
    # *languageL3WrittenTitleText* updates
    if languageL3WrittenTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3WrittenTitleText.frameNStart = frameN  # exact frame index
        languageL3WrittenTitleText.tStart = t  # local t and not account for scr refresh
        languageL3WrittenTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3WrittenTitleText, 'tStartRefresh')  # time at next scr refresh
        languageL3WrittenTitleText.setAutoDraw(True)
    
    # *languageL3WrittenText* updates
    if languageL3WrittenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3WrittenText.frameNStart = frameN  # exact frame index
        languageL3WrittenText.tStart = t  # local t and not account for scr refresh
        languageL3WrittenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3WrittenText, 'tStartRefresh')  # time at next scr refresh
        languageL3WrittenText.setAutoDraw(True)
    
    # *languageL3WrittenNextText* updates
    if languageL3WrittenNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageL3WrittenNextText.frameNStart = frameN  # exact frame index
        languageL3WrittenNextText.tStart = t  # local t and not account for scr refresh
        languageL3WrittenNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageL3WrittenNextText, 'tStartRefresh')  # time at next scr refresh
        languageL3WrittenNextText.setAutoDraw(True)
    
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
        theseKeys = languageL3WrittenKey.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _languageL3WrittenKey_allKeys.extend(theseKeys)
        if len(_languageL3WrittenKey_allKeys):
            languageL3WrittenKey.keys = _languageL3WrittenKey_allKeys[-1].name  # just the last key pressed
            languageL3WrittenKey.rt = _languageL3WrittenKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
# if Catalan is L2 or L3, skip
if (languageL2value=="CATALAN" or languageL3value=="CATALAN"):
    continueRoutine = False
    
# if ESCAPE is pressed, quit experiment
keys = event.getKeys(keyList = ['escape', 'space'])
n = len(keys)

if ('escape' in keys):
    core.quit()
# keep track of which components have finished
languageCatalanOralComponents = [languageCatalanOralTitleText, languageCatalanOralText, languageCatalanOralNextText, languageCatalanOralKey]
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
    
    # *languageCatalanOralTitleText* updates
    if languageCatalanOralTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanOralTitleText.frameNStart = frameN  # exact frame index
        languageCatalanOralTitleText.tStart = t  # local t and not account for scr refresh
        languageCatalanOralTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanOralTitleText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanOralTitleText.setAutoDraw(True)
    
    # *languageCatalanOralText* updates
    if languageCatalanOralText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanOralText.frameNStart = frameN  # exact frame index
        languageCatalanOralText.tStart = t  # local t and not account for scr refresh
        languageCatalanOralText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanOralText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanOralText.setAutoDraw(True)
    
    # *languageCatalanOralNextText* updates
    if languageCatalanOralNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanOralNextText.frameNStart = frameN  # exact frame index
        languageCatalanOralNextText.tStart = t  # local t and not account for scr refresh
        languageCatalanOralNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanOralNextText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanOralNextText.setAutoDraw(True)
    
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
        theseKeys = languageCatalanOralKey.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _languageCatalanOralKey_allKeys.extend(theseKeys)
        if len(_languageCatalanOralKey_allKeys):
            languageCatalanOralKey.keys = _languageCatalanOralKey_allKeys[-1].name  # just the last key pressed
            languageCatalanOralKey.rt = _languageCatalanOralKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
# if Catalan is L2 or L3, skip
if (languageL2value=="CATALAN" or languageL3value=="CATALAN"):
    continueRoutine = False
    
# if ESCAPE is pressed, quit experiment
keys = event.getKeys(keyList = ['escape', 'space'])
n = len(keys)

if ('escape' in keys):
    core.quit()
# keep track of which components have finished
languageCatalanWrittenComponents = [languageCatalanWrittenTitleText, languageCatalanWrittenText, languageCatalanWrittenNextText, languageCatalanWrittenKey]
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
    
    # *languageCatalanWrittenTitleText* updates
    if languageCatalanWrittenTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanWrittenTitleText.frameNStart = frameN  # exact frame index
        languageCatalanWrittenTitleText.tStart = t  # local t and not account for scr refresh
        languageCatalanWrittenTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanWrittenTitleText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanWrittenTitleText.setAutoDraw(True)
    
    # *languageCatalanWrittenText* updates
    if languageCatalanWrittenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanWrittenText.frameNStart = frameN  # exact frame index
        languageCatalanWrittenText.tStart = t  # local t and not account for scr refresh
        languageCatalanWrittenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanWrittenText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanWrittenText.setAutoDraw(True)
    
    # *languageCatalanWrittenNextText* updates
    if languageCatalanWrittenNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanWrittenNextText.frameNStart = frameN  # exact frame index
        languageCatalanWrittenNextText.tStart = t  # local t and not account for scr refresh
        languageCatalanWrittenNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanWrittenNextText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanWrittenNextText.setAutoDraw(True)
    
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
        theseKeys = languageCatalanWrittenKey.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _languageCatalanWrittenKey_allKeys.extend(theseKeys)
        if len(_languageCatalanWrittenKey_allKeys):
            languageCatalanWrittenKey.keys = _languageCatalanWrittenKey_allKeys[-1].name  # just the last key pressed
            languageCatalanWrittenKey.rt = _languageCatalanWrittenKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
# if ESCAPE is pressed, quit experiment
keys = event.getKeys(keyList = ['escape', 'space'])
n = len(keys)

if ('escape' in keys):
    core.quit()
# keep track of which components have finished
languageCatalanTimeComponents = [languageCatalanTimeTitleText, languageCatalanTimeText, languageCatalanTimeNextText, languageCatalanTimeKey]
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
    
    # *languageCatalanTimeTitleText* updates
    if languageCatalanTimeTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanTimeTitleText.frameNStart = frameN  # exact frame index
        languageCatalanTimeTitleText.tStart = t  # local t and not account for scr refresh
        languageCatalanTimeTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanTimeTitleText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanTimeTitleText.setAutoDraw(True)
    
    # *languageCatalanTimeText* updates
    if languageCatalanTimeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanTimeText.frameNStart = frameN  # exact frame index
        languageCatalanTimeText.tStart = t  # local t and not account for scr refresh
        languageCatalanTimeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanTimeText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanTimeText.setAutoDraw(True)
    
    # *languageCatalanTimeNextText* updates
    if languageCatalanTimeNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageCatalanTimeNextText.frameNStart = frameN  # exact frame index
        languageCatalanTimeNextText.tStart = t  # local t and not account for scr refresh
        languageCatalanTimeNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageCatalanTimeNextText, 'tStartRefresh')  # time at next scr refresh
        languageCatalanTimeNextText.setAutoDraw(True)
    
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
        theseKeys = languageCatalanTimeKey.getKeys(keyList=['1','2','3','4', '5'], waitRelease=False)
        _languageCatalanTimeKey_allKeys.extend(theseKeys)
        if len(_languageCatalanTimeKey_allKeys):
            languageCatalanTimeKey.keys = _languageCatalanTimeKey_allKeys[-1].name  # just the last key pressed
            languageCatalanTimeKey.rt = _languageCatalanTimeKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
# if Catalan is L2 or L3, skip
if (languageL2value=="SPANISH" or languageL3value=="SPANISH"):
    continueRoutine = False
    
# if ESCAPE is pressed, quit experiment
keys = event.getKeys(keyList = ['escape', 'space'])
n = len(keys)

if ('escape' in keys):
    core.quit()
# keep track of which components have finished
languageSpanishOralComponents = [languageSpanishOralTitleText, languageSpanishOralText, languageSpanishOralNextText, languageSpanishOralKey]
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
    
    # *languageSpanishOralTitleText* updates
    if languageSpanishOralTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishOralTitleText.frameNStart = frameN  # exact frame index
        languageSpanishOralTitleText.tStart = t  # local t and not account for scr refresh
        languageSpanishOralTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishOralTitleText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishOralTitleText.setAutoDraw(True)
    
    # *languageSpanishOralText* updates
    if languageSpanishOralText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishOralText.frameNStart = frameN  # exact frame index
        languageSpanishOralText.tStart = t  # local t and not account for scr refresh
        languageSpanishOralText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishOralText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishOralText.setAutoDraw(True)
    
    # *languageSpanishOralNextText* updates
    if languageSpanishOralNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishOralNextText.frameNStart = frameN  # exact frame index
        languageSpanishOralNextText.tStart = t  # local t and not account for scr refresh
        languageSpanishOralNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishOralNextText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishOralNextText.setAutoDraw(True)
    
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
        theseKeys = languageSpanishOralKey.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _languageSpanishOralKey_allKeys.extend(theseKeys)
        if len(_languageSpanishOralKey_allKeys):
            languageSpanishOralKey.keys = _languageSpanishOralKey_allKeys[-1].name  # just the last key pressed
            languageSpanishOralKey.rt = _languageSpanishOralKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
thisExp.addData('languageSpanishOralText.started', languageSpanishOralText.tStartRefresh)
thisExp.addData('languageSpanishOralText.stopped', languageSpanishOralText.tStopRefresh)
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
# if Catalan is L2 or L3, skip
if (languageL2value=="SPANISH" or languageL3value=="SPANISH"):
    continueRoutine = False
    
# if ESCAPE is pressed, quit experiment
keys = event.getKeys(keyList = ['escape', 'space'])
n = len(keys)

if ('escape' in keys):
    core.quit()
# keep track of which components have finished
languageSpanishWrittenComponents = [languageSpanishTitleText, languageSpanishWrittenText, languageSpanishNextText, languageSpanishWrittenKey]
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
    
    # *languageSpanishTitleText* updates
    if languageSpanishTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishTitleText.frameNStart = frameN  # exact frame index
        languageSpanishTitleText.tStart = t  # local t and not account for scr refresh
        languageSpanishTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishTitleText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishTitleText.setAutoDraw(True)
    
    # *languageSpanishWrittenText* updates
    if languageSpanishWrittenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishWrittenText.frameNStart = frameN  # exact frame index
        languageSpanishWrittenText.tStart = t  # local t and not account for scr refresh
        languageSpanishWrittenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishWrittenText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishWrittenText.setAutoDraw(True)
    
    # *languageSpanishNextText* updates
    if languageSpanishNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishNextText.frameNStart = frameN  # exact frame index
        languageSpanishNextText.tStart = t  # local t and not account for scr refresh
        languageSpanishNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishNextText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishNextText.setAutoDraw(True)
    
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
        theseKeys = languageSpanishWrittenKey.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _languageSpanishWrittenKey_allKeys.extend(theseKeys)
        if len(_languageSpanishWrittenKey_allKeys):
            languageSpanishWrittenKey.keys = _languageSpanishWrittenKey_allKeys[-1].name  # just the last key pressed
            languageSpanishWrittenKey.rt = _languageSpanishWrittenKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
thisExp.addData('languageSpanishWrittenText.started', languageSpanishWrittenText.tStartRefresh)
thisExp.addData('languageSpanishWrittenText.stopped', languageSpanishWrittenText.tStopRefresh)
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
languageSpanishTimeComponents = [languageSpanishTimeTitleText, languageSpanishTimeText, languageSpanishTimeNextText, languageSpanishTimeKey]
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
    
    # *languageSpanishTimeTitleText* updates
    if languageSpanishTimeTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishTimeTitleText.frameNStart = frameN  # exact frame index
        languageSpanishTimeTitleText.tStart = t  # local t and not account for scr refresh
        languageSpanishTimeTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishTimeTitleText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishTimeTitleText.setAutoDraw(True)
    
    # *languageSpanishTimeText* updates
    if languageSpanishTimeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishTimeText.frameNStart = frameN  # exact frame index
        languageSpanishTimeText.tStart = t  # local t and not account for scr refresh
        languageSpanishTimeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishTimeText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishTimeText.setAutoDraw(True)
    
    # *languageSpanishTimeNextText* updates
    if languageSpanishTimeNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        languageSpanishTimeNextText.frameNStart = frameN  # exact frame index
        languageSpanishTimeNextText.tStart = t  # local t and not account for scr refresh
        languageSpanishTimeNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(languageSpanishTimeNextText, 'tStartRefresh')  # time at next scr refresh
        languageSpanishTimeNextText.setAutoDraw(True)
    
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
        theseKeys = languageSpanishTimeKey.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _languageSpanishTimeKey_allKeys.extend(theseKeys)
        if len(_languageSpanishTimeKey_allKeys):
            languageSpanishTimeKey.keys = _languageSpanishTimeKey_allKeys[-1].name  # just the last key pressed
            languageSpanishTimeKey.rt = _languageSpanishTimeKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
demoAgeComponents = [demoAgeTitleText, demoAgeText, demoAgeNextText, demoAgeInputText]
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
    
    # *demoAgeTitleText* updates
    if demoAgeTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoAgeTitleText.frameNStart = frameN  # exact frame index
        demoAgeTitleText.tStart = t  # local t and not account for scr refresh
        demoAgeTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoAgeTitleText, 'tStartRefresh')  # time at next scr refresh
        demoAgeTitleText.setAutoDraw(True)
    
    # *demoAgeText* updates
    if demoAgeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoAgeText.frameNStart = frameN  # exact frame index
        demoAgeText.tStart = t  # local t and not account for scr refresh
        demoAgeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoAgeText, 'tStartRefresh')  # time at next scr refresh
        demoAgeText.setAutoDraw(True)
    
    # *demoAgeNextText* updates
    if demoAgeNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoAgeNextText.frameNStart = frameN  # exact frame index
        demoAgeNextText.tStart = t  # local t and not account for scr refresh
        demoAgeNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoAgeNextText, 'tStartRefresh')  # time at next scr refresh
        demoAgeNextText.setAutoDraw(True)
    
    # *demoAgeInputText* updates
    if demoAgeInputText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoAgeInputText.frameNStart = frameN  # exact frame index
        demoAgeInputText.tStart = t  # local t and not account for scr refresh
        demoAgeInputText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoAgeInputText, 'tStartRefresh')  # time at next scr refresh
        demoAgeInputText.setAutoDraw(True)
    if demoAgeInputText.status == STARTED:  # only update if drawing
        demoAgeInputText.setText('> ' + inputText, log=False)
    keys = event.getKeys(keyList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'escape', 'backspace', 'return'])
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
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
# the Routine "demoAge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoSex"-------
continueRoutine = True
# update component parameters for each repeat
demoSexKey.keys = []
demoSexKey.rt = []
_demoSexKey_allKeys = []
# keep track of which components have finished
demoSexComponents = [demoSexTitleText, demoSexText, demoSexNextText, demoSexKey]
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
    
    # *demoSexTitleText* updates
    if demoSexTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoSexTitleText.frameNStart = frameN  # exact frame index
        demoSexTitleText.tStart = t  # local t and not account for scr refresh
        demoSexTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoSexTitleText, 'tStartRefresh')  # time at next scr refresh
        demoSexTitleText.setAutoDraw(True)
    
    # *demoSexText* updates
    if demoSexText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoSexText.frameNStart = frameN  # exact frame index
        demoSexText.tStart = t  # local t and not account for scr refresh
        demoSexText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoSexText, 'tStartRefresh')  # time at next scr refresh
        demoSexText.setAutoDraw(True)
    
    # *demoSexNextText* updates
    if demoSexNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoSexNextText.frameNStart = frameN  # exact frame index
        demoSexNextText.tStart = t  # local t and not account for scr refresh
        demoSexNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoSexNextText, 'tStartRefresh')  # time at next scr refresh
        demoSexNextText.setAutoDraw(True)
    
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
        theseKeys = demoSexKey.getKeys(keyList=['f','m','o'], waitRelease=False)
        _demoSexKey_allKeys.extend(theseKeys)
        if len(_demoSexKey_allKeys):
            demoSexKey.keys = _demoSexKey_allKeys[-1].name  # just the last key pressed
            demoSexKey.rt = _demoSexKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
demoEducationComponents = [demoEducationTitleText, demoEducationText, demoEducationNextText, demoEducationKey]
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
    
    # *demoEducationTitleText* updates
    if demoEducationTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoEducationTitleText.frameNStart = frameN  # exact frame index
        demoEducationTitleText.tStart = t  # local t and not account for scr refresh
        demoEducationTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoEducationTitleText, 'tStartRefresh')  # time at next scr refresh
        demoEducationTitleText.setAutoDraw(True)
    
    # *demoEducationText* updates
    if demoEducationText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoEducationText.frameNStart = frameN  # exact frame index
        demoEducationText.tStart = t  # local t and not account for scr refresh
        demoEducationText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoEducationText, 'tStartRefresh')  # time at next scr refresh
        demoEducationText.setAutoDraw(True)
    
    # *demoEducationNextText* updates
    if demoEducationNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoEducationNextText.frameNStart = frameN  # exact frame index
        demoEducationNextText.tStart = t  # local t and not account for scr refresh
        demoEducationNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoEducationNextText, 'tStartRefresh')  # time at next scr refresh
        demoEducationNextText.setAutoDraw(True)
    
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
        theseKeys = demoEducationKey.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _demoEducationKey_allKeys.extend(theseKeys)
        if len(_demoEducationKey_allKeys):
            demoEducationKey.keys = _demoEducationKey_allKeys[-1].name  # just the last key pressed
            demoEducationKey.rt = _demoEducationKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
demoCityComponents = [demoCityTitleText, demoCityText, demoCityNextText, demoCityInputText]
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
    
    # *demoCityTitleText* updates
    if demoCityTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoCityTitleText.frameNStart = frameN  # exact frame index
        demoCityTitleText.tStart = t  # local t and not account for scr refresh
        demoCityTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoCityTitleText, 'tStartRefresh')  # time at next scr refresh
        demoCityTitleText.setAutoDraw(True)
    
    # *demoCityText* updates
    if demoCityText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoCityText.frameNStart = frameN  # exact frame index
        demoCityText.tStart = t  # local t and not account for scr refresh
        demoCityText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoCityText, 'tStartRefresh')  # time at next scr refresh
        demoCityText.setAutoDraw(True)
    
    # *demoCityNextText* updates
    if demoCityNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoCityNextText.frameNStart = frameN  # exact frame index
        demoCityNextText.tStart = t  # local t and not account for scr refresh
        demoCityNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoCityNextText, 'tStartRefresh')  # time at next scr refresh
        demoCityNextText.setAutoDraw(True)
    
    # *demoCityInputText* updates
    if demoCityInputText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoCityInputText.frameNStart = frameN  # exact frame index
        demoCityInputText.tStart = t  # local t and not account for scr refresh
        demoCityInputText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoCityInputText, 'tStartRefresh')  # time at next scr refresh
        demoCityInputText.setAutoDraw(True)
    if demoCityInputText.status == STARTED:  # only update if drawing
        demoCityInputText.setText('> ' + inputText, log=False)
    keys = event.getKeys(keyList = letterKeysAllowed)
    i = 0 # index whether how many keys have been previously pressed
    
    if len(keys): # if any key has been pressed...
    
         # ... and ESCAPE is pressed, quit experiment
        if keys[i]=='escape':
            thisExp.addData('city', inputText) # save data
            core.quit()
            # ... and RETURN is pressed, stop trial
        if (keys[i]=='return'):
            city = inputText
            thisExp.addData('city', inputText) # save data
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
            thisExp.addData('city', inputText) # save data
            i = i + 1 # index another key press
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
demoVisionComponents = [demoVisionTitleText, demoVisionText, demoTextNextText, demoVisionKey]
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
    
    # *demoVisionTitleText* updates
    if demoVisionTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoVisionTitleText.frameNStart = frameN  # exact frame index
        demoVisionTitleText.tStart = t  # local t and not account for scr refresh
        demoVisionTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoVisionTitleText, 'tStartRefresh')  # time at next scr refresh
        demoVisionTitleText.setAutoDraw(True)
    
    # *demoVisionText* updates
    if demoVisionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoVisionText.frameNStart = frameN  # exact frame index
        demoVisionText.tStart = t  # local t and not account for scr refresh
        demoVisionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoVisionText, 'tStartRefresh')  # time at next scr refresh
        demoVisionText.setAutoDraw(True)
    
    # *demoTextNextText* updates
    if demoTextNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoTextNextText.frameNStart = frameN  # exact frame index
        demoTextNextText.tStart = t  # local t and not account for scr refresh
        demoTextNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoTextNextText, 'tStartRefresh')  # time at next scr refresh
        demoTextNextText.setAutoDraw(True)
    
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
        theseKeys = demoVisionKey.getKeys(keyList=['y','n'], waitRelease=False)
        _demoVisionKey_allKeys.extend(theseKeys)
        if len(_demoVisionKey_allKeys):
            demoVisionKey.keys = _demoVisionKey_allKeys[-1].name  # just the last key pressed
            demoVisionKey.rt = _demoVisionKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
demoLanguageComponents = [demoLanguageTitleText, demoLanguageText, demoLanguageNextText, demoLanguageKey]
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
    
    # *demoLanguageTitleText* updates
    if demoLanguageTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoLanguageTitleText.frameNStart = frameN  # exact frame index
        demoLanguageTitleText.tStart = t  # local t and not account for scr refresh
        demoLanguageTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoLanguageTitleText, 'tStartRefresh')  # time at next scr refresh
        demoLanguageTitleText.setAutoDraw(True)
    
    # *demoLanguageText* updates
    if demoLanguageText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoLanguageText.frameNStart = frameN  # exact frame index
        demoLanguageText.tStart = t  # local t and not account for scr refresh
        demoLanguageText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoLanguageText, 'tStartRefresh')  # time at next scr refresh
        demoLanguageText.setAutoDraw(True)
    
    # *demoLanguageNextText* updates
    if demoLanguageNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoLanguageNextText.frameNStart = frameN  # exact frame index
        demoLanguageNextText.tStart = t  # local t and not account for scr refresh
        demoLanguageNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoLanguageNextText, 'tStartRefresh')  # time at next scr refresh
        demoLanguageNextText.setAutoDraw(True)
    
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
        theseKeys = demoLanguageKey.getKeys(keyList=['y','n'], waitRelease=False)
        _demoLanguageKey_allKeys.extend(theseKeys)
        if len(_demoLanguageKey_allKeys):
            demoLanguageKey.keys = _demoLanguageKey_allKeys[-1].name  # just the last key pressed
            demoLanguageKey.rt = _demoLanguageKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
setupLocationComponents = [setupLocationTitleText, setupLocationText, setupLocationNextText, setupLocationKey]
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
    
    # *setupLocationTitleText* updates
    if setupLocationTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupLocationTitleText.frameNStart = frameN  # exact frame index
        setupLocationTitleText.tStart = t  # local t and not account for scr refresh
        setupLocationTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupLocationTitleText, 'tStartRefresh')  # time at next scr refresh
        setupLocationTitleText.setAutoDraw(True)
    
    # *setupLocationText* updates
    if setupLocationText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupLocationText.frameNStart = frameN  # exact frame index
        setupLocationText.tStart = t  # local t and not account for scr refresh
        setupLocationText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupLocationText, 'tStartRefresh')  # time at next scr refresh
        setupLocationText.setAutoDraw(True)
    
    # *setupLocationNextText* updates
    if setupLocationNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupLocationNextText.frameNStart = frameN  # exact frame index
        setupLocationNextText.tStart = t  # local t and not account for scr refresh
        setupLocationNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupLocationNextText, 'tStartRefresh')  # time at next scr refresh
        setupLocationNextText.setAutoDraw(True)
    
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
        theseKeys = setupLocationKey.getKeys(keyList=['1','2','3','4','5', '6', '7'], waitRelease=False)
        _setupLocationKey_allKeys.extend(theseKeys)
        if len(_setupLocationKey_allKeys):
            setupLocationKey.keys = _setupLocationKey_allKeys[-1].name  # just the last key pressed
            setupLocationKey.rt = _setupLocationKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
setupNoiseComponents = [setupNoiseTitleText, setupNoiseText, setupNoiseNextText, setupNoiseKey]
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
    
    # *setupNoiseTitleText* updates
    if setupNoiseTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupNoiseTitleText.frameNStart = frameN  # exact frame index
        setupNoiseTitleText.tStart = t  # local t and not account for scr refresh
        setupNoiseTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupNoiseTitleText, 'tStartRefresh')  # time at next scr refresh
        setupNoiseTitleText.setAutoDraw(True)
    
    # *setupNoiseText* updates
    if setupNoiseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupNoiseText.frameNStart = frameN  # exact frame index
        setupNoiseText.tStart = t  # local t and not account for scr refresh
        setupNoiseText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupNoiseText, 'tStartRefresh')  # time at next scr refresh
        setupNoiseText.setAutoDraw(True)
    
    # *setupNoiseNextText* updates
    if setupNoiseNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        setupNoiseNextText.frameNStart = frameN  # exact frame index
        setupNoiseNextText.tStart = t  # local t and not account for scr refresh
        setupNoiseNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(setupNoiseNextText, 'tStartRefresh')  # time at next scr refresh
        setupNoiseNextText.setAutoDraw(True)
    
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
        theseKeys = setupNoiseKey.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _setupNoiseKey_allKeys.extend(theseKeys)
        if len(_setupNoiseKey_allKeys):
            setupNoiseKey.keys = _setupNoiseKey_allKeys[-1].name  # just the last key pressed
            setupNoiseKey.rt = _setupNoiseKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
instructionsKey.keys = []
instructionsKey.rt = []
_instructionsKey_allKeys = []
# keep track of which components have finished
instructionsComponents = [instructionsTitleText, instructionsText, instructionsNextText, instructionsKey]
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
    
    # *instructionsTitleText* updates
    if instructionsTitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionsTitleText.frameNStart = frameN  # exact frame index
        instructionsTitleText.tStart = t  # local t and not account for scr refresh
        instructionsTitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsTitleText, 'tStartRefresh')  # time at next scr refresh
        instructionsTitleText.setAutoDraw(True)
    
    # *instructionsText* updates
    if instructionsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionsText.frameNStart = frameN  # exact frame index
        instructionsText.tStart = t  # local t and not account for scr refresh
        instructionsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsText, 'tStartRefresh')  # time at next scr refresh
        instructionsText.setAutoDraw(True)
    
    # *instructionsNextText* updates
    if instructionsNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionsNextText.frameNStart = frameN  # exact frame index
        instructionsNextText.tStart = t  # local t and not account for scr refresh
        instructionsNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsNextText, 'tStartRefresh')  # time at next scr refresh
        instructionsNextText.setAutoDraw(True)
    
    # *instructionsKey* updates
    waitOnFlip = False
    if instructionsKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionsKey.frameNStart = frameN  # exact frame index
        instructionsKey.tStart = t  # local t and not account for scr refresh
        instructionsKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsKey, 'tStartRefresh')  # time at next scr refresh
        instructionsKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructionsKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructionsKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructionsKey.status == STARTED and not waitOnFlip:
        theseKeys = instructionsKey.getKeys(keyList=['space'], waitRelease=False)
        _instructionsKey_allKeys.extend(theseKeys)
        if len(_instructionsKey_allKeys):
            instructionsKey.keys = _instructionsKey_allKeys[-1].name  # just the last key pressed
            instructionsKey.rt = _instructionsKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
if instructionsKey.keys in ['', [], None]:  # No response was made
    instructionsKey.keys = None
thisExp.addData('instructionsKey.keys',instructionsKey.keys)
if instructionsKey.keys != None:  # we had a response
    thisExp.addData('instructionsKey.rt', instructionsKey.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions2"-------
continueRoutine = True
# update component parameters for each repeat
isntructions2Key.keys = []
isntructions2Key.rt = []
_isntructions2Key_allKeys = []
# keep track of which components have finished
instructions2Components = [instructions2TitleText, instructions2Text, isntructions2NextText, isntructions2Key]
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
    
    # *instructions2TitleText* updates
    if instructions2TitleText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2TitleText.frameNStart = frameN  # exact frame index
        instructions2TitleText.tStart = t  # local t and not account for scr refresh
        instructions2TitleText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2TitleText, 'tStartRefresh')  # time at next scr refresh
        instructions2TitleText.setAutoDraw(True)
    
    # *instructions2Text* updates
    if instructions2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2Text.frameNStart = frameN  # exact frame index
        instructions2Text.tStart = t  # local t and not account for scr refresh
        instructions2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2Text, 'tStartRefresh')  # time at next scr refresh
        instructions2Text.setAutoDraw(True)
    
    # *isntructions2NextText* updates
    if isntructions2NextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        isntructions2NextText.frameNStart = frameN  # exact frame index
        isntructions2NextText.tStart = t  # local t and not account for scr refresh
        isntructions2NextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(isntructions2NextText, 'tStartRefresh')  # time at next scr refresh
        isntructions2NextText.setAutoDraw(True)
    
    # *isntructions2Key* updates
    waitOnFlip = False
    if isntructions2Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        isntructions2Key.frameNStart = frameN  # exact frame index
        isntructions2Key.tStart = t  # local t and not account for scr refresh
        isntructions2Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(isntructions2Key, 'tStartRefresh')  # time at next scr refresh
        isntructions2Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(isntructions2Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(isntructions2Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if isntructions2Key.status == STARTED and not waitOnFlip:
        theseKeys = isntructions2Key.getKeys(keyList=['space'], waitRelease=False)
        _isntructions2Key_allKeys.extend(theseKeys)
        if len(_isntructions2Key_allKeys):
            isntructions2Key.keys = _isntructions2Key_allKeys[-1].name  # just the last key pressed
            isntructions2Key.rt = _isntructions2Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
# check responses
if isntructions2Key.keys in ['', [], None]:  # No response was made
    isntructions2Key.keys = None
thisExp.addData('isntructions2Key.keys',isntructions2Key.keys)
if isntructions2Key.keys != None:  # we had a response
    thisExp.addData('isntructions2Key.rt', isntructions2Key.rt)
thisExp.nextEntry()
# randomise testing language (between-participant)
versions = ['catalan', 'spanish']
versionRandom = random.sample(['catalan', 'spanish'], 1)
print(versionRandom)
if (versionRandom=="catalan"):
    trialsPracticeCatalanReps = 1
    trialsPracticeSpanishReps = 0
    trialsCatalanReps = 1
    trialsSpanishReps = 0
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
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    trialSound.setVolume(1.0, log=False)
    keysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'apostrophe', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'escape', 'space', 'return', 'backspace']
    inputText = ''
    debugText = ''
    isAccented = False
    error = False
    keyPressTime = 0
    wordT = word
    
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
                thisExp.addData('wordT', wordT) # save time
                thisExp.nextEntry()
                i = i+1
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    trialSound.setVolume(1.0, log=False)
    keysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'apostrophe', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'escape', 'space', 'return', 'backspace']
    inputText = ''
    debugText = ''
    isAccented = False
    error = False
    keyPressTime = 0
    wordT = word
    
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
                thisExp.addData('wordT', wordT) # save time
                thisExp.nextEntry()
                i = i+1
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
beginComponents = [beginText, beginNextText]
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
    
    # *beginNextText* updates
    if beginNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        beginNextText.frameNStart = frameN  # exact frame index
        beginNextText.tStart = t  # local t and not account for scr refresh
        beginNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(beginNextText, 'tStartRefresh')  # time at next scr refresh
        beginNextText.setAutoDraw(True)
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    trialSound.setVolume(1.0, log=False)
    keysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'apostrophe', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'escape', 'space', 'return', 'backspace']
    inputText = ''
    debugText = ''
    isAccented = False
    error = False
    keyPressTime = 0
    wordT = word
    
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
                thisExp.addData('wordT', wordT) # save time
                thisExp.nextEntry()
                i = i+1
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    trialSound.setVolume(1.0, log=False)
    keysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'apostrophe', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'escape', 'space', 'return', 'backspace']
    inputText = ''
    debugText = ''
    isAccented = False
    error = False
    keyPressTime = 0
    wordT = word
    
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
                thisExp.addData('wordT', wordT) # save time
                thisExp.nextEntry()
                i = i+1
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
farewellComponents = [farewellText]
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
    # if ESCAPE is pressed, quit experiment
    keys = event.getKeys(keyList = ['escape', 'space'])
    n = len(keys)
    
    if ('escape' in keys):
        core.quit()
    elif ('space' in keys):
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
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
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
