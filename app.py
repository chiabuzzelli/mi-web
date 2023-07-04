import pandas as pd
import ipywidgets as widgets
from IPython.display import display
from flask import Flask, render_template_string, request, redirect, url_for, render_template

app = Flask(__name__)

def obtener_descripcion(puntaje1, puntaje2, puntaje3, puntaje4, puntaje5, puntaje6, puntaje7, puntaje8):
    descripciones = []
    if puntaje1 == 0:
            descripciones.append("No es capaz de realizar ningún movimiento")
    elif puntaje1 == 1:
            descripciones.append("Se empuja hacia decúbito lateral con el MS sano y con el MI sano mueve el MI afectado")
    elif puntaje1 == 3:
            descripciones.append("Eleva y mueve el MS afectado por encima del cuerpo con el MS sano. El MI afectado se mueve de forma activa y el cuerpo gira en bloque")
    elif puntaje1 == 2:
            descripciones.append("Mueve el MI afectado de forma activa y el tronco inferior cae hacia delante. Al realizar el movimiento el MS afectado es dejado atrás del tronco")
    elif puntaje1 == 4:
            descripciones.append("Mueve el miembro superior afectado por encima del cuerpo y el cuerpo gira en bloque")
    elif puntaje1 == 5:
            descripciones.append("Mueve el MS y MI afectado y rola hacia el lado sano; pero pierde el equilibrio (el hombro afectado se protrae y se flexiona hacia delante)")
    elif puntaje1 == 6:
            descripciones.append("Rola hacia el lado sano en 3 segundos")
    else:
            descripciones.append("Descripción no disponible")

    if puntaje2 == 0:
            descripciones.append("No es capaz de iniciar la maniobra")
    elif puntaje2 == 1:
            descripciones.append("Desde DL, eleva su cabeza hacia el lado pero no es capaz de sentarse")
    elif puntaje2 == 2:
            descripciones.append("Desde DL, el terapeuta asiste la maniobra mientras el/la paciente controla la posición de la cabeza")
    elif puntaje2 == 3:
            descripciones.append("Desde DL, recibe asistencia para sacar las piernas por el lateral de la cama")
    elif puntaje2 == 4:
            descripciones.append("Desde DL, es capaz de sentarse sin ayuda")
    elif puntaje2 == 5:
            descripciones.append("Desde DS, es capaz de sentarse sin ayuda")
    elif puntaje2 == 6:
            descripciones.append("Desde DS, es capaz de sentarse en menos de 10 segundos sin ayuda")
    else:
            descripciones.append("Descripción no disponible")

    if puntaje3 == 0:
            descripciones.append("No es capaz de mantenerse sentado con soporte del terapista")
    elif puntaje3 == 1:
            descripciones.append("Mantiene la sedestación con soporte del terapista")
    elif puntaje3 == 2:
            descripciones.append("Mantiene la sedestación sin ayuda durante 10 segundos")
    elif puntaje3 == 3:
            descripciones.append("Mantiene la sedestación sin ayuda con el centro de gravedad hacia delante y el peso bien distribuido")
    elif puntaje3 == 4:
            descripciones.append("Mantiene la sedestación sin ayuda y es capaz de girar su tronco y cabeza para mirar hacia atrás")
    elif puntaje3 == 5:
            descripciones.append("Mantiene la sedestación sin ayuda y es capaz de tocar el suelo inclinándose hacia delante con cada mano por delante de los pies y volver a la posición inicial")
    elif puntaje3 == 6:
            descripciones.append("Mantiene la sedestación en un taburete sin ayuda y es capaz de tocar el suelo a ambos lados y volver al la posición de inicio")
    else:
            descripciones.append("Descripción no disponible")

    if puntaje4 == 0:
            descripciones.append("No es capaz de levantarse de ninguna manera")
    elif puntaje4 == 1:
            descripciones.append("Se levanta con ayuda del terapeuta utilizando cualquier método")
    elif puntaje4 == 2:
            descripciones.append("Se levanta con supervisión del terapeuta (El peso está distribuido asimétricamente y necesita sujetarse con las manos)")
    elif puntaje4 == 3:
            descripciones.append("Se levanta con peso distribuido simétricamente y sin apoyarse con las manos")
    elif puntaje4 == 4:
            descripciones.append("Se levanta y se mantiene de pie durante 5 segundos con las caderas y las rodilla extendidas y el peso simétricamente distribuido")
    elif puntaje4 == 5:
            descripciones.append("Se levanta y se sienta sin ayuda, con el peso simétricamente distribuido")
    elif puntaje4 == 6:
            descripciones.append("Se levanta y se sienta sin ayuda tres veces en 10 segundos con el peso distribuido simétricamente")
    else:
            descripciones.append("Descripción no disponible")

    if puntaje5 == 0:
            descripciones.append("No es capaz de dar ningún paso")
    elif puntaje5 == 1:
            descripciones.append("Se mantiene sobre el pie afecto y da el paso con el pie sano")
    elif puntaje5 == 2:
            descripciones.append("Camina con ayuda de una persona")
    elif puntaje5 == 3:
            descripciones.append("Camina 3 metros sin ayuda de una persona")
    elif puntaje5 == 4:
            descripciones.append("Camina 5 metros sin ayudas en 15 segundos")
    elif puntaje5 == 5:
            descripciones.append("Camina 10 metros sin ayuda, recoge del suelo un saco de arena pequeño, da la vuelta y vuelve en 25 segundos")
    elif puntaje5 == 6:
            descripciones.append("Sube y baja cuatro escalones (sin sujetarse en la baranda) tres veces en 35 segundos")
    else:
            descripciones.append("Descripción no disponible")

    if puntaje6 == 0:
            descripciones.append("En DS, no es capaz de protraer la cintura escapular con el hombro flexionado 90º")
    elif puntaje6 == 1:
            descripciones.append("En DS, protrae la cintura escapular con el hombro flexionado 90º. (El terapeuta coloca el brazo en posición y mantiene el codo extendido)")
    elif puntaje6 == 2:
            descripciones.append("En DS, mantiene el brazo con 90º de flexión de hombro durante 2 segundos")
    elif puntaje6 == 3:
            descripciones.append("En DS, mantiene el hombro flexionado 90º mientras flexiona y extiende el codo")
    elif puntaje6 == 4:
            descripciones.append("En sedestación, mantiene el brazo extendido hacia delante con flexión de hombro de 90º durante 2 segundos")
    elif puntaje6 == 5:
            descripciones.append("En sedestación, eleva el brazo extendido hacia delante con flexión de hombro de 90º, lo mantiene durante 10 segundos y lo desciende lentamente")
    elif puntaje6 == 6:
            descripciones.append("En bipedestación, mantiene la mano apoyada contra la pared, mientras gira el tronco hasta conseguir colocarse de perfil a la pared, con hombro abducido 90º")
    else:
            descripciones.append("Descripción no disponible")

    if puntaje7 == 0:
            descripciones.append("No realiza ningún movimiento con la muñeca o la mano")
    elif puntaje7 == 1:
            descripciones.append("En sedestación, con el antebrazo sobre una mesa, realiza extensión de muñeca")
    elif puntaje7 == 2:
            descripciones.append("En sedestación, con el codo flexionado al costado del tronco y el antebrazo sin apoyo, realiza pronosupinación de al menos 3/4 del recorrido")
    elif puntaje7 == 3:
            descripciones.append("En sedestación, eleva los brazos extendidos para alcanzar una pelota de 14 cm de diámetro y la baja")
    elif puntaje7 == 4:
            descripciones.append("En sedestación, mantiene el brazo extendido hacia delante con flexión de hombro de 90º durante 2 segundos")
    elif puntaje7 == 5:
            descripciones.append("En sedestación, toma un vaso de plástico y lo coloca al otro lado del cuerpo")
    elif puntaje7 == 6:
            descripciones.append("En sedestación, realiza oposición sucesiva del pulgar respecto cada dedo al menos 14 veces en 10 segundos")
    else:
            descripciones.append("Descripción no disponible")

    if puntaje8 == 0:
            descripciones.append("No es capaz de alcanzar un objeto sobre la mesa.")
    elif puntaje8 == 1:
            descripciones.append("Alcanza la tapa de una lapicera, situada al frente sobre la mesa, y la coloca cerca del cuerpo.")
    elif puntaje8 == 2:
            descripciones.append("Toma una bolita pequeña de un recipiente y la coloca en otro recipiente vacío.")
    elif puntaje8 == 3:
            descripciones.append("Es capaz de dibujar 10 líneas horizontales en 20 segundos.")
    elif puntaje8 == 4:
            descripciones.append("Es capaz de sujetar un lapiz y dibujar puntos sobre un papel  de forma rápida y consecutiva.")
    elif puntaje8 == 5:
            descripciones.append("Es capaz de tomar una cuchara de postre con líquido y llevársela a la boca.")
    elif puntaje8 == 6:
            descripciones.append("Es capaz de coger un peine y peinarse el pelo de la nuca.")
    else:
            descripciones.append("Descripción no disponible.")
    return descripciones


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        puntajes = {
            'puntaje1': int(request.form['puntaje1']),
            'puntaje2': int(request.form['puntaje2']),
            'puntaje3': int(request.form['puntaje3']),
            'puntaje4': int(request.form['puntaje4']),
            'puntaje5': int(request.form['puntaje5']),
            'puntaje6': int(request.form['puntaje6']),
            'puntaje7': int(request.form['puntaje7']),
            'puntaje8': int(request.form['puntaje8'])
        }
        descripciones = obtener_descripcion(**puntajes)
        descripcion_resultado = f'{descripciones[0]}; {descripciones[1]}; {descripciones[2]}; {descripciones[3]}; {descripciones[4]}; {descripciones[5]}; {descripciones[6]}; {descripciones[7]}'
        return render_template_string('''
            <h1>Escala Motora MAS</h1>
            <form action="{{ url_for('index') }}" method="POST">
                <h2>Puntajes:</h2>
                <label>Puntaje 1: <input type="number" name="puntaje1" min="0" max="6"></label><br>
                <label>Puntaje 2: <input type="number" name="puntaje2" min="0" max="6"></label><br>
                <label>Puntaje 3: <input type="number" name="puntaje3" min="0" max="6"></label><br>
                <label>Puntaje 4: <input type="number" name="puntaje4" min="0" max="6"></label><br>
                <label>Puntaje 5: <input type="number" name="puntaje5" min="0" max="6"></label><br>
                <label>Puntaje 6: <input type="number" name="puntaje6" min="0" max="6"></label><br>
                <label>Puntaje 7: <input type="number" name="puntaje7" min="0" max="6"></label><br>
                <label>Puntaje 8: <input type="number" name="puntaje8" min="0" max="6"></label><br>
                <input type="submit" value="Obtener descripción">
            </form>
            {% if descripcion_resultado %}
                <h2>Descripción:</h2>
                <p>{{ descripcion_resultado }}</p>
            {% endif %}
        ''', descripcion_resultado=descripcion_resultado)
    else:
        return render_template_string('''
            <h1>Escala Motora MAS</h1>
            <form action="{{ url_for('index') }}" method="POST">
                <h2>Puntajes:</h2>
                <label>Puntaje 1: <input type="number" name="puntaje1" min="0" max="6"></label><br>
                <label>Puntaje 2: <input type="number" name="puntaje2" min="0" max="6"></label><br>
                <label>Puntaje 3: <input type="number" name="puntaje3" min="0" max="6"></label><br>
                <label>Puntaje 4: <input type="number" name="puntaje4" min="0" max="6"></label><br>
                <label>Puntaje 5: <input type="number" name="puntaje5" min="0" max="6"></label><br>
                <label>Puntaje 6: <input type="number" name="puntaje6" min="0" max="6"></label><br>
                <label>Puntaje 7: <input type="number" name="puntaje7" min="0" max="6"></label><br>
                <label>Puntaje 8: <input type="number" name="puntaje8" min="0" max="6"></label><br>
                <input type="submit" value="Obtener descripción">
            </form>
        ''')



@app.route('/descripcion', methods=['POST'])
def descripcion():
    if request.method == 'POST':
        puntaje1 = int(request.form['puntaje1'])
        puntaje2 = int(request.form['puntaje2'])
        puntaje3 = int(request.form['puntaje3'])
        puntaje4 = int(request.form['puntaje4'])
        puntaje5 = int(request.form['puntaje5'])
        puntaje6 = int(request.form['puntaje6'])
        puntaje7 = int(request.form['puntaje7'])
        puntaje8 = int(request.form['puntaje8'])
        descripciones = obtener_descripcion(puntaje1, puntaje2, puntaje3, puntaje4, puntaje5, puntaje6, puntaje7, puntaje8)
        descripcion_resultado = f'{descripciones[0]}; {descripciones[1]}; {descripciones[2]}; {descripciones[3]}; {descripciones[4]}; {descripciones[5]}; {descripciones[6]}; {descripciones[7]}'

        return render_template_string('''
            <h1 class="title">Escala Motora MAS</h1>
            <form action="{{ url_for('descripcion') }}" method="POST">
                <label for="puntaje1" class="puntaje-label">Puntaje 1:</label>
        	<input type="number" name="puntaje1" id="puntaje1" required>
        	<!-- Repite el código anterior para puntaje2 hasta puntaje8 -->
        	<input type="submit" value="Obtener descripción">
            </form>
            {% if descripcion_resultado %}
                <h2>Descripción:</h2>
                <p>{{ descripcion_resultado }}</p>
            {% endif %}
        ''', descripcion_resultado=descripcion_resultado)


if __name__ == '__main__':
    app.run()
