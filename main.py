from servicios import servicios

lista_clientes = [] 

lista_clientes.append(servicios("Alejandro Morales", "3001234567", "Particular", "Limpieza", 1, "Normal", "2025-09-07"))
lista_clientes.append(servicios("Angie Morales", "3109876543", "EPS", "Calzas", 2, "Urgente", "2025-09-08"))
lista_clientes.append(servicios("Juio Morales", "3205556677", "Prepagada", "Extraccion", 1, "Normal", "2025-09-09"))
lista_clientes.append(servicios("Erika Morales", "3501112233", "Particular", "Diagnostico", 1, "Normal", "2025-09-10"))
lista_clientes.append(servicios("Daniel Morales", "3014445566", "EPS", "Limpieza", 1, "Urgente", "2025-09-11"))
lista_clientes.append(servicios("Karen Zamora", "3047778899", "Particular", "Calzas", 3, "Normal", "2025-09-12"))
lista_clientes.append(servicios("Paula Zamora", "3119990011", "Prepagada", "Limpieza", 1, "Normal", "2025-09-13"))
lista_clientes.append(servicios("Diana Herrera", "3152223344", "EPS", "Extraccion", 1, "Urgente", "2025-09-14"))
lista_clientes.append(servicios("Alba Herrera", "3185556677", "Particular", "Limpieza", 2, "Normal", "2025-09-15"))
lista_clientes.append(servicios("Juan Herrera", "3218889900", "EPS", "Diagnostico", 1, "Normal", "2025-09-16"))
lista_clientes.append(servicios("James Rodriguez", "3001112233", "Prepagada", "Calzas", 1, "Normal", "2025-09-17"))
lista_clientes.append(servicios("Falcao Garcia", "3014445566", "Particular", "Extraccion", 1, "Urgente", "2025-09-18"))
lista_clientes.append(servicios("Dayro Moreno", "3047778899", "EPS", "Limpieza", 1, "Normal", "2025-09-19"))
lista_clientes.append(servicios("Luis Diaz", "3119990011", "Prepagada", "Diagnostico", 1, "Normal", "2025-09-20"))

total_clientes = len(lista_clientes)
ingresos_totales = sum(cliente.valor_atencion for cliente in lista_clientes)
clientes_extraccion = sum(1 for cliente in lista_clientes if cliente.tipo_atencion == 'Extraccion')

print("--- Informe del Consultorio ---")
print(f"Total de clientes: {total_clientes}")
print(f"ingresos totales: ${ingresos_totales}")
print(f"Numero de clientes para extraccion: {clientes_extraccion}")
print("-------------------------------")

lista_ordenada = sorted(lista_clientes, key=lambda cliente: cliente.valor_atencion)

print("\n--- Lista de Clientes Ordenada por valor ---")
for cliente in lista_ordenada: 
    print(f"Nombre: {cliente.nombre}, Valor: ${cliente.valor_atencion:,}")
print("--------------------------")

nombre_a_buscar = "Paula Zamora"
cliente_buscado = next((c for c in lista_clientes if c.nombre == nombre_a_buscar),None)

if cliente_buscado:
    print(f"\nCliente encpntrado: {cliente_buscado.nombre}")
    print(f"Tipo de atencion: {cliente_buscado.tipo_atencion}")
    print(f"Valor: ${cliente_buscado.valor_atencion:,}")
else:
    print("\nCliente no encontrado.python main.py")