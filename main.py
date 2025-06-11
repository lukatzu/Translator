import sys

def main():
    print("DnD Translator Launcher\n")
    print("1. Command-line mode")
    print("2. GUI mode")
    print("3. Quit\n")
    choice = input("Select mode (1/2/3): ").strip()
    if choice == "1":
        from translator import main as cmd_main
        cmd_main()
    elif choice == "2":
        import gui
        import tkinter as tk
        root = tk.Tk()
        gui_app = gui.TranslatorGUI(root)
        root.deiconify()  # Show the main window
        root.lift()
        root.attributes('-topmost', True)
        root.after_idle(root.attributes, '-topmost', False)
        root.mainloop()
    elif choice == "3":
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()