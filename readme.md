# Teacher's Helper App
Created by Will Lapinel, CMS Science Teacher

## Note: Designed specifically for CMS teachers (code for login sequence is unique)

## This application:
- Logs in to MasteryConnect, 
- Downloads the data for a test (name provided by user), 
- And then processes the files to provide some basic analysis

## The analysis currently includes:
- Percent tested (combines ML and standard / honors)
- Avg Score (mean)
- Percent failed (where score < 60%) out of those who tested
- Problem questions (questions which less than 60% of students answered correctly)

## Developer Notes:
- Can create easy executable with Pyinstaller by running "pyinstaller --onefile main.py" and then enter /dist directory and run with "./Teacher-Helper.exe". Binary for Windows is also available as a download.
- Need to add encryption of credentials and 4-digit pin (also encrypted) to access application.
- To add to analysis report in future releases: 
- - names of untested students per class
- - median score