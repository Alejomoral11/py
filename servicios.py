class servicios:

    #LISTA DE PRECIOS 
    PRECIOS = {
        'Particular': {'Limpieza': 60000, 'Calzas': 80000, 'Extraccion': 100000, 'Diagnostico': 50000},
        'EPS': {'Limpieza': 0, 'Calzas': 40000, 'Extraccion': 40000, 'Diagnostico': 0},
        'Prepagada': {'Limpieza': 0, 'Calzas': 10000, 'Extraccion': 10000, 'Diagnostico' : 0},
    }
    
    def __init__(self, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad, fecha_cita):
        self.nombre = nombre 
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.cantidad = cantidad
        self.prioridad = prioridad
        self.fecha_cita = fecha_cita
        self.valor_atencion = self.calcular_valor_atencion() #calula valor 

    def calcular_valor_atencion(self):
        valor_base = self.PRECIOS.get(self.tipo_cliente, {}).get(self.tipo_atencion, 0)
        return valor_base * self.cantidad
    