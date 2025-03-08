import datetime
import os
import shutil

import exifread
from pyasn1.type.univ import Boolean

import dateextractor
from ai import AiClient
from result import Result


class Processor:
    def __init__(self, source_path, destination_path, month_format, date_format, copy_or_move, api_key):
        self.unorganised_files = []
        self.source_folder = None
        self.source_path = source_path
        self.destination_path = destination_path
        self.month_format = month_format
        self.date_format = date_format
        self.copy_or_move = copy_or_move
        self.client = None
        if api_key:
            self.client = AiClient(api_key)
        self.result = Result()
        self.map = {}
        self.run = False

    def process_files(self, complete):
        self.run = True
        self.desination_folder = os.path.join(self.destination_path, "Organised")
        if not os.path.exists(self.desination_folder):
            os.makedirs(self.desination_folder)


        folders_to_process = [self.source_path]
        while len(folders_to_process) > 0:
            if not self.run:
                return
            current_folder = folders_to_process.pop(0)
            for entry in os.scandir(current_folder):
                if entry.is_dir():
                    folders_to_process.append(entry.path)
                else:
                    if not entry.name.endswith((".json", ".html", ".xml", ".db", ".DS_Store")):
                        self.organize_file(entry)
        for file in self.unorganised_files:
            self.place_file_in_correct_location(file, "Unorganised")
        complete(self.result)
        pass

    def organize_file(self, file: os.DirEntry):
        year_month_day = self.get_year_month_day(file)
        if year_month_day and self.valid_date(year_month_day):
            year, month, day = self.get_year_month_day(file).split(":")
            if year not in self.map:
                self.result.year_folders += 1
                self.map[year] = True
            if (year+"_"+month) not in self.map:
                self.result.month_folders += 1
                self.map[year+"_"+month] = True

            self.place_file_in_correct_location(file.path, year+"/"+month+"/"+day)
            self.result.files_organised+=1
        else:
            self.unorganised_files.append(file.path)
            self.result.files_not_organised += 1

    def get_year_month_day(self, file):
        # First we will check the exif data
        creation_date = self.get_exif_creation_date(file.path)
        year, month, day = None, None, None
        if creation_date:
            # Got Creation Date from EXIF data
            return creation_date

        # Extract Creation Date from file name if no exif data
        extracted_date = dateextractor.extract_and_validate_date(file.name)
        if extracted_date:
            return extracted_date

        # Extract Creation Date from file name using AI
        if self.client:
            extracted_date = self.client.get_file_date(file)
            if extracted_date:
                return extracted_date

        # Extract Creation Date from file name using file info
        # stat = os.stat(file.path)
        # timestamp = stat.st_birthtime
        # dt = datetime.datetime.fromtimestamp(timestamp)
        # extracted_date = dt.strftime("%Y:%m:%d")
        # if extracted_date:
        #     return extracted_date
        return None

    def get_exif_creation_date(self,file_path):
        if file_path.lower().endswith(
                ('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            return self.get_exif_creation_dates_image(file_path)
        return None


    def get_exif_creation_dates_image(self, file):
        try:
            with open(file, 'rb') as fh:
                tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
                dateTaken = tags.get("EXIF DateTimeOriginal", None)
                if dateTaken:
                    return str(dateTaken).split()[0]
        except:
            pass
        return None

    def valid_date(self, year_month_day):
        if year_month_day:
            year, month, day = year_month_day.split(":")
            try:
                dt = datetime.datetime.strptime(year_month_day, "%Y:%m:%d")
                tomorrow = datetime.date.today() + datetime.timedelta(days=1)
                if dt.date() < tomorrow:
                    return True
            except ValueError:
                return False
        return False

    def place_file_in_correct_location(self, original_file_path, organised_folder_path):
        destination = os.path.join(self.desination_folder, organised_folder_path)
        os.makedirs(destination, exist_ok=True)
        # print(original_file_path, destination)
        print(self.copy_or_move)
        # if self.copy_or_move == "Move":
        #     shutil.move(original_file_path, destination)
        # else:
        #     shutil.copy(original_file_path, destination)

    def stop(self):
        self.run = False

