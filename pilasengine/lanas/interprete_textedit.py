# -*- encoding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar
import code
import sys
import inspect
import re

import os
os.environ['lanas'] = 'enabled'

from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import QTextEdit

from ..interprete import editor_base
import io


class InterpreteTextEdit(editor_base.EditorBase):
    """Representa el widget del interprete.

    Esta instancia tiene como atributo "self.ventana" al
    al QWidget representado por la clase Ventana.
    """

    def __init__(self, parent):
        super(InterpreteTextEdit,  self).__init__()
        self.ventana = parent
        self.ventana_interprete = self.ventana.ventana_interprete
        self.stdout_original = sys.stdout
        sys.stdout = io.NormalOutput(self)
        sys.stderr = io.ErrorOutput(self)
        self.refreshMarker = False
        self.multiline = False
        self.command = ''
        self.history = []
        self.historyIndex = -1
        self.interpreterLocals = {}

        # setting the color for bg and text
        palette = QPalette()
        #palette.setColor(QPalette.Base, QColor(20, 20, 20))
        palette.setColor(QPalette.Text, QColor(0, 0, 0))
        self.setPalette(palette)

        """
        if sys.platform == 'darwin':
            self._set_font_size(15)
        else:
            self._set_font_size(14)
        """

        self.marker()
        self.setUndoRedoEnabled(False)
        self.setContextMenuPolicy(Qt.NoContextMenu)

        self.timer_cursor = QTimer()
        self.timer_cursor.start(1000)
        self.timer_cursor.timeout.connect(self.marker_si_es_necesario)

    def insertFromMimeData(self, source):
        QTextEdit.insertPlainText(self, source.text())

    def canInsertFromMimeData(self, *k):
        return False

    def imprimir_linea(self, linea):
        self.insertPlainText(linea)

    def insertar_error(self, mensaje):
        self.insertHtml(u" <b style='color: #FF0000'> &nbsp; × %s </b>" %(mensaje))
        self.insertPlainText('\n')

    def insertar_mensaje(self, mensaje):
        self.insertHtml("<p style='color: green'>%s</p><p></p>" %(mensaje))

    def insertar_comando_falso(self, comando):
        self.marker()
        self.insertHtml(comando)
        self.insertPlainText('\n')

    def insertar_codigo(self, codigo):
        for line in codigo.splitlines():
            self.insertar_comando_falso(line)

    def marker(self):
        if self.multiline:
            self.insertHtml(u"<b style='color: #FF0000'>‥</b> ")
            self.insertPlainText("    ")
        else:
            self.insertHtml(u"<b style='color: #3583FC'>»</b> ")

    def init(self, interpreter_locals):
        if interpreter_locals:
            self.interpreter = code.InteractiveInterpreter(interpreter_locals)
            self.interpreter.runsource('raw_input = self.raw_input')
            self.interpreter.runsource('input = self.input')
            self.interpreter.runsource('help = self.help')
            self.interpreterLocals = interpreter_locals

    def updateInterpreterLocals(self, newLocals):
        className = newLocals.__class__.__name__
        self.interpreterLocals[className] = newLocals

    def clearCurrentBlock(self):
        length = len(self.document().lastBlock().text()[2:])

        if length:
            [self.textCursor().deletePreviousChar() for x in xrange(length)]

    def recall_history(self):
        self._mover_cursor_al_final()
        self.clearCurrentBlock()
        if self.historyIndex <> -1:
            self.insertPlainText(self.history[self.historyIndex])

    def _get_entered_line(self):
        textCursor = self.textCursor()
        position = len(self.document().toPlainText())
        textCursor.setPosition(position)
        self.setTextCursor(textCursor)

        line = unicode(self.document().lastBlock().text())[2:]
        line.rstrip()
        return line

    def _get_position_in_block(self):
        tc = self.textCursor()
        position = tc.positionInBlock() - 3
        return position

    def _get_current_block_prefix(self):
        tc = self.textCursor()
        tc.select(QTextCursor.BlockUnderCursor)
        current_block = tc.selectedText()
        words = current_block.split(" ")
        prefix = words[-1]

        if '(' in prefix:
            prefix = prefix.split('(')[-1]

        if '.' in prefix:
            prefixes = prefix.split('.')
            prefixes = prefixes[:-1]
            return '.'.join([str(s) for s in prefixes])
        else:
            return prefix

    def _set_current_word(self, word):
        tc = self.textCursor()
        tc.select(QTextCursor.WordUnderCursor)
        tc.removeSelectedText()
        tc.insertText(word)

    def _mover_cursor_al_final(self):
        textCursor = self.textCursor()
        textCursor.movePosition(QTextCursor.End)
        self.setTextCursor(textCursor)
        return textCursor

    def _get_current_line(self):
        "Obtiene la linea en donde se encuentra el cursor."
        tc = self.textCursor()
        tc.select(QTextCursor.LineUnderCursor)
        return tc.selectedText()[2:]

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_ParenLeft:
            self._autocompletar_argumentos_si_corresponde()

    def keyPressEvent(self, event):
        if editor_base.EditorBase.keyPressEvent(self, event):
            return None

        textCursor = self.textCursor()

        # Permite mantener pulsada la tecla CTRL para copiar o pegar.
        if event.modifiers() & Qt.ControlModifier:
            # Ignorando pegar texto si cursor está en medio de consola.
            if textCursor.blockNumber() != self.document().blockCount() - 1:
                if event.key() == Qt.Key_V:
                    textCursor = self._mover_cursor_al_final()
                    return

            # Ignorando pegar texto si cursor está sobre el prompt de consola.
            elif textCursor.positionInBlock() < 2:
                if event.key() == Qt.Key_V:
                    textCursor = self._mover_cursor_al_final()
                    return

            return QtGui.QTextEdit.keyPressEvent(self, event)

        # Ignorando la pulsación de tecla si está en medio de la consola.
        if textCursor.blockNumber() != self.document().blockCount() - 1:
            textCursor = self._mover_cursor_al_final()
            return

        # Ignora el evento si está sobre el cursor de la consola.
        if textCursor.positionInBlock() < 2:
            textCursor = self._mover_cursor_al_final()
            return

        if event.key() in [Qt.Key_Left, Qt.Key_Backspace]:
            if self.textCursor().positionInBlock() == 2:
                return

        # Elimina los pares de caracteres especiales si los encuentra
        if event.key() == Qt.Key_Backspace:
            self._eliminar_pares_de_caracteres()

        # navegar por el historial
        if event.key() == Qt.Key_Down:
            if self.historyIndex == len(self.history):
                self.historyIndex -= 1
            try:
                if self.historyIndex > -1:
                    self.historyIndex -= 1
                    self.recall_history()
                else:
                    self.clearCurrentBlock()
            except:
                pass
            return None

        # navegar por el historial
        if event.key() == Qt.Key_Up:
            try:
                if len(self.history) - 1 > self.historyIndex:
                    self.historyIndex += 1
                    self.recall_history()
                else:
                    self.historyIndex = len(self.history)
            except:
                pass
            return None

        # ir al primer caracter del interprete cuando pulsa HOME
        if event.key() == Qt.Key_Home:
            blockLength = len(self.document().lastBlock().text()[2:])
            lineLength = len(self.document().toPlainText())
            position = lineLength - blockLength
            textCursor = self.textCursor()
            textCursor.setPosition(position)
            self.setTextCursor(textCursor)
            return None

        try:
            if self.autocomplete(event):
                return None
        except UnicodeEncodeError:
            pass

        if event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            self.limpiar_consejo() # Limpiando consejo si existe

            line = self._get_entered_line()
            self.historyIndex = -1

            if line == "clear":
                self.clear()
                self.marker()
                return

            try:
                line[-1]
                self.haveLine = True
                if line[-1] in [':', ',', '[', '(']:
                    self.multiline = True
                self.history.insert(0, line)
            except:
                self.haveLine = False

            # Cuando pulsa ENTER luego de haber hecho un texto multilinea y borrado todos los caracteres.
            if self.multiline and (not self.haveLine or self._ha_ingresado_solo_espacios(line)): #  multi line done
                self.append('') # move down one line
                self.interpreter.runsource(self.command)
                self.command = '' # clear command
                self.multiline = False # back to single line
                self.marker() # handle marker style
                return None

            if self.haveLine and self.multiline: # multi line command
                self.command += line + '\n' # + command and line
                self.append('')
                self.marker()
                return None

            # Permite escribir lineas terminas con '?' para consultar la documentacion
            # de manera similar a como lo hace ipython.
            if line.endswith('?'):
                line = 'print ' + line[:-1] + '.__doc__'

            if self.haveLine and not self.multiline: # one line command
                self.command = line # line is the command
                self.append('') # move down one line
                self.interpreter.runsource(self.command)
                self.command = '' # clear command
                self.marker() # handle marker style
                return None

            # Cuando pulsa ENTER sin texto.
            if not self.haveLine and not self.multiline:
                self.append('')
                self.marker()
                return None

            return None

        return QTextEdit.keyPressEvent(self, event)

    def _autocompletar_argumentos_si_corresponde(self):
        """Muestra un mensaje con la documentación de una función ejecutar.

        Se invoca mientras que el usuario escribe, siempre y cuando
        se vea un paréntisis.

        Por ejemplo, si el usuario escribe 'os.system(' esta función
        intentará mostrar un tooltip con el contenido de 'os.system.__doc__'
        """
        linea = unicode(self.document().lastBlock().text())[2:]
        linea.rstrip()

        self.limpiar_consejo()

        if '(' in linea:
            principio = linea.split('(')[0]
            principio = principio.split(' ')[-1]

            # Obtiene el mensaje a mostrar y lo despliega en el tooltip
            texto_consejo = self._obtener_firma_de_funcion(principio)
            self.mostrar_consejo(texto_consejo)

    def limpiar_consejo(self):
        self.mostrar_consejo("")

    def _obtener_firma_de_funcion(self, texto):
        codigo = self.ver_codigo(texto)

        if codigo:
            posicion = codigo.find(":")
            codigo = codigo[:posicion].replace("def ", "").replace('  ', '').replace('self, ', '').replace('self', '').replace('\n', ' ')
            return codigo
        else:
            return ""

    def ver_codigo(self, texto):
        codigo = ""
        try:
            try:
                texto_a_ejecutar = 'inspect.isclass(' + texto + ")"
                es_clase = eval(texto_a_ejecutar, self.interpreterLocals)

                if es_clase:
                    texto = texto + ".__init__"

                texto_a_ejecutar = 'inspect.getsource(' + texto + ")"
                codigo = eval(texto_a_ejecutar, self.interpreterLocals)
            except TypeError, e:
                pass
        except Exception, e:
            pass

        return codigo

    def mostrar_consejo(self, linea):
        pos = self.mapToGlobal(self.cursorRect().bottomRight())
        self.ventana.tip_widget.setText(linea)

    def guardar_contenido_con_dialogo(self):
        ruta = self.abrir_dialogo_guardar_archivo()

        if ruta:
            self.guardar_contenido_en_el_archivo(ruta)
            self.nombre_de_archivo_sugerido = ruta
            self.mensaje_contenido_guardado()

    def _ha_ingresado_solo_espacios(self, linea):
        # TODO: Reemplazar por una expresion regular para
        #       detectar lineas donde solo hay espacios en blanco.
        if linea == "    ":
            return True

    def obtener_contenido(self):
        texto = self.document().toPlainText()
        texto = texto.replace(u'‥ ', '')
        texto = texto.replace(u'» ', '')
        return unicode(texto)

    def marker_si_es_necesario(self):
        line = unicode(self.document().lastBlock().text())
        if not line.startswith(u'» ') and not line.startswith(u'‥ '):
            self.insertPlainText("\n")
            self.marker()
