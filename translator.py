# This code is a simple command-line translator between English and Kyrsano Krysan).

# Author: Luka Niemelä

import json
import os
import sys

def resource_path(relative_path):
    # Get absolute path
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def load_alphabet(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    alphabet_large = {item["english"].upper(): item["large"] for item in data["alphabet"]}
    alphabet_small = {item["english"].lower(): item["small"] for item in data["alphabet"]}
    reverse_large = {item["large"]: item["english"].upper() for item in data["alphabet"]}
    reverse_small = {item["small"]: item["english"].lower() for item in data["alphabet"]}
    numerals_map = data.get("numerals", {})
    reverse_numerals_map = {v: k for k, v in numerals_map.items()}
    return alphabet_large, alphabet_small, reverse_large, reverse_small, numerals_map, reverse_numerals_map


def translate(text, alphabet_large, alphabet_small, numerals_map):
    result = ""
    for char in text:
        if char.isdigit() and char in numerals_map:
            result += numerals_map[char]
        elif char.isupper() and char in alphabet_large:
            result += alphabet_large[char]
        elif char.islower() and char in alphabet_small:
            result += alphabet_small[char]
        else:
            result += char
    return result


def reverse_translate(text, reverse_large, reverse_small, reverse_numerals_map):
    result = ""
    for char in text:
        if char in reverse_numerals_map:
            result += reverse_numerals_map[char]
        elif char in reverse_large:
            result += reverse_large[char]
        elif char in reverse_small:
            result += reverse_small[char]
        else:
            result += char
    return result


def main():
    print("DnD Translator")
    print("Choose language:")
    print("1. Kyrsan")
    print("2. Celestial")
    lang_choice = input("Enter number (1 or 2): ").strip()
    if lang_choice == "1":
        json_path = "kyrsan.json"
        lang_name = "Kyrsan"
    elif lang_choice == "2":
        json_path = "celestial.json"
        lang_name = "Celestial"
    else:
        print("Invalid language choice.")
        return

    alphabet_large, alphabet_small, reverse_large, reverse_small, numerals_map, reverse_numerals_map = load_alphabet(json_path)
    print(f"1. English to {lang_name}")
    print(f"2. {lang_name} to English")
    choice = input("Choose translation direction (1 or 2): ").strip()
    if choice == "1":
        user_input = input("Enter text to translate: ")
        translated = translate(user_input, alphabet_large, alphabet_small, numerals_map)
        print("Translated:", translated)
    elif choice == "2":
        user_input = input(f"Enter {lang_name} text to translate: ")
        translated = reverse_translate(user_input, reverse_large, reverse_small, reverse_numerals_map)
        print("Translated:", translated)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()