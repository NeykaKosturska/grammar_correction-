from transformers import pipeline

# Initialize a grammar correction pipeline using a pre-trained model
grammar_corrector = pipeline("text2text-generation", model="facebook/bart-large-mnli")


def correct_grammar(sentence: str) -> str:
    # Simple grammar and clarity correction with punctuation handling
    corrected_sentence = grammar_corrector(sentence)[0]['generated_text']

    # Ensure the first letter is capitalized
    corrected_sentence = corrected_sentence.capitalize()

    # Return the corrected sentence
    return corrected_sentence


# Example usage
if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    corrected_sentence = correct_grammar(input_sentence)
    print(f"Corrected sentence: {corrected_sentence}")
