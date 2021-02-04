# TranslationElicitation

Translation Elicitation task targeted at monolingual participants. This repository hosts the code for the behavioural task, and survey templates used to collect data on linguistic profiles. The behavioural task was written using PsychoPy, and implemented online via Pavlovia. We will collect reaction times and accuracy measures from participants. These data will be used to train and validate an algorithm aimed at computing a featured-based measure of phonological overlap across translation equivalents. This repository is organised as follows:

* **Code**: Scripts used to implement the online behavioural task in PsychoPy/Pavlovia (`.py`, `.psyexp` and `.js` files in the *Experiment* folder), to implement the feature similarity algorithm (`.ipynb` file in the *Algorithm* folder), and to process and analyse the data (`.R` files in the main subfolder, `te_analysis.R` is the main script, `te_functions.R` contains helper functions). The `.R` other files are outdated versions.
* **Manuscript**: Reproducible manuscript written using `Rmarkdown` via the `papaja` R package (`.Rmd` files), and BibText file `bib` containing the references for the manuscript.
* **Media**: Files use to recruit participants.
* **Data**: Raw, processed, and coded data from the behavioural task, and outputs of the feature similarity algorithm.
* **Figures**: Figures resulting from the scripts.
* **Results**: Outputs of the models.
* **Stimuli**: Stimuli and trial lists used in the behavioural task. The file `trials.xlsx` contains all the relevant information about the words and stimuli. Other properties of the audios are stored in the subfolders *Formatns* and *Pitch*.

The file `.gitignore` indicates Git what files/subfolders must *not* be kept track of (for privacy and storage limit, e.g., audios).

