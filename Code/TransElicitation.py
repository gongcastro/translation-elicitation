'''

Translation Elicitation task
@ author Gonzalo García-Castro
2020-03-09

'''
#### set up ############################################################

# import packages
print('[SETUP] Import packages')
import sys # import system
from psychopy import core, visual, gui, data, event # import modules
import psychtoolbox as ptb # import psychtoolbox and rename it
from psychopy import sound
import soundfile as sf # import sound device
import os # operative system settings
import random
 from psychopy.hardware import keyboard
from psychopy import logging
from psychopy.tools.filetools import fromFile, toFile

# set logs
print('[SETUP] Set logs')
logging.console.setLevel(logging.WARNING)
lastLog = logging.LogFile("lastRun.log", level=logging.INFO, filemode='w')

# define experimental parameters
print('[SETUP] Define experimental parameters')

# define keyboard keys
print('[SETUP] Define keys')
kb = keyboard.Keyboard()
keyQuit = 'escape'
keyOK = 'return'
keyNext = 'space'
keyPreviousPage = 'left'
keyNextPage = 'right'
keys = kb.getKeys(['return', 'space', 'q', 'scape']) # define keys
keysTrial = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ñ', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

# session details
print('[SETUP] Experimental session')

try:  # try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:
    expInfo = {'Experiment': 'TransElicitation'}
    expInfoDlg = gui.Dlg(title = "Translation Elicitation task", labelButtonOK = u"OK", labelButtonCancel=u"Cancel")
    expInfoDlg.addFixedField('Date', data.getDateStr(format="%Y-%m-%d_%H%M"))
    expInfoDlg.addText('Participant information', color = "blue")
    expInfoDlg.addField('ParticipantID', '')
    expInfoDlg.addField('Sex', choices = ["Male", "Female", "Other"])
    expInfoDlg.addField('DateBirth')
    expInfoDlg.addField('City', choices = ["Barcelona", "Madrid", "Oxford", "London"])
    expInfoDlg.addText('LangProf', color = "blue")
    expInfoDlg.addField('Language', choices = ["Spanish", "Catalan", "English"])
    expInfoDlg.addText('Please, rate you proficiency in each language:\n0 = No experience, 10 = Native speaker')
    expInfoDlg.addField('EngProf', 0)
    expInfoDlg.addField('CatProf', 0)
    expInfoDlg.addField('SpaProf', 0)
    expInfo = expInfoDlg.show()  # show dialog and wait for OK or Cancel
    if expInfoDlg.OK:
        expInfo = ['TransElicitation'] + expInfo
        print(expInfo)
    else:
        print('User cancelled')
        core.quit()

# open results file
print('[SETUP] Open results page')
fileName = '{}_{}_{}.csv'.format(expInfo[0], expInfo[1], expInfo[2]) # file name
dataFile = open(fileName, 'w') #open file
dataFile.write('ParticipantID,TrialNum,TrialID,Word,KeyPress,RT\n') # write header


#### configure window #########################################
print('[SETUP] Define window')
win = visual.Window([1000, 1000],
                    color=(-1, -1, -1),
                    monitor = "testMonitor",
                    allowGUI=False,
                    winType='pyglet',
                    gammaErrorPolicy='ignore'
                    ) # define window

#### configure sound ###########################################
deviceID = None
mode = 1 # playback only
reqLatencyClass = 2 # take full control of audio device
freq = 48000 # audio sampling rate
channels = 2 # audio is stereo
bufferSize = 0
suggestedLatency = None
selectedChannels = []
specialFlags = 0
audioVolume = 0.3
audioLeft = 0
audioRight = 1
pahandle_ = ptb.PsychPortAudio('Open', deviceID, mode, reqLatencyClass, freq, channels, bufferSize, suggestedLatency, selectedChannels)
ptb.PsychPortAudio('Volume', pahandle_, audioVolume)

#### experimental parameters ###################################
exp = data.ExperimentHandler(name = 'TransElicitation',
                             version = '0.0.1',
                             extraInfo = expInfo
                             )
#### trial parameters ##########################################
trialList = data.importConditions('trials.xlsx')
trials = data.TrialHandler(nReps = 1,
                           method = 'fullRandom',
                           trialList = trialList,
                           seed = None,
                           name = 'trials')

exp.addLoop(trials)  # add the loop to the experiment

#### create stimuli ############################################
print('[SETUP] Prepare stimuli')
welcomeText = '¡Hola! A continuación escucharás una serie de palabras en catalán.\n\nDebes intentar traducir cada palabra al español.\n\nTras escuchar una palabra en catalán, deberás escribir su equivalente en español lo más rápido que puedas.\n\n¡Intenta escribir la palabra correctamente!\n'
welcomeWin = visual.TextStim(win = win, text = welcomeText, color = 'white', bold = True, units = 'pix', height = 40)
trialText = visual.TextStim(win, pos = [0, 0], text = '+', color = 'yellow')
#fixationCross = visual.ShapeStim(win, lineWidth=1, pos=[0, 0], size=1, lineColor='yellow', vertices='cross', closeShape=True)

#### start experiment ##########################################

#### 0. Start clock
globalClock = core.Clock()
trialClock = core.Clock()

#### 1. Welcome
print('[WELCOME] Welcome page')
while True:

    welcomeWin.draw()
    win.flip()
    keyPress = event.waitKeys() 
    if keyNext in keyPress:
        if keyQuit in keyPress:
            print('[WELCOME] User quitted the session')
            core.quit()
        else:
            break

#### 2. Trials
print('[TASK] Start main routine')

print('[TASK] Draw window')
maxTrialDuration = 7.0 # max duration of trials
trialTimer = core.Clock() # start timer
trialNum = 1 # set chronological trial to 0

# start trials routine
for i in trials:
    win.flip()
    core.wait(2.0)
    print('[TASK %i] Start trial' % (trialNum))
    trialContinues = True
    trialTimer.reset() # restart timer

    while trialTimer.getTime() <= maxTrialDuration:

        if trialTimer.getTime() < 2.0:
            trialText.setText('+') # prepare fixation cross
            trialText.draw() # draw fixation cross
            win.flip() # show fixation cross

        elif 2.0 <= trialTimer.getTime():
            trialText.setText(trials.trialList[trials.thisIndex]['Word']) # prepare word
            trialText.draw() # draw word
            win.flip() # show word
            keyPress = event.getKeys()
            rt = trialTimer.getTime()
            
            if keyPress and keyQuit in keyPress:
                print('[TASK Trial %i] Session quitted by user' % (trialNum))
                core.quit()
                
            elif keyPress and keysTrial in keyPress:
                key = keyPress[0]
                print('[TASK Trial %i] KeyPress: %s, Time: %.4f' % (trialNum, key, rt))
                dataFile.write('%s,%i,%i,%s,%s,%.4f\n' % (expInfo[2], trialNum, trials.trialList[trials.thisIndex]['TrialID'], trials.trialList[trials.thisIndex]['Word'], key, rt))
                trialContinues = False
    
    print('[TASK Trial %i] End trial' % (trialNum))
    if not keyPress:
        dataFile.write('%s,%i,%i,%s,%s,%i\n' % (expInfo[2], trialNum, trials.trialList[trials.thisIndex]['TrialID'], trials.trialList[trials.thisIndex]['Word'], 'NA', -1))
    trialNum = trialNum+1
    ptb.PsychPortAudio('Stop', pahandle_)




#### save data ######################################################
print('[END] Export data')
dataFile.close()
core.quit()
win.close()
print('[END] Experiment finished successfully')



