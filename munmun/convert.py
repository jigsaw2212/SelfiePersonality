import csv,pandas, os

df = pandas.read_csv('EquiPartition.csv')

for item in range(len(df['Name'])):
	