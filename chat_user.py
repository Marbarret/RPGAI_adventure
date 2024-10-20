import tkinter
import customtkinter
from tkinter import filedialog
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class ChatApp(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_chat_ui()
   
    def create_chat_ui(self):
        # Configura o layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Informações do usuário - Esquerda
        self.left_frame = customtkinter.CTkFrame(self, width=250, corner_radius=0)
        self.left_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_frame.grid_rowconfigure(4, weight=1)

        # Carregamento da foto de perfil
        self.profile_image_label = customtkinter.CTkLabel(self.left_frame, text="Foto", width=150, height=150, fg_color="gray")
        self.profile_image_label.grid(row=0, column=0, padx=20, pady=20)

        self.photo_button = customtkinter.CTkButton(self.left_frame, text="Carregar Foto", command=self.upload_photo)
        self.photo_button.grid(row=1, column=0, padx=20, pady=10)

        self.nickname_label = customtkinter.CTkLabel(self.left_frame, text="Nickname: Rylie", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.nickname_label.grid(row=2, column=0, padx=20, pady=10)

        self.status_label = customtkinter.CTkLabel(self.left_frame, text="Status: Online", width=80)
        self.status_label.grid(row=3, column=0, padx=20, pady=10)

        # Seção de Chat
        self.chat_frame = customtkinter.CTkFrame(self)
        self.chat_frame.grid(row=0, column=1, sticky="nsew")
        self.chat_frame.grid_columnconfigure(0, weight=1)
        self.chat_frame.grid_rowconfigure(4, weight=1)

        self.chatbox = customtkinter.CTkTextbox(self.chat_frame, height=450, width=1000)
        self.chatbox.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.chatbox.insert("0.0", "Bem vindo ao AI Adventure! Vamos Jogar?\n")

        self.entry_frame = customtkinter.CTkFrame(self.chat_frame)
        self.entry_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.entry_frame.grid_columnconfigure(0, weight=1)
        self.entry_frame.grid_columnconfigure(1, weight=0)
        self.entry = customtkinter.CTkEntry(self.entry_frame, placeholder_text="Digite sua mensagem aqui...", height=100, width=500)
        self.entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.send_button = customtkinter.CTkButton(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.grid(row=0, column=1, padx=5, pady=5)

        self.entry.bind("<Return>", self.send_message_event)
        # Final chat

        self.right_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.right_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.right_frame.grid_rowconfigure(4, weight=1)

        self.dice_label = customtkinter.CTkLabel(self.right_frame, text="Selecione o dado:")
        self.dice_label.grid(row=0, column=0, padx=20, pady=20)

        self.dice_combobox = customtkinter.CTkComboBox(self.right_frame, values=["D4", "D6", "D8", "D10", "D12", "D20"])
        self.dice_combobox.grid(row=1, column=0, padx=20, pady=10)

        self.roll_button = customtkinter.CTkButton(self.right_frame, text="Rolar Dado", command=self.roll_dice)
        self.roll_button.grid(row=2, column=0, padx=20, pady=10)

    def send_message(self):
        message = self.entry.get()
        if message.strip() != "":
            self.chatbox.insert(tkinter.END, f"Você: {message}\n")  
            self.entry.delete(0, tkinter.END)

    def send_message_event(self, event):
        self.send_message()

    def roll_dice(self):
        dice_type = self.dice_combobox.get()
        if dice_type:
            import random
            max_value = int(dice_type[1:])
            roll_result = random.randint(1, max_value)
            self.chatbox.insert(tkinter.END, f"Você rolou um {dice_type}: {roll_result}\n")

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((150, 150))
            photo = ImageTk.PhotoImage(image)
            self.profile_image_label.configure(image=photo, text="")
            self.profile_image_label.image = photo

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = ChatApp(root)
    app.pack(fill="both", expand=True)
    root.mainloop()