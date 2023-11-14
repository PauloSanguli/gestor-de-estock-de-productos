from tkinter.filedialog import askdirectory
from tkinter import *
from tkinter import (ttk,Toplevel)
from tkinter.messagebox import (showinfo)

try:
    from Infra.menu import *
    from Infra.treview import (Treeview_properties,Insert_Treeview)
    from src.Admin.manage import (Alimentos)        
    from src.Admin.manage import (Cozinha)        
    from src.Admin.manage import (Vestuario)        
    from src.Admin.manage import (Ferramentas)   
    from src.Admin.manage import (Carros)   
    from src.Admin.manage import (Mobilia)      
    from src.Admin.manage import (Aparelhos)      
    from src.Admin.manage import (Mota)      
except:
    from .Infra.menu import *
    from .Infra.treview import (Treeview_properties,Insert_Treeview)
    from .src.Admin.manage import (Alimentos)        
    from .src.Admin.manage import (Cozinha)        
    from .src.Admin.manage import (Vestuario)        
    from .src.Admin.manage import (Ferramentas)   
    from .src.Admin.manage import (Carros)    
    from .src.Admin.manage import (Mobilia)      
    from .src.Admin.manage import (Aparelhos)      
    from .src.Admin.manage import (Mota)      





class App(Tk):
    def __init__(self):
        super().__init__()
        self.app = self
        self.colors()
        self.Position_window()
        self.Window_properties()
        self.Load_images()
        self.Create_widgets()
        self.Places_widgets()
        self.Process_bind()
        self.app.mainloop()



    def Categories_list(self):
        catg = ["Alimentos","Cozinha","Ferramentas","Vestuario","Carros","Mobilia","Aparelhos","Mota"]
        return catg



    def Events_list(self):
        evt = [
            lambda: Events.ButtonAlimentos_clicked(self),
            lambda: Events.ButtonCozinha_clicked(self),
            lambda: Events.ButtonFerramentas_clicked(self),
            lambda: Events.ButtonVestuario_clicked(self),
            lambda: Events.ButtonCarros_clicked(self),
            lambda: Events.ButtonMobilia_clicked(self),
            lambda: Events.ButtonAparelhos_clicked(self),
            lambda: Events.ButtonMota_clicked(self)
        ]
        return evt



    def colors(self):
        self.colorA = "#fff"
        self.colorB = "#000"
        self.colorC = "#418CD6"



    def Position_window(self):
        self.width = 800
        self.height = 650
        self.screen_width = self.app.winfo_screenwidth()
        self.screen_height = self.app.winfo_screenheight()
        self.posX = self.screen_width//2 - self.width//2
        self.posY = self.screen_height//2 - self.height//2



    def Window_properties(self):
        self.app.geometry(f"{self.width}x{self.height}+{self.posX}+{self.posY}")
        self.app.resizable(True,True)
        self.app.configure(bg=self.colorA)
        self.title("Admin database")



    def Create_widgets(self):
        self.Frame_header = Frame(self.app,bg=self.colorC)       
        self.header = Frame(self.Frame_header,bg=self.colorA)
        self.label_Imagedata = Label(self.Frame_header,image=self.ImageData,bg=self.colorC)
        self.Button_Sair = Button(self.Frame_header,text="Sair",fg=self.colorA,bg=self.colorC,bd=0,relief="solid")
        self.button_Novo = Button(self.header,text="Novo",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")
        self.button_Actualizar = Button(self.header,text="Actualizar",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")
        self.button_Carregar = Button(self.header,text="Carregar",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")
        self.button_Apagar = Button(self.header,text="Apagar",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")   


        self.Treeview = Treeview_properties(self.app)
        self.Scroll_Treeview = ttk.Scrollbar(self.app,orient="vertical",command=self.Treeview.yview)
        self.Treeview.configure(yscrollcommand = self.Scroll_Treeview.set)
        self.menuButton = MenuButton(self.header,"Categorias")
        self.menuButton = Add_item(self.menuButton,self.Categories_list(),self.Events_list())
        self.menuButton.configure(bg=self.colorC,fg=self.colorA)  


        #Frame Novo start here
        self.Frame_Novo = Frame(self.app,bg=self.colorA)
        self.label_ImageborderCod = Label(self.Frame_Novo,image=self.ImageBorder,bg=self.colorA)
        self.label_ImageborderName = Label(self.Frame_Novo,image=self.ImageBorder,bg=self.colorA)
        self.label_ImageborderStock = Label(self.Frame_Novo,image=self.ImageBorder,bg=self.colorA)
        self.label_ImageborderDescr = Label(self.Frame_Novo,image=self.ImageBorder,bg=self.colorA)
        self.label_ImageborderPrec = Label(self.Frame_Novo,image=self.ImageBorder,bg=self.colorA)
        self.label_cod = Label(self.Frame_Novo,text="Codigo",bg=self.colorA,fg=self.colorC)
        self.label_name = Label(self.Frame_Novo,text="Nome producto",bg=self.colorA,fg=self.colorC)
        self.label_descr = Label(self.Frame_Novo,text="Descrição",bg=self.colorA,fg=self.colorC)
        self.label_stock = Label(self.Frame_Novo,text="Estoque",bg=self.colorA,fg=self.colorC)
        self.label_prec = Label(self.Frame_Novo,text="Preço",bg=self.colorA,fg=self.colorC)
        self.Entry_cod = Entry(self.Frame_Novo,background=self.colorA,bd=0,relief="flat")
        self.Entry_name = Entry(self.Frame_Novo,background=self.colorA,bd=0,relief="flat")
        self.Entry_descript = Entry(self.Frame_Novo,background=self.colorA,bd=0,relief="flat")
        self.Entry_prec = Entry(self.Frame_Novo,background=self.colorA,bd=0,relief="flat")
        self.Entry_stock = Entry(self.Frame_Novo,background=self.colorA,bd=0,relief="flat")
        self.button_Cancelar = Button(self.Frame_Novo,image=self.ImagebtnCancelar,bg=self.colorA,bd=0)
        self.button_Apagar_entry = Button(self.Frame_Novo,image=self.ImagebtnApagar,bg=self.colorA,bd=0)
        #Categories
        self.button_Alimentos = Button(self.Frame_Novo,text="Alimentos",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")
        self.button_Vestuario = Button(self.Frame_Novo,text="Vestuario",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")
        self.button_Cozinha = Button(self.Frame_Novo,text="Cozinha",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")
        self.button_Ferramentas = Button(self.Frame_Novo,text="Ferramentas",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")
        self.button_carros = Button(self.Frame_Novo,text="Carros",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")    
        self.button_mobilia = Button(self.Frame_Novo,text="Mobilia",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")    
        self.button_aparelhos = Button(self.Frame_Novo,text="Aparelhos",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")      
        self.button_mota = Button(self.Frame_Novo,text="Mota",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")      


        #Frame Actualizar start here
        self.Frame_Actualizar = Frame(self.app,bg=self.colorA)
        self.label_ImageborderCod2 = Label(self.Frame_Actualizar,image=self.ImageBorder,bg=self.colorA)
        self.label_ImageborderStock2 = Label(self.Frame_Actualizar,image=self.ImageBorder,bg=self.colorA)
        self.label_cod2 = Label(self.Frame_Actualizar,text="Codigo",bg=self.colorA,fg=self.colorC,font=("10"))
        self.label_stock2 = Label(self.Frame_Actualizar,text="Estoque",bg=self.colorA,fg=self.colorC,font=("10"))
        self.Entry_cod2 = Entry(self.Frame_Actualizar,highlightbackground=self.colorA,highlightthickness=0,bd=0)
        self.Entry_stock2 = Entry(self.Frame_Actualizar,highlightbackground=self.colorA,highlightthickness=0,bd=0)
        self.button_Cancelar2 = Button(self.Frame_Actualizar,image=self.ImagebtnCancelar,bg=self.colorA,bd=0)
        self.button_Apagar_entry2 = Button(self.Frame_Actualizar,image=self.ImagebtnApagar,bg=self.colorA,bd=0)
        #Categories
        self.button_Vestuario2 = Button(self.Frame_Actualizar,text="Vestuario",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")
        self.button_Alimentos2 = Button(self.Frame_Actualizar,text="Alimentos",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")
        self.button_Cozinha2 = Button(self.Frame_Actualizar,text="Cozinha",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")
        self.button_Ferramentas2 = Button(self.Frame_Actualizar,text="Ferramentas",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")
        self.button_carros2 = Button(self.Frame_Actualizar,text="Carros",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")        
        self.button_mobilia2 = Button(self.Frame_Actualizar,text="Mobilia",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")            
        self.button_aparelhos2 = Button(self.Frame_Actualizar,text="Aparelhos",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")     
        self.button_mota2 = Button(self.Frame_Actualizar,text="Mota",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")     


        #Frame Apagar start here
        self.Frame_Apagar = Frame(self.app,bg=self.colorA)
        self.label_ImageborderCod3 = Label(self.Frame_Apagar,image=self.ImageBorder,bg=self.colorA)
        self.label_cod3 = Label(self.Frame_Apagar,text="Codigo",bg=self.colorA,fg=self.colorC,font=("10"))
        self.label_info3 = Label(self.Frame_Apagar,text="Insira o codigo do producto que deseja eliminar",bg=self.colorA,fg=self.colorC)
        self.Entry_cod3 = Entry(self.Frame_Apagar,background=self.colorA,bd=0)
        self.button_Cancelar3 = Button(self.Frame_Apagar,image=self.ImagebtnCancelar,bg=self.colorA,bd=0)
        self.button_Apagar_entry3 = Button(self.Frame_Apagar,image=self.ImagebtnApagar,bg=self.colorA,bd=0)
        #Categories
        self.button_Alimentos3 = Button(self.Frame_Apagar,text="Alimentos",bg=self.colorC,fg=self.colorA,bd=0)
        self.button_Vestuario3 = Button(self.Frame_Apagar,text="Vestuario",bg=self.colorC,fg=self.colorA,bd=0)
        self.button_Cozinha3 = Button(self.Frame_Apagar,text="Cozinha",bg=self.colorC,fg=self.colorA,bd=0)
        self.button_Ferramentas3 = Button(self.Frame_Apagar,text="Ferramentas",bg=self.colorC,fg=self.colorA,bd=0) 
        self.button_carros3 = Button(self.Frame_Apagar,text="Carros",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")     
        self.button_mobilia3 = Button(self.Frame_Apagar,text="Mobilia",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")               
        self.button_aparelhos3 = Button(self.Frame_Apagar,text="Aparelhos",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")           
        self.button_mota3 = Button(self.Frame_Apagar,text="Mota",bg=self.colorC,fg=self.colorA,bd=0,relief="sunken")           



    def Places_widgets(self):
        self.Frame_header.place(relheight=0.3,relwidth=1.0,relx=0,rely=0)        
        self.header.place(relheight=0.15,relwidth=0.66,rely=0.79,relx=0.19)
        self.label_Imagedata.place(relheight=0.5,relwidth=0.3,relx=0.38,rely=0.05)
        self.Button_Sair.place(relheight=0.24,relwidth=0.1,relx=0.9,rely=0.75)
        self.button_Novo.place(relheight=1.0,relwidth=0.2)
        self.button_Actualizar.place(relheight=1.0,relwidth=0.2,relx=0.2)
        self.button_Carregar.place(relheight=1.0,relwidth=0.2,relx=0.4)
        self.button_Apagar.place(relheight=1.0,relwidth=0.2,relx=0.6)
        self.Treeview.place(relwidth=1.0,rely=0.3,relheight=0.7)        
        self.Scroll_Treeview.place(relheight=0.69,rely=0.304,relx=0.984)
        self.menuButton.place(relheight=1.0,relwidth=0.2,relx=0.8) 

        #Frame novo places start here
        self.label_ImageborderCod.place(relx=0.2,rely=0.12)
        self.label_ImageborderName.place(relx=0.2,rely=0.3)
        self.label_ImageborderStock.place(relx=0.2,rely=0.5)
        self.label_ImageborderDescr.place(relx=0.2,rely=0.7)
        self.label_ImageborderPrec.place(relx=0.2,rely=0.9)
        self.label_cod.place(relx=0.06,rely=0.14)
        self.label_name.place(relx=0.06,rely=0.32)
        self.label_stock.place(relx=0.06,rely=0.52)
        self.label_descr.place(relx=0.06,rely=0.72)
        self.label_prec.place(relx=0.06,rely=0.92)
        self.Entry_cod.place(relheight=0.05,relwidth=0.25,relx=0.22,rely=0.14)
        self.Entry_name.place(relheight=0.05,relwidth=0.25,relx=0.22,rely=0.32)
        self.Entry_stock.place(relheight=0.05,relwidth=0.25,relx=0.22,rely=0.52)
        self.Entry_descript.place(relheight=0.05,relwidth=0.25,relx=0.22,rely=0.72)
        self.Entry_prec.place(relheight=0.05,relwidth=0.25,relx=0.22,rely=0.92)
        self.button_Apagar_entry.place(relx=0.55,rely=0.12)
        self.button_Cancelar.place(relx=0.55,rely=0.3)
        #Categories
        self.button_Alimentos.place(relwidth=0.12,relx=0,rely=0)
        self.button_Cozinha.place(relwidth=0.12,relx=0.13,rely=0.0)
        self.button_Vestuario.place(relwidth=0.12,relx=0.26,rely=0)
        self.button_Ferramentas.place(relwidth=0.12,relx=0.39,rely=0)
        self.button_carros.place(relwidth=0.12,relx=0.52,rely=0)
        self.button_mobilia.place(relwidth=0.12,relx=0.65,rely=0)
        self.button_aparelhos.place(relwidth=0.12,relx=0.78,rely=0)
        self.button_mota.place(relwidth=0.12,relx=0.91,rely=0)

        #Frame Actualizar
        self.label_ImageborderCod2.place(relx=0.35,rely=0.3)
        self.label_ImageborderStock2.place(relx=0.35,rely=0.5)
        self.label_cod2.place(rely=0.315,relx=0.25)
        self.label_stock2.place(rely=0.515,relx=0.25)
        self.Entry_cod2.place(relheight=0.05,relwidth=0.26,relx=0.361,rely=0.32)
        self.Entry_stock2.place(relheight=0.05,relwidth=0.26,relx=0.361,rely=0.52)
        self.button_Apagar_entry2.place(relx=0.65,rely=0.3)
        self.button_Cancelar2.place(relx=0.65,rely=0.5)
        #Categories
        self.button_Alimentos2.place(relwidth=0.12,relx=0,rely=0)
        self.button_Cozinha2.place(relwidth=0.12,relx=0.13,rely=0.0)
        self.button_Vestuario2.place(relwidth=0.12,relx=0.26,rely=0)
        self.button_Ferramentas2.place(relwidth=0.12,relx=0.39,rely=0)
        self.button_carros2.place(relwidth=0.12,relx=0.52,rely=0)
        self.button_mobilia2.place(relwidth=0.12,relx=0.65,rely=0)
        self.button_aparelhos2.place(relwidth=0.12,relx=0.78,rely=0)
        self.button_mota2.place(relwidth=0.12,relx=0.91,rely=0)

        #Frame Apagar
        self.label_ImageborderCod3.place(relx=0.26,rely=0.4)
        self.label_cod3.place(relx=0.17,rely=0.41)
        self.label_info3.place(relheight=0.14,relwidth=0.5,relx=0.27,rely=0.14)
        self.Entry_cod3.place(relheight=0.05,relwidth=0.26,relx=0.271,rely=0.42)
        self.button_Apagar_entry3.place(relx=0.56,rely=0.4)
        self.button_Cancelar3.place(relx=0.71,rely=0.4)
        #Categories
        self.button_Alimentos3.place(relwidth=0.12,relx=0,rely=0)
        self.button_Cozinha3.place(relwidth=0.12,relx=0.13,rely=0.0)
        self.button_Vestuario3.place(relwidth=0.12,relx=0.26,rely=0)
        self.button_Ferramentas3.place(relwidth=0.12,relx=0.39,rely=0)
        self.button_carros3.place(relwidth=0.12,relx=0.52,rely=0)
        self.button_mobilia3.place(relwidth=0.12,relx=0.65,rely=0)
        self.button_aparelhos3.place(relwidth=0.12,relx=0.78,rely=0)
        self.button_mota3.place(relwidth=0.12,relx=0.91,rely=0)
        


    def Load_images(self):
        try:
            self.ImageData = PhotoImage(file=r"Infra/ilustrations/Grupo 2.png")
            self.ImageBorder = PhotoImage(file=r"Infra/ilustrations/Retângulo 1.png")
            self.ImagebtnApagar = PhotoImage(file=r"Infra/ilustrations/btn_apagar.png")
            self.ImagebtnCancelar = PhotoImage(file=r"Infra/ilustrations/btn_cancelar.png")
        except:    
            self.dir = askdirectory()
            self.imgData = f"{self.dir}/{'Grupo 2.png'}"
            self.imgBorder = f"{self.dir}/{'Retângulo 1.png'}"
            self.imgBtnApagar = f"{self.dir}/{'btn_apagar.png'}"
            self.imgBtnCancelar = f"{self.dir}/{'btn_cancelar.png'}"
            self.ImageData = PhotoImage(file=f"{self.imgData}")
            self.ImageBorder = PhotoImage(file=f"{self.imgBorder}")
            self.ImagebtnApagar = PhotoImage(file=f"{self.imgBtnApagar}")
            self.ImagebtnCancelar = PhotoImage(file=f"{self.imgBtnCancelar}")



    def Process_bind(self):
        self.button_Novo.bind("<1>",lambda e: Events.ButtonNovo_clicked(self))
        self.Button_Sair.bind("<1>",lambda e: Events.ButtonSair_clicked(self))
        self.button_Actualizar.bind("<1>",lambda e: Events.ButtonActualizar_clicked(self))
        self.button_Carregar.bind("<1>",lambda e: Events.ButtonAlimentos_clicked(self))
        self.button_Apagar.bind("<1>",lambda e: Events.ButtonApagardb_clicked(self))

        self.button_Cancelar.bind("<1>",lambda e: Events.ButtonCancelar_clicked(self))
        self.button_Cancelar2.bind("<1>",lambda e: Events.ButtonCancelar_clicked(self))
        self.button_Cancelar3.bind("<1>",lambda e: Events.ButtonCancelar_clicked(self))
        
        self.button_Apagar_entry.bind("<1>",lambda e: Events.ButtonApagar_clicked(self))
        self.button_Apagar_entry2.bind("<1>",lambda e: Events.ButtonApagar_clicked(self))
        self.button_Apagar_entry3.bind("<1>",lambda e: Events.ButtonApagar_clicked(self))

        self.button_Alimentos.bind("<1>",lambda e: Alimentos.Insert_db(self.Entry_cod.get(),self.Entry_name.get(),self.Entry_descript.get(),self.Entry_stock.get(),self.Entry_prec.get()))
        self.button_Alimentos2.bind("<1>",lambda e: Alimentos.Update_db(self.Entry_cod2.get(),self.Entry_stock2.get()),)
        self.button_Alimentos3.bind("<1>",lambda e: Alimentos.Delete_db(self.Entry_cod3.get()))

        self.button_Vestuario.bind("<1>",lambda e: Vestuario.Insert_db(self.Entry_cod.get(),self.Entry_name.get(),self.Entry_descript.get(),self.Entry_stock.get(),self.Entry_prec.get()))
        self.button_Vestuario2.bind("<1>",lambda e: Vestuario.Update_db(self.Entry_cod2.get(),self.Entry_stock2.get()),)
        self.button_Vestuario3.bind("<1>",lambda e: Vestuario.Delete_db(self.Entry_cod3.get()))

        self.button_Ferramentas.bind("<1>",lambda e: Ferramentas.Insert_db(self.Entry_cod.get(),self.Entry_name.get(),self.Entry_descript.get(),self.Entry_stock.get(),self.Entry_prec.get()))
        self.button_Ferramentas2.bind("<1>",lambda e: Ferramentas.Update_db(self.Entry_cod2.get(),self.Entry_stock2.get()),)
        self.button_Ferramentas3.bind("<1>",lambda e: Ferramentas.Delete_db(self.Entry_cod3.get()))

        self.button_carros.bind("<1>",lambda e: Carros.Insert_db(self.Entry_cod.get(),self.Entry_name.get(),self.Entry_descript.get(),self.Entry_stock.get(),self.Entry_prec.get()))
        self.button_carros2.bind("<1>",lambda e: Carros.Update_db(self.Entry_cod2.get(),self.Entry_stock2.get()),)
        self.button_carros3.bind("<1>",lambda e: Carros.Delete_db(self.Entry_cod3.get()))

        self.button_Cozinha.bind("<1>",lambda e: Cozinha.Insert_db(self.Entry_cod.get(),self.Entry_name.get(),self.Entry_descript.get(),self.Entry_stock.get(),self.Entry_prec.get()))
        self.button_Cozinha2.bind("<1>",lambda e: Cozinha.Update_db(self.Entry_cod2.get(),self.Entry_stock2.get()),)
        self.button_Cozinha3.bind("<1>",lambda e: Cozinha.Delete_db(self.Entry_cod3.get()))

        self.button_aparelhos.bind("<1>",lambda e: Aparelhos.Insert_db(self.Entry_cod.get(),self.Entry_name.get(),self.Entry_descript.get(),self.Entry_stock.get(),self.Entry_prec.get()))
        self.button_aparelhos2.bind("<1>",lambda e: Aparelhos.Update_db(self.Entry_cod2.get(),self.Entry_stock2.get()),)
        self.button_aparelhos3.bind("<1>",lambda e: Aparelhos.Delete_db(self.Entry_cod3.get()))

        self.button_mobilia.bind("<1>",lambda e: Mobilia.Insert_db(self.Entry_cod.get(),self.Entry_name.get(),self.Entry_descript.get(),self.Entry_stock.get(),self.Entry_prec.get()))
        self.button_mobilia2.bind("<1>",lambda e: Mobilia.Update_db(self.Entry_cod2.get(),self.Entry_stock2.get()),)
        self.button_mobilia3.bind("<1>",lambda e: Mobilia.Delete_db(self.Entry_cod3.get()))

        self.button_mota.bind("<1>",lambda e: Mota.Insert_db(self.Entry_cod.get(),self.Entry_name.get(),self.Entry_descript.get(),self.Entry_stock.get(),self.Entry_prec.get()))
        self.button_mota2.bind("<1>",lambda e: Mota.Update_db(self.Entry_cod2.get(),self.Entry_stock2.get()),)
        self.button_mota3.bind("<1>",lambda e: Mota.Delete_db(self.Entry_cod3.get()))



class Events(App):
    def __init__(self):
        super().__init__()


    def ButtonAlimentos_clicked(self):
        print("Botão Alimentos clicado")        
        self.Treeview.destroy()
        self.Treeview = Insert_Treeview(Treeview_properties(self.app),Alimentos.Select_db())
        self.Scroll_Treeview = ttk.Scrollbar(self.app,orient="vertical",command=self.Treeview.yview)
        self.Places_widgets()        
        

    def ButtonCozinha_clicked(self):
        print("Botão Cozinha clicado") 
        self.Treeview.destroy()
        self.Treeview = Insert_Treeview(Treeview_properties(self.app),Cozinha.Select_db())
        self.Scroll_Treeview = ttk.Scrollbar(self.app,orient="vertical",command=self.Treeview.yview)
        self.Places_widgets()


    def ButtonVestuario_clicked(self):
        print("Botão Vestuario clicado")       
        self.Treeview.destroy()
        self.Treeview = Insert_Treeview(Treeview_properties(self.app),Vestuario.Select_db())
        self.Scroll_Treeview = ttk.Scrollbar(self.app,orient="vertical",command=self.Treeview.yview)
        self.Places_widgets()


    def ButtonFerramentas_clicked(self):
        print("Botão Ferramentas clicado")        
        self.Treeview.destroy()
        self.Treeview = Insert_Treeview(Treeview_properties(self.app),Ferramentas.Select_db())
        self.Scroll_Treeview = ttk.Scrollbar(self.app,orient="vertical",command=self.Treeview.yview)
        self.Places_widgets()


    def ButtonCarros_clicked(self):
        self.Treeview.destroy()
        self.Treeview = Insert_Treeview(Treeview_properties(self.app),Carros.Select_db())
        self.Scroll_Treeview = ttk.Scrollbar(self.app,orient="vertical",command=self.Treeview.yview)
        self.Places_widgets()


    def ButtonMota_clicked(self):
        self.Treeview.destroy()
        self.Treeview = Insert_Treeview(Treeview_properties(self.app),Mota.Select_db())
        self.Scroll_Treeview = ttk.Scrollbar(self.app,orient="vertical",command=self.Treeview.yview)
        self.Places_widgets()


    def ButtonMobilia_clicked(self):
        self.Treeview.destroy()
        self.Treeview = Insert_Treeview(Treeview_properties(self.app),Mobilia.Select_db())
        self.Scroll_Treeview = ttk.Scrollbar(self.app,orient="vertical",command=self.Treeview.yview)
        self.Places_widgets()    


    def ButtonAparelhos_clicked(self):
        self.Treeview.destroy()
        self.Treeview = Insert_Treeview(Treeview_properties(self.app),Aparelhos.Select_db())
        self.Scroll_Treeview = ttk.Scrollbar(self.app,orient="vertical",command=self.Treeview.yview)
        self.Places_widgets()        


    def ButtonCancelar_clicked(self):
        print("Cancelar")
        self.app.after(1000,Events.ButtonAlimentos_clicked(self))


    def ButtonSair_clicked(self):
        self.app.destroy()     


    def ButtonActualizar_clicked(self):
        print("Actualizar")
        self.Treeview.destroy()
        self.Frame_Novo.place(relheight=0,relwidth=0)
        self.Frame_Apagar.place(relheight=0,relwidth=0)
        self.Frame_Actualizar.place(relheight=0.6,relwidth=1.0,relx=0.0,rely=0.34)   


    def ButtonNovo_clicked(self):
        print("Novo")
        self.Treeview.destroy()
        self.Frame_Apagar.place(relheight=0,relwidth=0)
        self.Frame_Actualizar.place(relheight=0,relwidth=0)
        self.Frame_Novo.place(relheight=0.6,relwidth=1.0,relx=0.0,rely=0.34)


    def ButtonApagardb_clicked(self):
        print("Apagar db")
        self.Treeview.destroy()
        self.Frame_Novo.place(relheight=0,relwidth=0)
        self.Frame_Actualizar.place(relheight=0,relwidth=0)
        self.Frame_Apagar.place(relheight=0.6,relwidth=1.0,relx=0.0,rely=0.34)  


    def ButtonApagar_clicked(self):
        print("Apagar")
        self.Entry_cod.delete(0,END)
        self.Entry_name.delete(0,END)
        self.Entry_descript.delete(0,END)
        self.Entry_prec.delete(0,END)    
        self.Entry_stock.delete(0,END)   
        self.Entry_stock2.delete(0,END)   
        self.Entry_cod2.delete(0,END)   
        self.Entry_cod3.delete(0,END)       

if __name__=='__main__':
    App()