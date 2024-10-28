import json
from transformers import GPT2LMHeadModel, Trainer, TrainingArguments, AutoTokenizer
from torch.utils.data import Dataset, random_split
from transformers import DataCollatorForLanguageModeling

class RPGDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_length=512):
        with open(file_path, 'r') as f:
            data = json.load(f)

        self.inputs = []
        self.targets = []

        for entry in data["interacoes"]:
            prompt = (
                f"Contexto: {entry['contexto']}\n"
                f"Missão: {entry['missao']}\n"
                f"Condição: {entry['condicao']}\n"
                f"Usuário: {entry['user']}\nResposta:"
            )
            answer = entry["ai"]

            input_ids = tokenizer(prompt, padding="max_length", truncation=True, max_length=max_length, return_tensors="pt").input_ids
            target_ids = tokenizer(answer, padding="max_length", truncation=True, max_length=max_length, return_tensors="pt").input_ids
            self.inputs.append(input_ids)
            self.targets.append(target_ids)

            
    def __len__(self):
        return len(self.inputs)
    
    def __getitem__(self, idx):
        return {'input_ids': self.inputs[idx].squeeze(), 'labels': self.targets[idx].squeeze()}

def load_and_tokenize_data(file_path, tokenizer):
    dataset = RPGDataset(file_path, tokenizer)
    train_size = int(0.5 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
    return {'train': train_dataset, 'validation': val_dataset}

def train_model(tokenized_dataset, model_path="../models/fine_tuned_gpt2"):
    try:
        model = GPT2LMHeadModel.from_pretrained(model_path)
        print("Modelo existente carregado para treinamento incremental.")
    except:
        model = GPT2LMHeadModel.from_pretrained("gpt2")
        print("Modelo base GPT-2 carregado para fine-tuning inicial.")

    training_args = TrainingArguments(
        output_dir=model_path,
        overwrite_output_dir=True,
        num_train_epochs=1,
        per_device_train_batch_size=4,
        save_steps=500,
        save_total_limit=2,
        logging_dir='../logs',
        logging_steps=10,
        evaluation_strategy="epoch"
    )

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset['train'],
        eval_dataset=tokenized_dataset['validation'],
        data_collator=data_collator,
    )

    trainer.train()
    model.save_pretrained(model_path)
    print("Modelo atualizado e salvo com sucesso!")

def load_model(model_path="../models/fine_tuned_gpt2"):
    model = GPT2LMHeadModel.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    return model, tokenizer

if __name__ == "__main__":
    dataset_path = "data/rpg_ai/rpg_dataset.json"
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
    tokenized_dataset = load_and_tokenize_data(dataset_path, tokenizer)
    train_model(tokenized_dataset)
