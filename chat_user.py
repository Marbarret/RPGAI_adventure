import customtkinter
import random
from datetime import datetime
import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk

class ChatLayout(customtkinter.CTkFrame):
    def __init__(self, master, logic, model, tokenizer):
        super().__init__(master)
        self.master = master
        self.logic = logic
        self.model = model
        self.tokenizer = tokenizer
        self.create_chat_ui()

    def create_chat_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.left_frame = customtkinter.CTkFrame(self, width=250, corner_radius=0)
        self.left_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_frame.grid_rowconfigure(4, weight=1)

        self.profile_image_label = customtkinter.CTkLabel(self.left_frame, text="Foto", width=150, height=150, fg_color="gray")
        self.profile_image_label.grid(row=0, column=0, padx=20, pady=20)

        self.photo_button = customtkinter.CTkButton(self.left_frame, text="Carregar Foto", command=self.upload_photo)
        self.photo_button.grid(row=1, column=0, padx=20, pady=10)

        self.nickname_label = customtkinter.CTkLabel(self.left_frame, text="Nickname: Rylie", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.nickname_label.grid(row=2, column=0, padx=20, pady=10)
        self.status_label = customtkinter.CTkLabel(self.left_frame, text="Status: Online", width=80)
        self.status_label.grid(row=3, column=0, padx=20, pady=10)

        self.chat_frame = customtkinter.CTkFrame(self)
        self.chat_frame.grid(row=0, column=1, sticky="nsew")
        self.chat_frame.grid_columnconfigure(0, weight=1)
        self.chat_frame.grid_rowconfigure(4, weight=1)

        self.chatbox_frame = customtkinter.CTkScrollableFrame(self.chat_frame, width=1000, height=450)
        self.chatbox_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.entry_frame = customtkinter.CTkFrame(self.chat_frame)
        self.entry_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.entry_frame.grid_columnconfigure(0, weight=1)
        self.entry_frame.grid_columnconfigure(1, weight=0)
        self.entry = customtkinter.CTkEntry(self.entry_frame, placeholder_text="Digite sua mensagem aqui...", height=100, width=500)
        self.entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.send_button = customtkinter.CTkButton(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.grid(row=0, column=1, padx=5, pady=5)

        self.entry.bind("<Return>", self.send_message_event)

        self.right_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.right_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.right_frame.grid_rowconfigure(4, weight=1)

        self.dice_label = customtkinter.CTkLabel(self.right_frame, text="Selecione o dado:")
        self.dice_label.grid(row=0, column=0, padx=20, pady=20)
        self.dice_combobox = customtkinter.CTkComboBox(self.right_frame, values=["D4", "D6", "D8", "D10", "D12", "D20"])
        self.dice_combobox.grid(row=1, column=0, padx=20, pady=10)

        self.roll_button = customtkinter.CTkButton(self.right_frame, text="Rolar Dado", command=self.roll_dice)
        self.roll_button.grid(row=2, column=0, padx=20, pady=10)

        self.chatbox_frame = customtkinter.CTkScrollableFrame(self.chat_frame, height=450, width=1000)
        self.chatbox_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.send_button = customtkinter.CTkButton(self.entry_frame, text="Send", command=self.process_user_message)
        self.send_button.grid(row=0, column=1, padx=5, pady=5)

        self.entry.bind("<Return>", self.send_message_event)

    def roll_dice(self):
        selected_dice = self.dice_combobox.get()

        if not selected_dice:
            self.add_message("Erro", "Selecione um dado para rolar!", "system")
            return

        try:
            num_sides = int(selected_dice[1:])
            rolled_value = random.randint(1, num_sides)
            self.rolled_value = rolled_value
        except ValueError:
            self.add_message("Erro", "Selecione um dado válido (D4, D6, etc.)", "system")
            return

        self.add_message("Sistema", f"Você rolou o dado {selected_dice} e obteve {rolled_value}", "system")

    def send_message(self):
        user_message = self.entry.get()
        if user_message.strip():
            self.add_message("Você", user_message, "user")
            self.entry.delete(0, "end")
            return user_message

    def process_user_message(self):
        user_message = self.send_message()

        if user_message:
            input_ids = self.tokenizer.encode(user_message, return_tensors="pt")
            with torch.no_grad():
                output = self.model.generate(input_ids, max_length=150, num_return_sequences=1)
            ai_response = self.tokenizer.decode(output[0], skip_special_tokens=True)
            self.add_message("AI", ai_response, "ai")

    def send_message_event(self, event):
        self.process_user_message()

    def add_message(self, sender, message, message_type):
        message_frame = customtkinter.CTkFrame(self.chatbox_frame, corner_radius=15)
        message_frame.pack(anchor="e" if message_type == "user" else "w", padx=10, pady=5, fill="x")

        current_time = datetime.now().strftime("%I:%M %p")
        sender_label = customtkinter.CTkLabel(message_frame, text=f"{sender} ({current_time})", font=("Arial", 10, "bold"))
        sender_label.pack(anchor="w", padx=10, pady=5)

        if message_type == "user":
            message_label = customtkinter.CTkLabel(message_frame, text=message, fg_color="#ADD8E6", text_color="black", corner_radius=10, font=("Arial", 12), pady=10, padx=10)
        else:
            message_label = customtkinter.CTkLabel(message_frame, text=message, fg_color="#D3D3D3", text_color="black", corner_radius=10, font=("Arial", 12), pady=10, padx=10)

        message_label.pack(anchor="w" if message_type == "ai" else "e", padx=10, pady=5)

        self.chatbox_frame.update_idletasks()
        self.scroll_to_bottom()

    def scroll_to_bottom(self):
        self.chatbox_frame._parent_canvas.yview_moveto(1.0)

    def upload_photo(self):
        """
        Opens a file dialog and allows the user to select an image file.
        If an image is selected, resizes it, converts it to a PhotoImage,
        and updates the profile image label.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            try:
                image = Image.open(file_path)
                image = image.resize((150, 150))
                photo = ImageTk.PhotoImage(image)
                self.profile_image_label.configure(image=photo, text="")
                self.profile_image_label.image = photo
            except (IOError, OSError) as e:
                print(f"Error opening image: {e}")

    def load_model():
        model = GPT2LMHeadModel.from_pretrained("../models/fine_tuned_gpt2")
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        return model, tokenizer

