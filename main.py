import tkinter as tk
from ui import UI

genAI_API_Key = ""

def main():
    root = tk.Tk()
    ui = UI(root)
    root.deiconify()
    root.focus_force()
    root.mainloop()

if __name__ == "__main__":
    main()