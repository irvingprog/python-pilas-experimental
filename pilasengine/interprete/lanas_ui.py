# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lanas.ui'
#
# Created: Wed Sep 24 09:25:44 2014
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

class Ui_Lanas(object):
    def setupUi(self, Lanas):
        Lanas.setObjectName(_fromUtf8("Lanas"))
        Lanas.resize(656, 349)
        self.verticalLayout = QtGui.QVBoxLayout(Lanas)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_interprete = QtGui.QStackedWidget(Lanas)
        self.widget_interprete.setObjectName(_fromUtf8("widget_interprete"))
        self.verticalLayout.addWidget(self.widget_interprete)
        self.consejo = QtGui.QLabel(Lanas)
        self.consejo.setText(_fromUtf8(""))
        self.consejo.setObjectName(_fromUtf8("consejo"))
        self.verticalLayout.addWidget(self.consejo)

        self.retranslateUi(Lanas)
        QtCore.QMetaObject.connectSlotsByName(Lanas)

    def retranslateUi(self, Lanas):
        Lanas.setWindowTitle(_translate("Lanas", "Lanas - Interprete de Python", None))
        Lanas.setToolTip(_translate("Lanas", "Guardar contenido del interprete", None))
