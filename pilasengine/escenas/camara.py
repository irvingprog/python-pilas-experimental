# -*- encoding: utf -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar
import random


class Camara(object):
    """Representa la cámara principal de la escena.

    El objeto cámara permite desplazarse, hacer movimientos
    de automento, alejamiento e incluso rotaciones.

    Este objeto se puede acceder usando el atributos pilas.carama, por
    ejemplo:

        >>> pilas.camara.escala = [2]
        >>> pilas.camara.rotacion = [45]
    """

    def __init__(self, pilas, escena):
        self.pilas = pilas
        self.escena = escena
        self._x = 0
        self._y = 0
        self._escala = 1
        self._rotacion = 0
        self.cuando_mueve_camara_x = pilas.eventos.Evento('cuando_mueve_camara_x')
        self.cuando_mueve_camara_y = pilas.eventos.Evento('cuando_mueve_camara_y')
        self.cuando_mueve_camara_x.conectar(self.cuando_cambia_x)
        self.cuando_mueve_camara_y.conectar(self.cuando_cambia_y)

    def aplicar_transformaciones_completas(self, painter):
        centro_x, centro_y = self.pilas.obtener_centro_fisico()
        painter.translate(centro_x, centro_y)
        painter.scale(self._escala, self._escala)
        painter.rotate(-self._rotacion)

    def aplicar_translacion(self, painter):
        centro_x, centro_y = self.pilas.obtener_centro_fisico()
        painter.translate(centro_x, centro_y)

    def vibrar(self, intensidad=1, tiempo=0.5):
        valores = [x*intensidad for x in [-4, -3, -2, 2, 3, 4] * int(tiempo + 1)]
        cantidad_de_valores = float(len(valores)) + 1

        random.shuffle(valores)
        self.x = valores + [0], tiempo/cantidad_de_valores

        random.shuffle(valores)
        self.y = valores + [0], tiempo/cantidad_de_valores

    def obtener_escala(self):
        return self._escala

    def definir_escala(self, valor):
        self.pilas.utils.interpretar_propiedad_numerica(self, 'escala', valor)

    def obtener_rotacion(self):
        return self._rotacion

    def definir_rotacion(self, valor):
        self.pilas.utils.interpretar_propiedad_numerica(self, 'rotacion', valor)

    def obtener_x(self):
        return self._x

    def definir_x(self, valor):
        self.pilas.utils.interpretar_propiedad_numerica(self, 'x', valor,
                                                        self.cuando_mueve_camara_x,
                                                        self.cuando_termina)

    def cuando_cambia_x(self, evento):
        self.pilas.eventos.mueve_camara.emitir(x=evento.propiedad, y=self.y,
                                               dx=evento.propiedad-self.x,
                                               dy=0)

    def obtener_y(self):
        return self._y

    def definir_y(self, valor):
        self.pilas.utils.interpretar_propiedad_numerica(self, 'y', valor,
                                                        self.cuando_mueve_camara_y)

    def cuando_cambia_y(self, evento):
        self.pilas.eventos.mueve_camara.emitir(x=self.x, y=evento.propiedad,
                                               dx=0, dy=evento.propiedad-self.y)

    escala = property(obtener_escala, definir_escala,
                      doc="Cambia el escala o cercanía de la cámara.")
    rotacion = property(obtener_rotacion, definir_rotacion,
                        doc="Cambia la rotacion de la pantalla.")
    x = property(obtener_x, definir_x,
                 doc="Cambia la posición x de la pantalla.")
    y = property(obtener_y, definir_y,
                 doc="Cambia la posición y de la pantalla.")