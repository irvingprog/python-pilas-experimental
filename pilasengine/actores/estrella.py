# -*- encoding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilasengine.actores.actor import Actor


class Estrella(Actor):

    def iniciar(self):
        self.imagen = "estrella.png"
        self.radio_de_colision = 25

    def actualizar(self):
        pass

    def terminar(self):
        pass
