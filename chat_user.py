import customtkinter
from tkinter import filedialog

class ChatLayout(customtkinter.CTkFrame):
    def __init__(self, master, logic):
        super().__init__(master)
        self.master = master
        self.logic = logic  # Recebe a lógica no construtor
        self.create_chat_ui()

    def create_chat_ui(self):
        # Configuração de layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Frame à esquerda (Informações do usuário)
        self.left_frame = customtkinter.CTkFrame(self, width=250, corner_radius=0)
        self.left_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_frame.grid_rowconfigure(4, weight=1)

        # Label de foto de perfil
        self.profile_image_label = customtkinter.CTkLabel(self.left_frame, text="Foto", width=150, height=150, fg_color="gray")
        self.profile_image_label.grid(row=0, column=0, padx=20, pady=20)

        # Botão para carregar foto
        self.photo_button = customtkinter.CTkButton(self.left_frame, text="Carregar Foto", command=self.logic.upload_photo)
        self.photo_button.grid(row=1, column=0, padx=20, pady=10)

        # Nickname e Status
        self.nickname_label = customtkinter.CTkLabel(self.left_frame, text="Nickname: Rylie", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.nickname_label.grid(row=2, column=0, padx=20, pady=10)
        self.status_label = customtkinter.CTkLabel(self.left_frame, text="Status: Online", width=80)
        self.status_label.grid(row=3, column=0, padx=20, pady=10)

        # Frame de chat
        self.chat_frame = customtkinter.CTkFrame(self)
        self.chat_frame.grid(row=0, column=1, sticky="nsew")
        self.chat_frame.grid_columnconfigure(0, weight=1)
        self.chat_frame.grid_rowconfigure(4, weight=1)

        # Caixa de texto (Chatbox)
        self.chatbox = customtkinter.CTkTextbox(self.chat_frame, height=450, width=1000)
        self.chatbox.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.chatbox.insert("0.0", "Bem vindo ao AI Adventure! Vamos Jogar?\n")

        # Campo de entrada de mensagem
        self.entry_frame = customtkinter.CTkFrame(self.chat_frame)
        self.entry_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.entry_frame.grid_columnconfigure(0, weight=1)
        self.entry_frame.grid_columnconfigure(1, weight=0)
        self.entry = customtkinter.CTkEntry(self.entry_frame, placeholder_text="Digite sua mensagem aqui...", height=100, width=500)
        self.entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Botão de envio
        self.send_button = customtkinter.CTkButton(self.entry_frame, text="Send", command=self.logic.send_message)
        self.send_button.grid(row=0, column=1, padx=5, pady=5)

        # Vincula a tecla Enter ao envio da mensagem
        self.entry.bind("<Return>", self.logic.send_message_event)

        # Frame à direita (Dado)
        self.right_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.right_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.right_frame.grid_rowconfigure(4, weight=1)

        # Seleção de dado
        self.dice_label = customtkinter.CTkLabel(self.right_frame, text="Selecione o dado:")
        self.dice_label.grid(row=0, column=0, padx=20, pady=20)
        self.dice_combobox = customtkinter.CTkComboBox(self.right_frame, values=["D4", "D6", "D8", "D10", "D12", "D20"])
        self.dice_combobox.grid(row=1, column=0, padx=20, pady=10)

        # Botão para rolar o dado
        self.roll_button = customtkinter.CTkButton(self.right_frame, text="Rolar Dado", command=self.logic.roll_dice)
        self.roll_button.grid(row=2, column=0, padx=20, pady=10)
