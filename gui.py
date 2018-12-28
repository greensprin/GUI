# coding: UTF-8

import os
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog

def clicked_run_button():
    print(v1.get())
    print(entry.get())

def clicked_sel_button(entry):
    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    if (entry.get() != ""):
        iDir = entry.get()
    pull_down_elem = v1.get()
    file_or_dir = ""
    if (pull_down_elem == "Run Sim"): file_or_dir = tkinter.filedialog.askdirectory(initialdir=iDir)
    else:                             file_or_dir = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    entry.delete(0, tk.END)
    entry.insert(tk.END, file_or_dir)

def select_elem(event):
    # ファイル選択、フォルダ選択
    if (v1.get() == "Run Sim"):
        fileSelectButton.state(["!disabled"])
        label_value.set("select output dir")
    elif (v1.get() == "Make Pattern"):
        fileSelectButton.state(["!disabled"])
        label_value.set("select make pattern file")
    else:
        fileSelectButton.state(["disabled"])
        label_value.set("you push run bottun only")
    entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sim GUI")

    # frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # プルダウンメニュー
    v1 = tk.StringVar()
    cb = ttk.Combobox(frame1, textvariable=v1)
    cb.bind("<<ComboboxSelected>>", select_elem)

    cb["values"] = ("Run Sim", "Make Param", "Make Pattern")
    cb.set("Run Sim")
    cb.grid(row=0, column=0)

    # 実行ボタン
    runButton = ttk.Button(frame1, text="Run", command=clicked_run_button)
    runButton.grid(row=0, column=1)

    # save,load button
    saveButton = ttk.Button(frame1, text="save", command=clicked_run_button)
    saveButton.grid(row=2, column=2)

    loadButton = ttk.Button(frame1, text="load", command=clicked_run_button)
    loadButton.grid(row=2, column=3)

    # Label
    label_value = tk.StringVar()
    label_value.set("select output dir")
    Label = tk.Label(frame1, textvariable=label_value)
    Label.grid(row=1, column=0)


    # path入力と選択ボタン
    entry = tk.Entry(frame1)
    entry.grid(row=2, column=0)

    fileSelectButton = ttk.Button(frame1, text="Sel", command=lambda arg1=entry: clicked_sel_button(arg1))
    fileSelectButton.grid(row=2, column=1)

    tk.mainloop()