import customtkinter
from chat_user import ChatLayout
from chat_logic import ChatLogic
from model_loader import load_model

if __name__ == "__main__":
    model, tokenizer = load_model()

    root = customtkinter.CTk()
    logic = ChatLogic()
    chat_layout = ChatLayout(root, logic, model, tokenizer)
    logic.set_layout(chat_layout)
    chat_layout.pack(fill="both", expand=True)
    
    root.mainloop()
