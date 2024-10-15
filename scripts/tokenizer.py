# tokenizer.py
from transformers import GPT2Tokenizer
from config import PRETRAINED_MODEL_NAME

def get_tokenizer():
    """Função para inicializar o tokenizer GPT-Neo"""
    tokenizer = GPT2Tokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token  # Definir o token de padding como o EOS token
    return tokenizer

if __name__ == "__main__":
    tokenizer = get_tokenizer()
    print("Tokenizer carregado com sucesso.")
