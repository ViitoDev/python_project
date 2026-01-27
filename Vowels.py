def find_vowels(text):
    vowels = ("a e i o u")
    quantity = 0
    
    for letter in phrase.lower():
        if letter in vowels:
            quantity += 1
    return quantity

phrase = input("Enter your phrase: \n")
print(f"Your text have {find_vowels(phrase)} vowels.")