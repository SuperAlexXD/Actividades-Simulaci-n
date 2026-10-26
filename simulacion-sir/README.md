# 🦠 Simulación Epidemiológica SIR (Java + NetLogo)

Este proyecto implementa el modelo matemático **SIR** (Susceptibles, Infectados, Recuperados) para simular la propagación de un virus. Parámetros: población de 100 individuos, 5 infectados iniciales, tasa de contagio (β = 0.30) y tasa de recuperación (γ = 0.10).

El sistema se divide en dos partes que se comunican a través de un archivo CSV:

1. **Java (Cálculo):** Motor de simulación estocástica que calcula la evolución paso a paso y exporta los datos.
2. **NetLogo (Visualización):** Interfaz visual que lee el CSV generado por Java y representa la epidemia mediante gráficos y agentes.

---

## 📂 Estructura del Proyecto

```text
simulacion-sir/
├── src/                      # Código fuente en Java (Arquitectura MVC)
├── modelo-sir.nlogo          # Interfaz visual en NetLogo
├── resultados_java.csv       # Datos generados por la simulación en Java
├── informe/                  # Documento con conclusiones de la práctica
├── .gitignore                # Archivos ignorados por Git
└── README.md                 # Documentación del proyecto

🚀 Guía de Ejecución
Paso 1: Compilar y Ejecutar Java
Desde la terminal, ubicado en la carpeta raíz del proyecto:
# 1. Compilar el proyecto
javac -d out src/main/java/model/*.java src/main/java/view/*.java src/main/java/controller/*.java src/main/java/Main.java

# 2. Ejecutar la simulación
java -cp out Main
Al finalizar, verás la evolución impresa en la consola y se habrá creado o actualizado el archivo resultados_java.csv.

Paso 2: Visualizar en NetLogo
Abre el archivo modelo-sir.nlogo en NetLogo.

Haz clic en el botón Cargar CSV Java para leer los datos calculados por Java.

Haz clic en el botón Avanzar CSV para ver la evolución de los agentes y la gráfica paso a paso.

Nota: Para una visualización óptima, marca la opción "Continuamente" en el botón y ajusta la velocidad en la configuración.

.

🧠 Sobre los resultados
Debido a la naturaleza estocástica del modelo (uso de probabilidades y números aleatorios), los resultados varían ligeramente en cada ejecución de Java. Sin embargo, tanto Java como NetLogo reflejan la misma tendencia matemática: un brote explosivo que diezma a los susceptibles en los primeros pasos y culmina en la inmunidad de rebaño.

👥 Integrantes del Grupo
Santiago Villamagua

Martina Maldonado

Mark Gonzales

Richard Cajas


## Opción 2: Crear el archivo desde tu terminal (automático)

**En Linux/WSL2:**

```bash
cat > README.md << 'EOF'
# 🦠 Simulación Epidemiológica SIR (Java + NetLogo)
... (pega aquí el contenido completo)
EOF

