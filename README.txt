Instructions for Using Twitch Streamer App:

Requirements:

Python 3.7 or higher installed (Download from the official website: https://www.python.org/downloads)
Selenium library installed (Run the command pip install selenium in the command prompt or terminal)
PyQt5 library installed (Run the command pip install pyqt5 in the command prompt or terminal)
Chrome web browser installed

Step 1: Prepare the Environment:

Install Python: Download and install the Python programming language from the official website (https://www.python.org/downloads). Follow the installation instructions for your operating system.

Install Selenium: Open the command prompt or terminal and run the command pip install selenium to install the Selenium library. This library is required to automate the web browser.

Install PyQt5: Open the command prompt or terminal and run the command pip install pyqt5 to install the PyQt5 library. This library is required for the Twitch Streamer app's user interface.

Step 2: Set Up the ChromeDriver:

Determine Chrome Browser Version: Open Google Chrome and go to the following URL: chrome://settings/help. Note the version number displayed on this page.

Download the ChromeDriver: Visit the ChromeDriver website (https://sites.google.com/a/chromium.org/chromedriver/downloads) and download the version of ChromeDriver that matches your Chrome browser version. Make sure to download the appropriate version for your operating system.

Extract the ChromeDriver: Extract the downloaded ChromeDriver executable from the archive file. Remember the path where you have extracted the driver.

Step 3: Install the Chrome Extension:

Install the "Automatic Twitch Drops Monitor" extension: Open Google Chrome and navigate to the Chrome Web Store using the provided link (https://chrome.google.com/webstore/detail/automatic-twitch-drops-mo/kfhgpagdjjoieckminnmigmpeclkdmjm). Click on "Add to Chrome" to install the extension.

Configure the Extension: After installing the extension, follow the instructions within the extension to configure your Twitch account and desired settings.

Step 4: Configure the Twitch Streamer App:

Open the Twitch Streamer App Code: Open the Python script file for the Twitch Streamer app in a text editor.

Update the Configuration Variables: Locate the following variables in the code:

CHROME_DRIVER_PATH: Set this variable to the file path of the downloaded ChromeDriver executable.
CHROME_USER_DATA_DIR: Set this variable to the path of the Chrome user data directory (C:\Users\<your_username>\AppData\Local\Google\Chrome\User Data for Windows).
CHROME_PROFILE_DIRECTORY: Set this variable to the name of the profile directory you are using in Chrome.
Note: To find the profile directory you are using in Chrome, follow these steps:

Open Google Chrome.
In the address bar, type chrome://version and press Enter.
Look for the "Profile Path" field. The path mentioned there indicates the user profile you are currently using.
Set the CHROME_PROFILE_DIRECTORY variable in the code to match the profile directory name mentioned in the "Profile Path" field.
Please ensure that you have the correct profile directory name and update the CHROME_PROFILE_DIRECTORY variable accordingly.

Step 5: Launch and Use the Twitch Streamer App:

Run the Twitch Streamer App: Open a command prompt or terminal, navigate to the directory containing the Twitch Streamer app file, and execute the Python script by running the command python twitch_streamer.py.

Add Twitch Channels: In the app's user interface, enter the Twitch channel URLs in the "Input twitch URL here" text box and click the "Add Channel" button to add each channel you want to watch. Use the "Remove Channel" button to remove any channels if needed.

Set Duration and Start Watching: Enter the desired duration (in minutes) for each channel in the "Time per channel (minutes)" text box. Click the "Start" button to begin watching the channels. The app will automatically switch between the channels for the specified durations.

Please ensure that you have installed Python, Selenium, PyQt5, and Chrome, and have the correct ChromeDriver version that matches your Chrome browser version. Additionally, make sure the Chrome user data directory is properly configured with the desired profile and the "Automatic Twitch Drops Monitor" extension is set up for your Twitch account.
