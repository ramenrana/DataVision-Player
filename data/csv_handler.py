import os
import pandas as pd
def load_csv_files(video_path):
    """Loads CSV filenames from the same directory as the video."""
    directory = os.path.dirname(video_path)
    csv_files = []
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            csv_files.append(os.path.join(directory, file))
    return csv_files

def extract_common_columns(csv_files):
    """Extracts common column names across all CSV files."""
    common_columns = None
    exclude_columns = {'index', 'Unnamed: 0', 'MTS_TIME', 'timestamp', 'timestamp[s]'}

    for file in csv_files:
        try:
            df = pd.read_csv(file, nrows=1)  # Read only header
            columns = set(df.columns) - exclude_columns

            if common_columns is None:
                common_columns = columns
            else:
                common_columns &= columns  # Intersection
        except Exception as e:
            print(f"Error reading {file}: {e}")
    
    return sorted(list(common_columns)) if common_columns else []