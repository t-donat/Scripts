import tkinter as tk
from tkinter import Text, filedialog
import os

root = tk.Tk()
apps = []

if os.path.isfile("save_paths.txt"):
    with open("save_paths.txt", "r") as file:
        allApps = file.read()
        apps = [x for x in allApps.split(",") if x.strip()]


def add_app():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Please select a file",
                                          filetypes=(("Executables", "*.exe"), ("All Files", "*.*")))
    if filename != '':
        apps.append(filename)

    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()


def run_apps():
    for app in apps:
        os.startfile(app)


def clear_all():
    global apps
    apps = []

    for widget in frame.winfo_children():
        widget.destroy()




canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.07)

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=run_apps)
runApps.pack()


openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=add_app)
openFile.pack()

clearAll = tk.Button(root, text="Delete All", padx=10, pady=5, fg="white", bg="#263D42", command=clear_all)

clearAll.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()
print(apps)

with open("save_paths.txt", "w") as file:
    for app in apps:
        file.write(app + ',')
