class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
        self.tareas_asignadas = []

    def asignar_tarea(self, tarea):
        self.tareas_asignadas.append(tarea)
        print(f"{self.nombre} ha sido asignado a la tarea: {tarea.nombre}")

    def mostrar_tareas(self):
        if self.tareas_asignadas:
            print(f"Tareas asignadas a {self.nombre}:")
            for tarea in self.tareas_asignadas:
                print(f"- {tarea.nombre} (Prioridad: {tarea.prioridad}, Estado: {tarea.estado})")
        else:
            print(f"{self.nombre} no tiene tareas asignadas.")

if __name__ == "__main__":
    persona1 = Persona("Daniela", 23)
    print(f"Nombre: {persona1.nombre}, Edad: {perosna1.}")
