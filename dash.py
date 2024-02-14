import streamlit as st

# Título de la página
st.title("SCAN ON")

# Texto
texto = """
# Título del Texto

Este es un ejemplo de texto en **Markdown** para un dashboard de Streamlit.

Aquí puedes escribir todo el texto que desees. El área de desplazamiento vertical se activará automáticamente si el contenido es demasiado largo para caber en la pantalla.
"""

# Imagen
#imagen_url = "https://ejemplo.com/imagen.png"
#st.image(imagen_url, caption='Ejemplo de Imagen', use_column_width=True)

# Mostrar el texto usando Markdown
st.markdown(texto)

# Input de texto
#texto = st.text_input("Ingresa tu consulta aquí.")

# Input de archivo
#archivo = st.file_uploader("Cargar archivo", type=["csv", "txt"])

# Mostrar el texto ingresado
#st.write("Texto ingresado:", texto)

# Mostrar el contenido del archivo cargado
#if archivo is not None:
#    st.write("Contenido del archivo:")
#    st.write(archivo.read())
