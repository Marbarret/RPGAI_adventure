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
        dice_type = self.layout.dice_combobox.get()
        if dice_type:
            max_value = int(dice_type[1:])
            roll_result = random.randint(1, max_value)
            self.layout.chatbox.insert(tkinter.END, f"Você rolou um {dice_type}: {roll_result}\n")

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((150, 150))
            photo = ImageTk.PhotoImage(image)
            self.layout.profile_image_label.configure(image=photo, text="")
            self.layout.profile_image_label.image = photo
