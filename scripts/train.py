# train.py
import torch
from transformers import GPTNeoForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset
from tokenizer import get_tokenizer
from config import DATA_DIR, EPOCHS, BATCH_SIZE, LEARNING_RATE, SAVE_MODEL_PATH, PRETRAINED_MODEL_NAME

# Verifica se temos GPU disponível
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Carregar dataset
dataset = load_dataset('Marcylene/rpg_ai')

# Inicializar tokenizer
tokenizer = get_tokenizer()

def tokenize_function(examples):
    """Tokeniza o dataset usando o tokenizer GPT-Neo"""
    return tokenizer(examples['Text'], padding="max_length", truncation=True, max_length=512)

# Tokenizar o dataset
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Preparar colunas para treinamento
tokenized_datasets = tokenized_datasets.remove_columns(['Title', 'Objective', 'Text'])
tokenized_datasets.set_format("torch")

# Dividir dataset
train_dataset = tokenized_datasets['train']
eval_dataset = tokenized_datasets['validation']

# Carregar modelo GPT-Neo
model = GPTNeoForCausalLM.from_pretrained(PRETRAINED_MODEL_NAME)
model.to(device)

# Definir argumentos de treinamento
training_args = TrainingArguments(
    output_dir=SAVE_MODEL_PATH,
    num_train_epochs=EPOCHS,
    per_device_train_batch_size=BATCH_SIZE,
    per_device_eval_batch_size=BATCH_SIZE,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    evaluation_strategy="steps",
    save_steps=500,
    eval_steps=500,
    learning_rate=LEARNING_RATE,
    fp16=torch.cuda.is_available()  # Usar float16 se houver suporte
)

# Inicializar Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset
)

# Iniciar o treinamento
trainer.train()

# Salvar o modelo treinado
trainer.save_model(SAVE_MODEL_PATH)

if __name__ == "__main__":
    print("Treinamento concluído e modelo salvo em", SAVE_MODEL_PATH)
