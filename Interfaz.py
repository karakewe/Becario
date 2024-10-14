import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def radar_chart(values):
    # Categorías para el gráfico de araña
    categories = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4', 'Categoria 5', 'Categoria 6', 'Categoria 7']

    # Número de categorías
    N = len(categories)

    # Ángulos para cada categoría
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

    # Añadir el primer ángulo al final para cerrar el gráfico
    values += values[:1]
    angles += angles[:1]

    # Configuración del gráfico de araña
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='skyblue', alpha=0.4)
    ax.plot(angles, values, color='blue', linewidth=2, linestyle='solid')
    ax.set_yticks(np.arange(0, 21, 5))  # Establecer ticks en el eje radial
    ax.set_yticklabels([])  # Desactivar etiquetas
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12)

    return fig

# Configuración de la aplicación Streamlit
def main():
    st.title('Gráfico de Araña con Streamlit')

    # Entrada de valores del usuario
    st.header('Ingrese 7 valores entre 0 y 20:')
    values = []
    for i in range(7):
        value = st.slider(f'Valor {i+1}', 0, 20, 10)  # Inicializar en 10
        values.append(value)

    # Normalizar los valores para que el máximo sea 20
    normalized_values = [value for value in values]  # En este caso, no necesitas cambiar nada

    # Generar y mostrar el gráfico de araña
    st.pyplot(radar_chart(normalized_values))

if __name__ == '__main__':
    main()
