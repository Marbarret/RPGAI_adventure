import json
from transformers import GPT2LMHeadModel, Trainer, TrainingArguments, AutoTokenizer
from torch.utils.data import Dataset, random_split
from transformers import DataCollatorForLanguageModeling, GPT2Tokenizer

class RPGDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_length=512):
        with open(file_path, 'r') as f:
            data = json.load(f)

        self.inputs = []
        self.targets = []

        for entry in data:
            prompt = f"Pergunta: {entry['input']} Resposta:"
            answer = entry['response']
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
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
    return {'train': train_dataset, 'validation': val_dataset}

def train_model(tokenized_dataset):
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    training_args = TrainingArguments(
        output_dir="../models/fine_tuned_gpt2",
        overwrite_output_dir=True,
        num_train_epochs=3,
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
    model.save_pretrained("../models/fine_tuned_gpt2")
    print("Modelo salvo com sucesso!")

def load_model():
    model = GPT2LMHeadModel.from_pretrained("../models/fine_tuned_gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    return model, tokenizer

model, tokenizer = load_model()

if __name__ == "__main__":
    dataset_path = "data/rpg_ai/rpg_dataset.json"
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
    tokenized_dataset = load_and_tokenize_data(dataset_path, tokenizer)
    train_model(tokenized_dataset)
