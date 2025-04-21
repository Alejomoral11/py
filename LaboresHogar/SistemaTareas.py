from Persona import Persona
from Tarea import Tarea

class SistemaTareas:
    def __init__(self):
        self.personas = []
        self.tareas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)
        print(f"Se ha agregado a {persona.nombre} al sistema.")

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Se ha agregado la tarea: {tarea.nombre}")

    def asignar_tarea_a_persona(self, nombre_persona, nombre_tarea):
        persona = self.buscar_persona(nombre_persona)
        tarea = self.buscar_tarea(nombre_tarea)
        if persona and tarea:
            persona.asignar_tarea(tarea)
        else:
            print("No se encontró la persona o la tarea.")

    def marcar_tarea_completada(self, nombre_tarea):
        tarea = self.buscar_tarea(nombre_tarea)
        if tarea:
            tarea.marcar_completada()
        else:
            print(f"No se encontró la tarea '{nombre_tarea}'.")

    def buscar_persona(self, nombre):
        for persona in self.personas:
            if persona.nombre == nombre:
                return persona
        return None

    def buscar_tarea(self, nombre):
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                return tarea
        return None

    def mostrar_tareas_pendientes(self):
        tareas_pendientes = [tarea for tarea in self.tareas if tarea.estado == "Pendiente"]
        if tareas_pendientes:
            print("\n--- Tareas Pendientes ---")
            for tarea in tareas_pendientes:
                print(f"- {tarea.nombre} (Prioridad: {tarea.prioridad}, Límite: {tarea.fecha_limite})")
        else:
            print("\nNo hay tareas pendientes.")

    def mostrar_reporte_tareas_por_persona(self):
        print("\n--- Reporte de Tareas por Persona ---")
        for persona in self.personas:
            persona.mostrar_tareas()

    def mostrar_reporte_conteo_tareas_completadas(self):
        conteo_tareas = {}
        for persona in self.personas:
            conteo = sum(1 for tarea in persona.tareas_asignadas if tarea.estado == "Completada")
            conteo_tareas[persona.nombre] = conteo

        if conteo_tareas:
            print("\n--- Conteo de Tareas Completadas por Persona ---")
            for nombre, cantidad in conteo_tareas.items():
                print(f"- {nombre}: {cantidad} tareas completadas")
        else:
            print("\nAún no se han completado tareas.")

if __name__ == "__main__":
    # Ejemplo de uso independiente de la clase SistemaTareas
    sistema = SistemaTareas()
    persona1 = Persona("Elena", 26)
    tarea1 = Tarea("Regar las plantas", "Cada dos días", "Baja", "2025-04-21")

    sistema.agregar_persona(persona1)
    sistema.agregar_tarea(tarea1)
    sistema.asignar_tarea_a_persona("Elena", "Regar las plantas")
    sistema.marcar_tarea_completada("Regar las plantas")
    sistema.mostrar_tareas_pendientes()
    sistema.mostrar_reporte_tareas_por_persona()
    sistema.mostrar_reporte_conteo_tareas_completadas()