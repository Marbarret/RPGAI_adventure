import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk
import random

class ChatLogic:
    def __init__(self):
        self.layout = None  # Referência ao layout

    def set_layout(self, layout):
        self.layout = layout

    def send_message(self):
        message = self.layout.entry.get()
        if message.strip() != "":
            self.layout.chatbox.insert(tkinter.END, f"Você: {message}\n")  
            self.layout.entry.delete(0, tkinter.END)

    def send_message_event(self, event):
        self.send_message()

    def roll_dice(self):
        # Get the selected dice type from the combobox
        selected_dice = self.dice_combobox.get()

        # Validate the selection (optional)
        if not selected_dice:
            self.add_message("Erro", "Selecione um dado para rolar!", "system")
            return

        # Roll the dice and get the result
        try:
            num_sides = int(selected_dice[1:])  # Extract number of sides from "D#"
            rolled_value = random.randint(1, num_sides)
            self.rolled_value = rolled_value  # Store the rolled value
        except ValueError:
            self.add_message("Erro", "Selecione um dado válido (D4, D6, etc.)", "system")
            return

        # Display the rolled value
        self.add_message("Sistema", f"Você rolou o dado {selected_dice} e obteve {rolled_value}", "system")

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((150, 150))
            photo = ImageTk.PhotoImage(image)
            self.layout.profile_image_label.configure(image=photo, text="")
            self.layout.profile_image_label.image = photo

    def get_ai_response(self, user_message):
        # Lógica para gerar resposta com a IA
        inputs = self.model.encode(user_message, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=50)
        return self.model.decode(outputs[0], skip_special_tokens=True)