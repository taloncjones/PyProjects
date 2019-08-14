# File: Machine Learning/Kaggle_HousePrices_AdvancedRegressionTechniques/Main.py
# Use: The goal of this project is to begin learning ML and is taken from a tutorial found in the README
# Author: Talon Jones

# Import statements
import numpy as np
import pandas as pd

# Load dataset
train = pd.read_csv("house-prices-advanced-regression-techniques/train.csv")
test = pd.read_csv("house-prices-advanced-regression-techniques/test.csv")

# Verify data imported correctly
print("Train:")
print(train.head())
print(train.shape)
print(train.describe())

print("Test:")
print(test.head())
print(test.shape)
print(test.describe())