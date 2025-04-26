import tkinter as tk

def key_press(key):
    entry.insert(tk.END, key)

def backspace():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])

def space():
    entry.insert(tk.END, ' ')

def enter():
    print("Entered Text:", entry.get())
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Colorful Virtual Keyboard")
root.configure(bg="#2b2b2b")

entry = tk.Entry(root, width=50, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=12, padx=10, pady=15)

keys = [
    (['1','2','3','4','5','6','7','8','9','0'], '#ff9999'),
    (['Q','W','E','R','T','Y','U','I','O','P'], '#99ccff'),
    (['A','S','D','F','G','H','J','K','L'], '#99ff99'),
    (['Z','X','C','V','B','N','M'], '#ffff99'),
]

for row_idx, (row_keys, color) in enumerate(keys, start=1):
    for col_idx, key in enumerate(row_keys):
        btn = tk.Button(root, text=key, width=6, height=2, bg=color,
                        fg='black', font=('Arial', 12, 'bold'),
                        command=lambda k=key: key_press(k))
        btn.grid(row=row_idx, column=col_idx, padx=2, pady=2)

# Control buttons
tk.Button(root, text='Space', width=20, height=2, bg="#cccccc", font=('Arial', 12), command=space)\
    .grid(row=5, column=0, columnspan=4, padx=2, pady=10)
tk.Button(root, text='Backspace', width=12, height=2, bg="#ffcc99", font=('Arial', 12), command=backspace)\
    .grid(row=5, column=4, columnspan=2, padx=2, pady=10)
tk.Button(root, text='Enter', width=12, height=2, bg="#cc99ff", font=('Arial', 12), command=enter)\
    .grid(row=5, column=6, columnspan=3, padx=2, pady=10)

root.mainloop()