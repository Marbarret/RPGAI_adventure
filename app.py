import random
from flask import Flask, render_template, request
from transformers import GPTNeoForCausalLM, GPT2Tokenizer

app = Flask(__name__)

# Carregando o modelo GPT-2 e o tokenizer
model_name = "EleutherAI/gpt-neo-2.7B"
model = GPTNeoForCausalLM.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Dados do jogo
player_hp = 100
enemy_hp = 50

def generate_narrative(user_input, player_roll, enemy_roll):
    """Gera uma narrativa usando o modelo GPT-2 com um prompt mais detalhado"""
    prompt = f"""Você está jogando um RPG de fantasia. O jogador decide {user_input}. 
    O jogador rola um {player_roll}, e o inimigo rola {enemy_roll}.
    Descreva o que acontece em uma narrativa de RPG de forma detalhada e interessante, levando em conta o que o jogador quer fazer e o que acontece com base nos números rolados.
    """

    # Codifica a entrada do usuário e gera o texto com o modelo GPT-2
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, do_sample=True, top_p=0.95, temperature=0.7)
    
    # Decodifica o texto gerado
    narrative = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return narrative

@app.route('/')
def index():
    return render_template('index.html', player_hp=player_hp, enemy_hp=enemy_hp)

@app.route('/roll', methods=['POST'])
def roll_dice():
    global player_hp, enemy_hp

    # Ação do jogador
    user_action = request.form['action']

    # Tipo de dado selecionado
    dice_type = int(request.form['dice'])
    
    # Rolar o dado
    player_roll = random.randint(1, dice_type)
    enemy_roll = random.randint(1, 6)  # Inimigo sempre usa D6
    
    # Gera a narrativa com a ajuda do GPT-2
    narrative = generate_narrative(user_action, player_roll, enemy_roll)

    # Atualiza a vida de acordo com os resultados
    if player_roll > enemy_roll:
        enemy_hp -= player_roll
        result = f"Você rolou {player_roll} e derrotou o inimigo que rolou {enemy_roll}. Causou {player_roll} de dano!"
    elif player_roll < enemy_roll:
        player_hp -= enemy_roll
        result = f"O inimigo rolou {enemy_roll} e você rolou {player_roll}. Recebeu {enemy_roll} de dano!"
    else:
        result = "Empate! Ninguém sofreu dano."

    # Verifica se o jogo terminou
    if player_hp <= 0:
        result += " Você perdeu! :( "
        player_hp = 100  # Reiniciar o jogo
        enemy_hp = 50
    elif enemy_hp <= 0:
        result += " Você venceu! :) "
        player_hp = 100  # Reiniciar o jogo
        enemy_hp = 50

    return render_template('index.html', player_hp=player_hp, enemy_hp=enemy_hp, result=result, narrative=narrative)

if __name__ == '__main__':
    app.run(debug=True)
