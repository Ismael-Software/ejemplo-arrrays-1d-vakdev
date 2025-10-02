class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre:str = nombre
        self.apellido:str = apellido
        self.edad:int = edad

    def saludar(self):
        print(f"{self.nombre.capitalize()} está saludando.")

    def comer(self):
        print(f"{self.nombre.capitalize()} está comiendo.")

    def mostrarInfo(self):
        print(self)
        
    def __repr__(self):
        return f"Nombre completo= {self.nombre} {self.apellido}, Edad= {self.edad}"
    



profesor = Persona("Alberto", "Dominguez", 30)
alumno = Persona("Alejandro", "Barrera", 23)
chofer = Persona("Zayuri", "Espinoza", 29)
deportista = Persona("Lebron", "James", 30)

deportista.mostrarInfo()