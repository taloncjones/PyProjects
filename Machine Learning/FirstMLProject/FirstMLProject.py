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
