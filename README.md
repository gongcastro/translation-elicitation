# TranslationElicitation [[report]](https://github.com/bilingual-project/translation-elicitation/blob/master/Rmd/report.md)

Translation Elicitation task targeted at monolingual participants. This repository hosts the code for the behavioural task, and survey templates used to collect data on linguistic profiles. The behavioural task was written using PsychoPy, and implemented online via Pavlovia. We will collect reaction times and accuracy measures from participants. These data will be used to train and validate an algorithm aimed at computing a featured-based measure of phonological overlap across translation equivalents. This repository is organised as follows:

* **Data**: Raw, processed, and coded data from the behavioural task.
* **Figures**: Figures resulting from the scripts.
* **R**: R scripts used to preprocess and analyse the data.
* **Results**: Outputs of the models.
* **Rmd**: Rmarkdown files and outputs for the manuscript and lab notes.
* **Stan**: Stan code used to fit the Bayesian models (called via the R scripts).
* **Stimuli**: Stimuli and trial lists used in the behavioural task.

The file `.gitignore` indicates Git what files/subfolders must *not* be kept track of (for privacy and storage limit, e.g., audios).

The experimental set up and code (PsychoPy/Pavlovia) are stored in the following GitLab repositories:

* Version in Catalan for **Spanish speakers**: https://gitlab.pavlovia.org/gongcastro/translationelicitationspa
* Version in Spanish or Catalan for **English speakers**: https://gitlab.pavlovia.org/SiowSerene/translationelicitation_eng 
