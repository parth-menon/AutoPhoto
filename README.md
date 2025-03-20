# AutoPhoto

AutoPhoto is a simple Python program designed to help you organize images and videos you have been taking for years. Unlike many commercial solutions that either run locally(like PhotoMove) or on the cloud and often use your images to train AI models(like GooglePhotos), AutoPhoto offers a straightforward, privacy-focused approach to media organization.

<img width="706" alt="Photo" src="https://github.com/user-attachments/assets/c60eae0b-adac-44ee-98d6-5f305e7c26f4" />


## Features

- **Folder Organization**: Sorts images and videos into folders based on the date they were taken, using the format **YEAR > MONTH > DAY** by default.
- **Customizable Formats**: Offers options in the UI to select alternative folder formats if desired.
- **Usable UI**: No command-line interaction is required; everything is accessible through a user-friendly interface.
- **Date Extraction Methods**:
  - Uses EXIF data on images to determine the creation date.
  - If EXIF data is not available, attempts to extract the date from the filename.
  - If both methods fail, places the file in an **Unorganized** folder.
- **Gemini API Integration**: Allows users to pass a Gemini API key, which can be used to extract the date based on the file names. This is particularly useful when the normal filename date extraction fails.

## Installation and Running

Couple of ways to run AutoPhoto

  1. **Using the released app**
     Head over to the releases section and download the latest version and run the app.<br />
     On MacOS, if the app says it cannot run, please run Terminal, go to the folder that contains AutoPhoto.app and enter the command<br />
     `chmod -R +x AutoPhoto.app`<br />
     This enables the app to be executable on your device.

  2. **Running the code directly**
     Download the repo from github.<br />
     Ensure Python3 is installed, preferably version 3.12.<br />
     Open Terminal or Command Prompt, go to the folder that contains AutoPhoto folder and enter the command<br />
     `python main.py`

  3. **Using an IDE**
     If you are not comfortable using terminal, then Download and install PyCharm Community Edition from the official JetBrains website https://www.jetbrains.com/pycharm/download/<br />
     Clone or download this repository to your local machine and open it in PyCharm.<br />
     Right-click on `main.py` and select "Run" to start the application.

## Contributing

Thanks for your interest in contributing to AutoPhoto!

## License

AutoPhoto is released under **The Apache License, Version 2.0**.

## Acknowledgments

A special thanks to all the crappy file and gallery organizing apps that are paid but don't even use basic filename extraction. They forced me to build one myself.
