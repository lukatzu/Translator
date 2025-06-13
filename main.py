import sys
import os

def detect_languages():
    # Detect available language JSON files in the current directory
    langs = []
    if os.path.exists("kyrsan.json"):
        langs.append(("Kyrsan", "kyrsan.json"))
    if os.path.exists("celestial.json"):
        langs.append(("Celestial", "celestial.json"))
    # to add more languages, simply add their names and JSON paths here
    # example:
    """
    if os.path.exists("language_path.json"): 
        languages.append(("Language_NAME", "language_path.json"))
    """
    return langs

def main():
    languages = detect_languages()
    if not languages:
        print("No languages detected!")
        sys.exit(1)

    print("DnD Translator Launcher\n")
    print("1. Command-line mode")
    print("2. GUI mode")
    print("3. Quit\n")
    choice = input("Select mode (1/2/3): ").strip()
    if choice == "1":
        from translator import main as cmd_main
        cmd_main(languages)  # Pass the available languages
    elif choice == "2":
        import gui
        import tkinter as tk
        # Patch gui.LANGUAGES dynamically
        gui.LANGUAGES = [("English", None)] + languages
        root = tk.Tk()
        gui_app = gui.TranslatorGUI(root)
        root.deiconify()
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