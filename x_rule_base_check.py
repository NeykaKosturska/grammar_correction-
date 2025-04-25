from autocorrect import Speller
import nltk

nltk.download('punkt')
from nltk.tokenize import word_tokenize

spell = Speller(lang='en')

def correct_grammar(sentence: str) -> str:
    words = word_tokenize(sentence)
    corrected_words = [spell(word) for word in words]
    corrected_sentence = " ".join(corrected_words)
    return corrected_sentence.capitalize()

def main():
    input_sentence = input("Enter a sentence: ")
    corrected_sentence = correct_grammar(input_sentence)
    print(f"Corrected sentence: {corrected_sentence}")

if __name__ == "__main__":
    main()