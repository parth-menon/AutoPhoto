import tkinter as tk
from ui import UI

genAI_API_Key = None

def main():
    root = tk.Tk()
    ui = UI(root, genAI_API_Key)
    root.protocol("WM_DELETE_WINDOW", ui.close)
    root.deiconify()
    root.focus_force()
    root.mainloop()

if __name__ == "__main__":
    main()