def anti_vowel(text:str)->str:
    result = ""
    for char in text:
        if char.lower() not in "aeiou"