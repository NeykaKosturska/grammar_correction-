import language_tool_python

# Load the LanguageTool model for English
tool = language_tool_python.LanguageTool('en-US')

def correct_grammar(sentence: str) -> str:
    """Fix grammar, punctuation, and clarity in a sentence."""
    corrected_sentence = tool.correct(sentence)
    return corrected_sentence.capitalize()

if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    corrected_sentence = correct_grammar(input_sentence)
    print(f"Corrected sentence: {corrected_sentence}")

