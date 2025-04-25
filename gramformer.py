import torch
from gramformer import Gramformer
import en_core_web_sm

nlp = en_core_web_sm.load()


# Load Gramformer in inference mode
gf = Gramformer(models=1, use_gpu=torch.cuda.is_available())

def correct_grammar(sentence: str) -> str:
    corrected_sentences = gf.correct(sentence, max_candidates=1)
    return list(corrected_sentences)[0] if corrected_sentences else sentence

if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    corrected_sentence = correct_grammar(input_sentence)
    print(f"Corrected sentence: {corrected_sentence}")
