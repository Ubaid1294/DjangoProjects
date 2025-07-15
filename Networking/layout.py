from tkinter import *

# Simulated message send
def send(listbox, entry):
    msg = entry.get()
    if msg:
        listbox.insert(END, f"You: {msg}")
        entry.delete(0, END)

# Simulated message receive
def receive(listbox):
    listbox.insert(END, "Friend: Hello!")

# Main window
root = Tk()
root.title("Client Chat")
root.geometry("500x500")
root.configure(bg="#1e1e2f")  # Background color

# Custom fonts & colors
FONT = ("Segoe UI", 11)
ENTRY_BG = "#2e2e3e"
BTN_BG = "#4e8cff"
BTN_FG = "white"
LISTBOX_BG = "#2e2e3e"
LISTBOX_FG = "white"

# Main container frame
main_frame = Frame(root, bg="#1e1e2f", padx=10, pady=10)
main_frame.pack(fill=BOTH, expand=True)

# Chat display area with scrollbar
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
listbox.pack(fill=BOTH, expand=True, side=LEFT)
scrollbar.config(command=listbox.yview)

# Entry and buttons
bottom_frame = Frame(main_frame, bg="#1e1e2f", pady=10)
bottom_frame.pack(fill=X)

entry = Entry(
    bottom_frame,
    font=FONT,
    bg=ENTRY_BG,
    fg="white",
    insertbackground="white",
    relief=FLAT
)
entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10), ipady=6)

send_button = Button(
    bottom_frame,
    text="Send",
    font=FONT,
    bg=BTN_BG,
    fg=BTN_FG,
    activebackground="#3e6fcc",
    activeforeground="white",
    relief=FLAT,
    padx=10,
    pady=5,
    command=lambda: send(listbox, entry)
)
send_button.pack(side=LEFT)

receive_button = Button(
    main_frame,
    text="Receive",
    font=FONT,
    bg="#5c5c6d",
    fg="white",
    activebackground="#6c6c7d",
    relief=FLAT,
    padx=10,
    pady=5,
    command=lambda: receive(listbox)
)
receive_button.pack(pady=(5, 0))

root.mainloop()
