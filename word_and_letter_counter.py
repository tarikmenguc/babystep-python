# Word Counter Program

def word_and_letter_counter(text):
    # Calculate total word count (separated by spaces)
    words = text.split()
    word_count = len(words)

    # Calculate total number of letters (excluding spaces)
    letter_count = sum(len(word) for word in words)

    # Calculate number of spaces
    space_count = text.count(" ")

    # Find the most frequently occurring word
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    most_common_word = max(word_frequency, key=word_frequency.get)

    # Find the most frequently occurring letter (without counting spaces)
    letter_frequency = {}
    for char in text.replace(" ", ""):
        letter_frequency[char] = letter_frequency.get(char, 0) + 1
    most_common_letter = max(letter_frequency, key=letter_frequency.get)

    # Print results to screen
    print("\n--- Text Analysis ---")
    print(f"Total Words       : {word_count}")
    print(f"Total Letters     : {letter_count}")
    print(f"Total Spaces      : {space_count}")
    print(f"Most Common Word  : '{most_common_word}' ({word_frequency[most_common_word]} times)")
    print(f"Most Common Letter: '{most_common_letter}' ({letter_frequency[most_common_letter]} times)")


# Get text input from user
user_text = input("Enter a text: ")
word_and_letter_counter(user_text)
