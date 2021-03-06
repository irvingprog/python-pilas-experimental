# -*- encoding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar


from pilasengine.actores.deslizador_horizontal import DeslizadorHorizontal
from pilasengine import colores


class ManejadorPropiedad(DeslizadorHorizontal):

    def __init__(self, pilas, x, y, actor, propiedad, min, max):
        valor_inicial = getattr(actor, propiedad)
        DeslizadorHorizontal.__init__(self, pilas, x, y, min, max, propiedad, valor_inicial=valor_inicial)
        self.actor = actor
        self.propiedad = propiedad

    def iniciar(self):
        DeslizadorHorizontal.iniciar(self)
        self.conectar(self.cuando_cambia)

    def cuando_cambia(self, valor):
        setattr(self.actor, self.propiedad, valor)