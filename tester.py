from translator import load_alphabet, translate

def test_language(json_path, lang_name):
    alphabet_large, alphabet_small, _, _, numerals_map, _ = load_alphabet(json_path)
    sentences = [
        "A QUICK BROWN FOX JUMPS OVER THE LAZY DOG.",
        "a quick brown fox jumps over the lazy dog."
    ]
    print(f"\n--- {lang_name} ---")
    for s in sentences:
        translated = translate(s, alphabet_large, alphabet_small, numerals_map)
        print(f"Original:   {s}")
        print(f"Translated: {translated}")
    # Print numbers 0-9
    numbers = ''.join(str(i) for i in range(10))
    translated_numbers = translate(numbers, alphabet_large, alphabet_small, numerals_map)
    print(f"Numbers 0-9: {translated_numbers}")

if __name__ == "__main__":
    test_language("kyrsan.json", "Kyrsan")
    test_language("celestial.json", "Celestial")