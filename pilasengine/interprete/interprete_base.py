# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pilasengine/interprete/interprete.ui'
#
# Created: Sun Aug 31 19:27:07 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_InterpreteWindow(object):
    def setupUi(self, InterpreteWindow):
        InterpreteWindow.setObjectName(_fromUtf8("InterpreteWindow"))
        InterpreteWindow.resize(794, 605)
        InterpreteWindow.setMinimumSize(QtCore.QSize(660, 530))
        self.centralwidget = QtGui.QWidget(InterpreteWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.manual_button = QtGui.QPushButton(self.centralwidget)
        self.manual_button.setMaximumSize(QtCore.QSize(20, 20))
        self.manual_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.manual_button.setCheckable(True)
        self.manual_button.setFlat(True)
        self.manual_button.setObjectName(_fromUtf8("manual_button"))
        self.horizontalLayout_3.addWidget(self.manual_button)
        self.interprete_button = QtGui.QPushButton(self.centralwidget)
        self.interprete_button.setMaximumSize(QtCore.QSize(20, 20))
        self.interprete_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.interprete_button.setCheckable(True)
        self.interprete_button.setChecked(True)
        self.interprete_button.setFlat(True)
        self.interprete_button.setObjectName(_fromUtf8("interprete_button"))
        self.horizontalLayout_3.addWidget(self.interprete_button)
        self.editor_button = QtGui.QPushButton(self.centralwidget)
        self.editor_button.setMaximumSize(QtCore.QSize(20, 20))
        self.editor_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editor_button.setCheckable(True)
        self.editor_button.setFlat(True)
        self.editor_button.setObjectName(_fromUtf8("editor_button"))
        self.horizontalLayout_3.addWidget(self.editor_button)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.splitter_vertical = QtGui.QSplitter(self.centralwidget)
        self.splitter_vertical.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_vertical.setObjectName(_fromUtf8("splitter_vertical"))
        self.navegador = QtWebKit.QWebView(self.splitter_vertical)
        self.navegador.setMinimumSize(QtCore.QSize(250, 0))
        self.navegador.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.navegador.setObjectName(_fromUtf8("navegador"))
        self.splitter_editor = QtGui.QSplitter(self.splitter_vertical)
        self.splitter_editor.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_editor.setObjectName(_fromUtf8("splitter_editor"))
        self.splitter = QtGui.QSplitter(self.splitter_editor)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.canvas = QtGui.QStackedWidget(self.layoutWidget)
        self.canvas.setMinimumSize(QtCore.QSize(320, 240))
        self.canvas.setObjectName(_fromUtf8("canvas"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.canvas.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.canvas.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.canvas)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.guardar_button = QtGui.QPushButton(self.layoutWidget)
        self.guardar_button.setMaximumSize(QtCore.QSize(20, 20))
        self.guardar_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.guardar_button.setFlat(True)
        self.guardar_button.setObjectName(_fromUtf8("guardar_button"))
        self.horizontalLayout_2.addWidget(self.guardar_button)
        self.configuracion_button = QtGui.QPushButton(self.layoutWidget)
        self.configuracion_button.setMaximumSize(QtCore.QSize(20, 20))
        self.configuracion_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configuracion_button.setFlat(True)
        self.configuracion_button.setObjectName(_fromUtf8("configuracion_button"))
        self.horizontalLayout_2.addWidget(self.configuracion_button)
        spacerItem1 = QtGui.QSpacerItem(37, 13, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_6 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.console = QtGui.QStackedWidget(self.layoutWidget1)
        self.console.setObjectName(_fromUtf8("console"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.console.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.console.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.console)
        self.layoutWidget2 = QtGui.QWidget(self.splitter_editor)
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.boton_abrir = QtGui.QPushButton(self.layoutWidget2)
        self.boton_abrir.setEnabled(True)
        self.boton_abrir.setMaximumSize(QtCore.QSize(20, 20))
        self.boton_abrir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_abrir.setFlat(True)
        self.boton_abrir.setObjectName(_fromUtf8("boton_abrir"))
        self.horizontalLayout.addWidget(self.boton_abrir)
        self.boton_guardar = QtGui.QPushButton(self.layoutWidget2)
        self.boton_guardar.setEnabled(True)
        self.boton_guardar.setMaximumSize(QtCore.QSize(20, 20))
        self.boton_guardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_guardar.setFlat(True)
        self.boton_guardar.setObjectName(_fromUtf8("boton_guardar"))
        self.horizontalLayout.addWidget(self.boton_guardar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.boton_ejecutar = QtGui.QPushButton(self.layoutWidget2)
        self.boton_ejecutar.setMaximumSize(QtCore.QSize(20, 20))
        self.boton_ejecutar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_ejecutar.setFlat(True)
        self.boton_ejecutar.setObjectName(_fromUtf8("boton_ejecutar"))
        self.horizontalLayout.addWidget(self.boton_ejecutar)
        self.boton_pausar = QtGui.QPushButton(self.layoutWidget2)
        self.boton_pausar.setMaximumSize(QtCore.QSize(20, 20))
        self.boton_pausar.setCheckable(True)
        self.boton_pausar.setFlat(True)
        self.boton_pausar.setObjectName(_fromUtf8("boton_pausar"))
        self.horizontalLayout.addWidget(self.boton_pausar)
        self.boton_siguiente = QtGui.QPushButton(self.layoutWidget2)
        self.boton_siguiente.setMaximumSize(QtCore.QSize(20, 20))
        self.boton_siguiente.setFlat(True)
        self.boton_siguiente.setObjectName(_fromUtf8("boton_siguiente"))
        self.horizontalLayout.addWidget(self.boton_siguiente)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label = QtGui.QLabel(self.layoutWidget2)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setMaximumSize(QtCore.QSize(80, 80))
        self.label.setLineWidth(0)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.editor_placeholder = QtGui.QStackedWidget(self.layoutWidget2)
        self.editor_placeholder.setObjectName(_fromUtf8("editor_placeholder"))
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.editor_placeholder.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.editor_placeholder.addWidget(self.page_6)
        self.verticalLayout_3.addWidget(self.editor_placeholder)
        self.gridLayout.addWidget(self.splitter_vertical, 1, 0, 1, 1)
        InterpreteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(InterpreteWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        InterpreteWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(InterpreteWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        InterpreteWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(InterpreteWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))

        self.retranslateUi(InterpreteWindow)
        self.console.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InterpreteWindow)

    def retranslateUi(self, InterpreteWindow):
        InterpreteWindow.setWindowTitle(_translate("InterpreteWindow", "pilas-engine", None))
        self.manual_button.setToolTip(_translate("InterpreteWindow", "Mostrar el manual lateral", None))
        self.manual_button.setText(_translate("InterpreteWindow", "M", None))
        self.interprete_button.setToolTip(_translate("InterpreteWindow", "Mostrar el intérprete", None))
        self.interprete_button.setText(_translate("InterpreteWindow", "I", None))
        self.editor_button.setToolTip(_translate("InterpreteWindow", "Mostrar el editor lateral", None))
        self.editor_button.setText(_translate("InterpreteWindow", "E", None))
        self.guardar_button.setToolTip(_translate("InterpreteWindow", "Guardar el contenido del intérprete", None))
        self.guardar_button.setText(_translate("InterpreteWindow", "G", None))
        self.configuracion_button.setToolTip(_translate("InterpreteWindow", "Abre el dialogo de configuración", None))
        self.configuracion_button.setText(_translate("InterpreteWindow", "C", None))
        self.pushButton_6.setToolTip(_translate("InterpreteWindow", "Mostrar información del sistema", None))
        self.pushButton_6.setText(_translate("InterpreteWindow", "F7", None))
        self.pushButton_5.setToolTip(_translate("InterpreteWindow", "Mostrar puntos de control", None))
        self.pushButton_5.setText(_translate("InterpreteWindow", "F8", None))
        self.pushButton_4.setToolTip(_translate("InterpreteWindow", "Mostrar radios de colisión", None))
        self.pushButton_4.setText(_translate("InterpreteWindow", "F9", None))
        self.pushButton_3.setToolTip(_translate("InterpreteWindow", "Mostrar areas", None))
        self.pushButton_3.setText(_translate("InterpreteWindow", "F10", None))
        self.pushButton_2.setToolTip(_translate("InterpreteWindow", "Mostrar figuras físicas", None))
        self.pushButton_2.setText(_translate("InterpreteWindow", "F11", None))
        self.pushButton.setToolTip(_translate("InterpreteWindow", "Mostrar posiciones", None))
        self.pushButton.setText(_translate("InterpreteWindow", "F12", None))
        self.boton_abrir.setToolTip(_translate("InterpreteWindow", "Abrir archivo", None))
        self.boton_abrir.setText(_translate("InterpreteWindow", "A", None))
        self.boton_guardar.setToolTip(_translate("InterpreteWindow", "Guardar código en un archivo", None))
        self.boton_guardar.setText(_translate("InterpreteWindow", "G", None))
        self.boton_ejecutar.setToolTip(_translate("InterpreteWindow", "Ejecutar el código actual (F5 o CTRL+R)", None))
        self.boton_ejecutar.setText(_translate("InterpreteWindow", "E", None))
        self.boton_pausar.setText(_translate("InterpreteWindow", "P", None))
        self.boton_siguiente.setText(_translate("InterpreteWindow", "S", None))
        self.actionSalir.setText(_translate("InterpreteWindow", "Salir", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    InterpreteWindow = QtGui.QMainWindow()
    ui = Ui_InterpreteWindow()
    ui.setupUi(InterpreteWindow)
    InterpreteWindow.show()
    sys.exit(app.exec_())

