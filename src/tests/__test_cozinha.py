try:
    import sqlite3
    from .Utils.clean import (Clear)
    from .Utils.intervalo import (Aguarde)
    from .Utils.get_date import (Datetime)
    from .interface.interface import (Interface)
    from typing import (Type,Any)
except:
    import sqlite3
    from Utils.clean import (Clear)
    from Utils.intervalo import (Aguarde)
    from Utils.get_date import (Datetime)
    from interface.interface import (Interface)
    from typing import (Type,Any)



class db(Interface):
    def __init__(self):
        super().__init__()
        method = self
        self.Conect()
        #self.Create_table()
        #self.Insert(8,"Cimento","Unidade",16600,50.00)
        #self.Delete(12)
        #self.test_show()

    def _return_self(self):
        return self

 
    def Conect(self):        
        Clear()
        try:
            print("Conectando...")
            database = sqlite3.connect(r"database/cozinha.db")
        except:
            Aguarde()
            print("Erro ao conectar ao banco!")
        else:
            Aguarde()
            print("Conectado ao banco!")
            return database
        finally:
            Aguarde()
            Clear()


    def Create_table(self):
        Clear()
        try:
            self.Conect()
            print("Criando tabela...")
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Cozinha(
                Acesso INTEGER PRIMARY KEY NOT NULL,
                Nome TEXT NOT NULL,
                Descricao TEXT NOT NULL,
                Estoque INTEGER NOT NULL,
                Preco FLOAT NOT NULL,
                Data_add TEXT NOT NULL
            )''')           
        except:
            Aguarde()
            print("Tabela não criada!")
        else:
            Aguarde()
            print("Tabela criada!")
            self.db.commit()
            self.Desconect()
        finally:
            Aguarde()
            Clear()


    def Desconect(self):
        Clear()
        try:
            print("Desconectando...")      
            self.db.close()
        except:
            Aguarde()      
            print("Falha ao fechar o banco!")
        else:
            Aguarde()      
            print("Desconectado do banco!")
        finally:
            Aguarde()
            Clear()


    def Insert(self, acesso: int, nome: str, descript: str, stock: int, buy: float,data: str = Datetime()):
        Clear()
        try:
            self.Conect()
            print("Adicionando productos...")
            self.cursor.execute('''INSERT INTO Cozinha (Acesso,Nome,Descricao,Estoque,Preco,Data_add) VALUES(?,?,?,?,?,?)''',(acesso,nome,descript,stock,buy,data))
            self.db.commit()
        except:
            Aguarde()
            print("Erro ao adicionar os valores!")    
        else:
            Aguarde()
            print("Producto adicionado com sucesso!")    
            Aguarde()
            self.Desconect()
        finally:
            Clear()         


    def Delete(self,acess: int):
        Clear()
        try:
            self.Conect()
            print("Apagando productos...")
            self.cursor.execute(f'''DELETE FROM Cozinha WHERE Acesso = {acess}''')            
        except:
            Aguarde()
            print("Erro ao apagar do banco!")
        else:
            Aguarde()
            print("Producto apagado com sucesso!")    
            self.db.commit()
            Aguarde()
            self.Desconect()
        finally: 
            Aguarde()
            Clear() 


    def Select(self):
        Clear()
        try:
            self.Conect()
            print("Selecionando productos...")
            self.products = self.cursor.execute("""SELECT * FROM Cozinha""").fetchall()
            #self.products = self.cursor.fetchall()
            self.db.commit()
        except:
            Aguarde()
            print("Erro ao selecionar os productos!")
            Aguarde()
            Clear()
            return 300
        else:
            Aguarde()
            print("Producto selecionado")
            Aguarde()
            self.Desconect()
            Aguarde()
            Clear()       
            return self.products


    def Update(self,acess: int,stock: int):
        Clear()
        try:
            self.Conect()
            print("Actualizando dados...")
            self.cursor.execute(f"""UPDATE Alimentos set Estoque = ({stock}) where Acesso = ({acess})""")
            self.db.commit()
        except:
            Aguarde()
            print("Erro ao actualizar dados!")    
        else:
            Aguarde()
            print("Actualizado com sucesso!")    
            Aguarde()
            self.Desconect()
        finally:
            Aguarde()
            Clear()     
                

    def test_show(self):# -> None
        try:
            self.fetch = self.Select()
            for product in self.fetch:
                print(product)
        except:
            print("Erro ao realizar o teste")    



if __name__=='__main__':
    db() 
