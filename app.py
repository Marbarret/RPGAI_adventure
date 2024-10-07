import tkinter as tk
import numpy as np
from transformers import pipeline

chatbot = pipeline('text-generation', model='gpt2')

def gerar_resposta(pergunta):
    resposta = chatbot(pergunta, max_length=100, num_return_sequences=1)
    return resposta[0]['generated_text']

def enviar_mensagem():
    mensagem = entrada_usuario.get()
    if mensagem.strip(): 
        caixa_chat.insert(tk.END, f"Jogador: {mensagem}\n")
        resposta = gerar_resposta(mensagem)
        caixa_chat.insert(tk.END, f"NPC: {resposta}\n")
        entrada_usuario.delete(0, tk.END)
    else:
        caixa_chat.insert(tk.END, "Você precisa escrever algo!\n")

janela = tk.Tk()
janela.title("RPG Chatbot")

caixa_chat = tk.Text(janela, height=20, width=50)
caixa_chat.pack()

entrada_usuario = tk.Entry(janela, width=50)
entrada_usuario.pack()

botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem)
botao_enviar.pack()

janela.mainloop()