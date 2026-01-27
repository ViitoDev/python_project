from Counter import counter_words

phrase = input("Enter your phrase: \n")
if not phrase:
    print("ERROR: No phrases were found")
else:
    result = counter_words(phrase)
    if result:
        print("Words counter: ")
        for word, quantity in result.items():
            print(f"{word} : {quantity}")
    else:
        print("ERROR: No phrases were found")