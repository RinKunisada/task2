import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('sorted_output.csv')  # Replace 'data.csv' with the path to your CSV file

# Group by the 'project' column and sum up the 'duration'
project_summary = df.groupby('project')['duration'].sum().reset_index()

# Rename the columns for clarity
project_summary.columns = ['Project', 'Total Duration']

# Calculate the total duration across all projects
total_duration = project_summary['Total Duration'].sum()

# Append a new row for the total duration
total_row = pd.DataFrame({'Project': ['Total'], 'Total Duration': [total_duration]})
project_summary = pd.concat([project_summary, total_row], ignore_index=True)

# Print the resulting DataFrame
print(project_summary)

# Save the resulting DataFrame to a new CSV file
project_summary.to_csv('project_summary.csv', index=False)
