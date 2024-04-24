import os
import glob

def most_recent_csv_in_downloads():
    downloads_dir = os.path.expanduser('~/Downloads')
    csv_files = glob.glob(os.path.join(downloads_dir, '*.csv'))
    if not csv_files:
        return None
    return max(csv_files, key=os.path.getctime)

# Example usage:
most_recent_csv = most_recent_csv_in_downloads()
if most_recent_csv:
    print("The most recent CSV file in the downloads directory is:", most_recent_csv)
else:
    print("No CSV files found in the downloads directory.")
