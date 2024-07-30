import pandas as pd
data=pd.read_csv("filtered_output.csv")
# print(data)
# print(data.index)
# print(data.columns)
def process_projects(input_file, output_file):
    df=pd.read_csv(input_file)
    result=df.groupby(['person', 'project'])['duration'].sum().reset_index()
    result.to_csv(output_file, index=False)
    return result

if __name__ == "__main__":
    import sys
    # input_file = sys.argv[1]
    # output_file = sys.argv[2]
    input_file = "filtered_output.csv"
    output_file ="sorted_output.csv" 
    df=process_projects(input_file, output_file)
    print(df)

 