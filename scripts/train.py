from transformers import GPT2LMHeadModel, Trainer, TrainingArguments
from tokenizer import load_and_tokenize_data

def train_model(tokenized_dataset):
    # Carregar o modelo pré-treinado GPT-2
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Configuração do treinamento
    training_args = TrainingArguments(
        output_dir="../models/fine_tuned_gpt2",
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=500,
        save_total_limit=2,
        logging_dir='../logs',
        logging_steps=10,
    )

    # Configurar o Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset['train'],
    )

    # Treinamento
    trainer.train()

    # Salvar o modelo
    model.save_pretrained("../models/fine_tuned_gpt2")
    print("Modelo salvo com sucesso!")

if __name__ == "__main__":
    dataset_path = "data/rpg_ai/rpg_dataset.json"
    tokenized_dataset = load_and_tokenize_data(dataset_path)
    train_model(tokenized_dataset)
