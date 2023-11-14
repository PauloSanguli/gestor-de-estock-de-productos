from tkinter import (Menubutton,Menu)
from typing import (Any,List)


def MenuButton(app: Any,txt: str):
    menuButton = Menubutton(app,text=f"{txt}")
    menuButton.menu = Menu(menuButton)
    menuButton['menu'] = menuButton.menu

    return menuButton

def Add_item(menuButton: Any,items: List,events: Any):
    for pos in range(0,len(items)):
        menuButton.menu.add_checkbutton(label=f"{items[pos]}",command=events[pos])

    return menuButton    