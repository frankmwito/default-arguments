# character frequency in a string

def character_freq(word, character='a'):
    frequency = 0
    for ch in word:
        if ch == character:
            frequency += 1
    return frequency

word = input("Enter any word: ")

print("The frequency of the character is:", character_freq(word, character='a'))
