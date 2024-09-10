print("introduccion a clase")

class animal:
    edad=3
    raza="chihuahua"
    comida="croquetas"
    def come(self):
        print("el perro come "+self.comida)
print(animal)
print("creando el objeto de la clase animal")
perro=animal()
print(f"Edad del perro: {perro.edad}")
print(f"raza del perro: {perro.raza}")
perro.come ()