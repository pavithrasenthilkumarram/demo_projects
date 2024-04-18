import pandas as pd
import matplotlib.pyplot as plt
import csv

with open("/content/processed_machine_data.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)
data = pd.read_csv("processed_machine_data.csv")
data
