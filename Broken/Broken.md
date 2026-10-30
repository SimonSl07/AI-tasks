In summer break, Gigel went together with his family on vacation to multiple countries. Of course, he brought his camera to capture the beautiful landscapes he saw. After he returned, Gigel, proud of the photos he took, wanted to transfer them to his phone in order to upload them to his blog. Unfortunately, that's when he noticed the camera had a bug due to it's compression algorithm! This led to each image (originally of **512x512** resolution) to be split into **16 tiles** with **128x128** resolution which are scrambled around in the memory.

Gigel, upset but not discouraged, decided to start the grueling work of taking the tiles and rebuilding the original images. He managed to recreate **60 images** from those tiles, which he has put at your disposal, along with some other pieces of data. He then gives you the remaining tiles, which he doesn't have time to rebuild into an image, and asks that for given pairs of tiles (**tile1** and **tile2**), you classify them using the following label:

- label = 0 -> tile1 and tile2 are from **different images**
- label = 1 -> tile1 is **to the left** of tile2 in the original image
- label = 2 -> tile1 is **above** tile2 in the original image
- label = 3 -> tile1 is **to the right** of tile2 in the original image
- label = 4 -> tile1 is **under** tile2 in the original image
- label = 5 -> tile1 and tile2 are part of the **same image**, but **aren't neighbours**

**For labels 1, 2, 3 and 4 tiles must be neighbours (next to each other)**

Gigel does not know much about AI, but he has heard that the **resnet18** is quite good!


### Dataset description

The dataset consists of the following folders:

**training** archive
-  contains the **60** whole images (**512x512**)

**test** archive
- contains the folder **test_tiles** with **320** tiles
- contains the file **test_pairs.csv** describing the pairs of tiles for which you need to predict the labels. The csv contains the following columns:

datapointID | tile1 | tile2 
-|-|-
id of this row of data | id of the first tile | id of the second tile



**starter kit** archive
- contains **starter_kit.ipynb** which provides a small setup to help you with your task
- contains the folder **validation_tiles**, which has **240 tiles** (following the naming convention "id.jpg"), part of the 60 images in **training_data**
- also contains **validation_data.csv**, which has **2470** rows with 4 columns:

tile1 | tile2 | answer
-|-|-
id of this row of data | id of the first tile | id of the second tile | label, as described above


### Subtasks


#### Subtask 1 (40p)
- Due to the large number of tiles, Gigel is happy even if you only predict the label 0 correctly!
- **Objective** - for the given pairs of tiles, as described in **sample_submission.csv**, train a classifier to predict wether the tiles are part of the same image or not
- **Output** -  The labels as described above, although you will not be penalized if you are wrong about the relative placement of the tiles (for example, if you predict label = 3 but the correct label was 1 / 2 / 3 / 4 / 5, it will be marked as correct; but if you predict label = 0, you need the correct label to be 0 for it to be marked as correct)

#### Subtask 2 (60p)
- But Gigel would like to not have to work at all, so he would be even happier if you do the prediction perfectly.
- **Objective** - for the given pairs of tiles, as described in **sample_submission.csv**, train a classifier to predict wether the tiles are part of the same image (**and their relative placement**) or not
- **Output** - The labels as described above

**Output format**

subtaskID | datapointID | answer
-|-|-
id of subtask | id of this row of data | label, as described above

### Scoring

#### Subtask1 (40p)

Baseline score = 0.261
Scoring is based on Macro F1 score, the amount of points awarded being calculated as follows

- Macro F1 score < Baseline score:
     - Points awarded: 4

- Macro F1 score < 0.67:
    - s = normalized score calculated as $(Macro F1 score - baseline) / (0.67 - baseline)$
    - Points awarded: $4 + 36 \cdot ((e^{3s} - 1) / (e^{3} - 1))$
    - Thus, scoring follows an exponential curve, with a minimum score of 4 points

- Macro F1 score >= 0.67:
    - Points awarded: 40

#### Subtask2 (60p)

Baseline score = 0.087
Scoring is based on Macro F1 score, the amount of points awarded being calculated as follows

- Macro F1 score < Baseline score:
     - Points awarded: 6

- Macro F1 score < 0.36:
    - s = normalized score calculated as $(Macro F1 score - baseline) / (0.36 - baseline)$
    - Points awarded: $6 + 54 \cdot ((e^{3s} - 1) / (e^{3} - 1))$
    - Thus, scoring follows an exponential curve, with a minimum score of 6 points

- Macro F1 score >= 0.36:
    - Points awarded: 60