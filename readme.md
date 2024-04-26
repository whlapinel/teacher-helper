# Teacher's Helper App
Created by Will Lapinel, CMS Science Teacher

## Note: Designed specifically for CMS teachers (code for login sequence is unique)

## This application:
- Logs in to MasteryConnect, 
- Downloads the data for a test (name provided by user), 
- And then processes the files to provide some basic analysis

## The analysis currently includes:
- Percent tested (combines ML version and Std/Honors)
- Avg Score 
- Percent failed (< 60%)
- Problem questions (questions which less than 60% of students answered correctly)

## Developer Notes:
- Can create easy executable with Pyinstaller by running pynstaller "--one-file main.py" and then enter /dist directory and run with "./main.exe"
- Need to add encryption of credentials and 4-digit pin (also encrypted) to access application.
- To add to analysis report: 
- - names of untested students per class
- - combined percentage tested (combine ML and Standard)