from datasets import load_dataset
from transformers import GPT2Tokenizer

def load_and_tokenize_data(dataset_path):
    # Carregar o dataset
    dataset = load_dataset('json', data_files=dataset_path)

    # Carregar o tokenizer GPT-2
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # Função de tokenização
    def tokenize_function(examples):
        return tokenizer(examples['Text'], truncation=True)

    # Tokenizar o dataset
    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    return tokenized_dataset

if __name__ == "__main__":
    dataset_path = "data/rpg_ai/rpg_dataset.json"  # Caminho relativo ao arquivo do dataset
    tokenized_dataset = load_and_tokenize_data(dataset_path)
    print("Tokenização concluída!")
