# DnD Translator GUI (Work in progress) 1.0
# This script provides a graphical user interface for the DnD Translator, allowing users to translate text between English and supported languages.

import tkinter as tk # Standard library for GUI
from tkinter import ttk, scrolledtext # For text areas and comboboxes
from translator import load_alphabet, translate, reverse_translate # Import translation functions

# List of supported languages with their JSON files
LANGUAGES = [
    ("English", None),
    ("Kyrsan", "kyrsan.json"),
    ("Celestial", "celestial.json"),
]

class TranslatorGUI: # Main GUI class for the translator application
    def __init__(self, root):
        self.root = root # Initialize the main window
        self.root.title("DnD Translator") # Set the window title

        # Language selectors
        self.left_lang = tk.StringVar(value="English")
        self.right_lang = tk.StringVar(value="Kyrsan")

        lang_names = [name for name, _ in LANGUAGES]
        self.left_lang.set(lang_names[0])
        self.right_lang.set(lang_names[1] if len(lang_names) > 1 else lang_names[0])

        top_frame = tk.Frame(root)
        top_frame.pack(padx=10, pady=10, fill="x")

        self.left_combo = ttk.Combobox(top_frame, values=lang_names, textvariable=self.left_lang, state="readonly", width=15)
        self.left_combo.grid(row=0, column=0, padx=5)
        swap_btn = ttk.Button(top_frame, text="⇄", command=self.swap_languages)
        swap_btn.grid(row=0, column=1, padx=5)
        self.right_combo = ttk.Combobox(top_frame, values=lang_names, textvariable=self.right_lang, state="readonly", width=15)
        self.right_combo.grid(row=0, column=2, padx=5)

        # Warning label for celestial numerals
        self.warning_label = tk.Label(root, text="", fg="red", font=("TkDefaultFont", 10), anchor="w", justify="left")
        self.warning_label.pack(padx=10, pady=(0, 5), fill="x")

        # Text areas
        main_frame = tk.Frame(root)
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # set a good default font for Unicode characters
        # doenst work for numbers in Celestial, but works for Kyrsan (exepct for nr. 2)
        unicode_font = ("Segoe UI Symbol", 16)

        self.input_text = scrolledtext.ScrolledText(main_frame, height=8, font=unicode_font)
        self.input_text.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.input_text.insert("1.0", "Write text") # Placeholder text

        self.output_text = scrolledtext.ScrolledText(main_frame, height=8, font=unicode_font, state="disabled")
        self.output_text.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        self.output_text.configure(bg="#fafbfc") # Set a light background color for output

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # Bind events
        self.input_text.bind("<KeyRelease>", self.on_translate)
    
    # Swap the selected languages in the comboboxes
    def swap_languages(self):
        left = self.left_lang.get()
        right = self.right_lang.get()
        self.left_lang.set(right)
        self.right_lang.set(left)
        self.on_translate()

    # Translate the input text based on selected languages
    def on_translate(self, event=None):
        src = self.left_lang.get()
        tgt = self.right_lang.get()
        text = self.input_text.get("1.0", "end-1c")

        # If both are English, just copy
        if src == tgt:
            result = text
        elif src == "English":
            # English to constructed language
            json_path = dict(LANGUAGES).get(tgt)
            if json_path:
                alphabet_large, alphabet_small, _, _, numerals_map, _ = load_alphabet(json_path)
                result = translate(text, alphabet_large, alphabet_small, numerals_map)
            else:
                result = text
        elif tgt == "English":
            # Constructed language to English
            json_path = dict(LANGUAGES).get(src)
            if json_path:
                _, _, reverse_large, reverse_small, _, reverse_numerals_map = load_alphabet(json_path)
                result = reverse_translate(text, reverse_large, reverse_small, reverse_numerals_map)
            else:
                result = text
        else:
            # Between two constructed languages: English as bridge
            json_path_src = dict(LANGUAGES).get(src)
            json_path_tgt = dict(LANGUAGES).get(tgt)
            _, _, reverse_large, reverse_small, _, reverse_numerals_map = load_alphabet(json_path_src)
            intermediate = reverse_translate(text, reverse_large, reverse_small, reverse_numerals_map)
            alphabet_large, alphabet_small, _, _, numerals_map, _ = load_alphabet(json_path_tgt)
            result = translate(intermediate, alphabet_large, alphabet_small, numerals_map)

        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)
        self.output_text.configure(state="disabled")
