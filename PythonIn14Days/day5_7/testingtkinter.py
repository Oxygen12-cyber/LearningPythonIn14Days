import customtkinter as ctk


root = ctk.CTk()
count = 0

def increment():
    global count
    count += 1
    label.configure(text=f"Count: {count}")

label = ctk.CTkLabel(root, text="Count: 0")
button = ctk.CTkButton(root, text="Increment", command=increment)

label.pack(padx = 600, pady = 200)
button.pack(pady = 10)
root.mainloop()