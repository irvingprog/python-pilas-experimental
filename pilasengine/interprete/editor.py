# -*- encoding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar
import codecs
import time

from PyQt4.Qt import (QFrame, QWidget, QHBoxLayout,
                        QVBoxLayout, QPainter, QSize)
from PyQt4.QtGui import (QTextEdit, QTextCursor, QFileDialog,
                         QIcon, QPushButton, QCursor, QMessageBox)
from PyQt4.QtCore import Qt
from PyQt4 import QtCore

import editor_base
import pilasengine

CONTENIDO = u"""import pilasengine

pilas = pilasengine.iniciar()

mono = pilas.actores.Mono()

# Algunas transformaciones:
# (Pulsá el botón derecho del
#  mouse sobre alguna de las
#  sentencias)

mono.x = 0
mono.y = 0
mono.escala = 1.0
mono.rotacion = 0

pilas.ejecutar()"""


class WidgetEditor(QWidget):

    class NumberBar(QWidget):

        def __init__(self, *args):
            QWidget.__init__(self, *args)
            self.edit = None
            # This is used to update the width of the control.
            # It is the highest line that is currently visible.
            self.highest_line = 0

        def setTextEdit(self, edit):
            self.edit = edit

        def update(self, *args):
            '''
            Updates the number bar to display the current set of numbers.
            Also, adjusts the width of the number bar if necessary.
            '''
            # The + 4 is used to compensate for the current line being bold.
            width = self.fontMetrics().width(str(self.highest_line)) + 4

            if self.width() != width:
                self.setFixedWidth(width + 15)

            QWidget.update(self, *args)

        def paintEvent(self, event):
            contents_y = self.edit.verticalScrollBar().value()
            page_bottom = contents_y + self.edit.viewport().height()
            font_metrics = self.fontMetrics()

            painter = QPainter(self)

            line_count = 0

            # Iterate over all text blocks in the document.
            block = self.edit.document().begin()

            while block.isValid():
                line_count += 1

                # The top left position of the block in the document
                position = self.edit.document().documentLayout().blockBoundingRect(block).topLeft()

                # Check if the position of the block is out side of the visible
                # area.
                if position.y() > page_bottom:
                    break

                # Draw the line number right justified at the y position of the
                # line. 3 is a magic padding number. drawText(x, y, text).
                painter.drawText(-5 + self.width() - font_metrics.width(str(line_count)) - 3,
                                round(position.y()) - contents_y + font_metrics.ascent(),
                                str(line_count))

                block = block.next()

            self.highest_line = line_count
            painter.end()

            QWidget.paintEvent(self, event)


    def __init__(self, main, interpreterLocals, ventana_interprete, *args):
        QWidget.__init__(self, *args)

        self.editor = Editor(self, interpreterLocals, ventana_interprete)
        self.editor.setFrameStyle(QFrame.NoFrame)
        self.editor.setAcceptRichText(False)

        self.number_bar = self.NumberBar()
        self.number_bar.setTextEdit(self.editor)

        # Layout principal: envuelve al editor y layout de acciones
        vbox = QVBoxLayout(self)
        vbox.setSpacing(0)
        vbox.setMargin(0)

        hbox_buttons = QHBoxLayout()
        hbox_buttons.setSpacing(0)
        hbox_buttons.setMargin(0)
        vbox.addLayout(hbox_buttons)

        # Botón abrir del editor
        self.button_open = QPushButton(self)
        self.button_open.setMaximumSize(QSize(20, 20))
        self.button_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_open.setFlat(True)
        #self.guardar_button.setObjectName(_fromUtf8("guardar_button"))
        self.set_icon(self.button_open, 'iconos/abrir.png')
        self.button_open.connect(self.button_open,
                                   QtCore.SIGNAL("clicked()"),
                                   self.editor.abrir_archivo_con_dialogo)
        hbox_buttons.addWidget(self.button_open)

        # Botón guardar del editor
        self.button_save = QPushButton(self)
        self.button_save.setMaximumSize(QSize(20, 20))
        self.button_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_save.setFlat(True)
        #self.guardar_button.setObjectName(_fromUtf8("guardar_button"))
        self.set_icon(self.button_save, 'iconos/guardar.png')
        self.button_save.connect(self.button_save,
                                   QtCore.SIGNAL("clicked()"),
                                   self.editor.guardar_contenido_con_dialogo)
        hbox_buttons.addWidget(self.button_save)


        # Layout para el Editor y barra de numeros
        hbox_editor = QHBoxLayout()
        hbox_editor.setSpacing(0)
        hbox_editor.setMargin(0)
        hbox_editor.addWidget(self.number_bar)
        hbox_editor.addWidget(self.editor)
        vbox.addLayout(hbox_editor)

        self.editor.installEventFilter(self)
        self.editor.viewport().installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj in (self.editor, self.editor.viewport()):
            self.number_bar.update()
            return False
        return QFrame.eventFilter(obj, event)

    def set_icon(self, boton, ruta):
        icon = QIcon()
        archivo = pilasengine.utils.obtener_ruta_al_recurso(ruta)
        icon.addFile(archivo, QSize(), QIcon.Normal, QIcon.Off)
        boton.setIcon(icon)
        boton.setText('')


class Editor(editor_base.EditorBase):
    """Representa el editor de texto que aparece en el panel derecho.

    El editor soporta autocompletado de código y resaltado de sintáxis.
    """

    def __init__(self, main, interpreterLocals, ventana_interprete):
        super(Editor, self).__init__()
        self.interpreterLocals = interpreterLocals
        self.insertPlainText(CONTENIDO)
        self.setLineWrapMode(QTextEdit.NoWrap)
        self._cambios_sin_guardar = False
        self.main = main
        self.ventana_interprete = ventana_interprete

    def keyPressEvent(self, event):
        "Atiene el evento de pulsación de tecla."
        self._cambios_sin_guardar = True

        if editor_base.EditorBase.keyPressEvent(self, event):
            return None

        # Elimina los pares de caracteres especiales si los encuentra
        if event.key() == Qt.Key_Backspace:
            self._eliminar_pares_de_caracteres(es_consola=False)

        if event.key() == Qt.Key_Tab:
            tc = self.textCursor()
            tc.insertText("    ")
        else:
            if self.autocomplete(event):
                return None

            return QTextEdit.keyPressEvent(self, event)

    def tiene_cambios_sin_guardar(self):
        return self._cambios_sin_guardar

    def _get_current_line(self):
        "Obtiene la linea en donde se encuentra el cursor."
        tc = self.textCursor()
        tc.select(QTextCursor.LineUnderCursor)
        return tc.selectedText()

    def _get_position_in_block(self):
        tc = self.textCursor()
        position = tc.positionInBlock() - 1
        return position

    def cargar_contenido_desde_archivo(self, ruta):
        "Carga todo el contenido del archivo indicado por ruta."
        with codecs.open(unicode(ruta), 'r', 'utf-8') as archivo:
            contenido = archivo.read()
        self.setText(contenido)

    def _restaurar_rutina_de_redibujado_original(self, paint_event_original):
        pilas = self.interpreterLocals['pilas']
        pilas.reiniciar()
        widget = pilas.obtener_widget()
        widget.__class__.paintEvent = paint_event_original

    def abrir_dialogo_cargar_archivo(self):
        return QFileDialog.getOpenFileName(self, "Abrir Archivo",
                                   self.nombre_de_archivo_sugerido,
                                   "Archivos python (*.py)",
                                   options=QFileDialog.DontUseNativeDialog)

    def abrir_archivo_con_dialogo(self):
        self.quiere_perder_cambios()

        ruta = self.abrir_dialogo_cargar_archivo()

        if ruta:
            self.cargar_contenido_desde_archivo(ruta)
            self.nombre_de_archivo_sugerido = ruta
            self._cambios_sin_guardar = False
            self.ejecutar()

    def quiere_perder_cambios(self):
        if self.tiene_cambios_sin_guardar():
            if not self.mensaje_quiere_perder_cambios():
                self.guardar_contenido_con_dialogo()

    def mensaje_quiere_perder_cambios(self):
        """Realizar una consulta usando un cuadro de dialogo simple.
        Este método retorna True si el usuario acepta la pregunta."""

        titulo = u"Se perderán los cambios sin guardar"
        mensaje = u"Se perderán los cambios sin guardar... ¿Quieres perder los cambios del editor realmente?"

        # False si respuesta es "Si", True si la respuesta es "No"
        respuesta = QMessageBox.question(self, titulo, mensaje, "Si", "No")

        return (respuesta == False)

    def ejecutar(self):
        texto = unicode(self.document().toPlainText())
        self.ventana_interprete.ejecutar_codigo_como_string(texto)

    def guardar_contenido_con_dialogo(self):
        ruta = self.abrir_dialogo_guardar_archivo()

        if ruta:
            self.guardar_contenido_en_el_archivo(ruta)
            self._cambios_sin_guardar = False
            self.nombre_de_archivo_sugerido = ruta
            self.mensaje_contenido_guardado()

    def obtener_contenido(self):
        return unicode(self.document().toPlainText())




