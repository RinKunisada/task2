import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the CSV file into a DataFrame
df = pd.read_csv('filtered_output.csv')  # Replace 'data.csv' with the path to your CSV file

# Convert 'time-start' to datetime and extract the month-year for grouping
df['time_start'] = pd.to_datetime(df['time_start'])
df['month'] = df['time_start'].dt.to_period('M').astype(str)

# Aggregate data by month and person
monthly_summary = df.groupby(['month', 'person'])['duration'].sum().unstack(fill_value=0)

# Plotting
ax = monthly_summary.plot(kind='bar', stacked=True, figsize=(12, 8))

# Set labels and title
ax.set_xlabel('Month')
ax.set_ylabel('Total Duration')
ax.set_title('Monthly Work Duration by Person')

# Format the x-axis to show month and year
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
