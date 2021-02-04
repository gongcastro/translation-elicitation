#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Wed May  6 11:51:30 2020
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
expInfo = {'participant': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'Data/%s_%s_%s' % (expName, expInfo['date'], expInfo['participant'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/GonzaloGGC/Desktop/TranslationElicitationSpaTest/TranslationElicitationSpaTest_lastrun.py',
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
    text='PREPARACIÓN',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
setupText = visual.TextStim(win=win, name='setupText',
    text='Por favor, desde ahora hasta el final o abandono del estudio:\n\n - Si es posible, utiliza Chrome o Mozilla.\n\n - Utiliza un ordenador (no una tablet o un teléfono móvil)\n\n - Utiliza auriculares\n\n - Cierra todas las pestañas de tu navegador, excepto esta\n\n - No cambies de pestaña en el navegador\n\nSi, por alguna razón, reinicias el estudio (por ejemplo, al haber actualizado la página o por un corte de internet), háznoslo saber escribiendo a gonzalo.garciadecastro@upf.edu.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
setupTextNext = visual.TextStim(win=win, name='setupTextNext',
    text='Pulsa ESPACIO para continuar >',
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

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcomeTextTitle = visual.TextStim(win=win, name='welcomeTextTitle',
    text='BIENVENIDO/A',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcomeText = visual.TextStim(win=win, name='welcomeText',
    text='Este es un estudio diseñado por investigadores/as de la Universitat Pompeu Fabra (Barcelona, España) y la Universidad de Oxford (Oxford, Reino Unido). Su objetivo es investigar cómo bebés y adultos procesan palabras en una lengua desconocida. Los audios que escucharás durante el estudio están dirigidos a bebés. \n\nSe te ha invitado/a a participar, dado que tienes entre 18 y 40 años, y eres hablante de castellano sin conocimientos de catalán.\n',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
welcomeTextNext = visual.TextStim(win=win, name='welcomeTextNext',
    text='Pulsa ESPACIO para continuar >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "description"
descriptionClock = core.Clock()
descriptionTextTitle = visual.TextStim(win=win, name='descriptionTextTitle',
    text='DESCRIPCIÓN',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
descriptionText = visual.TextStim(win=win, name='descriptionText',
    text='Primero, te pediremos que completes un BREVE CUESTIONARIO sobre tu perfil lingüístico, nivel educativo, etc.\n\nEn el ESTUDIO, escucharás un serie de palabras en catalán. Tu tarea consistirá en ADIVINAR la TRADUCCIÓN de cada palabra en CASTELLANO, y ESCRIBIR tu respuesta utilizando el teclado.\n\nEl estudio durará 30 minutos aproximadamente.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
descriptionTextNext = visual.TextStim(win=win, name='descriptionTextNext',
    text='Pulsa ESPACIO para continuar >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "voluntary"
voluntaryClock = core.Clock()
voluntaryTextTitle = visual.TextStim(win=win, name='voluntaryTextTitle',
    text='¿ES OBLIGATORIO QUE PARTICIPE?',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
voluntaryText = visual.TextStim(win=win, name='voluntaryText',
    text='Tu participación en este estudio es COMPLETAMENTE voluntaria. Podrás abandonar el estudio en cualquier momento pulsando la tecla ESC. Sin embargo, únicamente recibirás la compensación por tu participación si lo completas.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
voluntaryTextNext = visual.TextStim(win=win, name='voluntaryTextNext',
    text='Pulsa ESPACIO para continuar >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "contact"
contactClock = core.Clock()
contactTextTitle = visual.TextStim(win=win, name='contactTextTitle',
    text='CONTACTO',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
contactText = visual.TextStim(win=win, name='contactText',
    text='Si tienes cualquier pregunta sobre este estudio, por favor contacta con el equipo de investigación:\nEmail: gonzalo.garciadecastro@upf.edu\n\nInvestigadores/as Principales: Núria Sebastian-Galles y Kim Plunkett\nInvestigadores: Gonzalo García-Castro y Serene Siow\n\nCenter for Brain and Cognition, Universitat Pompeu Fabra\nDepartment of Experimental Psychology, University of Oxford',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
contactTextNext = visual.TextStim(win=win, name='contactTextNext',
    text='Pulsa ESPACIO para continuar >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "confidentiality"
confidentialityClock = core.Clock()
confidentialityTextTitle = visual.TextStim(win=win, name='confidentialityTextTitle',
    text='CONFIDENCIALIDAD',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
confidentialityText = visual.TextStim(win=win, name='confidentialityText',
    text='Tu respuestas serán completamente ANÓNIMAS, y tomaremos las medidas necesarias para que se mantengan como tal.\n\nSE GUARDARÁN tus datos en un archivo protegido por contraseña y SE PODRÁN UTILIZAR DE MANERA COMPLETAMENTE ANONIMIZADA en publicaciones académicas. NO REGISTRAREMOS tu dirección de IP. Los datos resultantes de este estudio se archivarán durante un mínimo de tres años tras ser publicados.\n\nNos gustaría tener tu permiso para utilizar tus datos anonimizados para estudios futuros y para COMPARTIRLOS con otros equipos de investigación (ej., a través de bases de datos online). SE ELIMINARÁ cualquier información personal que pudiera identificarte O SE REEMPLAZARÁ antes de que los archivos SE COMPARTAN O SE PUBLIQUEN.\n\nEste proyecto HA SIDO APROBADO POR  el Comité de Ètica de la Investigación con Medicamentos (CEIm) del Hospital del Mar.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
confidentialityTextNext = visual.TextStim(win=win, name='confidentialityTextNext',
    text='Pulsa ESPACIO para continuar >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "information"
informationClock = core.Clock()
informationTextTitle = visual.TextStim(win=win, name='informationTextTitle',
    text='¿NECESITAS MÁS INFORMACIÓN?',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
informationText = visual.TextStim(win=win, name='informationText',
    text='Si tienes alguna duda sobre algún aspecto de este estudio, por favor ponte en contacto  con Gonzalo García-Castro (gonzalo.garciadecastro@upf.edu), y haremos lo posible para responder tus preguntas. En caso de que desees hacer una queja formal, por favor, contacta con el/la responsable del Comit de Ètica de Investigación con Medicamentos (CEIm) del Hospital del Mar, quien tratará de resolver el problema cuanto antes.\n\nComité de Ética de Investigación con Medicamentos (CEIm), Hospital del Mar;\nEmail: ceic-psmar@imim.es',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
informationTextNext = visual.TextStim(win=win, name='informationTextNext',
    text='Pulsa ESPACIO para continuar >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "consent"
consentClock = core.Clock()
consentTextTitle = visual.TextStim(win=win, name='consentTextTitle',
    text='CONSENTIMIENTO INFORMADO',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
consentText = visual.TextStim(win=win, name='consentText',
    text='AL PRESIONAR LA TECLA DEL ESPACIO, doy mi consentimiento para participar en este estudio. He tomado esta decisión basándome en la información que he leído en el consentimiento informado. He tenido la oportunidad de recibir información adicional sobre el estudio, y comprendo que podré pedir más información en el futuro. Comprendo que puedo retirar este consentimiento en cualquier momento.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
consentTextNext = visual.TextStim(win=win, name='consentTextNext',
    text='Pulsa ESPACIO para continuar >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
consentKey = keyboard.Keyboard()

# Initialize components for Routine "languageL1"
languageL1Clock = core.Clock()
languageL1TextTitle = visual.TextStim(win=win, name='languageL1TextTitle',
    text='CUESTIONARIO DE LENGUAS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL1Text = visual.TextStim(win=win, name='languageL1Text',
    text='¿Cuál es tu lengua NATIVA?\n\ne) Español/Castellano\nc) Catalán\ni) Inglés\no) Otra\n\nPor favor, presiona la letra correspondiente.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL1TextNext = visual.TextStim(win=win, name='languageL1TextNext',
    text='Por favor, presiona la letra correspondiente.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL1Key = keyboard.Keyboard()

# Initialize components for Routine "languageL2"
languageL2Clock = core.Clock()
languageL2TextTitle = visual.TextStim(win=win, name='languageL2TextTitle',
    text='CUESTIONARIO DE LENGUAS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL2Text = visual.TextStim(win=win, name='languageL2Text',
    text='¿Conoces una SEGUNDA LENGUA, distinta de la que has indicado anteriormente? Si es así, escribe cuál y presiona ENTER. Si no, presiona ENTER sin escribir nada.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL2TextNext = visual.TextStim(win=win, name='languageL2TextNext',
    text='Presiona ENTER para continuar.',
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
    text='CUESTIONARIO DE LENGUAS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL2OralText = visual.TextStim(win=win, name='languageL2OralText',
    text='En una escala de 1-5, ¿cómo puntuarías tu capacidad de COMPRENSIÓN ORAL de tu SEGUNDA LENGUA?\n\n1) No entiendo prácticamente nada\n2) Entiendo algunas palabras\n3) Entiendo de qué va la conversación/algunas frases\n4) Entiendo casi todo\n5) Como un/a nativo/a o soy nativo/a\n',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL2OralTextNext = visual.TextStim(win=win, name='languageL2OralTextNext',
    text='Por favor, presiona el número correspondiente.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL2OralKey = keyboard.Keyboard()

# Initialize components for Routine "languageL2Written"
languageL2WrittenClock = core.Clock()
languageL2WrittenTextTitle = visual.TextStim(win=win, name='languageL2WrittenTextTitle',
    text='CUESTIONARIO DE LENGUAS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL2WrittenText = visual.TextStim(win=win, name='languageL2WrittenText',
    text='En una escala de 1-5, ¿cómo puntuarías tu ORTOGRAFÍA en tu SEGUNDA LENGUA?\n\n1) No he recibido educación en la ortografía de esta lengua\n2) Cometo muchas faltas de ortografía\n3) Cometo bastantes faltas de ortografía\n4) Cometo algunas faltas de ortografía\n5) No cometo ninguna falta de ortografía',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL2WrittenTextNext = visual.TextStim(win=win, name='languageL2WrittenTextNext',
    text='Por favor, presiona el número correspondiente.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL2WrittenKey = keyboard.Keyboard()

# Initialize components for Routine "languageL3"
languageL3Clock = core.Clock()
languageL3TextTitle = visual.TextStim(win=win, name='languageL3TextTitle',
    text='CUESTIONARIO DE LENGUAS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL3Text = visual.TextStim(win=win, name='languageL3Text',
    text='¿Conoces una TERCERA LENGUA, distinta de la que has indicado anteriormente? Si es así, escribe cuál y presiona ENTER. Si no, presiona ENTER sin escribir nada.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL3TextNext = visual.TextStim(win=win, name='languageL3TextNext',
    text='Presiona ENTER para continuar.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
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
    text='CUESTIONARIO DE LENGUAS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL3OralText = visual.TextStim(win=win, name='languageL3OralText',
    text='En una escala de 1-5, ¿cómo puntuarías tu capacidad de COMPRENSIÓN ORAL de tu TERCERA LENGUA?\n\n1) No entiendo prácticamente nada\n2) Entiendo algunas palabras\n3) Entiendo de qué va la conversación/algunas frases\n4) Entiendo casi todo\n5) Como un/a nativo/a o soy nativo/a',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL3OralTextNext = visual.TextStim(win=win, name='languageL3OralTextNext',
    text='Por favor, presiona el número correspondiente.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL3OralKey = keyboard.Keyboard()

# Initialize components for Routine "languageL3Written"
languageL3WrittenClock = core.Clock()
languageL3WrittenTextTitle = visual.TextStim(win=win, name='languageL3WrittenTextTitle',
    text='CUESTIONARIO DE LENGUAS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageL3WrittenText = visual.TextStim(win=win, name='languageL3WrittenText',
    text='En una escala de 1-5, ¿cómo puntuarías tu ORTOGRAFÍA en tu TERCERA LENGUA?\n\n1) No he recibido educación en la orografía de esta lengua\n2) Cometo muchas faltas de ortografía\n3) Cometo bastantes faltas de ortografía\n4) Cometo algunas faltas de ortografía\n5) No cometo ninguna falta de ortografía',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageL3WrittenTextNext = visual.TextStim(win=win, name='languageL3WrittenTextNext',
    text='Por favor, presiona el número correspondiente.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageL3WrittenKey = keyboard.Keyboard()

# Initialize components for Routine "languageCatalanOral"
languageCatalanOralClock = core.Clock()
languageCatalanOralTextTitle = visual.TextStim(win=win, name='languageCatalanOralTextTitle',
    text='CUESTIONARIO DE LENGUAS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageCatalanOralText = visual.TextStim(win=win, name='languageCatalanOralText',
    text='En una escala de 1-5, ¿cómo puntuarías tu capacidad de COMPRENSIÓN ORAL en CATALÁN?\n\n1) No entiendo prácticamente nada\n2) Entiendo algunas palabras\n3) Entiendo de qué va la conversación/algunas frases\n4) Entiendo casi todo\n5) Como un/a nativo/a o soy nativo/a',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageCatalanOralTextNext = visual.TextStim(win=win, name='languageCatalanOralTextNext',
    text='Por favor, presiona el número correspondiente.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageCatalanOralKey = keyboard.Keyboard()

# Initialize components for Routine "languageCatalanWritten"
languageCatalanWrittenClock = core.Clock()
languageCatalanWrittenTextTitle = visual.TextStim(win=win, name='languageCatalanWrittenTextTitle',
    text='CUESTIONARIO DE LENGUAS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageCatalanWrittenText = visual.TextStim(win=win, name='languageCatalanWrittenText',
    text='En una escala de 1-5, ¿cómo puntuarías tu ORTOGRAFÍA en CATALÁN?\n\n1) No he recibido educación en la orografía de esta lengua\n2) Cometo muchas faltas de ortografía\n3) Cometo bastantes faltas de ortografía\n4) Cometo algunas faltas de ortografía\n5) No cometo ninguna falta de ortografía',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageCatalanWrittenTextNext = visual.TextStim(win=win, name='languageCatalanWrittenTextNext',
    text='Por favor, presiona el número correspondiente.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageCatalanWrittenKey = keyboard.Keyboard()

# Initialize components for Routine "languageCatalanTime"
languageCatalanTimeClock = core.Clock()
languageCatalanTimeTextTitle = visual.TextStim(win=win, name='languageCatalanTimeTextTitle',
    text='CUESTIONARIO DE LENGUAS',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
languageCatalanTimeText = visual.TextStim(win=win, name='languageCatalanTimeText',
    text='¿Cuánto tiempo has pasado en REGIONES donde se habla CATALÁN (Cataluña, Comunidad Valenciana, Islas Baleares), incluyendo tu infancia? Escoge la opción que mejor describe tu situación:\n\n1) Nunca o menos de 1 mes\n2) Entre 1 y 3 meses\n3) Solía pasar las vacaciones allí\n4) He vivido allí por menos de 6 meses\n5) He vivido allí por 6 o más meses',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
languageCatalanTimeTextNext = visual.TextStim(win=win, name='languageCatalanTimeTextNext',
    text='Por favor, presiona el número correspondiente.',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
languageCatalanTimeKey = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsTextTitle = visual.TextStim(win=win, name='instructionsTextTitle',
    text='INSTRUCCIONES',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructionsText = visual.TextStim(win=win, name='instructionsText',
    text='A continuación escucharás palabras EN CATALÁN a través de tus auriculares.\n\nLas palabras estarán en CATALÁN y han sido grabadas como si estuvieran dirigidas a bebés.\n\nTendrás que adivinar la TRADUCCIÓN DE CADA PALABRA AL CASTELLANO.\n\nEmpieza a escribir TAN PRONTO como tengas una respuesta. Es muy posible que no la sepas. Escribe lo que creas que es más probable.\n\nDebes escribir una respuesta PARA CADA PALABRA.\n\nCORRIGE errores utilizando la TECLA de BORRAR como lo harías normalmente.\n\nTras escribir la traducción, presiona ENTER para continuar con la siguiente palabra.\n\n\nA CONTINUACIÓN COMPLETARÁS 5 ENSAYOS DE PRÁCTICA',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructionsTextNext = visual.TextStim(win=win, name='instructionsTextNext',
    text='Pulsa ESPACIO para continuar >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instructionsKeys = keyboard.Keyboard()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instructions2TextTitle = visual.TextStim(win=win, name='instructions2TextTitle',
    text='INSTRUCCIONES',
    font='Arial',
    pos=(0, 0.8), height=0.11, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructions2Text = visual.TextStim(win=win, name='instructions2Text',
    text='Ajusta el volumen para que las palabras se oigan de forma clara durante estos ensayos de práctica, para evitar tener que hacerlo durante el experimento.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructions2TextNext = visual.TextStim(win=win, name='instructions2TextNext',
    text='Presiona ESPACIO para comenzar los 5 ensayos de PRACTICA >',
    font='Arial',
    pos=(0.7, -0.8), height=0.06, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixationText = visual.TextStim(win=win, name='fixationText',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.13, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
taskText = visual.TextStim(win=win, name='taskText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.13, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trialSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='trialSound')
trialSound.setVolume(1)

# Initialize components for Routine "begin"
beginClock = core.Clock()
beginText = visual.TextStim(win=win, name='beginText',
    text='Has finalizado los ensayos de PRÁCTICA.',
    font='Arial',
    pos=(0, 0.8), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
beginNext = visual.TextStim(win=win, name='beginNext',
    text='Presiona ESPACIO para COMENZAR >',
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
    pos=(0, 0), height=0.13, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
taskText = visual.TextStim(win=win, name='taskText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.13, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trialSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='trialSound')
trialSound.setVolume(1)

# Initialize components for Routine "farewell"
farewellClock = core.Clock()
farewellText = visual.TextStim(win=win, name='farewellText',
    text='¡Enhorabuena!\n\nHas terminado.\n\nMUCHAS GRACIAS POR TU PARTICIPACIÓN.\n\nTu ID de participante es:\n\n\n\nPor favor, ponte en contacto con nosotros para recoger tu compensación:\n\ngonzalo.garciadecastro@upf.edu\n',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
farewellTextNext = visual.TextStim(win=win, name='farewellTextNext',
    text='Pulsa ESPACIO o ESC para salir >',
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
        theseKeys = languageL1Key.getKeys(keyList=['e', 'c', 'i', 'o', 'escape'], waitRelease=False)
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
        languageL2TextInput.setText('>' + inputText, log=False)
    keys = event.getKeys()
    i = 0 # index whether how many keys have been previously pressed
    
    # Keys are mapped onto a Spanish keyboard
    
    if len(keys): # if any key has been pressed...
    
         # ... and ESCAPE is pressed, quit experiment
        if keys[i]=='escape':
            thisExp.addData('languageL2', inputText) # save data
            core.quit()
            # ... and RETURN is pressed, stop trial
        if (keys[i]=='return'):
            language2 = inputText
            thisExp.addData('languageL2', inputText) # save data
            continueRoutine = False 
        # ... and BACKSPACE is pressed, delete last character
        elif (keys[i]=='backspace'):
            inputText = inputText[:-1]
        # and 'minus' is pressed, add apostrophe
        elif (keys[i]=='minus'):
            inputText += "'"
        elif (keys[i]=='semicolon'): # if 'semicolon' is pressed, write 'ñ'
            inputText += '\u00d1' 
        # and 'apostrophe' is pressed, flag accent
        elif (keys[i]=='apostrophe'):
            isAccented = True
        # ... and any other allowed key is pressed, print it
        elif (isAccented): # if accent is flagged
            if keys[i]=='a': # and 'a' is pressed
                inputText += '\u00c1' # write "Á"
                isAccented = False # remove accent flag for subsequent keys
            elif (keys[i]=='e'): # and 'e' is pressed
                inputText += '\u00c9'# write "É"
                isAccented = False # remove accent flag for subsequent keys
            elif (keys[i]=='i'): # and 'i' is pressed
                inputText += '\u00cd' # write "Í"
                isAccented = False # remove accent flag for subsequent keys
            elif (keys[i]=='o'): # and 'o' is pressed
                inputText += '\u00d3' # write "Ó"
                isAccented = False # remove accent flag for subsequent keys
            elif (keys[i]=='u'): # and 'u' is pressed
                inputText += '\u00da' # write "Ú"
                isAccented = False # remove accent flag for subsequent keys
            else:
                isAccented = False
                
            thisExp.addData('languageL2', inputText) # save data
            i = i + 1 # index another key press
                
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
if inputText=='':
    languageL2 =  ''
else:
    languageL2 = inputText
# the Routine "languageL2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "languageL2Oral"-------
continueRoutine = True
# update component parameters for each repeat
languageL2OralKey.keys = []
languageL2OralKey.rt = []
_languageL2OralKey_allKeys = []
if languageL2=='':
    continueRoutine = False
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
if languageL2=='':
    continueRoutine = False
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
if languageL2=='':
    continueRoutine = False
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
        languageL3TextInput.setText('>' + inputText, log=False)
    keys = event.getKeys()
    i = 0 # index whether how many keys have been previously pressed
    
    # keys are mapped onto a Spanish keyboard
    
    if len(keys): # if any key has been pressed...
    
         # ... and ESCAPE is pressed, quit experiment
        if keys[i]=='escape':
            thisExp.addData('languageL2', inputText) # save data
            core.quit()
            # ... and RETURN is pressed, stop trial
        elif (keys[i]=='return'):
            language2 = inputText
            thisExp.addData('languageL2', inputText) # save data
            continueRoutine = False
        # ... and BACKSPACE is pressed, delete last character
        elif (keys[i]=='backspace'):
            inputText = inputText[:-1]
        # and 'minus' is pressed, add apostrophe
        elif (keys[i]=='minus'):
            inputText += "'"
        elif (keys[i]=='semicolon'): # if 'semicolon' is pressed, write 'ñ'
            inputText += '\u00d1'
        # and 'apostrophe' is pressed, flag accent
        elif (keys[i]=='apostrophe'):
            isAccented = True
        # ... and any other allowed key is pressed, print it
        elif (isAccented): # if accent is flagged
            if keys[i]=='a': # and 'a' is pressed
                inputText += '\u00c1' # write "Á"
                isAccented = False # remove accent flag for subsequent keys
            elif (keys[i]=='e'): # and 'e' is pressed
                inputText += '\u00c9'# write "É"
                isAccented = False # remove accent flag for subsequent keys
            elif (keys[i]=='i'): # and 'i' is pressed
                inputText += '\u00cd' # write "Í"
                isAccented = False # remove accent flag for subsequent keys
            elif (keys[i]=='o'): # and 'o' is pressed
                inputText += '\u00d3' # write "Ó"
                isAccented = False # remove accent flag for subsequent keys
            elif (keys[i]=='u'): # and 'u' is pressed
                inputText += '\u00da' # write "Ú"
                isAccented = False # remove accent flag for subsequent keys
            else:
                isAccented = False
    
            thisExp.addData('languageL2', inputText) # save data
            i = i + 1 # index another key press
    
        else:
            # write key as it is (in capital letters)
            inputText += keys[i].upper()
            thisExp.addData('languageL2', inputText) # save data
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
if inputText=='':
    languageL3 = ''
else:
    languageL3 = inputText
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
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials/01_trials_practice.xlsx'),
    seed=None, name='trials_practice')
thisExp.addLoop(trials_practice)  # add the loop to the experiment
thisTrials_practice = trials_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
if thisTrials_practice != None:
    for paramName in thisTrials_practice:
        exec('{} = thisTrials_practice[paramName]'.format(paramName))

for thisTrials_practice in trials_practice:
    currentLoop = trials_practice
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
    if thisTrials_practice != None:
        for paramName in thisTrials_practice:
            exec('{} = thisTrials_practice[paramName]'.format(paramName))
    
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
    keysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'semicolon', 'apostrophe', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'escape', 'space', 'return', 'backspace']
    inputText = ''
    debugText = ''
    isAccented = False
    error = False
    # keep track of which components have finished
    trialComponents = [taskText, trialSound]
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
        
        # *taskText* updates
        if taskText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskText.frameNStart = frameN  # exact frame index
            taskText.tStart = t  # local t and not account for scr refresh
            taskText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskText, 'tStartRefresh')  # time at next scr refresh
            taskText.setAutoDraw(True)
        if taskText.status == STARTED:  # only update if drawing
            taskText.setText('> ' + inputText, log=False)
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
                debugText += ' ' + keys[i]
            
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
                
                elif 'minus' in keys[i]: # 
                    inputText += "'" #add apostrophe
                    
                elif 'apostrophe' in keys[i]: # and it's apostrophe
                    isAccented = True # flag 'accent' for subsequent keys
        
                elif 'semicolon' in  keys[i]: # if 'semicolon' is pressed
                    inputText += '\u00d1' # write 'ñ'
                
                else:
                    if isAccented: # and accent is flagged
                        if 'a' in keys[i]: # and 'a' is pressed
                            inputText += '\u00c1' # write "á"
                            isAccented = False # remove accent flag for subsequent keys
                        elif 'e' in keys[i]: # and 'e' is pressed
                            inputText += '\u00c9'# write "é"
                            isAccented = False # remove accent flag for subsequent keys
                        elif 'i' in keys[i]: # and 'i' is pressed
                            inputText += '\u00cd' # write "í"
                            isAccented = False # remove accent flag for subsequent keys
                        elif 'o' in keys[i]: # and 'ó' is pressed
                            inputText += '\u00d3' # write "ó"
                            isAccented = False # remove accent flag for subsequent keys
                        elif 'u' in keys[i]: # and 'u' is pressed
                            inputText += '\u00da' # write "ú"
                            isAccented = False # remove accent flag for subsequent keys
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
    trials_practice.addData('trialSound.started', trialSound.tStartRefresh)
    trials_practice.addData('trialSound.stopped', trialSound.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_practice'


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
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Trials/02_trials_catalan.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
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
    keysAllowed = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'semicolon', 'apostrophe', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'escape', 'space', 'return', 'backspace']
    inputText = ''
    debugText = ''
    isAccented = False
    error = False
    # keep track of which components have finished
    trialComponents = [taskText, trialSound]
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
        
        # *taskText* updates
        if taskText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            taskText.frameNStart = frameN  # exact frame index
            taskText.tStart = t  # local t and not account for scr refresh
            taskText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(taskText, 'tStartRefresh')  # time at next scr refresh
            taskText.setAutoDraw(True)
        if taskText.status == STARTED:  # only update if drawing
            taskText.setText('> ' + inputText, log=False)
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
                debugText += ' ' + keys[i]
            
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
                
                elif 'minus' in keys[i]: # 
                    inputText += "'" #add apostrophe
                    
                elif 'apostrophe' in keys[i]: # and it's apostrophe
                    isAccented = True # flag 'accent' for subsequent keys
        
                elif 'semicolon' in  keys[i]: # if 'semicolon' is pressed
                    inputText += '\u00d1' # write 'ñ'
                
                else:
                    if isAccented: # and accent is flagged
                        if 'a' in keys[i]: # and 'a' is pressed
                            inputText += '\u00c1' # write "á"
                            isAccented = False # remove accent flag for subsequent keys
                        elif 'e' in keys[i]: # and 'e' is pressed
                            inputText += '\u00c9'# write "é"
                            isAccented = False # remove accent flag for subsequent keys
                        elif 'i' in keys[i]: # and 'i' is pressed
                            inputText += '\u00cd' # write "í"
                            isAccented = False # remove accent flag for subsequent keys
                        elif 'o' in keys[i]: # and 'ó' is pressed
                            inputText += '\u00d3' # write "ó"
                            isAccented = False # remove accent flag for subsequent keys
                        elif 'u' in keys[i]: # and 'u' is pressed
                            inputText += '\u00da' # write "ú"
                            isAccented = False # remove accent flag for subsequent keys
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
    trials.addData('trialSound.started', trialSound.tStartRefresh)
    trials.addData('trialSound.stopped', trialSound.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


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
