def clean_text(text):
    text = text.lower()
    characteres = str(r",.!'|?;:\[]{}()")
    for char in characteres:
        text = text.replace(char, "")
    return text 

def counter_words(phrase):
    phrase = clean_text(phrase)
    if not phrase.strip():
        return {}
    words = phrase.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count