import streamlit as st
import random

# Función para generar un ejercicio de cinemática
def generar_ejercicio():
    tipo_ejercicio = random.choice(['velocidad', 'aceleracion'])
    if tipo_ejercicio == 'velocidad':
        distancia = random.randint(10, 100)  # Distancia en metros
        tiempo = random.randint(1, 10)  # Tiempo en segundos
        respuesta_correcta = distancia / tiempo
        ejercicio = f"Un objeto recorre {distancia} metros en {tiempo} segundos. ¿Cuál es su velocidad?"
    else:
        velocidad_inicial = random.randint(10, 30)
        aceleracion = random.randint(1, 5)
        tiempo = random.randint(1, 10)
        respuesta_correcta = velocidad_inicial + (aceleracion * tiempo)
        ejercicio = f"Un objeto parte de una velocidad inicial de {velocidad_inicial} m/s y tiene una aceleración de {aceleracion} m/s² durante {tiempo} segundos. ¿Cuál es su velocidad final?"
    
    return ejercicio, respuesta_correcta

# Generar el ejercicio
st.title("Ejercicios de Cinemática")
ejercicio, respuesta_correcta = generar_ejercicio()

# Mostrar el ejercicio
st.write(ejercicio)

# Campo de entrada para la respuesta
respuesta_usuario = st.number_input("Ingresa tu respuesta:", min_value=0.0, step=0.1)

# Botón para verificar la respuesta
if st.button("Verificar respuesta"):
    if respuesta_usuario == respuesta_correcta:
        st.success("¡Correcto!")
    else:
        st.error(f"Incorrecto. La respuesta correcta era: {respuesta_correcta:.2f}")

# Instrucciones
st.write("Presiona 'Generar' para obtener un nuevo ejercicio.")
