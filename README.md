# Automatically create Instagram accounts!

## Installation Requirements
This project was implemented on MacOs. Therefore, for other operating systems, please download the corresponding web-driver for chrome from [here](https://chromedriver.chromium.org). The screen resolution for my laptop was set at (1440,900) pixels.  
- Python 3.6.10  
- selenium `pip install selenium==3.141.0`.  
- beautifulsoup4 `pip install beautifulsoup4==4.9.1`.  
- PyAutoGUI  `pip install PyAutoGUI==0.9.50`.  

## Project motivation  
This project was developed soley for the purpose of showcasing the power of automation using python. **The code in this repository has been left incomplete** on purpose, for obvious ethical reasons. **Please use this repo for learning purposes only!.**   
This project aims to automatically create an instagram account without any user intervention.  

## File Descriptions
- login.py: The program that is the work-horse of the project. It contains the code that will automatically create a temporary mail-id; and use that to create an instagram account.  
- mail_signup.py: Program that only creates a temporary mail-id *(not required for running of project)*  
- mouse_test.py: Program that is used to find the position of the mouse pointer, and various buttons on the screen to facilitate automation. *(not required for running of the project)*
- chromedriver84: chrome driver used by the selenium python package to work with google chrome browser (download the version that corresponds with the version of chrome on your machine). The folder that this file is located in must be added to the PATH variable. (This can be done by opening that folder in the terminal and entering `export PATH="$pwd:$PATH")`.  

## Working/ Interacting with the project
After the required packages are installed and the chrome driver's location has been added to the path variable run `python login.py`.  
The project uses python GUI automation, where the python program controls the keyboard and the mouse pointer.  
In the case of my laptop, the window of chrome opened such that the top left corner of the window was at pixel(23,46) and the bottom right corner was at pixel(1220,820). The rest of the values (i.e for inputting date, clicking submit button) are all hard coded. Thus, if the window does not open at the correct size, these will not give required output. This problem can be fixed by hardcoding for each individual machine that the program is run on.  

## Project summary.  
- The project successfully setup a temporary mail id (Different each time it is run).  
- This mail id was used to enter the signup details for instagram.  
- Python GUI automation was used to enter the details for the birth-date verification and submit.  
- Obtain the verification code from the temporary mail-id.  
**Stop execution of program, without actually submitting the verification code**.  

