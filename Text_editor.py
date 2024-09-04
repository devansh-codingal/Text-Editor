from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Text Editor")
window.geometry('400x500')
window.rowconfigure(1, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
    filepath = askopenfilename(filetypes=[("Text files", "*.txt*"), ("All files", "*.*")])
    if not filepath:
        return
    text_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_edit.insert(END, text)
        input_file.close()
    window.title(f"Text editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text files", "*.txt*"), ("All files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Text editor - {filepath}")

text_edit = Text(window)
fr_btn = Frame(window, relief=RAISED, bd=2)
btn_o = Button(fr_btn, text="Open", command=open_file)
btn_s = Button(fr_btn, text="Save...", command=save_file)

btn_o.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_s.grid(row=1, column=0, sticky="ew", padx=5)

fr_btn.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=0, sticky="nsew")

window.mainloop()