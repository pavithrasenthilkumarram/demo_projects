# @title
import pandas as pd
from datetime import datetime, timedelta

# Function to calculate delay time
def calculate_delay(arrival_time, scheduled_arrival_time):
    arrival_time = datetime.strptime(arrival_time, '%H:%M')
    scheduled_arrival = datetime.strptime(scheduled_arrival_time, '%H:%M')
    delay = (arrival_time - scheduled_arrival).total_seconds() / 60
    return delay

# Read input file
input_file = "/content/sample_data_train.csv"  # Taking the input file is in CSV format
df = pd.read_csv(input_file)

# Filter data for the past 30 days
current_date = datetime.now().date()
thirty_days_ago = current_date - pd.DateOffset(days=30)
df['date_of_journey'] = pd.to_datetime(df['date_of_journey'])
past_30_days_data = df[df['date_of_journey'] >= thirty_days_ago]

# Get train number from user
train_num = int(input("Enter the train number:"))

# Filter data for the specified train number
train_data = past_30_days_data[past_30_days_data['train_number'] == train_num]

if len(train_data) == 0:
    print("No data available for the specified train number.")
else:
    # Calculate delay time for the specified train
    delay_in_minutes = []
    for index, row in train_data.iterrows():
        delay = calculate_delay(row['actual_arrival_time'], row['scheduled_arrival_time'])
        delay_in_minutes.append(delay)

    # Calculate average delay time
    average_delay = sum(delay_in_minutes) / len(delay_in_minutes)
    print("Average delay time of train", train_num , "in the past 30 days:", round(average_delay,0), "minutes")
