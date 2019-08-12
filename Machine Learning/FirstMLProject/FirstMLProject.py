# File: CodeSnippets.py
# Use: The goal of this project is to begin learning ML and is taken from a tutorial found in the README
# Author: Talon Jones

# Purpose: Begin learning ML

import numpy as np
import pandas as pd

# Splits data into groups
from sklearn.model_selection import train_test_split

# Preprocessing module
from sklearn import preprocessing

# Model family
from sklearn.ensemble import RandomForestRegressor

# Cross-validation
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

# Metrics for model performance
from sklearn.metrics import mean_squared_error, r2_score

# Persist model for the future
from sklearn.externals import joblib

# Load tutorial dataset
dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')

# # Show section of data table, number of rows/columns, and statistics for data
# print(data.head())
# print(data.shape)
# print(data.describe())

# Split data into target (y) and training (x) inputs
y = data.quality
x = data.drop('quality', axis=1)

# Further split inputs into training (80%) and test (20%) sets, a random state seed, and stratifies based on y
# # Stratified sampling aims to diversify the training sample by pulling from each subclass equally. In cases where
# # subclass sizes are about equal this is roughly the same as random sampling, but in cases where some subclass sizes
# # are larger/smaller this will prevent weighing the sample with data from the larger subclasses.
# # https://en.wikipedia.org/wiki/Stratified_sampling
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123, stratify=y)

### Manual preprocessing
# # Fit transformer (standardizes the data to find mean, standard deviation) on the training set
# scaler = preprocessing.StandardScaler().fit(x_train)
# # Confirm it worked with:
# x_train_scaled = scaler.transform(x_train)
# print(x_train_scaled.mean(axis=0))
# print(x_train_scaled.std(axis=0))
# # Confirm it works with the x_test set
# x_test_scaled = scaler.transform(x_test)
# print(x_test_scaled.mean(axis=0))
# print(x_test_scaled.std(axis=0))

### Automated preprocessing and scaling
# Pipeline with preprocessing and model. This replaces the above section when doing cross-validation.
pipeline = make_pipeline(preprocessing.StandardScaler(), RandomForestRegressor(n_estimators=100))

# Declare hyperparameters for tuning
# # Unlike model parameters, which are learned from the dataset, hyperparameters declare structural information prior
# # to training the model. Hyperparameter optimization attempts to find a tuple of hyperparameters that yields the
# # optimal model while minimizing data loss through overtuning.
# # https://en.wikipedia.org/wiki/Hyperparameter_optimization
# # More on optimization here: https://towardsdatascience.com/hyperparameter-tuning-c5619e7e6624
hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                    'randomforestregressor__max_depth' : [None, 5, 3, 1]}

# Perform cross-validation (CV) across x_train and y_train
# # Cross-validation estimates the performance of a method for building a model by repeatedly training and evaluating
# # the model using the same method. K-Fold cross-validation splits the data into K parts, trains the model on K-1
# # folds, and then evaluates the model on the Kth fold. By repeating this process K times (using a new "hold-out" (Kth)
# # fold each time) and aggregating the performance of each model, the performance metric for that method is attained.
# Cross-validation across the "grid" (all permutations) of hyperparameters. Uses the preprocessing pipeline.
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
# Fit and tune model
clf.fit(x_train, y_train)
# # Print best parameters found using CV
# print(clf.best_params_)
# # Confirm that GridSearchCV automatically refit our model with the best hyperparameters for the entire training set
# print(clf.refit)