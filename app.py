import os
import random
import threading
from flask import Flask, render_template, request
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch
import subprocess

MODEL_DIR = './models/fine_tuned_gpt_neo'

app = Flask(__name__)

# Função para verificar se o modelo já existe
def check_if_model_exists():
    return os.path.exists(MODEL_DIR) and os.path.isdir(MODEL_DIR)

# Função para treinar o modelo em segundo plano
def train_model():
    print("Treinando o modelo em background...")
    subprocess.call(['python', 'train.py'])

# Verificação do modelo e treinamento em segundo plano
if not check_if_model_exists():
    # Cria uma thread para rodar o treinamento em background
    train_thread = threading.Thread(target=train_model)
    train_thread.start()

# Carregar o modelo e tokenizer depois do treinamento
def load_model_and_tokenizer():
    model = GPTNeoForCausalLM.from_pretrained(MODEL_DIR)
    tokenizer = GPT2Tokenizer.from_pretrained(MODEL_DIR)
    model.eval()
    return model, tokenizer

# Verificar e carregar o modelo, ou aguardar o treinamento
if check_if_model_exists():
    model, tokenizer = load_model_and_tokenizer()
else:
    print("Aguardando o término do treinamento para carregar o modelo...")
    model, tokenizer = None, None

player_hp = 100
enemy_hp = 50

def generate_narrative(user_input, player_roll, enemy_roll):
    prompt = f"""Você está jogando um RPG de fantasia. O jogador decide {user_input}. 
    O jogador rola um {player_roll}, e o inimigo rola {enemy_roll}.
    Descreva o que acontece em uma narrativa de RPG de forma detalhada e interessante, levando em conta o que o jogador quer fazer e o que acontece com base nos números rolados.
    """
    
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    inputs = inputs.to('cuda' if torch.cuda.is_available() else 'cpu')
    
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, do_sample=True, top_p=0.95, 
