class Result:
    def __init__(self):
        self.year_folders = 0
        self.month_folders = 0
        self.files_organised = 0
        self.files_not_organised = 0

    def update(self, year_folders, month_folders, files_organised, files_not_organised):
        self.year_folders = year_folders
        self.month_folders = month_folders
        self.files_organised = files_organised
        self.files_not_organised = files_not_organised
