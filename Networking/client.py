import socket
from tkinter import *


def send(listbox,entry):
    message = entry.get()
    listbox.insert('end', "Clinet: " + message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))
    receive(listbox)

def receive(listbox):
    message = s.recv(50)
    listbox.insert('end', "Server: " + message.decode("utf-8"))



root = Tk()
root.title("Client Window")
root.geometry("500x500")
root.configure(bg="#1e1e2f")

FONT = ("Courier", 20, "bold")
ENTRY_BG = "#2e2e3e"
BTN_BG = "#4e8cff"
BTN_FG = "white"
LISTBOX_BG = "#2e2e3e"
LISTBOX_FG = "white"

main_frame = Frame(root, bg="#1e1e2f", padx=10, pady=10)
main_frame.pack(fill=BOTH, expand=True)

list_frame = Frame(main_frame, bg="#1e1e2f")
list_frame.pack(fill=BOTH, expand=True)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(
    list_frame,
    yscrollcommand=scrollbar.set,
    font=FONT,
    bg=LISTBOX_BG,
    fg=LISTBOX_FG,
    selectbackground="#4e8cff",
    highlightthickness=0,
    relief=FLAT
)

bottom_frame = Frame(main_frame, bg="#1e1e2f", pady=10)
bottom_frame.pack(fill=X)

entry = Entry(bottom_frame,
    font=FONT,
    bg=ENTRY_BG,
    fg="white",
    insertbackground="white",
    relief=FLAT)
entry.pack(side=BOTTOM)

listbox = Listbox(
    list_frame,
    yscrollcommand=scrollbar.set,
    font=FONT,
    bg=LISTBOX_BG,
    fg=LISTBOX_FG,
    selectbackground="#4e8cff",
    highlightthickness=0,
    relief=FLAT
)
listbox.pack(fill=BOTH, expand=True, side=LEFT)
scrollbar.config(command=listbox.yview)


button = Button(bottom_frame,
                font=FONT,
                bg=BTN_BG,
                fg=BTN_FG,
                activebackground="#3e6fcc",
                activeforeground="white",
                relief=FLAT,
                padx=10,
                pady=5,
                text="Send",
                command=lambda: send(listbox,entry)
                )
button.pack(side=BOTTOM)

rbutton = Button(root,
                 font=FONT,
                 bg="#5c5c6d",
                 fg="white",
                 activebackground="#6c6c7d",
                 relief=FLAT,
                 padx=10,
                 pady=5,
                 text="Receive",
                 command=lambda: receive(listbox)
                 )
rbutton.pack(pady=(5,0))







s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))






# while True:
#     # message = s.recv(50)
#     print("Server Reply: ",message.decode("utf-8"))
#
#     message_to_send = input("Client is typing..... ")
#     # s.send(bytes(message_to_send, "utf-8"))
#






# while True:
#     message = ''
#     while True:
#         msg = s.recv(10)
#         if len(msg) <= 0:
#             break
#         message += msg.decode('utf-8')
#     if len(message) > 0:
#         print(message)

# msg = s.recv(10)
# msg1 = s.recv(10)
# print(msg.decode('utf-8'))
# print(msg1.decode('utf-8'))

root.mainloop()