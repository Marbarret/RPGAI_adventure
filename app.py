import tkinter as tk
import numpy as np
from transformers import pipeline

# Carregar o modelo de linguagem antes de iniciar a interface
chatbot = pipeline('text-generation', model='gpt2')

# Função para gerar respostas
def gerar_resposta(pergunta):
    resposta = chatbot(pergunta, max_length=100, num_return_sequences=1)
    return resposta[0]['generated_text']

# Função que será chamada ao enviar a mensagem
def enviar_mensagem():
    mensagem = entrada_usuario.get()
    if mensagem.strip():  # Verifica se a mensagem não está vazia
        caixa_chat.insert(tk.END, f"Jogador: {mensagem}\n")
        resposta = gerar_resposta(mensagem)
        caixa_chat.insert(tk.END, f"NPC: {resposta}\n")
        entrada_usuario.delete(0, tk.END)  # Limpa o campo de entrada
    else:
        caixa_chat.insert(tk.END, "Você precisa escrever algo!\n")

# Configurar a janela do jogo
janela = tk.Tk()
janela.title("RPG Chatbot")

# Caixa de texto para o chat
caixa_chat = tk.Text(janela, height=20, width=50)
caixa_chat.pack()

# Entrada do jogador
entrada_usuario = tk.Entry(janela, width=50)
entrada_usuario.pack()

# Botão de enviar
botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem)
botao_enviar.pack()

# Loop principal da janela
janela.mainloop()
