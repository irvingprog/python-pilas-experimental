# -*- encoding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar
import random

from pilasengine.actores.actor import Actor
from pilasengine.actores.texto import Texto
from pilasengine.actores.grupo import Grupo


from pilasengine import colores


class Actores(object):
    """Representa la forma de acceso y construcción de actores.

    Esta clase representa el objeto creado por pilas que
    se puede acceder escribiendo ``pilas.actores``. Desde aquí
    se puede acceder a los actores pre-diseñados de pilas y
    agregarlos a la escena.

    Por ejemplo, para crear una nave en pantalla podemos escribir:

        >>> nave = pilas.actores.Nave()

    """
    _lista_actores_personalizados = []

    def __init__(self, pilas):
        self.pilas = pilas

    def vincular(self, clase_del_actor):
        """Permite vincular una clase de actor con pilas.

        Esto permite de después el actor se pueda crear desde
        el módulo "pilas.actores".

        Por ejemplo, si tengo una clase ``MiActor`` lo puedo
        vincular con:

            >>> pilas.actores.vincular(MiActor)
            >>> mi_actor = pilas.actores.MiActor()

        """

        if not issubclass(clase_del_actor, Actor):
            raise Exception("Solo se pueden vincular clases que heredan de\
                            pilasengine.actores.Actor")

        def metodo_crear_actor(self):
            nuevo_actor = clase_del_actor(self.pilas)
            return nuevo_actor

        nombre_del_actor = clase_del_actor.__name__
        existe = getattr(self.__class__, nombre_del_actor, None)

        if existe:
            raise Exception("Lo siento, ya existe un actor con el nombre " +
                            nombre_del_actor)

        setattr(self.__class__, nombre_del_actor, metodo_crear_actor)
        Actores._lista_actores_personalizados.append(nombre_del_actor)

    def obtener_actores_personalizados(self):
        "Retorna una lista con todos los nombres de actores personalizados."
        return Actores._lista_actores_personalizados

    def eliminar_actores_personalizados(self):
        "Recorre todos los actores personalizados y los elimina."
        for x in Actores._lista_actores_personalizados:
            delattr(self.__class__, x)

        Actores._lista_actores_personalizados = []

    def agregar_actor(self, actor):
        """Agrega un actor a la escena actual.

        Este método se ejecuta internamente cada vez que se
        contruye un actor escribiendo algo como:

            >>> actor = pilas.actores.Actor()
        """
        if isinstance(actor, Actor):
            escena_actual = self.pilas.obtener_escena_actual()

            self.pilas.log("Agregando el actor", actor, "en la escena",
                           escena_actual)
            escena_actual.agregar_actor(actor)

            self.pilas.log("Iniciando el actor, llamando a actor.iniciar() \
                           del objeto ", actor)
            actor.iniciar()
        else:
            raise Exception("Solo puedes agregar actores de esta forma.")

        return actor

    def agregar_grupo(self, grupo):
        if isinstance(grupo, Grupo):
            escena_actual = self.pilas.obtener_escena_actual()
            self.pilas.log("Agregando el grupo", grupo, "a la escena",
                           escena_actual)
            escena_actual.agregar_grupo(grupo)
        else:
            raise Exception("Solo puedes agregar grupos de esta forma.")

        return grupo

    def Aceituna(self, x=0, y=0):
        return self._crear_actor('aceituna', 'Aceituna', x=x, y=y)

    def Mono(self, x=0, y=0):
        return self._crear_actor('mono', 'Mono', x=x, y=y)

    def Actor(self, x=0, y=0):
        return self._crear_actor('actor', 'Actor', x=x, y=y)

    def Palo(self, x=0, y=0):
        return self._crear_actor('palo', 'Palo', x=x, y=y)

    def Ejes(self, x=0, y=0):
        return self._crear_actor('ejes', 'Ejes', x=x, y=y)

    def Puntaje(self, x=0, y=0):
        return self._crear_actor('puntaje', 'Puntaje', x=x, y=y)

    def Pingu(self, x=0, y=0):
        return self._crear_actor('pingu', 'Pingu', x=x, y=y)

    def Pizarra(self, x=0, y=0, ancho=None, alto=None):
        return self._crear_actor('pizarra', 'Pizarra', x=x, y=y,
                                  ancho=ancho, alto=alto)

    def Martian(self, x=0, y=0):
        return self._crear_actor('martian', 'Martian', x=x, y=y)

    def Tortuga(self, x=0, y=0, dibuja=True):
        return self._crear_actor('tortuga', 'Tortuga', x=x, y=y, dibuja=dibuja)

    def CursorMano(self, x=0, y=0):
        return self._crear_actor('cursor_mano', 'CursorMano', x=x, y=y)

    def CursorDisparo(self, x=0, y=0, usar_el_mouse=True):
        return self._crear_actor('cursor_disparo', 'CursorDisparo', x=x, y=y, usar_el_mouse=usar_el_mouse)

    def EstrellaNinja(self, x=0, y=0):
        return self._crear_actor('estrella_ninja', 'EstrellaNinja', x=x, y=y)

    def Menu(self, opciones=[], x=0, y=0, fuente=None,
             color_normal=colores.gris, color_resaltado=colores.blanco):
        return self._crear_actor('menu', 'Menu', x=x, y=y, opciones=opciones,
                                 fuente=fuente, color_normal=color_normal,
                                 color_resaltado=color_resaltado)

    def Opcion(self, texto="", x=0, y=0,
                 funcion_a_invocar=None,argumentos=None,fuente=None,
                 color_normal=colores.gris,
                 color_resaltado=colores.blanco):
        return self._crear_actor("opcion", "Opcion", x=x, y=y,
                                 texto=texto,
                                 funcion_a_invocar=funcion_a_invocar,
                                 argumentos=argumentos, fuente=fuente,
                                 color_normal=color_normal,
                                 color_resaltado=color_resaltado)

    def _crear_actor(self, modulo, clase, *k, **kw):
        import importlib

        referencia_a_modulo = importlib.import_module('pilasengine.actores.' + modulo)
        referencia_a_clase = getattr(referencia_a_modulo, clase)

        try:
            nuevo_actor = referencia_a_clase(self.pilas, *k, **kw)
        except TypeError, error:
            mensaje_extendido = ", en clase %s con los argumentos: %s %s" %(str(referencia_a_clase), str(k), str(kw))
            raise TypeError(str(error) + mensaje_extendido)

        # Importante: cuando se inicializa el actor, el método __init__
        #             realiza una llamada a pilas.actores.agregar_actor
        #             para vincular el actor a la escena.
        return nuevo_actor

    def MensajeError(self, error, descripcion):
        return self._crear_actor('mensaje_error', 'MensajeError', error,
                                 descripcion)

    def Animacion(self, grilla, ciclica=False, x=0, y=0, velocidad=10):
        return self._crear_actor('animacion', 'Animacion', grilla=grilla,
                                 ciclica=ciclica, x=x, y=y, velocidad=velocidad)

    def Grupo(self):
        import grupo
        nuevo_grupo = grupo.Grupo(self.pilas)
        return self.agregar_grupo(nuevo_grupo)

    def Dialogo(self):
        return self._crear_actor('dialogo', 'Dialogo', 0, 0)

    def Energia(self, x=0, y=0, progreso=100, ancho=200, alto=30,
                color_relleno=colores.amarillo, con_sombra=True,
                con_brillo=True):
        return self._crear_actor('energia', 'Energia', x=x, y=y,
                                 progreso=progreso, ancho=ancho, alto=alto,
                                 color_relleno=color_relleno,
                                 con_sombra=con_sombra,
                                 con_brillo=con_brillo)

    def Boton(self, x=0, y=0,
                ruta_normal='boton/boton_normal.png',
                ruta_press='boton/boton_press.png',
                ruta_over='boton/boton_over.png'):
        return self._crear_actor('boton', 'Boton', x=x, y=y,
                                 ruta_normal=ruta_normal,
                                 ruta_press=ruta_press,
                                 ruta_over=ruta_over)

    def Banana(self, x=0, y=0):
        return self._crear_actor('banana', 'Banana', x=x, y=y)

    def Bala(self, x=0, y=0, rotacion=0, velocidad_maxima=9,
             angulo_de_movimiento=90):
        return self._crear_actor('bala', 'Bala', x=x, y=y, rotacion=rotacion,
                                 velocidad_maxima=velocidad_maxima,
                                 angulo_de_movimiento=angulo_de_movimiento)

    def Bomba(self, x=0, y=0):
        return self._crear_actor('bomba', 'Bomba', x=x, y=y)

    def Explosion(self, x=0, y=0):
        return self._crear_actor('explosion', 'Explosion', x=x, y=y)

    def Estrella(self, x=0, y=0):
        return self._crear_actor('estrella', 'Estrella', x=x, y=y)

    def Fantasma(self, x=0, y=0):
        return self._crear_actor('fantasma', 'Fantasma', x=x, y=y)

    def Humo(self, x=0, y=0):
        return self._crear_actor('humo', 'Humo', x=x, y=y)

    def Manzana(self, x=0, y=0):
        return self._crear_actor('manzana', 'Manzana', x=x, y=y)

    def Ovni(self, x=0, y=0):
        return self._crear_actor('ovni', 'Ovni', x=x, y=y)

    def Nave(self, x=0, y=0):
        return self._crear_actor('nave', 'Nave', x=x, y=y)

    def NaveKids(self, x=0, y=0):
        return self._crear_actor('nave_kids', 'NaveKids', x=x, y=y)

    def Planeta(self, x=0, y=0):
        return self._crear_actor('planeta', 'Planeta', x=x, y=y)

    def Piedra(self, x=0, y=0):
        return self._crear_actor('piedra', 'Piedra', x=x, y=y)

    def Pelota(self, x=0, y=0):
        return self._crear_actor('pelota', 'Pelota', x=x, y=y)

    def Caja(self, x=0, y=0):
        return self._crear_actor('caja', 'Caja', x=x, y=y)

    def Zanahoria(self, x=0, y=0):
        return self._crear_actor('zanahoria', 'Zanahoria', x=x, y=y)

    def Cooperativista(self, x=0, y=0):
        return self._crear_actor('cooperativista', 'Cooperativista', x=x, y=y)

    def Pacman(self, x=0, y=0):
        return self._crear_actor('pacman', 'Pacman', x=x, y=y)

    def Moneda(self, x=0, y=0):
        return self._crear_actor('moneda', 'Moneda', x=x, y=y)

    def Globo(self, texto, x=0, y=0, dialogo=None, avance_con_clicks=True,
              autoeliminar=False, ancho_globo=0, alto_globo=0):
        return self._crear_actor('globo', 'Globo', texto=texto, x=x, y=y,
                                 dialogo=dialogo,
                                 avance_con_clicks=avance_con_clicks,
                                 autoeliminar=autoeliminar,
                                 ancho_globo=ancho_globo,
                                 alto_globo=alto_globo)

    def Texto(self, cadena_de_texto="Sin texto", magnitud=20, vertical=False,
              fuente=None, fijo=True, ancho=0, x=0, y=0):
        import texto
        nuevo_actor = texto.Texto(self.pilas, cadena_de_texto, magnitud,
                                  vertical, fuente, fijo, ancho, x, y)
        return nuevo_actor

    def TextoInferior(self, texto="Sin texto", magnitud=20, retraso=5):
        import texto_inferior
        nuevo_actor = texto_inferior.TextoInferior(self.pilas, texto, magnitud,
                                                   retraso=retraso)
        return nuevo_actor

    def DeslizadorHorizontal(self, x=0, y=0, min=0, max=100, etiqueta=''):
        return self._crear_actor('deslizador_horizontal',
                                 'DeslizadorHorizontal',
                                 x=x, y=y, min=min, max=max,
                                 etiqueta=etiqueta)

    def Emisor(self, x=0, y=0):
        return self._crear_actor('emisor', 'Emisor', x=x, y=y)

    def Controlador(self, x=0, y=0):
        return self._crear_actor('controlador', 'Controlador', x=x, y=y)

    def ManejadorPropiedad(self, x, y, actor, propiedad, minimo, maximo):
        return self._crear_actor('manejador_propiedad',
                                 'ManejadorPropiedad',
                                 x, y,
                                 actor=actor, propiedad=propiedad,
                                 min=minimo, max=maximo)

    def Particula(self, emisor, x=0, y=0, dx=0, dy=0, imagen="particula.png", vida=1):
        actor = self._crear_actor('particula', 'Particula', emisor=emisor,
                                  x=x, y=y,
                                  dx=dx, dy=dy,
                                  imagen=imagen,
                                  vida=vida)
        return actor

    def fabricar(self, clase, cantidad):
        grupo = self.Grupo()
        ancho_ventana, alto_ventana = self.pilas.widget.obtener_area()

        for i in xrange(cantidad):
            _x = random.randint(-ancho_ventana/2, ancho_ventana/2)
            _y = random.randint(-alto_ventana/2, alto_ventana/2)
            grupo.agregar(clase(self.pilas, x=_x, y=_y))

        return grupo



from pilasengine.actores.bomba import Bomba
from pilasengine.actores.aceituna import Aceituna
from pilasengine.actores.actor import ActorEliminadoException
from pilasengine.actores.actor import ActorEliminado
from pilasengine.actores.actor import Actor
from pilasengine.actores.animacion import Animacion
from pilasengine.actores.animado import Animado
from pilasengine.actores.banana import Banana
from pilasengine.actores.bomba import Bomba
from pilasengine.actores.caja import Caja
from pilasengine.actores.controlador import Controlador
from pilasengine.actores.cooperativista import Cooperativista
from pilasengine.actores.cooperativista import Esperando
from pilasengine.actores.cooperativista import Caminando
from pilasengine.actores.cooperativista import DecirOk
from pilasengine.actores.deslizador_horizontal import DeslizadorHorizontal
from pilasengine.actores.dialogo import Dialogo
from pilasengine.actores.ejes import Ejes
from pilasengine.actores.emisor import Emisor
from pilasengine.actores.energia import Energia
from pilasengine.actores.estrella import Estrella
from pilasengine.actores.estudiante import Estudiante
from pilasengine.actores.explosion import Explosion
from pilasengine.actores.fantasma import Fantasma
from pilasengine.actores.globo import Globo
from pilasengine.actores.grupo import Grupo
from pilasengine.actores.humo import Humo
from pilasengine.actores.manejador_propiedad import ManejadorPropiedad
from pilasengine.actores.manzana import Manzana
from pilasengine.actores.martian import Martian
from pilasengine.actores.martian import Esperando
from pilasengine.actores.martian import Caminando
from pilasengine.actores.martian import Saltando
from pilasengine.actores.martian import Disparar
from pilasengine.actores.mensaje_error import MensajeError
from pilasengine.actores.menu import Menu
from pilasengine.actores.moneda import Moneda
from pilasengine.actores.mono import Mono
from pilasengine.actores.nave import Nave
from pilasengine.actores.navekids import NaveKids
from pilasengine.actores.opcion import Opcion
from pilasengine.actores.ovni import Ovni
from pilasengine.actores.pacman import Pacman
from pilasengine.actores.palo import Palo
from pilasengine.actores.particula import Particula
from pilasengine.actores.pelota import Pelota
from pilasengine.actores.piedra import Piedra
from pilasengine.actores.pingu import Pingu
from pilasengine.actores.pingu import Esperando
from pilasengine.actores.pingu import Caminando
from pilasengine.actores.pingu import Saltando
from pilasengine.actores.pizarra import Pizarra
from pilasengine.actores.planeta import Planeta
from pilasengine.actores.puntaje import Puntaje
from pilasengine.actores.texto import Texto
from pilasengine.actores.texto_inferior import TextoInferior
from pilasengine.actores.tortuga import Tortuga
from pilasengine.actores.zanahoria import Zanahoria
