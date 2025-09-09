import pandas as pd
from google.colab import files
uploaded=files.upload()import pandas as pd
import numpy as np

"""airline=pd.read_csv("airlines.csv")
#print(airline.to_string())

airports=pd.read_csv("airports.csv")
"""
flight=pd.read_excel("flight.xlsx")

df=pd.DataFrame(flight)

# 1] we first find out any duplicated values are there then we dropped duplicated values

print(df.duplicated().sum()) # 0 duplicated

df=df.drop_duplicates()

#2] Then we finded null values, column wise we found much more null values

#print(df.isna().sum())


#3]THEN WE REPLACED MISSING TAIL NO WITH MODE VALUE

#print(df['TAIL_NUMBER'].to_string())

mode_tail=df['TAIL_NUMBER'].mode()[0]
df.fillna({'TAIL_NUMBER':mode_tail},inplace=True)

print(df['TAIL_NUMBER'].isna().sum())

#print(df.isna().sum())

#4]Converting time columns


# Function to convert numeric time (e.g., 2354) to a string 'HH:MM'
def format_time(time_value):
    if pd.isna(time_value):
        return np.nan
    time_value = int(time_value)
    hours = time_value // 100
    minutes = time_value % 100
    return f'{hours:02d}:{minutes:02d}'

df['SCHEDULED_DEPARTURE']=df['SCHEDULED_DEPARTURE'].apply(format_time)
df['DEPARTURE_TIME']=df['DEPARTURE_TIME'].apply(format_time)

df['WHEELS_OFF']=df['WHEELS_OFF'].apply(format_time)
df['SCHEDULED_TIME']=df['SCHEDULED_TIME'].apply(format_time)

df['WHEELS_ON']=df['WHEELS_ON'].apply(format_time)

df['SCHEDULED_ARRIVAL']=df['SCHEDULED_ARRIVAL'].apply(format_time)

df['AIR_SYSTEM_DELAY']=df['AIR_SYSTEM_DELAY'].apply(format_time)
df['SECURITY_DELAY']=df['SECURITY_DELAY'].apply(format_time)
df['AIRLINE_DELAY']=df['AIRLINE_DELAY'].apply(format_time)
df['LATE_AIRCRAFT_DELAY']=df['LATE_AIRCRAFT_DELAY'].apply(format_time)
df['WEATHER_DELAY']=df['WEATHER_DELAY'].apply(format_time)


#4] Fill missing values in delay columns with 0
delay_columns = [
    'DEPARTURE_DELAY', 'ARRIVAL_DELAY', 'AIR_SYSTEM_DELAY',
    'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY',
    'WEATHER_DELAY'
]

for col in delay_columns:
    df[col] = df[col].fillna(0)


modedep=df['DEPARTURE_TIME'].mode()[0]
df.fillna({'DEPARTURE_TIME':modedep},inplace=True)

modetaxi=df['TAXI_OUT'].mode()[0]
df.fillna({'TAXI_OUT':modetaxi},inplace=True)

modewh=df['WHEELS_OFF'].mode()[0]
df.fillna({'WHEELS_OFF':modewh},inplace=True)


modeela=df['ELAPSED_TIME'].mode()[0]
df.fillna({'ELAPSED_TIME':modeela},inplace=True)


modeair=df['AIR_TIME'].mode()[0]
df.fillna({'AIR_TIME':modeair},inplace=True)


modew=df['WHEELS_ON'].mode()[0]
df.fillna({'WHEELS_ON':modew},inplace=True)


modetaxii=df['TAXI_IN'].mode()[0]
df.fillna({'TAXI_IN':modetaxii},inplace=True)


modearr=df['ARRIVAL_TIME'].mode()[0]
df.fillna({'ARRIVAL_TIME':modearr},inplace=True)


#by this we can get the notnull values in the column
"""notnull=df[df['CANCELLATION_REASON'].notnull()]
print(notnull.to_string())"""


modec=df['CANCELLATION_REASON'].mode()[0]
df.fillna({'CANCELLATION_REASON':modec},inplace=True)

#print(df.isna().sum())
print(df.head())
import seaborn as sns
import matplotlib.pyplot as plt

# Group the data by Airline and calculate the mean of departure and arrival delays
df_airlines = df.groupby('AIRLINE')[['DEPARTURE_DELAY', 'ARRIVAL_DELAY']].mean().reset_index()


# Create and save the Departure Delay bar chart
plt.figure(figsize=(5, 4))
sns.barplot(x='AIRLINE', y='DEPARTURE_DELAY', data=df_airlines, palette='viridis')
plt.title('Average Departure Delay by Airline', fontsize=16)
plt.xlabel('Airline', fontsize=12)
plt.ylabel('Average Departure Delay (Minutes)', fontsize=12)
plt.grid(axis='y',linestyle='--')

# Sort by mean arrival delay for the second chart
#df_airlines_sorted_arr = df_airlines.sort_values(by='ARRIVAL_DELAY', ascending=False)

# Create and save the Arrival Delay bar chart
plt.figure(figsize=(5, 4))
sns.barplot(x='AIRLINE', y='ARRIVAL_DELAY', data=df_airlines, palette='magma')
plt.title('Average Arrival Delay by Airline', fontsize=16)
plt.xlabel('Airline', fontsize=12)
plt.ylabel('Average Arrival Delay (Minutes)', fontsize=12)
plt.grid(axis='y',linestyle='--')

# Filter the DataFrame for cancelled flights
cancelled_flights_df = df[df['CANCELLED'] == 1]

# Get the count of cancelled flights per airline
cancelled_by_airline = cancelled_flights_df['AIRLINE'].value_counts().reset_index()
cancelled_by_airline.columns = ['Airline', 'Count']

# Create the bar chart
plt.figure(figsize=(5,4))
sns.barplot(x='Airline', y='Count', data=cancelled_by_airline, palette='plasma')
plt.title('Number of Cancelled Flights by Airline', fontsize=16)
plt.xlabel('Airline', fontsize=12)
plt.ylabel('Number of Cancelled Flights', fontsize=12)
# Filter the data to get only cancelled flights
cancelled_flights = df[df['CANCELLED'] == 1]

# Get the count of each cancellation reason
cancellation_reasons = cancelled_flights['CANCELLATION_REASON'].value_counts()
print(cancellation_reasons)
reasons = cancellation_reasons.index.tolist()
counts = cancellation_reasons.values.tolist()

# Create the pie chart
plt.figure(figsize=(4, 5))
plt.pie(x=counts, labels=reasons, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Distribution of Flight Cancellation Reasons', fontsize=16)
plt.legend()


"""'A': Carrier (Airline) related issues

'B': Weather"""import matplotlib.pyplot as plt
import seaborn as sns

# Check unique cancellation reasons
print(df['CANCELLATION_REASON'].unique())

# Count cancellations by reason
cancel_counts = df['CANCELLATION_REASON'].value_counts().reset_index()
print(cancel_counts)
cancel_counts.columns = ['Reason', 'Count']

# Map reason codes
reason_map = {
    'A': 'Carrier',
    'B': 'Weather',
    'C': 'NAS (Air System)',
    'D': 'Security'
}
cancel_counts['Reason'] = cancel_counts['Reason'].map(reason_map).fillna(cancel_counts['Reason'])

# Plot
plt.figure(figsize=(4,5))
sns.barplot(x='Reason', y='Count', data=cancel_counts, palette='viridis')
plt.title('Flight Cancellations by Reason', fontsize=14)
plt.xlabel('Cancellation Reason')
plt.ylabel('Number of Flights Cancelled')
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt


# Airline code to name mapping
airline_names = {
    "AA": "American Airlines",
    "DL": "Delta Airlines",
    "UA": "United Airlines",
    "WN": "Southwest Airlines",
    "AS": "Alaska Airlines",
    "B6": "JetBlue Airways",
    "F9": "Frontier Airlines",
    "NK": "Spirit Airlines",
    "HA": "Hawaiian Airlines",
    "VX": "Virgin America"
}

# Step 1: Define on-time flights
df['ON_TIME'] = df['ARRIVAL_DELAY'] <= 0

# Step 2: Group by airline and calculate punctuality %
punctuality = df.groupby('AIRLINE')['ON_TIME'].mean().reset_index()
punctuality['ON_TIME'] = punctuality['ON_TIME'] * 100   # convert to %

# Step 3: Map airline codes to full names
punctuality['AIRLINE_NAME'] = punctuality['AIRLINE'].map(airline_names)


# Step 4: Horizontal bar plot
plt.figure(figsize=(6,5))
sns.barplot(y='AIRLINE_NAME', x='ON_TIME', data=punctuality, palette='crest')
plt.title('Punctuality by Airline (On-Time Arrival %)', fontsize=16)
plt.xlabel('On-Time Arrival (%)', fontsize=12)
plt.ylabel('Airline', fontsize=12)
plt.grid(axis='x', linestyle='--')
