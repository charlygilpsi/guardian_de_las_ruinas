# 1️⃣ Estructura del proyecto (modular sin usar POO)

Podéis organizar el proyecto en módulos funcionales, por ejemplo:

guardian_ruinas/
│
├── main.py # Orquestador del programa
├── personajes.py # Todo lo relacionado con aventureros y enemigo
├── gemas.py # Lógica del tesoro
├── combate.py # Sistema de turnos y combate
└── utils.py # Funciones auxiliares (si hicieran falta)


## 📌 Responsabilidad de cada módulo

### personajes.py

- Crear lista de aventureros  
- Crear diccionario del enemigo  
- Funciones relacionadas con mostrar estadísticas  

---

### gemas.py

- Pedir al usuario los 5 valores  
- Calcular:
  - Máximo
  - Mínimo
  - Promedio
- Mostrar resultados  

---

### combate.py

- Función `turno(...)`
- Simulación del duelo
- Lógica de decisiones
- Gestión del flujo del combate

---

### main.py

- Llama a los otros módulos  
- Controla el orden del juego:
  1. Crear personajes
  2. Gestionar gemas
  3. Iniciar combate

> 🔹 **Muy importante:** `main.py` no debe tener lógica pesada. Solo coordina.

---

# 2️⃣ División del trabajo entre vosotros

Podéis repartir por responsabilidad funcional:

## 👤 Persona A

- `personajes.py`
- `gemas.py`

## 👤 Persona B

- `combate.py`
- Integración en `main.py`

---

## Alternativa más equilibrada

- Una persona se encarga de **datos y cálculos** (`gemas.py` + `personajes.py`).
- La otra persona se encarga de **lógica dinámica** (`combate.py` + turnos).
