# Sistema de Control de Presupuesto del Hogar

---

## 📚 Información General del Proyecto

| Aspecto | Detalle |
|--------|---------|
| **Universidad** | Corporación Universitaria del Caribe - CUC |
| **Asignatura** | Algoritmia y Programación |
| **Año Académico** | 2026 |
| **Tipo de Proyecto** | Aplicación de Consola en Python |
| **Versión** | 1.0 |

---

## 🎯 Descripción del Proyecto

El **Sistema de Control de Presupuesto del Hogar** es una aplicación educativa desarrollada en Python que permite a los usuarios gestionar y controlar sus gastos del hogar de manera efectiva. Esta herramienta fue desarrollada como proyecto académico de la asignatura Algoritmia y Programación, implementando conceptos fundamentales de programación como estructuras de datos, control de flujo y manejo de excepciones.

El sistema proporciona una interfaz interactiva basada en línea de comandos que facilita el registro, seguimiento y análisis de gastos clasificados en tres categorías: servicios, comida y gastos extras. Los datos se almacenan en estructuras de datos en memoria, permitiendo al usuario visualizar su situación presupuestaria en tiempo real y recibir alertas cuando se exceda el presupuesto establecido.

---

## ✨ Funcionalidades

El sistema implementa las siguientes funcionalidades principales:

### 1. **Registrar Gasto**
   - Permite al usuario ingresar un nuevo gasto
   - Solicita: nombre del gasto, categoría y valor
   - Valida que la categoría sea una de las tres opciones válidas
   - Valida que el valor sea un número entero positivo
   - Asigna automáticamente un ID único a cada gasto
   - Manejo de excepciones para entradas inválidas

### 2. **Ver Lista de Gastos**
   - Muestra todos los gastos registrados en orden de ingreso
   - Presenta: ID, nombre, categoría y valor de cada gasto
   - Notifica si no hay gastos registrados

### 3. **Ver Total Gastado**
   - Calcula la suma total de todos los gastos registrados
   - Presenta el resultado al usuario de manera clara

### 4. **Ver Saldo Restante**
   - Solicita el ingreso del hogar
   - Calcula el saldo restante (ingreso - gastos)
   - Muestra una alerta si el gasto excede el ingreso presupuestado

### 5. **Salir**
   - Termina la ejecución del programa

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Descripción |
|-----------|------------|
| **Lenguaje** | Python 3.x |
| **Paradigma** | Programación Estructurada y Funcional |
| **Estructuras de Datos** | Listas y Diccionarios |
| **Entrada/Salida** | Consola (input/print) |
| **Control de Errores** | Try-Except para manejo de excepciones |

---

## 🚀 Cómo Ejecutarlo

### Requisitos Previos
- Python 3.x instalado en el sistema
- Terminal o línea de comandos disponible
- Acceso al archivo `final.py`

### Pasos de Ejecución

1. **Abrir la terminal** en el directorio del proyecto
   ```bash
   cd ruta/al/proyecto/main
   ```

2. **Ejecutar el programa**
   ```bash
   python final.py
   ```

3. **Usar el menú interactivo**
   - El programa mostrará un menú con 5 opciones
   - Ingresa el número de la opción que deseas utilizar
   - Sigue las instrucciones que aparecen en pantalla

### Ejemplo de Uso

```
=== MENÚ PRINCIPAL ===
1. Registrar gasto
2. Ver lista de gastos
3. Ver total gastado
4. Ver saldo restante
5. Salir

Selecciona una opción: 1
Ingresa el nombre del gasto: Supermercado
Ingrese la categoria:
Comida | servicio | extra: comida
Ingresa el valor de gasto: 50000
```

---

## 📂 Estructura del Código

### Archivo Principal: `final.py`

#### Variables Globales
- **`gastos`**: Lista que almacena todos los gastos registrados
- **`contador_id`**: Contador entero que asigna ID único a cada gasto

#### Funciones Implementadas

```python
def registrar_gasto()
```
- **Propósito**: Captura y valida los datos de un nuevo gasto
- **Parámetros**: Ninguno (usa entrada interactiva)
- **Proceso**:
  1. Solicita nombre, categoría y valor del gasto
  2. Valida que la categoría esté en ["comida", "servicio", "extra"]
  3. Valida que el valor sea mayor a 0
  4. Crea un diccionario con los datos del gasto
  5. Agrega el gasto a la lista `gastos`
  6. Incrementa el contador de IDs
- **Manejo de Errores**: Captura excepciones e imprime el mensaje de error

```python
def mostrar_gastos()
```
- **Propósito**: Muestra la lista completa de gastos registrados
- **Parámetros**: Ninguno
- **Proceso**:
  1. Verifica si existen gastos registrados
  2. Si no hay gastos, imprime mensaje informativo
  3. Si hay gastos, itera sobre la lista y imprime cada uno con su información

```python
def calcular_total()
```
- **Propósito**: Calcula el total acumulado de gastos
- **Parámetros**: Ninguno
- **Retorna**: Entero con el total de gastos
- **Proceso**: Itera sobre la lista de gastos sumando los valores

```python
def calcular_saldo(ingreso_hogar, total_gastado)
```
- **Propósito**: Calcula el saldo presupuestario y valida límites
- **Parámetros**: 
  - `ingreso_hogar`: Ingreso mensual del hogar
  - `total_gastado`: Total de gastos calculado
- **Proceso**:
  1. Resta gastos del ingreso
  2. Imprime el saldo restante
  3. Emite alerta si el saldo es negativo

#### Estructura de Datos - Diccionario de Gasto
```python
{
    "id": int,           # Identificador único
    "nombre": str,       # Nombre del gasto
    "categoria": str,    # Categoría (comida, servicio, extra)
    "valor": int         # Monto del gasto
}
```

---

## 👥 Autores

| Nombre Completo | Rol |
|-----------------|-----|
| **Walter Samuel Carroll Nieto** | Desarrollador |
| **Samuel Almario Ventura** | Desarrollador |

**Institución**: Corporación Universitaria del Caribe - CUC  
**Programa**: Ingenierías (Asignatura: Algoritmia y Programación)  
**Fecha de Realización**: Año Académico 2026

---

## 📝 Notas Académicas

Este proyecto implementa conceptos fundamentales de programación:

- ✅ **Estructuras de Datos**: Uso de listas para almacenamiento dinámico y diccionarios para agrupación lógica de datos
- ✅ **Control de Flujo**: Condicionales (if-else) para validaciones y decisiones
- ✅ **Iteración**: Bucles (for) para procesar colecciones de datos
- ✅ **Funciones**: Modularización del código en funciones reutilizables
- ✅ **Manejo de Excepciones**: Try-except para captura y gestión de errores
- ✅ **Variables Globales**: Uso de variables compartidas entre funciones

---

## 📌 Estado del Proyecto

| Aspecto | Estado |
|--------|--------|
| Funcionalidades Básicas | ✅ Completado |
| Validación de Datos | ✅ Completado |
| Menú Interactivo | ✅ Completado |
| Documentación | ✅ Completado |

**Versión Actual**: 1.0 - Versión estable inicial

---

## 📄 Licencia

Proyecto académico de la Corporación Universitaria del Caribe - CUC

