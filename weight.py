#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load
import os
import data_manipulations
import plot


def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	
	df = load.to_df(filename)
	
	weight(df)
	calories(df)
	
	return


def weight(df):
	''' Plot weight data times series and year-over-year'''

	variable = 'Weight (pounds)'

	plot.year_over_year(df, variable)
	plot.single_variable_time_series(df, variable, "orange")

	return


def calories(df):
	''' Plot calorie data year-over-year'''

	variable = 'Calories consumed'

	plot.year_over_year(df, variable)
	plot.single_variable_time_series(df, variable, "purple")

	return


if __name__ == '__main__':
	main()
