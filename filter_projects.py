import pandas as pd
import sys

def filter_data(input_file, output_file, year, hours_threshold):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Convert the 'time_start' and 'time_end' columns to datetime
    try:
        df['time_start'] = pd.to_datetime(df['time_start'])
        df['time_end'] = pd.to_datetime(df['time_end'])
    except Exception as e:
        print(f"Error parsing datetime: {e}")
        sys.exit(1)

    # Filter entries by year
    df = df[df['time_start'].dt.year == year]

    # Group by project and sum the durations
    project_hours = df.groupby('project')['duration'].sum().reset_index()

    # Filter projects by hours threshold
    valid_projects = project_hours[project_hours['duration'] >= hours_threshold]['project']
    df = df[df['project'].isin(valid_projects)]

    # Write the filtered result to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python filter_projects.py <input_file> <output_file> <year> <hours_threshold>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    year = int(sys.argv[3])
    hours_threshold = int(sys.argv[4])
    
    filter_data(input_file, output_file, year, hours_threshold)
