#!/usr/bin/python3

# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
import numpy as np
import load
import pandas as pd


def main():
	''' Main function for testing purposes'''

	# Download latest Google Sheet data as a csv file
	load.get_url()

	# Load csv file to a pandas dataframe
	filename = 'trainingLog.csv'
	df = load.to_df(filename)
	array = df.to_numpy()
	print(array)
'''
	predictors, target = get_data()
	print(predictors.shape)
	print(target.shape)
	specify_model(predictors, target)
'''

def specify_model(predictors, target):
	''' Add hidden layer and an output layer. Fit and do optimization'''

	# Save the number of columns in predictors: n_cols
	n_cols = predictors.shape[1]

	# Set up the model: model
	model = Sequential()

	# Add the first layer
	model.add(Dense(50, activation='relu', input_shape=(n_cols,)))

	# Add the second layer
	model.add(Dense(32, activation='relu', input_shape=(n_cols,)))

	# Add the output layer
	model.add(Dense(1))

	# Compile the model
	model.compile(optimizer='adam', loss='mean_squared_error')

	# Verify that model contains information from compiling
	print("Loss function: " + model.loss)

	# Fit the model
	model.fit(predictors, target, epochs=10)


def get_data():
	''' Creates numpy array for analysis'''

	predictors = np.array([[ 0,  8, 21, 35,  1,  1,  0,  1,  0],
       [ 0,  9, 42, 57,  1,  1,  0,  1,  0],
       [ 0, 12,  1, 19,  0,  0,  0,  1,  0],
       [ 0, 12,  4, 22,  0,  0,  0,  0,  0],
       [ 0, 12, 17, 35,  0,  1,  0,  0,  0],
       [ 1, 13,  9, 28,  0,  0,  0,  0,  0],
       [ 0, 10, 27, 43,  0,  0,  1,  0,  0],
       [ 0, 12,  9, 27,  0,  0,  0,  0,  0],
       [ 0, 16, 11, 33,  0,  1,  0,  1,  0],
       [ 0, 12,  9, 27,  0,  0,  0,  0,  0],
       [ 1, 12, 17, 35,  0,  1,  0,  0,  0],
       [ 1, 12, 19, 37,  0,  0,  0,  1,  0],
       [ 0,  8, 27, 41,  0,  1,  1,  0,  0],
       [ 1,  9, 30, 45,  0,  0,  1,  0,  0],
       [ 0,  9, 29, 44,  0,  1,  1,  0,  0],
       [ 0, 12, 37, 55,  0,  1,  0,  0,  1],
       [ 0,  7, 44, 57,  0,  1,  1,  0,  0],
       [ 1, 12, 26, 44,  0,  1,  0,  1,  0],
       [ 0, 11, 16, 33,  0,  0,  0,  0,  0],
       [ 0, 12, 33, 51,  0,  1,  0,  0,  0],
       [ 1, 12, 16, 34,  1,  1,  0,  1,  0],
       [ 1,  7, 42, 55,  0,  1,  0,  1,  0],
       [ 0, 12,  9, 27,  0,  0,  0,  0,  0],
       [ 0, 11, 14, 31,  0,  1,  1,  0,  0],
       [ 0, 12, 23, 41,  0,  1,  0,  0,  0],
       [ 0,  6, 45, 57,  0,  1,  1,  1,  0],
       [ 0, 12,  8, 26,  0,  1,  0,  1,  0],
       [ 0, 10, 30, 46,  0,  1,  0,  0,  0],
       [ 0, 12,  8, 26,  1,  1,  0,  1,  0],
       [ 0, 12,  8, 26,  0,  1,  0,  0,  0],
       [ 0, 14, 13, 33,  0,  0,  0,  0,  0],
       [ 0, 12, 46, 64,  1,  0,  1,  0,  0],
       [ 0,  8, 19, 33,  0,  1,  0,  0,  0],
       [ 0, 17,  1, 24,  1,  0,  1,  0,  0],
       [ 0, 12, 19, 37,  0,  0,  0,  1,  0],
       [ 0, 12, 36, 54,  0,  0,  0,  0,  0],
       [ 0, 12, 20, 38,  0,  1,  1,  0,  1],
       [ 1, 12, 35, 53,  0,  1,  0,  0,  1],
       [ 0, 12,  3, 21,  0,  0,  0,  0,  0],
       [ 0, 14, 10, 30,  0,  1,  1,  1,  0],
       [ 0, 12,  0, 18,  0,  0,  0,  0,  0],
       [ 1, 14, 14, 34,  0,  1,  1,  1,  0],
       [ 0, 12, 14, 32,  0,  1,  0,  1,  0],
       [ 0,  9, 16, 31,  1,  1,  0,  1,  0],
       [ 0, 13,  8, 27,  0,  0,  1,  0,  1],
       [ 0,  7, 15, 28,  1,  1,  1,  1,  0],
       [ 0, 16, 12, 34,  0,  1,  0,  1,  0],
       [ 0, 10, 13, 29,  0,  0,  1,  0,  0],
       [ 1,  8, 33, 47,  0,  1,  0,  0,  0],
       [ 0, 12,  9, 27,  0,  1,  0,  1,  0],
       [ 0, 12,  7, 25,  0,  1,  0,  0,  0],
       [ 1, 16, 13, 35,  0,  1,  0,  1,  0],
       [ 0, 12,  7, 25,  1,  1,  0,  1,  0],
       [ 0, 12, 16, 34,  1,  1,  0,  1,  0],
       [ 0, 13,  0, 19,  0,  0,  0,  0,  0],
       [ 0, 12, 11, 29,  1,  0,  0,  1,  0],
       [ 0, 13, 17, 36,  0,  0,  0,  1,  0],
       [ 0, 10, 13, 29,  0,  1,  0,  1,  0],
       [ 1, 12, 22, 40,  0,  0,  0,  1,  0],
       [ 0, 12, 28, 46,  1,  1,  0,  1,  0],
       [ 0, 11, 17, 34,  0,  0,  0,  0,  0],
       [ 1, 12, 24, 42,  0,  1,  0,  0,  1],
       [ 0,  3, 55, 64,  0,  1,  1,  1,  0],
       [ 0, 12,  3, 21,  0,  0,  1,  0,  1],
       [ 1, 12,  6, 24,  0,  0,  0,  1,  0],
       [ 0, 10, 27, 43,  0,  1,  0,  0,  1],
       [ 1, 12, 19, 37,  0,  1,  1,  1,  0],
       [ 1, 12, 19, 37,  0,  1,  0,  0,  1],
       [ 0, 12, 38, 56,  1,  1,  0,  1,  0],
       [ 1, 10, 41, 57,  0,  1,  1,  1,  0],
       [ 0, 11,  3, 20,  0,  0,  1,  1,  0],
       [ 1, 14, 20, 40,  0,  1,  0,  0,  0],
       [ 0, 10, 15, 31,  0,  1,  0,  0,  0],
       [ 0,  8,  8, 22,  0,  1,  1,  1,  0],
       [ 0,  8, 39, 53,  1,  1,  1,  1,  0],
       [ 1,  6, 43, 55,  1,  1,  0,  1,  0],
       [ 1, 11, 25, 42,  1,  1,  1,  1,  0],
       [ 1, 12, 11, 29,  0,  1,  0,  0,  0],
       [ 0, 12, 12, 30,  0,  1,  0,  0,  0],
       [ 1, 12, 35, 53,  0,  1,  1,  1,  0],
       [ 0, 14, 14, 34,  0,  0,  0,  0,  0],
       [ 1, 12, 16, 34,  0,  1,  0,  0,  0],
       [ 1, 10, 44, 60,  1,  0,  0,  1,  0],
       [ 0, 16, 13, 35,  1,  0,  1,  0,  0],
       [ 1, 13,  8, 27,  0,  0,  0,  1,  0],
       [ 0, 12, 13, 31,  0,  0,  0,  1,  0],
       [ 1, 11, 18, 35,  0,  1,  0,  0,  0],
       [ 0, 12, 18, 36,  1,  1,  0,  0,  0],
       [ 0, 12,  6, 24,  1,  0,  1,  0,  0],
       [ 1, 11, 37, 54,  0,  1,  1,  1,  0],
       [ 0, 12,  2, 20,  0,  1,  1,  1,  0],
       [ 0, 12, 23, 41,  0,  1,  0,  1,  0],
       [ 0, 12,  1, 19,  0,  0,  0,  0,  0],
       [ 0, 12, 10, 28,  1,  1,  1,  1,  0],
       [ 0, 12, 23, 41,  0,  1,  0,  1,  0],
       [ 1, 12,  8, 26,  0,  1,  0,  0,  0],
       [ 0, 15,  9, 30,  1,  1,  0,  1,  0],
       [ 1, 12, 33, 51,  0,  1,  0,  0,  1],
       [ 0, 12, 19, 37,  1,  1,  0,  1,  0],
       [ 0, 13, 14, 33,  0,  1,  0,  0,  0],
       [ 1, 11, 13, 30,  0,  1,  0,  0,  0],
       [ 0, 10, 12, 28,  0,  1,  0,  0,  1],
       [ 0, 12,  8, 26,  0,  0,  0,  0,  0],
       [ 0, 12, 23, 41,  0,  1,  0,  1,  0],
       [ 0, 14, 13, 33,  1,  0,  0,  1,  0],
       [ 0, 12,  9, 27,  0,  1,  1,  0,  0],
       [ 1, 14, 21, 41,  0,  1,  0,  0,  0],
       [ 0,  5, 44, 55,  0,  1,  1,  0,  1],
       [ 1, 12,  4, 22,  0,  1,  0,  0,  0],
       [ 0,  8, 42, 56,  0,  1,  0,  1,  0],
       [ 1, 13, 10, 29,  0,  1,  0,  0,  0],
       [ 0, 12, 11, 29,  0,  0,  0,  0,  1],
       [ 1, 12, 40, 58,  0,  1,  0,  0,  1],
       [ 0, 12,  8, 26,  0,  0,  0,  0,  1],
       [ 0, 11, 29, 46,  0,  1,  1,  0,  1],
       [ 1, 16,  3, 25,  0,  0,  0,  0,  0],
       [ 0, 11, 11, 28,  0,  0,  0,  0,  1],
       [ 1, 12, 12, 30,  0,  1,  0,  0,  0],
       [ 0,  8, 22, 36,  1,  1,  0,  0,  0],
       [ 0, 12, 12, 30,  0,  1,  0,  0,  0],
       [ 1, 12,  7, 25,  0,  1,  0,  0,  0],
       [ 0, 12, 15, 33,  1,  0,  0,  1,  0],
       [ 0, 12, 28, 46,  0,  1,  0,  0,  0],
       [ 1, 12, 20, 38,  0,  1,  1,  1,  0],
       [ 0, 12,  6, 24,  0,  0,  1,  0,  1],
       [ 0, 12,  5, 23,  0,  0,  1,  1,  0],
       [ 0,  9, 30, 45,  1,  1,  1,  1,  0],
       [ 0, 13, 18, 37,  0,  1,  0,  0,  0],
       [ 0, 12,  6, 24,  1,  1,  1,  1,  0],
       [ 0, 12, 16, 34,  0,  0,  1,  0,  0],
       [ 1, 12,  1, 19,  0,  0,  1,  0,  0],
       [ 0, 12,  3, 21,  0,  0,  0,  1,  0],
       [ 0, 12,  8, 26,  0,  1,  0,  0,  0],
       [ 0, 14,  2, 22,  0,  0,  0,  1,  0],
       [ 0,  9, 16, 31,  0,  0,  0,  1,  0],
       [ 0, 10,  9, 25,  0,  1,  1,  0,  1],
       [ 0, 12,  2, 20,  0,  0,  0,  0,  0],
       [ 0,  7, 43, 56,  0,  1,  1,  1,  0],
       [ 0,  9, 38, 53,  0,  1,  0,  1,  0],
       [ 0, 12,  9, 27,  0,  1,  0,  0,  0],
       [ 0, 12, 12, 30,  0,  1,  1,  0,  0],
       [ 0, 12, 18, 36,  0,  1,  0,  1,  0],
       [ 1, 11, 15, 32,  0,  0,  0,  1,  0],
       [ 1, 11, 28, 45,  0,  1,  1,  0,  1],
       [ 1, 10, 27, 43,  0,  1,  1,  0,  1],
       [ 0, 12, 38, 56,  0,  1,  1,  0,  0],
       [ 0, 12,  3, 21,  1,  0,  0,  1,  0],
       [ 1, 12, 41, 59,  0,  1,  0,  0,  0],
       [ 1, 12, 16, 34,  0,  1,  1,  0,  0],
       [ 0, 13,  7, 26,  0,  1,  1,  1,  0],
       [ 0,  6, 33, 45,  1,  0,  1,  1,  0],
       [ 0, 14, 25, 45,  0,  1,  0,  1,  0],
       [ 0, 12,  5, 23,  0,  1,  1,  0,  0],
       [ 0, 14, 17, 37,  0,  0,  1,  0,  0],
       [ 0, 12,  1, 19,  0,  0,  1,  0,  0],
       [ 0, 12, 13, 31,  0,  1,  0,  1,  0],
       [ 0, 16, 18, 40,  0,  1,  0,  0,  0],
       [ 0, 14, 21, 41,  0,  1,  1,  0,  0],
       [ 0, 14,  2, 22,  0,  0,  0,  0,  0],
       [ 0, 12,  4, 22,  1,  0,  1,  0,  0],
       [ 0, 12, 30, 48,  1,  1,  1,  0,  0],
       [ 0, 13, 32, 51,  0,  0,  0,  0,  0],
       [ 0, 17, 13, 36,  1,  1,  0,  0,  0],
       [ 0, 12, 17, 35,  0,  0,  0,  0,  0],
       [ 0, 14, 26, 46,  1,  1,  0,  0,  0],
       [ 0, 16,  9, 31,  0,  0,  0,  0,  0],
       [ 0, 16,  8, 30,  0,  0,  0,  0,  0],
       [ 1, 15,  1, 22,  0,  1,  0,  0,  0],
       [ 0, 17, 32, 55,  0,  1,  1,  0,  0],
       [ 0, 12, 24, 42,  1,  1,  0,  0,  0],
       [ 0, 14,  1, 21,  1,  0,  0,  0,  0],
       [ 0, 12, 42, 60,  0,  1,  0,  1,  0],
       [ 0, 16,  3, 25,  1,  0,  0,  1,  0],
       [ 0, 12, 32, 50,  1,  1,  0,  0,  0],
       [ 0, 14, 22, 42,  0,  0,  0,  0,  0],
       [ 0, 16, 18, 40,  0,  1,  0,  0,  0],
       [ 0, 18, 19, 43,  1,  1,  0,  0,  0],
       [ 0, 15, 12, 33,  0,  1,  0,  0,  0],
       [ 0, 12, 42, 60,  1,  1,  0,  0,  0],
       [ 0, 12, 34, 52,  0,  1,  1,  0,  0],
       [ 0, 18, 29, 53,  0,  1,  0,  0,  0],
       [ 0, 16,  8, 30,  0,  0,  1,  0,  0],
       [ 0, 18, 13, 37,  0,  0,  0,  1,  0],
       [ 0, 16, 10, 32,  0,  0,  0,  0,  0],
       [ 0, 16, 22, 44,  0,  1,  0,  0,  0],
       [ 0, 16, 10, 32,  0,  1,  1,  0,  0],
       [ 0, 17, 15, 38,  1,  1,  0,  0,  0],
       [ 0, 12, 26, 44,  0,  1,  0,  0,  0],
       [ 0, 14, 16, 36,  0,  0,  0,  0,  0],
       [ 0, 18, 14, 38,  1,  1,  0,  0,  0],
       [ 0, 12, 38, 56,  1,  1,  0,  0,  0],
       [ 0, 12, 14, 32,  0,  1,  1,  0,  0],
       [ 0, 12,  7, 25,  1,  1,  0,  0,  0],
       [ 0, 18, 13, 37,  1,  0,  1,  0,  0],
       [ 0, 10, 20, 36,  0,  1,  0,  0,  0],
       [ 1, 16,  7, 29,  0,  1,  0,  0,  0],
       [ 0, 16, 26, 48,  1,  1,  0,  0,  0],
       [ 0, 16, 14, 36,  0,  1,  0,  0,  0],
       [ 0, 13, 36, 55,  0,  0,  0,  0,  0],
       [ 0, 12, 24, 42,  0,  1,  0,  0,  0],
       [ 0, 14, 41, 61,  0,  1,  1,  0,  0],
       [ 0, 16,  7, 29,  0,  1,  0,  0,  0],
       [ 0, 17, 14, 37,  0,  0,  1,  0,  0],
       [ 0, 12,  1, 19,  1,  0,  1,  0,  0],
       [ 0, 16,  6, 28,  1,  1,  0,  1,  0],
       [ 0, 12,  3, 21,  1,  1,  0,  0,  0],
       [ 0, 15, 31, 52,  0,  1,  0,  0,  0],
       [ 0, 13, 14, 33,  1,  1,  0,  1,  0],
       [ 0, 14, 13, 33,  1,  1,  0,  0,  0],
       [ 1, 16, 26, 48,  0,  1,  0,  1,  0],
       [ 0, 18, 14, 38,  0,  1,  0,  0,  0],
       [ 0, 13, 33, 52,  1,  1,  0,  0,  0],
       [ 0, 12, 16, 34,  0,  1,  0,  0,  0],
       [ 0, 18, 10, 34,  0,  1,  0,  0,  0],
       [ 0, 14, 22, 42,  0,  0,  0,  0,  0],
       [ 0, 14,  2, 22,  0,  0,  0,  0,  0],
       [ 0, 12, 29, 47,  1,  1,  1,  0,  0],
       [ 0, 12, 43, 61,  0,  1,  0,  1,  0],
       [ 0, 12,  5, 23,  1,  1,  0,  0,  0],
       [ 0, 16, 14, 36,  1,  1,  1,  0,  0],
       [ 0, 12, 28, 46,  0,  1,  1,  0,  0],
       [ 0, 11, 25, 42,  1,  1,  1,  0,  0],
       [ 0, 12, 45, 63,  1,  1,  0,  0,  0],
       [ 0, 14,  5, 25,  0,  0,  1,  0,  0],
       [ 0, 12, 20, 38,  0,  1,  1,  1,  0],
       [ 0, 16,  6, 28,  1,  1,  0,  0,  0],
       [ 0, 16, 16, 38,  0,  1,  0,  0,  0],
       [ 0, 11, 33, 50,  1,  1,  0,  0,  0],
       [ 0, 13,  2, 21,  1,  1,  1,  0,  0],
       [ 0, 12, 10, 28,  1,  0,  1,  0,  0],
       [ 0, 14, 44, 64,  0,  1,  1,  0,  0],
       [ 0, 14,  6, 26,  1,  1,  1,  0,  0],
       [ 0, 12, 15, 33,  1,  0,  0,  0,  0],
       [ 0, 12,  5, 23,  0,  1,  0,  0,  0],
       [ 0, 13,  4, 23,  1,  1,  0,  1,  0],
       [ 0, 14, 14, 34,  0,  1,  0,  0,  0],
       [ 0, 14, 32, 52,  1,  1,  0,  0,  0],
       [ 0, 12, 14, 32,  1,  1,  0,  0,  0],
       [ 0, 14, 21, 41,  0,  1,  0,  0,  0],
       [ 1, 12, 43, 61,  0,  1,  0,  0,  0],
       [ 0, 12, 27, 45,  1,  1,  1,  0,  0],
       [ 0, 12,  4, 22,  1,  0,  0,  0,  0],
       [ 0, 14,  0, 20,  0,  0,  0,  0,  0],
       [ 0, 12, 32, 50,  0,  1,  1,  0,  0],
       [ 0, 12, 20, 38,  0,  1,  0,  0,  0],
       [ 0, 15,  4, 25,  0,  0,  1,  0,  0],
       [ 0, 12, 34, 52,  0,  1,  0,  0,  0],
       [ 0, 13,  5, 24,  0,  0,  0,  0,  0],
       [ 0, 17, 13, 36,  0,  1,  0,  1,  0],
       [ 0, 14, 17, 37,  1,  1,  0,  0,  0],
       [ 0, 13, 10, 29,  1,  1,  1,  0,  0],
       [ 0, 16,  7, 29,  1,  1,  0,  0,  0],
       [ 0, 12, 25, 43,  1,  0,  0,  0,  0],
       [ 0, 12, 18, 36,  1,  1,  0,  0,  0],
       [ 0, 16, 27, 49,  1,  1,  0,  1,  0],
       [ 0, 16,  2, 24,  1,  0,  0,  0,  0],
       [ 0, 13, 13, 32,  0,  1,  0,  0,  0],
       [ 0, 14, 24, 44,  1,  0,  0,  0,  0],
       [ 0, 18, 13, 37,  1,  1,  1,  0,  0],
       [ 1, 14, 15, 35,  1,  0,  0,  0,  0],
       [ 0, 12, 12, 30,  1,  0,  1,  0,  0],
       [ 0, 12, 24, 42,  1,  1,  0,  0,  0],
       [ 0, 12, 43, 61,  1,  1,  0,  0,  1],
       [ 0, 12, 13, 31,  1,  1,  0,  1,  0],
       [ 0, 12, 16, 34,  1,  1,  1,  0,  0],
       [ 0, 11, 24, 41,  1,  1,  0,  0,  0],
       [ 0, 16,  4, 26,  1,  1,  1,  0,  0],
       [ 0, 12, 24, 42,  1,  1,  0,  0,  0],
       [ 0, 12, 45, 63,  1,  1,  0,  0,  0],
       [ 1, 12, 20, 38,  0,  1,  0,  0,  0],
       [ 0, 12, 38, 56,  1,  1,  0,  0,  0],
       [ 0, 18, 10, 34,  0,  1,  1,  0,  0],
       [ 0, 11, 16, 33,  1,  1,  0,  0,  0],
       [ 0, 12, 32, 50,  1,  1,  1,  0,  0],
       [ 0, 16,  2, 24,  1,  0,  1,  0,  0],
       [ 0, 13, 28, 47,  1,  0,  1,  0,  0],
       [ 0, 16,  3, 25,  0,  0,  0,  0,  0],
       [ 1, 13,  8, 27,  1,  0,  0,  0,  0],
       [ 0, 12, 44, 62,  1,  1,  0,  1,  0],
       [ 0, 12, 12, 30,  0,  1,  1,  0,  0],
       [ 0, 12,  8, 26,  0,  1,  1,  0,  0],
       [ 0, 12,  4, 22,  1,  1,  0,  0,  0],
       [ 0, 12, 28, 46,  1,  1,  1,  0,  0],
       [ 0, 13,  0, 19,  1,  0,  1,  0,  0],
       [ 0, 14,  1, 21,  0,  0,  1,  0,  0],
       [ 0, 14, 12, 32,  1,  1,  0,  1,  0],
       [ 0, 12, 39, 57,  1,  1,  0,  0,  0],
       [ 0, 12, 24, 42,  1,  1,  0,  0,  0],
       [ 0, 17, 32, 55,  1,  1,  0,  0,  0],
       [ 0, 16,  4, 26,  0,  0,  0,  0,  0],
       [ 0, 12, 25, 43,  1,  0,  0,  0,  0],
       [ 0, 12,  8, 26,  0,  0,  0,  0,  0],
       [ 0, 13, 16, 35,  1,  1,  0,  0,  0],
       [ 0, 12,  5, 23,  0,  0,  1,  0,  0],
       [ 0, 13, 31, 50,  0,  0,  0,  0,  0],
       [ 0, 12, 25, 43,  1,  0,  0,  0,  0],
       [ 0, 12, 15, 33,  1,  1,  0,  0,  0],
       [ 0, 14, 15, 35,  1,  1,  1,  0,  0],
       [ 0, 12,  0, 18,  1,  0,  0,  0,  0],
       [ 0, 12, 19, 37,  0,  1,  0,  0,  0],
       [ 0, 12, 21, 39,  1,  0,  0,  0,  0],
       [ 0, 12,  6, 24,  1,  0,  0,  0,  0],
       [ 1, 12, 14, 32,  1,  1,  0,  0,  0],
       [ 0, 13, 30, 49,  1,  1,  0,  0,  0],
       [ 0, 12,  8, 26,  1,  0,  0,  0,  0],
       [ 1,  9, 33, 48,  0,  0,  0,  0,  0],
       [ 0, 13, 16, 35,  0,  0,  0,  0,  0],
       [ 0, 12, 20, 38,  1,  0,  1,  0,  0],
       [ 0, 13,  6, 25,  1,  1,  1,  0,  0],
       [ 1, 12, 10, 28,  1,  1,  0,  0,  0],
       [ 0, 13,  1, 20,  1,  0,  1,  0,  0],
       [ 0, 12,  2, 20,  0,  0,  1,  0,  0],
       [ 0, 13,  0, 19,  1,  0,  1,  0,  0],
       [ 0, 16, 17, 39,  0,  1,  0,  0,  0],
       [ 0, 12,  8, 26,  1,  0,  0,  0,  0],
       [ 0, 12,  4, 22,  0,  0,  1,  0,  0],
       [ 0, 12, 15, 33,  1,  0,  0,  0,  0],
       [ 0, 12, 29, 47,  1,  1,  0,  0,  0],
       [ 0, 12, 23, 41,  1,  1,  1,  0,  0],
       [ 0, 12, 39, 57,  1,  1,  1,  0,  0],
       [ 0, 12, 14, 32,  1,  1,  1,  0,  0],
       [ 0, 17,  6, 29,  1,  0,  1,  0,  0],
       [ 1, 14, 12, 32,  0,  1,  1,  0,  0],
       [ 0, 12, 26, 44,  1,  0,  1,  0,  0],
       [ 0, 14, 32, 52,  1,  1,  0,  0,  0],
       [ 0, 15,  6, 27,  1,  1,  0,  0,  0],
       [ 0, 12, 40, 58,  1,  1,  0,  0,  0],
       [ 0, 12, 18, 36,  1,  1,  0,  1,  0],
       [ 0, 11, 12, 29,  1,  0,  0,  0,  0],
       [ 0, 12, 36, 54,  1,  1,  1,  0,  1],
       [ 0, 12, 19, 37,  1,  1,  0,  0,  0],
       [ 0, 16, 42, 64,  1,  0,  0,  1,  0],
       [ 0, 13,  2, 21,  1,  1,  0,  0,  0],
       [ 0, 12, 33, 51,  1,  1,  0,  0,  0],
       [ 0, 12, 14, 32,  1,  1,  1,  0,  0],
       [ 0, 12, 22, 40,  0,  0,  0,  0,  0],
       [ 0, 12, 20, 38,  1,  1,  0,  0,  0],
       [ 0, 12, 15, 33,  1,  1,  0,  0,  0],
       [ 0, 12, 35, 53,  0,  1,  0,  0,  0],
       [ 0, 12,  7, 25,  1,  1,  0,  0,  0],
       [ 0, 12, 45, 63,  1,  0,  0,  1,  0],
       [ 0, 12,  9, 27,  1,  0,  0,  0,  0],
       [ 0, 12,  2, 20,  1,  1,  1,  0,  0],
       [ 0, 17,  3, 26,  0,  0,  1,  0,  0],
       [ 1, 14, 19, 39,  1,  1,  0,  0,  0],
       [ 0, 12, 14, 32,  1,  1,  1,  0,  0],
       [ 0,  4, 54, 64,  0,  1,  0,  0,  0],
       [ 0, 14, 17, 37,  0,  1,  0,  0,  0],
       [ 0,  8, 29, 43,  1,  1,  0,  0,  0],
       [ 0, 15, 26, 47,  1,  0,  1,  0,  0],
       [ 0,  2, 16, 24,  0,  0,  0,  0,  0],
       [ 0,  8, 29, 43,  1,  0,  0,  0,  0],
       [ 0, 11, 20, 37,  1,  1,  0,  0,  0],
       [ 0, 10, 38, 54,  1,  1,  1,  0,  0],
       [ 0,  8, 37, 51,  1,  1,  1,  0,  0],
       [ 0,  9, 48, 63,  0,  0,  0,  0,  0],
       [ 0, 12, 16, 34,  1,  0,  0,  0,  0],
       [ 0,  8, 38, 52,  1,  1,  0,  0,  0],
       [ 0, 14,  0, 20,  0,  0,  0,  0,  0],
       [ 1, 12, 14, 32,  0,  0,  0,  0,  0],
       [ 0, 12,  2, 20,  1,  1,  0,  0,  0],
       [ 0, 16, 21, 43,  0,  1,  0,  0,  0],
       [ 0, 13, 15, 34,  1,  1,  0,  0,  0],
       [ 0, 16, 20, 42,  1,  0,  0,  0,  0],
       [ 0, 14, 12, 32,  1,  1,  0,  0,  0],
       [ 0, 12,  7, 25,  0,  0,  1,  0,  0],
       [ 0, 11,  4, 21,  0,  1,  0,  0,  0],
       [ 0, 13,  9, 28,  0,  1,  1,  0,  0],
       [ 0, 12, 43, 61,  1,  1,  1,  0,  0],
       [ 0, 10, 19, 35,  0,  0,  1,  0,  0],
       [ 0,  8, 49, 63,  1,  0,  0,  0,  0],
       [ 0, 12, 38, 56,  1,  1,  0,  0,  0],
       [ 0, 12, 13, 31,  1,  1,  0,  0,  0],
       [ 0, 12, 14, 32,  1,  1,  0,  0,  0],
       [ 0, 12, 20, 38,  0,  0,  0,  0,  0],
       [ 0, 12,  7, 25,  1,  0,  0,  0,  0],
       [ 1, 12,  9, 27,  1,  1,  0,  1,  0],
       [ 0, 12,  6, 24,  1,  0,  0,  0,  0],
       [ 0, 12,  5, 23,  1,  1,  1,  0,  0],
       [ 0, 13,  1, 20,  1,  0,  1,  0,  0],
       [ 1, 14, 22, 42,  0,  1,  0,  0,  0],
       [ 0, 12, 24, 42,  1,  1,  0,  0,  0],
       [ 1, 12, 15, 33,  1,  0,  0,  0,  0],
       [ 0, 11,  8, 25,  1,  1,  1,  0,  0],
       [ 0, 11, 17, 34,  1,  1,  1,  0,  0],
       [ 0, 12,  2, 20,  0,  0,  1,  0,  0],
       [ 0, 12, 20, 38,  0,  1,  1,  0,  0],
       [ 1, 12, 26, 44,  0,  1,  0,  0,  0],
       [ 0, 10, 37, 53,  1,  1,  1,  0,  0],
       [ 0, 12, 41, 59,  1,  0,  0,  0,  0],
       [ 0, 12, 27, 45,  1,  1,  0,  0,  0],
       [ 1, 12,  5, 23,  1,  1,  0,  0,  0],
       [ 0, 14, 16, 36,  0,  1,  0,  0,  0],
       [ 0, 14, 19, 39,  1,  1,  0,  0,  0],
       [ 0, 12, 10, 28,  0,  1,  0,  0,  0],
       [ 1, 13,  1, 20,  0,  0,  1,  0,  0],
       [ 1, 12, 43, 61,  1,  1,  0,  0,  0],
       [ 0, 13,  3, 22,  0,  0,  0,  0,  0],
       [ 0, 12,  0, 18,  1,  0,  0,  0,  0],
       [ 0, 12, 26, 44,  1,  1,  1,  0,  0],
       [ 1, 10, 25, 41,  1,  1,  0,  0,  0],
       [ 0, 12, 15, 33,  1,  1,  0,  0,  0],
       [ 0, 14, 10, 30,  1,  0,  1,  0,  0],
       [ 1, 11, 45, 62,  1,  0,  0,  0,  0],
       [ 0, 11,  3, 20,  0,  0,  0,  0,  0],
       [ 1,  8, 47, 61,  0,  1,  0,  0,  0],
       [ 0, 16,  6, 28,  1,  1,  0,  0,  0],
       [ 0, 10, 33, 49,  1,  0,  1,  0,  0],
       [ 0, 16,  3, 25,  0,  0,  0,  1,  0],
       [ 1, 14,  4, 24,  0,  0,  0,  0,  0],
       [ 1, 14, 34, 54,  0,  1,  0,  0,  0],
       [ 0, 11, 39, 56,  0,  1,  1,  0,  0],
       [ 0, 12, 17, 35,  1,  1,  1,  0,  0],
       [ 1,  9, 47, 62,  0,  1,  0,  0,  0],
       [ 0, 11,  2, 19,  0,  0,  0,  0,  0],
       [ 0, 13,  0, 19,  0,  0,  1,  0,  0],
       [ 0, 14, 24, 44,  1,  0,  0,  0,  0],
       [ 1, 12, 25, 43,  0,  1,  0,  0,  0],
       [ 0, 14,  6, 26,  1,  0,  0,  0,  0],
       [ 0, 12, 10, 28,  1,  0,  0,  0,  0],
       [ 0, 12, 33, 51,  1,  1,  0,  0,  0],
       [ 0, 12, 12, 30,  0,  0,  0,  0,  0],
       [ 0, 12,  9, 27,  1,  1,  1,  0,  0],
       [ 1, 11, 18, 35,  0,  1,  1,  0,  0],
       [ 0, 12, 10, 28,  0,  1,  0,  0,  0],
       [ 0,  8, 45, 59,  1,  0,  1,  0,  0],
       [ 1,  9, 46, 61,  1,  1,  0,  0,  0],
       [ 0,  7, 14, 27,  0,  1,  1,  0,  0],
       [ 0, 11, 36, 53,  1,  0,  0,  0,  0],
       [ 1, 13, 34, 53,  0,  1,  0,  0,  1],
       [ 0, 18, 15, 39,  0,  1,  0,  0,  0],
       [ 0, 17, 31, 54,  0,  1,  0,  1,  0],
       [ 0, 16,  6, 28,  1,  0,  0,  1,  0],
       [ 0, 14, 15, 35,  0,  1,  1,  0,  0],
       [ 0, 12, 30, 48,  0,  1,  0,  0,  0],
       [ 0, 18,  8, 32,  0,  1,  0,  0,  0],
       [ 0, 18,  5, 29,  0,  1,  0,  1,  0],
       [ 1, 17,  3, 26,  1,  0,  0,  0,  0],
       [ 0, 13, 17, 36,  0,  1,  1,  0,  0],
       [ 1, 16,  5, 27,  0,  1,  0,  1,  0],
       [ 0, 14, 10, 30,  1,  1,  0,  0,  0],
       [ 0, 15, 33, 54,  1,  0,  0,  0,  0],
       [ 0, 18,  3, 27,  0,  1,  0,  0,  0],
       [ 0, 16,  0, 18,  1,  0,  0,  0,  0],
       [ 0, 16, 13, 35,  0,  1,  1,  0,  0],
       [ 0, 18, 12, 36,  0,  1,  0,  0,  0],
       [ 0, 16,  6, 28,  1,  1,  0,  0,  0],
       [ 0, 17,  7, 30,  0,  1,  0,  0,  0],
       [ 1, 16, 14, 36,  0,  1,  1,  0,  0],
       [ 0, 17,  5, 28,  1,  0,  0,  0,  0],
       [ 0, 15, 10, 31,  1,  1,  1,  0,  0],
       [ 0, 18, 11, 35,  1,  1,  0,  0,  0],
       [ 0, 17, 24, 47,  1,  1,  0,  0,  0],
       [ 0, 16,  9, 31,  0,  0,  0,  1,  0],
       [ 0, 18, 12, 36,  0,  1,  1,  0,  0],
       [ 0, 18, 19, 43,  0,  1,  0,  0,  0],
       [ 0, 14, 14, 34,  1,  1,  0,  0,  0],
       [ 0, 16, 17, 39,  1,  0,  0,  1,  0],
       [ 0, 18,  7, 31,  0,  0,  1,  0,  0],
       [ 0, 18,  7, 31,  0,  1,  0,  0,  0],
       [ 0, 16, 22, 44,  1,  1,  0,  0,  0],
       [ 0, 12, 28, 46,  1,  1,  0,  0,  0],
       [ 0, 16, 16, 38,  1,  0,  0,  0,  0],
       [ 0, 16, 16, 38,  0,  0,  1,  0,  0],
       [ 0, 16,  7, 29,  1,  1,  0,  0,  0],
       [ 0, 12, 11, 29,  1,  0,  0,  0,  0],
       [ 0, 12, 11, 29,  1,  1,  0,  0,  0],
       [ 0, 12, 16, 34,  1,  0,  0,  0,  0],
       [ 1, 18, 33, 57,  0,  0,  0,  0,  0],
       [ 0, 12, 21, 39,  1,  1,  1,  0,  0],
       [ 0, 16,  4, 26,  0,  1,  0,  1,  0],
       [ 0, 15, 13, 34,  0,  1,  0,  0,  0],
       [ 1, 18, 14, 38,  0,  1,  0,  0,  0],
       [ 0, 16, 10, 32,  1,  1,  0,  0,  0],
       [ 0, 18, 14, 38,  0,  1,  1,  0,  0],
       [ 0, 16, 29, 51,  0,  1,  1,  0,  0],
       [ 0, 12,  4, 22,  0,  0,  0,  0,  0],
       [ 0, 18, 27, 51,  0,  1,  0,  0,  0],
       [ 0, 12,  3, 21,  0,  1,  0,  0,  0],
       [ 1, 16, 14, 36,  0,  1,  1,  0,  0],
       [ 0, 14,  0, 20,  0,  1,  0,  0,  1],
       [ 0, 18, 33, 57,  0,  1,  0,  0,  0],
       [ 0, 16, 38, 60,  0,  1,  1,  0,  0],
       [ 1, 18, 18, 42,  1,  1,  0,  0,  0],
       [ 0, 17,  3, 26,  0,  0,  0,  1,  0],
       [ 0, 18, 40, 64,  1,  0,  0,  0,  0],
       [ 0, 14, 19, 39,  0,  0,  0,  1,  0],
       [ 0, 14,  4, 24,  1,  0,  0,  0,  0],
       [ 0, 16, 11, 33,  1,  1,  0,  0,  0],
       [ 0, 16, 16, 38,  1,  1,  0,  0,  0],
       [ 0, 14, 22, 42,  0,  1,  0,  0,  0],
       [ 1, 17, 13, 36,  1,  0,  0,  0,  0],
       [ 1, 16, 28, 50,  1,  1,  1,  0,  0],
       [ 0, 16, 10, 32,  1,  1,  0,  0,  0],
       [ 0, 16,  5, 27,  1,  0,  1,  0,  0],
       [ 0, 15,  5, 26,  0,  0,  0,  0,  0],
       [ 0, 18, 37, 61,  1,  0,  0,  1,  0],
       [ 1, 17, 26, 49,  1,  1,  0,  0,  0],
       [ 0, 16,  4, 26,  1,  1,  1,  0,  0],
       [ 1, 18, 31, 55,  1,  0,  0,  0,  0],
       [ 1, 17, 13, 36,  1,  1,  0,  0,  0],
       [ 0, 12, 42, 60,  1,  1,  0,  0,  0],
       [ 0, 17, 18, 41,  0,  1,  0,  0,  0],
       [ 0, 12,  3, 21,  1,  1,  0,  0,  0],
       [ 0, 17, 10, 33,  1,  0,  0,  0,  0],
       [ 1, 16, 10, 32,  1,  0,  0,  0,  0],
       [ 0, 16, 17, 39,  1,  1,  0,  0,  0],
       [ 0, 18,  7, 31,  0,  1,  0,  0,  0],
       [ 0, 16, 14, 36,  1,  1,  0,  0,  0],
       [ 1, 16, 22, 44,  1,  1,  0,  0,  0],
       [ 0, 17, 14, 37,  1,  1,  0,  0,  0],
       [ 0, 16, 11, 33,  0,  1,  0,  0,  0],
       [ 1, 18, 23, 47,  0,  1,  0,  0,  0],
       [ 1, 12, 39, 57,  0,  1,  0,  0,  0],
       [ 0, 16, 15, 37,  0,  1,  0,  0,  0],
       [ 0, 14, 15, 35,  1,  0,  0,  0,  0],
       [ 0, 16, 10, 32,  0,  0,  0,  0,  0],
       [ 0, 12, 25, 43,  1,  0,  1,  0,  0],
       [ 0, 14, 12, 32,  1,  1,  0,  0,  0],
       [ 0, 16,  7, 29,  1,  1,  1,  0,  0],
       [ 1, 17,  7, 30,  0,  1,  0,  0,  0],
       [ 0, 16, 17, 39,  0,  1,  0,  1,  0],
       [ 1, 16, 10, 32,  0,  1,  0,  0,  0],
       [ 0, 17,  2, 25,  0,  1,  1,  0,  0],
       [ 1,  9, 34, 49,  1,  1,  1,  0,  0],
       [ 0, 15, 11, 32,  1,  1,  0,  0,  0],
       [ 0, 15, 10, 31,  0,  0,  0,  0,  0],
       [ 0, 12, 12, 30,  0,  1,  1,  0,  0],
       [ 1, 16,  6, 28,  1,  0,  0,  0,  0],
       [ 0, 18,  5, 29,  0,  0,  0,  0,  0],
       [ 0, 12, 33, 51,  1,  1,  0,  0,  0],
       [ 1, 17, 25, 48,  1,  1,  0,  0,  0],
       [ 1, 12, 13, 31,  0,  1,  1,  0,  0],
       [ 0, 16, 33, 55,  0,  1,  0,  1,  0]])

	target = np.array([ 5.1 ,  4.95,  6.67,  4.  ,  7.5 , 13.07,  4.45, 19.47, 13.28,
        8.75, 11.35, 11.5 ,  6.5 ,  6.25, 19.98,  7.3 ,  8.  , 22.2 ,
        3.65, 20.55,  5.71,  7.  ,  3.75,  4.5 ,  9.56,  5.75,  9.36,
        6.5 ,  3.35,  4.75,  8.9 ,  4.  ,  4.7 ,  5.  ,  9.25, 10.67,
        7.61, 10.  ,  7.5 , 12.2 ,  3.35, 11.  , 12.  ,  4.85,  4.3 ,
        6.  , 15.  ,  4.85,  9.  ,  6.36,  9.15, 11.  ,  4.5 ,  4.8 ,
        4.  ,  5.5 ,  8.4 ,  6.75, 10.  ,  5.  ,  6.5 , 10.75,  7.  ,
       11.43,  4.  ,  9.  , 13.  , 12.22,  6.28,  6.75,  3.35, 16.  ,
        5.25,  3.5 ,  4.22,  3.  ,  4.  , 10.  ,  5.  , 16.  , 13.98,
       13.26,  6.1 ,  3.75,  9.  ,  9.45,  5.5 ,  8.93,  6.25,  9.75,
        6.73,  7.78,  2.85,  3.35, 19.98,  8.5 ,  9.75, 15.  ,  8.  ,
       11.25, 14.  , 10.  ,  6.5 ,  9.83, 18.5 , 12.5 , 26.  , 14.  ,
       10.5 , 11.  , 12.47, 12.5 , 15.  ,  6.  ,  9.5 ,  5.  ,  3.75,
       12.57,  6.88,  5.5 ,  7.  ,  4.5 ,  6.5 , 12.  ,  5.  ,  6.5 ,
        6.8 ,  8.75,  3.75,  4.5 ,  6.  ,  5.5 , 13.  ,  5.65,  4.8 ,
        7.  ,  5.25,  3.35,  8.5 ,  6.  ,  6.75,  8.89, 14.21, 10.78,
        8.9 ,  7.5 ,  4.5 , 11.25, 13.45,  6.  ,  4.62, 10.58,  5.  ,
        8.2 ,  6.25,  8.5 , 24.98, 16.65,  6.25,  4.55, 11.25, 21.25,
       12.65,  7.5 , 10.25,  3.35, 13.45,  4.84, 26.29,  6.58, 44.5 ,
       15.  , 11.25,  7.  , 10.  , 14.53, 20.  , 22.5 ,  3.64, 10.62,
       24.98,  6.  , 19.  , 13.2 , 22.5 , 15.  ,  6.88, 11.84, 16.14,
       13.95, 13.16,  5.3 ,  4.5 , 10.  , 10.  , 10.  ,  9.37,  5.8 ,
       17.86,  1.  ,  8.8 ,  9.  , 18.16,  7.81, 10.62,  4.5 , 17.25,
       10.5 ,  9.22, 15.  , 22.5 ,  4.55,  9.  , 13.33, 15.  ,  7.5 ,
        4.25, 12.5 ,  5.13,  3.35, 11.11,  3.84,  6.4 ,  5.56, 10.  ,
        5.65, 11.5 ,  3.5 ,  3.35,  4.75, 19.98,  3.5 ,  4.  ,  7.  ,
        6.25,  4.5 , 14.29,  5.  , 13.75, 13.71,  7.5 ,  3.8 ,  5.  ,
        9.42,  5.5 ,  3.75,  3.5 ,  5.8 , 12.  ,  5.  ,  8.75, 10.  ,
        8.5 ,  8.63,  9.  ,  5.5 , 11.11, 10.  ,  5.2 ,  8.  ,  3.56,
        5.2 , 11.67, 11.32,  7.5 ,  5.5 ,  5.  ,  7.75,  5.25,  9.  ,
        9.65,  5.21,  7.  , 12.16,  5.25, 10.32,  3.35,  7.7 ,  9.17,
        8.43,  4.  ,  4.13,  3.  ,  4.25,  7.53, 10.53,  5.  , 15.03,
       11.25,  6.25,  3.5 ,  6.85, 12.5 , 12.  ,  6.  ,  9.5 ,  4.1 ,
       10.43,  5.  ,  7.69,  5.5 ,  6.4 , 12.5 ,  6.25,  8.  ,  9.6 ,
        9.1 ,  7.5 ,  5.  ,  7.  ,  3.55,  8.5 ,  4.5 ,  7.88,  5.25,
        5.  ,  9.33, 10.5 ,  7.5 ,  9.5 ,  9.6 ,  5.87, 11.02,  5.  ,
        5.62, 12.5 , 10.81,  5.4 ,  7.  ,  4.59,  6.  , 11.71,  5.62,
        5.5 ,  4.85,  6.75,  4.25,  5.75,  3.5 ,  3.35, 10.62,  8.  ,
        4.75,  8.5 ,  8.85,  8.  ,  6.  ,  7.14,  3.4 ,  6.  ,  3.75,
        8.89,  4.35, 13.1 ,  4.35,  3.5 ,  3.8 ,  5.26,  3.35, 16.26,
        4.25,  4.5 ,  8.  ,  4.  ,  7.96,  4.  ,  4.15,  5.95,  3.6 ,
        8.75,  3.4 ,  4.28,  5.35,  5.  ,  7.65,  6.94,  7.5 ,  3.6 ,
        1.75,  3.45,  9.63,  8.49,  8.99,  3.65,  3.5 ,  3.43,  5.5 ,
        6.93,  3.51,  3.75,  4.17,  9.57, 14.67, 12.5 ,  5.5 ,  5.15,
        8.  ,  5.83,  3.35,  7.  , 10.  ,  8.  ,  6.88,  5.55,  7.5 ,
        8.93,  9.  ,  3.5 ,  5.77, 25.  ,  6.85,  6.5 ,  3.75,  3.5 ,
        4.5 ,  2.01,  4.17, 13.  ,  3.98,  7.5 , 13.12,  4.  ,  3.95,
       13.  ,  9.  ,  4.55,  9.5 ,  4.5 ,  8.75, 10.  , 18.  , 24.98,
       12.05, 22.  ,  8.75, 22.2 , 17.25,  6.  ,  8.06,  9.24, 12.  ,
       10.61,  5.71, 10.  , 17.5 , 15.  ,  7.78,  7.8 , 10.  , 24.98,
       10.28, 15.  , 12.  , 10.58,  5.85, 11.22,  8.56, 13.89,  5.71,
       15.79,  7.5 , 11.25,  6.15, 13.45,  6.25,  6.5 , 12.  ,  8.5 ,
        8.  ,  5.75, 15.73,  9.86, 13.51,  5.4 ,  6.25,  5.5 ,  5.  ,
        6.25,  5.75, 20.5 ,  5.  ,  7.  , 18.  , 12.  , 20.4 , 22.2 ,
       16.42,  8.63, 19.38, 14.  , 10.  , 15.95, 20.  , 10.  , 24.98,
       11.25, 22.83, 10.2 , 10.  , 14.  , 12.5 ,  5.79, 24.98,  4.35,
       11.25,  6.67,  8.  , 18.16, 12.  ,  8.89,  9.5 , 13.65, 12.  ,
       15.  , 12.67,  7.38, 15.56,  7.45,  6.25,  6.25,  9.37, 22.5 ,
        7.5 ,  7.  ,  5.75,  7.67, 12.5 , 16.  , 11.79, 11.36,  6.1 ,
       23.25, 19.88, 15.38])

	return predictors, target


if __name__ == '__main__':
	main()
