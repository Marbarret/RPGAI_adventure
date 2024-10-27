import customtkinter
from chat_user import ChatLayout
from chat_logic import ChatLogic

if __name__ == "__main__":
    root = customtkinter.CTk()
    logic = ChatLogic()
    chat_layout = ChatLayout(root, logic, model, tokenizer)
    logic.set_layout(layout)
    layout.pack(fill="both", expand=True)
    root.mainloop()
