def count_vowels_consonants(text):
    text = text.lower()
    vowels = "aeiou"
    
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        # Check only for alphabetic characters
        if 'a' <= char <= 'z':
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count

# --- Example Usage ---
phrase = "Programming is Fun"
v, c = count_vowels_consonants(phrase)
print(f"Phrase: '{phrase}'")
print(f"Vowels: {v}, Consonants: {c}") # Vowels: 5 (o, a, i, i, u), Consonants: 11
