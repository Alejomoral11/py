class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.tareas_asignadas = []

    def asignar_tarea(self, tarea):
        self.tareas_asignadas.append(tarea)
        print(f"{self.nombre} ha sido asignado/a a la tarea: {tarea.nombre}")

    def mostrar_tareas(self):
        if self.tareas_asignadas:
            print(f"Tareas asignadas a {self.nombre}:")
            for tarea in self.tareas_asignadas:
                print(f"- {tarea.nombre} (Prioridad: {tarea.prioridad}, Estado: {tarea.estado})")
        else:
            print(f"{self.nombre} no tiene tareas asignadas.")

class Tarea:
    def __init__(self, nombre, descripcion, prioridad, fecha_limite):
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = "Pendiente"
        self.fecha_limite = fecha_limite

    def marcar_completada(self):
        self.estado = "Completada"
        print(f"La tarea '{self.nombre}' ha sido marcada como completada.")

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
    sistema = SistemaTareas()

    ana = Persona("Camila", 24)
    pedro = Persona("Daniela", 26)
    lucia = Persona("Paula", 30)

    sistema.agregar_persona(ana)
    sistema.agregar_persona(pedro)
    sistema.agregar_persona(lucia)

    limpiar_cocina = Tarea("Limpiar la cocina", "Lavar platos, limpiar meson y piso", "Alta", "2025-05-01")
    sacar_basura = Tarea("Sacar la basura", "Llevar las bolsas al contenedor y lavar la caneca", "Media", "2025-05-02")
    limpiar_banio = Tarea("Limpiar el baño", "Limpiar inodoro, lavamanos y ducha", "Alta", "2025-05-05")
    hacer_compra = Tarea("Hacer las compras", "Comprar los alimentos para la semana", "Media", "2025-05-08")

    sistema.agregar_tarea(limpiar_cocina)
    sistema.agregar_tarea(sacar_basura)
    sistema.agregar_tarea(limpiar_banio)
    sistema.agregar_tarea(hacer_compra)

    sistema.asignar_tarea_a_persona("Ana", "Limpiar la cocina")
    sistema.asignar_tarea_a_persona("Pedro", "Sacar la basura")
    sistema.asignar_tarea_a_persona("Lucía", "Limpiar el baño")
    sistema.asignar_tarea_a_persona("Ana", "Hacer la compra")

    sistema.marcar_tarea_completada("Limpiar la cocina")
    sistema.marcar_tarea_completada("Sacar la basura")

    sistema.mostrar_tareas_pendientes()
    sistema.mostrar_reporte_tareas_por_persona()
    sistema.mostrar_reporte_conteo_tareas_completadas()