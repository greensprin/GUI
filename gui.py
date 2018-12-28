# coding: UTF-8

import os
import pickle
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog

setting = {"Run Sim":"", "Make Pattern":"", "Make Param":""}

def clicked_run_button():
    print("Run Start")
    print(v1.get())
    print(entry.get())
    print("Run End")

def clicked_save_button():
    print("Save setting file")
    fTyp = [("", "*.pkl")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    save_file = tkinter.filedialog.asksaveasfilename(filetypes=fTyp, initialdir=iDir)
    with open(save_file, mode="wb") as pf:
        pickle.dump(setting, pf)
    print(setting)

def clicked_load_button():
    print("Load setting file")
    fTyp = [("", "*.pkl")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    load_file = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    with open(load_file, mode="rb") as pf:
        setting = pickle.load(pf)
    print(setting)
    entry.delete(0, tk.END)
    entry.insert(tk.END, setting[v1.get()])

def clicked_sel_button(entry):
    fTyp = [("", "*.txt")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    if (entry.get() != ""):
        iDir = entry.get()
    pull_down_elem = v1.get()
    setting[pull_down_elem] = ""
    if (pull_down_elem == "Run Sim"): setting[pull_down_elem] = tkinter.filedialog.askdirectory(initialdir=iDir)
    else:                             setting[pull_down_elem] = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    entry.delete(0, tk.END)
    entry.insert(tk.END, setting[pull_down_elem])

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
    entry.insert(tk.END, setting[v1.get()])

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

    # save button
    saveButton = ttk.Button(frame1, text="save", command=clicked_save_button)
    saveButton.grid(row=2, column=2)

    # load button
    loadButton = ttk.Button(frame1, text="load", command=clicked_load_button)
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