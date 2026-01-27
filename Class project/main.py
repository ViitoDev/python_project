from Counter import counter_words

phrase = input("Enter your phrase: \n")
quantity = counter_words(phrase)
print(f"The phrase has {quantity} words")