# This script quickly tests the translation functionality of the translator module

from translator import load_alphabet, translate, reverse_translate

def test_language(json_path, lang_name):
    alphabet_large, alphabet_small, reverse_large, reverse_small, numerals_map, reverse_numerals_map = load_alphabet(json_path)
    sentences = [
        "A QUICK BROWN FOX JUMPS OVER THE LAZY DOG.",
        "a quick brown fox jumps over the lazy dog.",
        "Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz"
    ]
    print(f"\n--- {lang_name} ---")
    for s in sentences:
        translated = translate(s, alphabet_large, alphabet_small, numerals_map)
        reversed_text = reverse_translate(translated, reverse_large, reverse_small, reverse_numerals_map)
        print(f"Original:   {s}")
        print(f"Translated: {translated}")
        print(f"Reversed:   {reversed_text}")
        print(f"Match:      {s == reversed_text}")
    # Print numbers 0-9
    numbers = ''.join(str(i) for i in range(10))
    translated_numbers = translate(numbers, alphabet_large, alphabet_small, numerals_map)
    reversed_numbers = reverse_translate(translated_numbers, reverse_large, reverse_small, reverse_numerals_map)
    print(f"Numbers 0-9: {translated_numbers}")
    print(f"Reversed:    {reversed_numbers}")
    print(f"Match:       {numbers == reversed_numbers}")

if __name__ == "__main__":
    test_language("kyrsan.json", "Kyrsan")
    test_language("celestial.json", "Celestial")