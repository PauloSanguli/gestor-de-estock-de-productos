try:
    from db.alimentos import db as alimentos
    from db.carros import db as carros
    from db.cozinha import db as cozinha
    from db.ferramentas import db as ferramentas
    from db.vestuario import db as vestuario
    from db.mobilia import db as mobilia
    from db.aparelhos import db as aparelhos    
    from db.mota import db as mota
except:
    from .db.alimentos import db as alimentos
    from .db.carros import db as carros
    from .db.cozinha import db as cozinha
    from .db.ferramentas import db as ferramentas
    from .db.mobilia import db as mobilia
    from .db.aparelhos import db as aparelhos
    from .db.vestuario import db as vestuario
    from .db.mota import db as mota




class Alimentos(alimentos):
    def __init__(self):
        super().__init__()
        
    def Insert_db(acess: int,nome: str, descript: str, stock: int,buy: float):
        self = alimentos()
        self.Insert(acess,nome,descript,stock,buy)


    def Update_db(acess: int,stock: int):
        self = alimentos()
        self.Update(acess,stock)


    def Delete_db(acess: int):
        self = alimentos()
        self.Delete(acess)  


    def Select_db():
        self = alimentos()
        return self.Select() 


        
class Cozinha(cozinha):
    def __init__(self):
        super().__init__()


    def Insert_db(acess: int,nome: str, descript: str, stock: int,buy: float):
        self = cozinha()
        self.Insert(acess,nome,descript,stock,buy)


    def Update_db(acess: int,stock: int):
        self = cozinha()
        self.Update(acess,stock)


    def Delete_db(acess: int):
        self = cozinha()
        self.Delete(acess)  


    def Select_db():
        self = cozinha()
        return self.Select()



class Ferramentas(ferramentas):
    def __init__(self):
        super().__init__()


    def Insert_db(acess: int,nome: str, descript: str, stock: int,buy: float):
        self = ferramentas()
        self.Insert(acess,nome,descript,stock,buy)


    def Update_db(acess: int,stock: int):
        self = ferramentas()
        self.Update(acess,stock)


    def Delete_db(acess: int):
        self = ferramentas()
        self.Delete(acess)  


    def Select_db():
        self = ferramentas()
        return self.Select()



class Vestuario(vestuario):
    def __init__(self):
        super().__init__()


    def Insert_db(acess: int,nome: str, descript: str, stock: int,buy: float):
        self = vestuario()
        self.Insert(acess,nome,descript,stock,buy)


    def Update_db(acess: int,stock: int):
        self = vestuario()
        self.Update(acess,stock)


    def Delete_db(acess: int):
        self = vestuario()
        self.Delete(acess)  


    def Select_db():
        self = vestuario()
        return self.Select()


class Carros(carros):
    def __init__(self):
        super().__init__()


    def Insert_db(acess: int,nome: str, descript: str, stock: int,buy: float):
        self = carros()
        self.Insert(acess,nome,descript,stock,buy)


    def Update_db(acess: int,stock: int):
        self = carros()
        self.Update(acess,stock)


    def Delete_db(acess: int):
        self = carros()
        self.Delete(acess)  


    def Select_db():
        self = carros()
        return self.Select()


class Mobilia(mobilia):
    def __init__(self):
        super().__init__()


    def Insert_db(acess: int,nome: str, descript: str, stock: int,buy: float):
        self = mobilia()
        self.Insert(acess,nome,descript,stock,buy)


    def Update_db(acess: int,stock: int):
        self = mobilia()
        self.Update(acess,stock)


    def Delete_db(acess: int):
        self = mobilia()
        self.Delete(acess)  


    def Select_db():
        self = mobilia()
        return self.Select()        


class Aparelhos(aparelhos):
    def __init__(self):
        super().__init__()


    def Insert_db(acess: int,nome: str, descript: str, stock: int,buy: float):
        self = aparelhos()
        self.Insert(acess,nome,descript,stock,buy)


    def Update_db(acess: int,stock: int):
        self = aparelhos()
        self.Update(acess,stock)


    def Delete_db(acess: int):
        self = aparelhos()
        self.Delete(acess)  


    def Select_db():
        self = aparelhos()
        return self.Select()


class Mota(mota):
    def __init__(self):
        super().__init__()
        
    def Insert_db(acess: int,nome: str, descript: str, stock: int,buy: float):
        self = mota()
        self.Insert(acess,nome,descript,stock,buy)


    def Update_db(acess: int,stock: int):
        self = mota()
        self.Update(acess,stock)


    def Delete_db(acess: int):
        self = mota()
        self.Delete(acess)  


    def Select_db():
        self = mota()
        return self.Select() 