import os
import glob

def get_latest_csv():
    downloads_dir = os.path.expanduser('~/Downloads')
    csv_files = glob.glob(os.path.join(downloads_dir, '*.csv'))
    if not csv_files:
        return None
    return max(csv_files, key=os.path.getctime)
