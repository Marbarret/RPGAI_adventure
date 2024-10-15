# config.py
import os

# Caminhos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'rpg_ai')
MODEL_SAVE_PATH = os.path.join(BASE_DIR, 'models', 'fine_tuned_gpt_neo')

# Nome do modelo pré-treinado
PRETRAINED_MODEL_NAME = 'EleutherAI/gpt-neo-2.7B'

# Hiperparâmetros
EPOCHS = 3
BATCH_SIZE = 4
LEARNING_RATE = 5e-5

# Tokenizer params
MAX_LENGTH = 512

# Caminho para salvar o modelo após o treinamento
SAVE_MODEL_PATH = './models/fine_tuned_gpt_neo'
