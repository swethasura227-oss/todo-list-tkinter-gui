from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("400x400")

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        tasks.pop(selected[0])

title = Label(root, text="To-Do List", font=("Arial", 16))
title.pack(pady=10)

entry = Entry(root, width=30)
entry.pack(pady=10)

add_btn = Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

delete_btn = Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

listbox = Listbox(root, width=40, height=10)
listbox.pack(pady=20)

root.mainloop()