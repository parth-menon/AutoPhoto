import atexit
import getpass
import os
import threading
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from processor import Processor
from result import Result

class UI:
    def __init__(self, root, api_key):
        self.root = root
        self.api_key = api_key
        self.root.title("GallerySorter")
        self.root.geometry("700x600")  # Set the window size to 400x300 pixels

        self.folder_label = tk.Label(root, text="Select Folder:")
        self.folder_label.pack()

        self.folder_entry = tk.Label(root, width=50)
        self.folder_entry.pack()

        self.folder_button = tk.Button(root, text="Browse", command=self.select_folder)
        self.folder_button.pack()

        self.year_label = tk.Label(root, text="Year: YYYY")
        self.year_label.pack()

        self.month_format = tk.StringVar()
        self.month_format.set("MM")  # default value

        self.month_label = tk.Label(root, text="Month Format:")
        self.month_label.pack()

        self.month_format_frame = tk.Frame(root)
        self.month_format_frame.pack()
        self.month_format_mm = tk.Radiobutton(self.month_format_frame, text="MM", variable=self.month_format, value="MM")
        self.month_format_mm.pack(side=tk.LEFT)
        self.month_format_yyyymm = tk.Radiobutton(self.month_format_frame, text="YYYY_MM", variable=self.month_format, value="YYYY_MM")
        self.month_format_yyyymm.pack(side=tk.LEFT)

        self.date_format = tk.StringVar()
        self.date_format.set("DD")  # default value

        self.date_label = tk.Label(root, text="Date Format:")
        self.date_label.pack()

        self.date_frame = tk.Frame(root)
        self.date_frame.pack()
        self.date_no_date = tk.Radiobutton(self.date_frame, text="No Date (attribute photos to the month folder)",
                                      variable=self.date_format, value="No Date")
        self.date_no_date.pack(side=tk.LEFT)
        self.date_dd = tk.Radiobutton(self.date_frame, text="DD", variable=self.date_format, value="DD")
        self.date_dd.pack(side=tk.LEFT)
        self.date_mm_dd = tk.Radiobutton(self.date_frame, text="MM_DD", variable=self.date_format, value="MM_DD")
        self.date_mm_dd.pack(side=tk.LEFT)
        self.date_yyyymmdd = tk.Radiobutton(self.date_frame, text="YYYY_MM_DD", variable=self.date_format, value="YYYY_MM_DD")
        self.date_yyyymmdd.pack(side=tk.LEFT)

        self.destination_label = tk.Label(root, text="Select Destination:")
        self.destination_label.pack()

        self.destination_entry = tk.Label(root, width=50)
        self.destination_entry.pack()

        self.destination_button = tk.Button(root, text="Browse", command=self.select_destination)
        self.destination_button.pack()

        self.copy_or_move = tk.StringVar()
        self.copy_or_move.set("Copy")  # default value

        self.copy_move_frame = tk.Frame(root)
        self.copy_move_frame.pack()
        self.copy = tk.Radiobutton(self.copy_move_frame, text="Copy Files", variable=self.copy_or_move,
                                              value="Copy")
        self.copy.pack(side=tk.LEFT)
        self.move = tk.Radiobutton(self.copy_move_frame, text="Move Files", variable=self.copy_or_move,
                                                  value="Move")
        self.move.pack(side=tk.LEFT)

        self.go_button = tk.Button(root, text="Go", command=self.go, width=7, height=2)
        self.go_button.pack()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Horizontal.TProgressbar", troughcolor='white', bordercolor='white', background='green',
                        lightcolor='green', darkcolor='green',thickness=20)
        self.loading_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="indeterminate",
                                       style="Horizontal.TProgressbar")
        self.loading_bar.pack()

        tk.Label(root, text="").pack()
        self.processed_label = tk.Label(root, text="Processed:", font=("Arial", 16, "bold"))
        self.processed_label.pack()

        self.year_folders_label = tk.Label(root, text="Year folders generated: 0")
        self.year_folders_label.pack()

        self.month_folders_label = tk.Label(root, text="Month folders generated: 0")
        self.month_folders_label.pack()

        self.files_organised_label = tk.Label(root, text="Files organised: 0")
        self.files_organised_label.pack()

        self.files_not_organised_label = tk.Label(root, text="Files that could not be organised: 0")
        self.files_not_organised_label.pack()
        self.files_not_moved_label = tk.Label(root, text="Files not copied/moved: 0")
        self.files_not_moved_label.pack()

        self.close_button = tk.Button(root, text="Close", command=self.close)
        self.close_button.pack()
        root.protocol("WM_DELETE_WINDOW", self.close)
        atexit.register(self.close)


    def select_folder(self):
        folder_path = filedialog.askdirectory(initialdir="/Users/" + getpass.getuser() + "/Downloads/")
        self.folder_entry.config(text=folder_path)

    def select_destination(self):
        folder_path = filedialog.askdirectory(initialdir="/Users/" + getpass.getuser() + "/Downloads/")
        self.destination_entry.config(text=folder_path)

    def go(self):
        source_path = self.folder_entry.cget("text")
        if not source_path:
            tk.messagebox.showerror("Error", "Please select a folder")
            self.go_button.config(state="normal")
            self.close_button.config(state="normal")
            return
        destination_path = self.destination_entry.cget("text")
        if not destination_path:
            tk.messagebox.showerror("Error", "Please select a destination")
            self.go_button.config(state="normal")
            self.close_button.config(state="normal")
            return
        if os.path.commonpath([source_path, destination_path]) == source_path:
            tk.messagebox.showwarning("Warning", "Destination is inside source folder. This will cause issues.")
            return

        self.go_button.config(state="disabled")
        self.close_button.config(state="disabled")
        self.processor = Processor(source_path, destination_path, self.month_format.get(), self.date_format.get(), self.copy_or_move.get(), self.api_key)
        threading.Thread(target=self.processor.process_files, args=(self.complete,)).start()
        self.loading_bar.start(20)

    def complete(self, result: Result):
        self.loading_bar.stop()
        self.year_folders_label.config(text="Year folders generated: " + str(result.year_folders))
        self.month_folders_label.config(text="Month folders generated: " + str(result.month_folders))
        self.files_organised_label.config(text="Files organised: " + str(result.files_organised))
        self.files_not_organised_label.config(text="Files that could not be organised: "+ str(result.files_not_organised))
        self.files_not_moved_label.config(
            text="Files not copied/moved: " + str(result.files_not_moved))
        self.go_button.config(state="normal")
        self.close_button.config(state="normal")

    def close(self):
        if hasattr(self, 'processor') and self.processor:
            self.processor.stop()
        self.root.destroy()