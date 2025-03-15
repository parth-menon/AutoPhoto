# GallerySorter

GallerySorter is a simple Python program designed to help you organize images and videos you have been taking for years. Unlike many commercial solutions that either run locally(like PhotoMove) or on the cloud and often use your images to train AI models(like GooglePhotos), GallerySorter offers a straightforward, privacy-focused approach to media organization.

<img width="723" alt="Screenshot 2025-03-08 at 6 43 07 pm" src="https://github.com/user-attachments/assets/cfdce1d1-6b35-4d51-a833-c2905e24d92c" />

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

To run GallerySorter, follow these steps:

1. **Install PyCharm Community Edition**: Download and install PyCharm Community Edition from the official JetBrains website https://www.jetbrains.com/pycharm/download/
2. **Download the Repository**: Clone or download this repository to your local machine.
3. **Open the Project in PyCharm**: Open the downloaded repository in PyCharm.
4. **Run the Program**: Right-click on `main.py` and select "Run" to start the application.

## Contributing

Thanks for your interest in contributing to GallerySorter!

## License

GallerySorter is released under **The Apache License, Version 2.0**.

## Acknowledgments

A special thanks to all the crappy file and gallery organizing apps that are paid but don't even use basic filename extraction. They forced me to build one myself.
