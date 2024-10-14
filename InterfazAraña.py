import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Función para cada sección
def bienestar_social():
    st.header('Bienestar Social')
    st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
    questions = [
        "Contribuyo con tiempo y/o dinero a proyectos sociales y comunitarios.",
        "Estoy comprometido con una vida de voluntariado.",
        "Demuestro imparcialidad y justicia al tratar con personas.",
        "Tengo una red de amigos cercanos y/o familiares.",
        "Me interesan los demás, incluso aquellos de diferentes antecedentes que el mío.",
        "Puedo equilibrar mis propias necesidades con las necesidades de los demás.",
        "Puedo comunicarme y llevarme bien con una gran variedad de personas.",
        "Obedezco las leyes y reglas de nuestra sociedad.",
        "Soy una persona compasiva y trato de ayudar a los demás cuando puedo.",
        "Apoyo y ayudo con las reuniones sociales de la familia, el vecindario y el trabajo."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])  # Selección de valores 0, 1 o 2
        values.append(value)
    return np.mean(values)  # Retornar el promedio de las respuestas

def bienestar_intelectual():
    st.header('Bienestar Intelectual')
    st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
    questions = [
        "Estoy interesado en aprender cosas nuevas.",
        "Trato de mantenerme al tanto de los asuntos actuales a nivel local, nacional e internacional.",
        "Disfruto asistiendo a conferencias, obras de teatro, actuaciones musicales, museos, galerías y/o bibliotecas.",
        "Selecciono cuidadosamente películas y/o programas de televisión.",
        "Disfruto de actividades/juegos mentales creativos y estimulantes.",
        "Estoy contento con la cantidad y variedad que leo.",
        "Me esfuerzo por mejorar mis habilidades verbales y escritas.",
        "Un programa de educación continua es/será importante para mí en mi carrera.",
        "Puedo analizar, sintetizar y ver más de un lado de un problema.",
        "Me gusta participar en discusiones intelectuales."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienestar_ocupacional():
    st.header('Bienestar Ocupacional')
    st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
    questions = [
        "Estoy contento con mi elección de carrera.",
        "Estoy buscando trabajar.",
        "Mis responsabilidades/obligaciones laborales/estudiantiles son consistentes con mis valores.",
        "Los pagos/ventajas en mi elección de campo profesional son consistentes con mis valores.",
        "Estoy contento con el equilibrio entre mi tiempo de trabajo y mi tiempo libre.",
        "Estoy contento con la cantidad de control que tengo en mi trabajo.",
        "Mi trabajo me da satisfacción y estimulación personal.",
        "Estoy contento con el crecimiento profesional que he tenido.",
        "Siento que mi trabajo me permite hacer una diferencia.",
        "Mi trabajo contribuye positivamente a mi bienestar."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienestar_emocional():
    st.header('Bienestar Emocional')
    st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
    questions = [
        "Puedo desarrollar y mantener relaciones cercanas.",
        "Acepto la responsabilidad de mis acciones.",
        "Veo desafíos y cambios como oportunidades de crecimiento.",
        "Siento que tengo un control considerable sobre mí.",
        "Puedo reírme de la vida y de mí mismo.",
        "Me siento bien conmigo mismo.",
        "Soy capaz de lidiar adecuadamente con el estrés.",
        "Puedo reconocer mis deficiencias personales y trabajar en ellas.",
        "Tengo un fuerte sentido de optimismo de vida y uso mis pensamientos y actitudes en formas que afirmen la vida.",
        "Mi trabajo contribuye positivamente a mi bienestar general."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienestar_espiritual():
    st.header('Bienestar Espiritual')
    st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
    questions = [
        "Me siento cómodo con mi vida espiritual.",
        "Existe una relación directa entre mis valores y acciones.",
        "Cuando me deprimo o me frustro, mis creencias me ayudan.",
        "La oración, la meditación y/o reflexión son parte de mi vida.",
        "La vida es significativa para mí, y siento que tengo un propósito.",
        "Puedo hablar cómodamente de mis valores y creencias.",
        "Constantemente estoy tratando de crecer espiritualmente.",
        "Soy tolerante e intento aprender sobre las creencias de otros.",
        "Encuentro consuelo en la naturaleza y el entorno que me rodea.",
        "Practico gratitud regularmente en mi vida."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienestar_financiero():
    st.header('Bienestar Financiero')
    st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
    questions = [
        "¿Tienes efectivo en tu bolsillo?",
        "¿Equilibras tu presupuesto?",
        "¿Conoces la cantidad total de la deuda que tienes?",
        "¿Administras bien tu tiempo?",
        "¿Tienes una cuenta propia de ahorro?",
        "¿Sabes cuánto hay en tu cuenta de ahorro?",
        "¿Tu situación financiera te genera estrés?",
        "¿Realizas alguna actividad que te genere ingresos?",
        "¿Tienes un plan financiero a largo plazo?",
        "¿Evalúas regularmente tu situación financiera?"
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienestar_fisico():
    st.header('Bienestar Fisico')
    st.write('PUNTUACIÓN: Casi siempre = 2 puntos | A veces/ ocasionalmente = 1 punto | Muy raramente = 0 puntos')
    questions = [
        "Hago ejercicio aeróbico (vigoroso, continuo) durante 20 o 30 min. al menos 3 veces por semana.",
        "Como fruta, vegetales y granos integrales todos los días.",
        "Evito los productos de tabaco.",
        "Uso un cinturón de seguridad mientras viajo en o conduzco un automóvil.",
        "Minimizo deliberadamente mi ingesta de colesterol, grasas y aceites.",
        "Evito tomar bebidas alcohólicas o no consumo más de una bebida por día.",
        "Tengo una cantidad adecuada de agua.",
        "Tengo mecanismos adecuados para enfrentar el estrés.",
        "Mantengo un horario regular de inmunizaciones, exámenes físicos, chequeos dentales y autoexámenes.",
        "Mantengo un peso razonable, evitando los extremos de sobrepeso y bajo peso."
    ]
    values = []
    for question in questions:
        value = st.radio(question, options=[0, 1, 2])
        values.append(value)
    return np.mean(values)

def bienvenida_encuesta():
    st.write("""
    Esta encuesta tiene como objetivo evaluar diferentes dimensiones de tu bienestar.
    A través de una serie de preguntas, podrás reflexionar sobre aspectos importantes de tu vida en las siguientes áreas:
    - Bienestar Social
    - Bienestar Intelectual
    - Bienestar Ocupacional
    - Bienestar Emocional
    - Bienestar Espiritual
    - Bienestar Financiero
    - Bienestar Físico

    Por favor, responde cada pregunta con sinceridad. Al final de la encuesta, podrás ver un gráfico que refleja tu bienestar en cada una de estas dimensiones.
    """)
    return 0

# Configuración de la aplicación Streamlit
def radar_chart(values):
    categories = ['Social', 'Intelectual', 'Ocupacional', 'Emocional', 'Espiritual', 'Financiero', 'Físico']
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

    # Close the chart loop
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='skyblue', alpha=0.4)
    ax.plot(angles, values, color='blue', linewidth=2, linestyle='solid')
    ax.set_yticks(np.arange(0, 3, 1))  # Cambiado a rango 0-2
    ax.set_yticklabels([])  # Desactivar etiquetas
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12)

    return fig

# Configuración de la aplicación Streamlit
def main():
    st.title('Bienvenido a la Encuesta Rueda de la Vida')
    bienvenida_encuesta()
    # Índice en la parte superior
    st.sidebar.markdown("""
    ### Índice
    - [Bienvenida](#bienvenida-encuesta)
    - [Bienestar Social](#bienestar-social)
    - [Bienestar Intelectual](#bienestar-intelectual)
    - [Bienestar Ocupacional](#bienestar-ocupacional)
    - [Bienestar Emocional](#bienestar-emocional)
    - [Bienestar Espiritual](#bienestar-espiritual)
    - [Bienestar Financiero](#bienestar-financiero)
    - [Bienestar Físico](#bienestar-fisico)
    - [Resultados](#resultados)
    """)

    # Llamar a las funciones de cada sección
    scores = []
    scores.append(bienestar_social())
    scores.append(bienestar_intelectual())
    scores.append(bienestar_ocupacional())
    scores.append(bienestar_emocional())
    scores.append(bienestar_espiritual())
    scores.append(bienestar_financiero())
    scores.append(bienestar_fisico())

    # Generar y mostrar el gráfico de araña
    if st.button('Mostrar Resultados'):
        st.header('Resultados')
        st.pyplot(radar_chart(scores))

if __name__ == '__main__':
    main()
