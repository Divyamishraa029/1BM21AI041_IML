import string
from collections import Counter

def preprocess_text(text):
    # Remove commas and special characters
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def analyze_text(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            # Preprocess the text
            processed_text = preprocess_text(content)

            # Count the number of lines
            num_lines = content.count('\n') + 1

            # Count the number of words
            num_words = len(processed_text.split())

            # Identify the most frequent word
            word_counts = Counter(processed_text.split())
            most_frequent_word = word_counts.most_common(1)[0][0]

            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Most frequent word: {most_frequent_word}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'story.txt'
analyze_text(file_path)
