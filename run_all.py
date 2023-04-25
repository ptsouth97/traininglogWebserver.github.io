#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load
import os
import data_manipulations
import plot
import body_metrics
import runstats
import power
import recovery
from itertools import cycle
from time import sleep


def main():
	''' Load dataframe from csv file'''

	# Download latest Google Sheet data as a csv file
	load.get_url()

	# Load csv file to a pandas dataframe
	filename = 'trainingLog.csv'
	df = load.to_df(filename)

	'''	
	for frame in cycle(r'-\|/'):
		print('\r', frame, sep='', end='', flush=True)
		sleep(0.2)
	'''
	print("Calculating body metrics...")
	body_metrics.weight(df)
	body_metrics.calories(df)

	print("Calculating run stats...")
	runstats.hr(df)
	runstats.pace(df)
	#runstats.by_run_type(df, "GARMIN Average HR (bpm)")
	
	return


if __name__ == '__main__':
	main()
