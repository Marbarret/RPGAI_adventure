import tkinter as tk
import customtkinter
from chat_user import ChatApp

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("RPG AI Adventure")
        self.geometry(f"{1000}x700")

        self.current_frame = None
        self.show_initial_screen()  

    def show_initial_screen(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = customtkinter.CTkFrame(self)
        self.current_frame.pack(fill="both", expand=True)

        self.title_label = customtkinter.CTkLabel(self.current_frame, text="Bem-vindo ao RPG AI Adventure!", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=40)

        self.create_char_button = customtkinter.CTkButton(self.current_frame, text="Criar Personagem", command=self.create_character_screen)
        self.create_char_button.pack(pady=20)

        self.start_game_button = customtkinter.CTkButton(self.current_frame, text="Iniciar Partida", command=self.show_chat_screen)
        self.start_game_button.pack(pady=20)

        self.history_button = customtkinter.CTkButton(self.current_frame, text="Histórico de Partidas", command=self.show_history)
        self.history_button.pack(pady=20)

    def show_chat_screen(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = ChatApp(self)
        self.current_frame.pack(fill="both", expand=True)

    def create_character_screen(self):
        pass

    def show_history(self):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()