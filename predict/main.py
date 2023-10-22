import pandas
import numpy as np
from tkinter import *
from tkinter import ttk, filedialog, messagebox

#----------------------------Tkinker init work----------------------------#
## window/ interface
window = Tk()
width_gemetry = 2200
window.geometry(f"{width_gemetry}x550")
window.pack_propagate(True)
title = window.title("House to You")

tip_label = Label(text="Clique no botão para ver os clientes selecionados pelos sistema ")
tip_label.grid(column=1, row=0, columnspan=3, padx=200, pady=50)

canvas = Canvas(width=300, height=300, highlightthickness=0)
frame = Frame(canvas)
frame.grid(column=1, columnspan=2, row=1, padx=50)

#----------------------------Data work----------------------------#
def import_data():
    """import data"""
    origin_data = pandas.read_csv("german_credit_data.csv", index_col=0)
    data = origin_data[origin_data["Housing"] == "rent"]
    customers = pandas.DataFrame(data=data)
    customers = customers.to_csv("Potential_customers.csv", index=False)
    return customers


def add_columns():
    """ initial transform data"""
    mail = pandas.read_csv("Potential_customers.csv")
    mail["email"] = "customers@mail.com"
    mail.to_csv("Potential_customers.csv", index=False)
    status_of = pandas.read_csv("Potential_customers.csv")
    status_of["Status"] = "waiting"
    full_csv = status_of.to_csv("Potential_customers.csv", index=False)
    return full_csv

def converter():
    df_new = pandas.read_csv('Potential_customers.csv')
    writer = pandas.ExcelWriter('Potential_customers.xlsx')
    df_new.to_excel(writer, index=False)
    writer.close()

def file_open():
    """open the xlsx file"""
    converter()
    global width_gemetry
    file = "Potential_customers.xlsx"
    my_tree = ttk.Treeview(window)
    my_tree.grid(column=1, columnspan=3, row=1, pady=20)
    try:
        df = pandas.read_excel(file)
    except Exception as e:
        messagebox.showerror("Oou", f"Something didn't work!\n{e}")
#tree
    my_tree.delete(*my_tree.get_children())
    my_tree['column'] = list(df.columns)
    my_tree['show'] = 'headings'
    for col in my_tree['column']:
        my_tree.heading(col, text=col)
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)





view_button = Button(window, text="Ver clientes", bg="green", command=file_open)
view_button.grid(column=1, row=2, padx=300)

import_data()
add_columns()
window.mainloop()
