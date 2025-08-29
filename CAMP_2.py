import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros del campo de potencial
K_atractivo = 0.5
K_repulsivo = 3.0
radio_repulsion = 3.0

# Función para calcular el campo de potencial
def calcular_potencial(posicion_agente, objetivo, obstaculos, epsilon=0.25):
    # Potencial de atracción hacia el objetivo
    potencial_atractivo = 0.5 * K_atractivo * np.linalg.norm(objetivo - posicion_agente)**2
    
    # Potencial de repulsión de los obstáculos
    potencial_repulsivo = 0
    for obstaculo in obstaculos:
        distancia = np.linalg.norm(posicion_agente - obstaculo)
        if 1 <= distancia < radio_repulsion:
            potencial_repulsivo += 0.5 * K_repulsivo * (1 / distancia - 1 / radio_repulsion)**2
        elif epsilon < distancia < 1:
            potencial_repulsivo += 0.5 * K_repulsivo * (1 / distancia - 1 / radio_repulsion)
        else:
            potencial_repulsivo += 0

    # Potencial total
    return potencial_atractivo + potencial_repulsivo

# Función para calcular gradiente del campo de potencial
def calcular_gradiente(posicion_agente, objetivo, obstaculos, epsilon=0.15):
    gradiente = np.zeros(2)
    for i in range(2):
        delta_pos = np.zeros(2)
        delta_pos[i] = epsilon
        potencial_pos = calcular_potencial(posicion_agente + delta_pos, objetivo, obstaculos)
        potencial_neg = calcular_potencial(posicion_agente - delta_pos, objetivo, obstaculos)
        gradiente[i] = (potencial_pos - potencial_neg) / (2 * epsilon)
    return gradiente

# Clase para el agente BDI
class AgenteBDI:
    def __init__(self, posicion_inicial, objetivo, obstaculos):
        self.posicion = posicion_inicial
        self.objetivo = objetivo
        self.obstaculos = obstaculos
        self.estado = "navegando"
        self.contador_atascado = 0
        self.historial_posiciones = [posicion_inicial.copy()]
        self.direccion_escape = None
        self.contador_escape = 0
        self.puntos_atasco = []
        self.contador_evitacion = 0
        self.direccion_evitacion = None
        
    def actualizar_creencias(self):
        if len(self.historial_posiciones) > 10:
            desplazamiento = np.linalg.norm(self.historial_posiciones[-1] - self.historial_posiciones[-10])
            if desplazamiento < 0.5:
                self.estado = "atascado"
                self.contador_atascado += 1
                es_nuevo_atasco = True
                for punto in self.puntos_atasco:
                    if np.linalg.norm(self.posicion - punto) < 1.0:
                        es_nuevo_atasco = False
                        break
                if es_nuevo_atasco:
                    self.puntos_atasco.append(self.posicion.copy())
            else:
                self.estado = "navegando"
                self.contador_atascado = 0
                
        if np.linalg.norm(self.posicion - self.objetivo) < 0.5:
            self.estado = "completado"
            
        for punto in self.puntos_atasco:
            if np.linalg.norm(self.posicion - punto) < 2.0:
                self.estado = "evitando"
                break
    
    def generar_deseos(self):
        if self.estado == "completado":
            return "permanecer"
        elif self.estado == "atascado" and self.contador_atascado > 5:
            return "escapar"
        elif self.estado == "evitando":
            return "evitar"
        else:
            return "navegar"
    
    def planificar_intenciones(self, deseo):
        if deseo == "permanecer":
            return np.zeros(2)
        elif deseo == "escapar":
            punto_mas_cercano = None
            distancia_minima = float('inf')
            for punto in self.puntos_atasco:
                distancia = np.linalg.norm(self.posicion - punto)
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    punto_mas_cercano = punto
            if punto_mas_cercano is not None:
                direccion_alejamiento = self.posicion - punto_mas_cercano
                if np.linalg.norm(direccion_alejamiento) < 0.1:
                    angulo = np.random.uniform(0, 2*np.pi)
                    direccion_alejamiento = np.array([np.cos(angulo), np.sin(angulo)])
                else:
                    direccion_alejamiento = direccion_alejamiento / np.linalg.norm(direccion_alejamiento)
                direccion_objetivo = self.objetivo - self.posicion
                if np.linalg.norm(direccion_objetivo) > 0:
                    direccion_objetivo = direccion_objetivo / np.linalg.norm(direccion_objetivo)
                direccion_combinada = 0.6 * direccion_alejamiento + 0.4 * direccion_objetivo
                direccion_combinada = direccion_combinada / np.linalg.norm(direccion_combinada)
                self.direccion_escape = direccion_combinada
                self.contador_escape = 0
            else:
                if self.direccion_escape is None or self.contador_escape > 20:
                    angulo = np.random.uniform(0, 2*np.pi)
                    self.direccion_escape = np.array([np.cos(angulo), np.sin(angulo)])
                    self.contador_escape = 0
                else:
                    self.contador_escape += 1
            return self.direccion_escape * 0.3
        elif deseo == "evitar":
            puntos_cercanos = []
            for punto in self.puntos_atasco:
                if np.linalg.norm(self.posicion - punto) < 2.0:
                    puntos_cercanos.append(punto)
            direccion_evitacion = np.zeros(2)
            for punto in puntos_cercanos:
                direccion_punto = self.posicion - punto
                if np.linalg.norm(direccion_punto) > 0:
                    direccion_punto = direccion_punto / np.linalg.norm(direccion_punto)
                    peso = 1.0 / (0.1 + np.linalg.norm(self.posicion - punto))
                    direccion_evitacion += peso * direccion_punto
            if np.linalg.norm(direccion_evitacion) > 0:
                direccion_evitacion = direccion_evitacion / np.linalg.norm(direccion_evitacion)
            direccion_objetivo = self.objetivo - self.posicion
            if np.linalg.norm(direccion_objetivo) > 0:
                direccion_objetivo = direccion_objetivo / np.linalg.norm(direccion_objetivo)
            direccion_combinada = 0.5 * direccion_evitacion + 0.5 * direccion_objetivo
            if np.linalg.norm(direccion_combinada) > 0:
                direccion_combinada = direccion_combinada / np.linalg.norm(direccion_combinada)
            return direccion_combinada * 0.15
        else:
            return -calcular_gradiente(self.posicion, self.objetivo, self.obstaculos) * 0.1
    
    def ejecutar(self):
        """Ejecuta un ciclo completo BDI"""
        self.actualizar_creencias()
        deseo = self.generar_deseos()
        movimiento = self.planificar_intenciones(deseo)

        # Proponer nueva posición
        nueva_posicion = self.posicion + movimiento

        # Verificación de colisión con obstáculos
        colision = False
        for obstaculo in self.obstaculos:
            if np.linalg.norm(nueva_posicion - obstaculo) < 0.5:  # margen de seguridad
                colision = True
                break

        if not colision:
            self.posicion = nueva_posicion
        else:
            # Si choca, prueba un pequeño desvío aleatorio
            angulo = np.random.uniform(0, 2*np.pi)
            self.posicion += 0.1 * np.array([np.cos(angulo), np.sin(angulo)])

        self.historial_posiciones.append(self.posicion.copy())
        return self.posicion, calcular_potencial(self.posicion, self.objetivo, self.obstaculos)


# Configuración inicial de la visualización
fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 5))

agente_posicion = np.array([1.0, 1.0])
objetivo = np.array([12, 12])
obstaculos = np.array([[2, 2],[2, 3], [2, 4],[2, 5],[2, 6],[2, 7],[2, 8],[2, 9], [2, 10],[10, 10], 
                        [10, 9],[10, 8],[10, 7],[10, 6],[10, 5],[10, 4],[10, 3],[10, 2], 
                        [9, 2], [9, 3],[9, 4],[9, 5],[9, 6],[9, 7],[9, 8],[9, 9], 
                        [3, 9],[3, 8],[3, 7],[3, 6],[3, 5],[3, 4],[3, 3], [3, 2],
                        [4,9],[5,9],[6,9],[7,9],[8,9],[3,10],[4,10],[5,10],[6,10],
                        [7,10],[8,10],[9,10]])

agente = AgenteBDI(agente_posicion, objetivo, obstaculos)
historial_energia_potencial = []

def update(frame):
    global historial_energia_potencial
    nueva_posicion, energia_potencial = agente.ejecutar()
    historial_energia_potencial.append(energia_potencial)
    
    ax.clear()
    ax.scatter(nueva_posicion[0], nueva_posicion[1], color='red', marker='o', s=200, label='Agente')
    ax.scatter(objetivo[0], objetivo[1], color='green', marker='x', s=100, label='Objetivo')
    
    for obstaculo in obstaculos:
        ax.scatter(obstaculo[0], obstaculo[1], color='black', marker='s', s=100)
    
    for i, punto in enumerate(agente.puntos_atasco):
        ax.scatter(punto[0], punto[1], color='orange', marker='*', s=150, label='Punto de atasco' if i == 0 else "")
        circulo = plt.Circle((punto[0], punto[1]), 2.0, color='orange', fill=False, alpha=0.3, linestyle='--')
        ax.add_patch(circulo)
    
    historial = np.array(agente.historial_posiciones)
    ax.plot(historial[:, 0], historial[:, 1], 'b--', alpha=0.5)
    
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    ax.set_title(f'Agente BDI - Estado: {agente.estado}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    
    ax2.clear()
    ax2.plot(historial_energia_potencial, label='Energía Potencial')
    ax2.set_title('Evolución de la Energía Potencial')
    ax2.set_xlabel('Iteración')
    ax2.set_ylabel('Energía Potencial')
    ax2.legend()

ani = FuncAnimation(fig, update, frames=500, interval=200)
plt.show()