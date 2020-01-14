from utils import data_preprocessing
from utils.jaccard import jaccard
from predictions.SVM_Classifier import SVM_Classifier
from predictions.UNet import UNet
from draw_mass import drawer

import os
import cv2 as cv
import numpy as np
from PIL import Image

############################ PATH DEFINITION ############################
nomass_path = "dataset/images/nomass"
mass_path = "dataset/images/mass"
overlay_path = "dataset/overlay"
test_path = "dataset/test"
mask_path = "dataset/masks"
ground_path = "dataset/groundtruth/groundtruth"
################################   END   ################################
'''
# STEP 1:   Extracting the features from the training set in order to fit the SVM classifier. This step ends with a list of
#           predicted masses (it is also shown the accuracy of the classifier).
classifier = SVM_Classifier(nomass_path, mass_path, overlay_path, mask_path, ground_path, test_path)
classifier.labelling()
classifier.extract_features()
classifier.train_classifier()
predicted_mass, path_predicted_mass = classifier.prediction()

#STEP 2:    Pre-processing of the images to enhance internal structures, before to give them to the Neural Net.
predicted_mass = data_preprocessing.preprocessing(predicted_mass)
predicted_mass = data_preprocessing.cropping(mask_path, predicted_mass, path_predicted_mass)

#STEP 3:    Loading the U-Net model and predicting masses of test set
unet = UNet()
predictions = unet.unet_predict(predicted_mass)
'''

predictions = []
predicted_mass = []
path_predicted_mass = os.listdir("dataset/unet_input")
path_predictions = os.listdir("dataset/predictions")

for p in path_predicted_mass:
    path = "dataset/unet_input/" + p
    img = cv.imread(path, cv.IMREAD_ANYDEPTH)
    predicted_mass.append(img)

for p in path_predictions:
    path = "dataset/predictions/" + p
    img = cv.imread(path, cv.IMREAD_ANYDEPTH)
    predictions.append(img)

segmented_images = drawer.clean_unet_images(predicted_mass, predictions)
outcomes, ground_images = drawer.my_draw_contours(segmented_images, ground_path, path_predicted_mass)


'''
#STEP 4:    Segmentation process and final output
segmented_images = drawer.clean_unet_images(predicted_mass, predictions)
outcomes, ground_images = drawer.my_draw_contours(segmented_images)

while(1):
    cv.imshow("outc", outcomes[0])
    cv.imshow("ground", ground_images[0])
    key = cv.waitKey(1)
    if key == 27:
        break

#STEP 5:    Evaluating performance
#jaccard_list, average = jaccard(ground_images, path_predicted_mass)
'''