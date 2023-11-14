from tkinter import (ttk,END)
from typing import (Any,List)


def Treeview_properties(app: Any):
    treeview = ttk.Treeview(app,columns=("col1","col2","col3","col4","col5","col6","col7"))

    treeview.heading("#0",text="")
    treeview.heading("#1",text="Cod")
    treeview.heading("#2",text="Nome")
    treeview.heading("#3",text="Descrição")
    treeview.heading("#4",text="Estoque")
    treeview.heading("#5",text="Preço")
    treeview.heading("#6",text="Data")
    treeview.heading("#7",text="")

    treeview.column("#0",width=0)
    treeview.column("#1",width=95)
    treeview.column("#2",width=95)
    treeview.column("#3",width=95)
    treeview.column("#4",width=95)
    treeview.column("#5",width=95)
    treeview.column("#6",width=95)
    treeview.column("#7",width=0)

    return treeview

def Insert_Treeview(treeview,products: List):#
        for n in products:
            treeview.insert("",END,values=(n[0],n[1],n[2],n[3],n[4],n[5]))    

        return treeview    