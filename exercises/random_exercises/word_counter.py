# Exercise: Word Count

# Create a Python program that prompts the user to input a sentence, counts the number of words in the sentence, and displays the word count.

sentence = input("Write a sentence.")

print(f"Number of words: {sentence.count(" ") + 1}")
