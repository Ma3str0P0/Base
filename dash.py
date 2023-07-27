import streamlit as st

# Título de la página
st.title("Mi Dashboard")

# Input de texto
texto = st.text_input("Ingresa tu texto aquí")

# Input de archivo
archivo = st.file_uploader("Cargar archivo", type=["csv", "txt"])

# Mostrar el texto ingresado
st.write("Texto ingresado:", texto)

# Mostrar el contenido del archivo cargado
if archivo is not None:
    st.write("Contenido del archivo:")
    st.write(archivo.read())