<img align="center" src="AUGURY_logo.png" width="421" height="200" />

# Work Assignment - Machine Learning Developer
## Overview
The task we wish to tackle is speaker gender classification. The task is a well known and basic task of speech processing, and is often a preliminary stage before higher-order tasks such as speaker diarization.

We are looking at a binary classification task, based on 100 auditory features.
The dataset consists of a training set with 1515 audio recordings and a test set with 460 audio recordings. Unfortunately, the names and origins of the features were lost, and we can’t reproduce which features are more or less relevant, and need to learn it from the data.

In addition, we don’t have accurate labels - we hired 5 annotators, 
each with a different level of skill in speaker gender classification, who gave us their best opinions.
Since the task is relatively simple, we expect all annotators to be better than
chance, but some may be worse than others.
We need to decide on a ground truth for the data given the feedback we have.

Note that there might not be the same amount of male and female speakers in the training data - 
it's hard to know exactly without accurate ground truth, but one class seems more populated than the other. 
Despite this, we want to avoid our classifier having a bias towards one of the classes - we want to be equally accurate on both genders, as in a real world setting we expect the distribution to be more or less 50-50.

## Task
Classify each speaker in the test set to “male” or “female”, and send us a csv file with 460 rows and one column, each element being either “male” or “female”.
Prepare a short presentation describing your workflow. Please specify what you did, what challenges you encountered, and how you overcame them. Anything presented visually will be appreciated.

## Setup
You can download the dataset from [here](https://github.com/augurysys/machine_learning_assignment/raw/master/augury_ml_assignment.zip).

Once you’re finished, please send your results by email to [dbarsky@augury.com](mailto:dbarsky@augury.com). The email should have two attachments:
1. _predicted_labels_test.csv_ - your predictions for the test set, in CSV format, as specified above.
2. A presentation outlining your work process and conclusions.
