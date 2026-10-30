**Dataset Authors**:
* Columbia Object Image Library (COIL-100)
    S. A. Nene, S. K. Nayar and H. Murase

**Task Author**:
 * Slănină Simon - TU Delft, Olanda

**Statement Authors**: 
* Slănină Simon - TU Delft, Olanda

**Translators**:
* Ionescu Clara - Universitatea Babeș-Bolyai, Cluj-Napoca
* Slănină Simon - TU Delft, Olanda

**Testers**
* Mogovan Jonathan
* Andrei Arhire

### About the Dataset

The dataset contains pictures of objects taken from multiple angles, as well as the angle each picture was taken from.

### About the Task

The core idea is to successfully extract enough information from images in order to correctly predict the angle from which they are observed. There are many ways to do this but one comes out above the rest.

#### Intended solution

We will extract **HOG (Histogram of Oriented Gradient)** data from the images. This fits subtask 2 perfectly as the purpose of HOG is to capture the shape, structure and edges of an object.

We also extract **Color Histograms** as HOG ignores color and thus two objects with similar shape might be mistaken to be the same object in subtask 1. By extracting color data we help mitigate this risk.

By concatenating these features we form the mathematical representations of the images. This can also be done in many other ways, from simple extraction of raw pixel values, to building a CNN model that encodes the images and predicts their angle.

### Subtask 1

We take the feature representations of all three images. For each image, we calculate a "similarity score" by adding its cosine similarity to the other two images. The image with the lowest total score is the "least similar" and must be the intruder.

### Subtask 2

We run the representation of the images through two SVR models, that predict the sine and cosine of the angle for each image. This is done because angles are cyclical, as if the model predicts 0 degrees during training and the actual angle is 359 degrees, it gets heavily penalized, even though it was really close. The outputted angle is reconstructed using the arctangent of the sine and cosine predictions.

Solution:

```py
import os
import cv2
import math
import numpy as np
import pandas as pd
from skimage.feature import hog
from sklearn.svm import SVR
from sklearn.metrics.pairwise import cosine_similarity
import zipfile

with zipfile.ZipFile("test_data.zip", 'r') as zip_ref:
    zip_ref.extractall(path="test_data")

with zipfile.ZipFile("train_data.zip", 'r') as zip_ref:
    zip_ref.extractall(path="train_data")


TRAIN_CSV = "./train_data/train_data.csv"
TRAIN_IMGS_DIR = "./train_data/images/"
TEST_CSV = "./test_data/test_data.csv"
TEST_IMGS_DIR = "./test_data/images/"
OUTPUT_CSV = "submission.csv"

def extract_hog_features(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # HOG parameters
    hog_feats = hog(gray, orientations=9, pixels_per_cell=(32, 32),
                    cells_per_block=(2, 2), block_norm='L2-Hys',
                    visualize=False, feature_vector=True)

    # Calculate histograms for color channels
    hist_b = cv2.calcHist([img], [0], None, [16], [0, 256]).flatten()
    hist_g = cv2.calcHist([img], [1], None, [16], [0, 256]).flatten()
    hist_r = cv2.calcHist([img], [2], None, [16], [0, 256]).flatten()
    
    color_feats = np.concatenate([hist_b, hist_g, hist_r])
    # Normalize color features
    color_feats = color_feats / (np.linalg.norm(color_feats) + 1e-6)

    # Combine features
    return np.concatenate((hog_feats, color_feats))

train_df = pd.read_csv(TRAIN_CSV)

X_train = []
y_sin_train = []
y_cos_train = []

for _, row in train_df.iterrows():
    img_path = os.path.join(TRAIN_IMGS_DIR, row['image'])
    features = extract_hog_features(img_path)
    X_train.append(features)

    angle_rad = math.radians(row['angle'])
    y_sin_train.append(math.sin(angle_rad))
    y_cos_train.append(math.cos(angle_rad))

X_train = np.array(X_train)
y_sin_train = np.array(y_sin_train)
y_cos_train = np.array(y_cos_train)

regr_sin = SVR(kernel='rbf', C=500.0, epsilon=0.01, gamma='scale')
regr_cos = SVR(kernel='rbf', C=500.0, epsilon=0.01, gamma='scale')

regr_sin.fit(X_train, y_sin_train)
regr_cos.fit(X_train, y_cos_train)

test_df = pd.read_csv(TEST_CSV)
submission_data = []

test_features_cache = {}

def get_test_feature(img_name):
    if pd.isna(img_name) or img_name == "":
        return None
    if img_name not in test_features_cache:
        path = os.path.join(TEST_IMGS_DIR, img_name)
        test_features_cache[img_name] = extract_hog_features(path)
    return test_features_cache[img_name]

for _, row in test_df.iterrows():
    subtask_id = int(row['subtaskID'])
    datapoint_id = int(row['datapointID'])

    if subtask_id == 1:
        f1 = get_test_feature(row['img1']).reshape(1, -1)
        f2 = get_test_feature(row['img2']).reshape(1, -1)
        f3 = get_test_feature(row['img3']).reshape(1, -1)

        # Pairwise cosine similarities
        sim_12 = cosine_similarity(f1, f2)[0][0]
        sim_13 = cosine_similarity(f1, f3)[0][0]
        sim_23 = cosine_similarity(f2, f3)[0][0]

        score1 = sim_12 + sim_13
        score2 = sim_12 + sim_23
        score3 = sim_13 + sim_23

        # The minimum score identifies the intruder
        scores = [score1, score2, score3]
        intruder_index = scores.index(min(scores)) + 1

        submission_data.append([subtask_id, datapoint_id, intruder_index])

    elif subtask_id == 2:
        f1 = get_test_feature(row['img1']).reshape(1, -1)

        # Predict sin and cos
        pred_sin = regr_sin.predict(f1)[0]
        pred_cos = regr_cos.predict(f1)[0]

        # Reconstruct the angle using arctan2
        angle_rad = math.atan2(pred_sin, pred_cos)
        angle_deg = math.degrees(angle_rad)

        angle_deg = round(angle_deg) % 360

        submission_data.append([subtask_id, datapoint_id, angle_deg])

sub_df = pd.DataFrame(submission_data, columns=['subtaskID', 'datapointID', 'answer'])
sub_df.to_csv(OUTPUT_CSV, index=False)
```