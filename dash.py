import streamlit as st

# Título de la página
st.title("Mi Título **Amarillo**", key="titulo_amarillo")

# Texto
texto = """
-
-
-
-
-
Análisis: La última tensión máxima observada es de 3.092 voltios de SKY_MTY S1A_BCU01_VOLT_MIN, y la última tensión mínima es de 2.985 voltios de SKY_MTY S1A_BCU09_VOLT_MIN, lo que resulta en una variación de voltaje de 0.107 voltios.
Diagnóstico: La variación de voltaje excede el umbral de 0.05 voltios durante el proceso de descarga de la batería, ya que el SOC está entre el 10% y el 50%. El sistema no está operando dentro del rango aceptable de equilibrio de voltaje, lo que podría llevar a una detención prematura en la descarga.

Severidad del desequilibrio: 7/10
Probabilidad de desequilibrio de rack: 1.0

Acciones sugeridas: 1. Iniciar un procedimiento de equilibrio para corregir las diferencias de voltaje. 2. Inspeccionar SKY_MTY S1A_BCU09 en busca de posibles problemas que causen la alta caída de voltaje.

Enviar mensaje al operador: sí

SKY_MTY S1A
"""

# Imagen
#imagen_url = "https://ejemplo.com/imagen.png"
#st.image(imagen_url, caption='Ejemplo de Imagen', use_column_width=True)

# Mostrar el texto usando Markdown
st.markdown(texto)

# Input de texto
texto = st.text_input("Ingresa tu consulta aquí.")

# Input de archivo
#archivo = st.file_uploader("Cargar archivo", type=["csv", "txt"])

# Mostrar el texto ingresado
#st.write("Texto ingresado:", texto)

# Mostrar el contenido del archivo cargado
#if archivo is not None:
#    st.write("Contenido del archivo:")
#    st.write(archivo.read())
