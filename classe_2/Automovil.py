
class Automovil:
    marca:str
    color:str
    modelo:str
    año:int

    def __init__(self, marca:str):
        self.marca = marca

    def set_color(self,color:str):
        self.color=color

    def set_modelo(self,modelo:str):
                self.modelo=modelo

    def set_año(self,año:int):
                    self.año=año


    def Inf(self)-> bool:
     #codigo.........                    
     return True

    Auto1=Automovil('mazda')
    Auto2=Automovil('toyota')
    Auto3=Automovil('mazda')


    numero1=5
    numero2=5
    if(Auto1==Auto3):
        print("son iguales")
    else:
        print("no son iguales")


    print("objeto 1:",Auto1)
    print("objeto 2:",Auto2)
    print("objeto 3:",Auto3)


pass
                  

