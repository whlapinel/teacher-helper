# Test Data Helper App
by Will Lapinel

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
- Was hoping to run with easy executable via PyInstaller but I'm having issues with it. Might require teachers to install Python and run the same way I'm running in testing and development.
- Need to add encryption of credentials and 4-digit pin (also encrypted) to access application. 