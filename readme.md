# Teacher's Helper App
Created by Will Lapinel, Science Teacher in Charlotte-Mecklenburg Schools


## Purpose:
- Our PLC (Earth Science teachers) at my school spend a lot of time (up to an hour for each test, for a total of 8 hours per semester) manually retrieving and processing test data from Mastery Connect. I wrote this command-line-interface application in order to give that time back to myself and my colleagues.

## This application:
- Logs in to MasteryConnect
- Downloads the data for a test (name provided by user), 
- And then processes the files to provide some basic analysis
- Produces data in CSV file format 

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
- This is designed specifically for teachers at Charlotte-Mecklenburg Schools, as the code for login sequence is unique, but if you can modify it for your own login then the rest of it may work.  I will try in the future to add the ability to parse the CSV files after manually downloading, but currently that feature is not available. Currently the program just looks for the latest CSV file in the downloads folder and processes them sequentially.
