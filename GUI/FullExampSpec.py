# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FullExampSpec.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FullExampSpec(object):
    def setupUi(self, FullExampSpec):
        FullExampSpec.setObjectName("FullExampSpec")
        FullExampSpec.resize(632, 500)
        self.gridLayout_2 = QtWidgets.QGridLayout(FullExampSpec)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fInput = QtWidgets.QPushButton(FullExampSpec)
        self.fInput.setObjectName("fInput")
        self.gridLayout_2.addWidget(self.fInput, 5, 0, 1, 1)
        self.leNumWien = QtWidgets.QLineEdit(FullExampSpec)
        self.leNumWien.setObjectName("leNumWien")
        self.gridLayout_2.addWidget(self.leNumWien, 4, 1, 1, 1)
        self.txtHeader = QtWidgets.QLabel(FullExampSpec)
        self.txtHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.txtHeader.setObjectName("txtHeader")
        self.gridLayout_2.addWidget(self.txtHeader, 0, 0, 1, 2)
        self.leDimdX = QtWidgets.QLineEdit(FullExampSpec)
        self.leDimdX.setObjectName("leDimdX")
        self.gridLayout_2.addWidget(self.leDimdX, 4, 0, 1, 1)
        self.cbProbSpec = QtWidgets.QComboBox(FullExampSpec)
        self.cbProbSpec.setObjectName("cbProbSpec")
        self.cbProbSpec.addItem("")
        self.cbProbSpec.addItem("")
        self.cbProbSpec.addItem("")
        self.cbProbSpec.addItem("")
        self.cbProbSpec.addItem("")
        self.cbProbSpec.addItem("")
        self.gridLayout_2.addWidget(self.cbProbSpec, 1, 0, 1, 2)
        self.txtDimdX = QtWidgets.QLabel(FullExampSpec)
        self.txtDimdX.setAlignment(QtCore.Qt.AlignCenter)
        self.txtDimdX.setObjectName("txtDimdX")
        self.gridLayout_2.addWidget(self.txtDimdX, 3, 0, 1, 1)
        self.txtNumWien = QtWidgets.QLabel(FullExampSpec)
        self.txtNumWien.setAlignment(QtCore.Qt.AlignCenter)
        self.txtNumWien.setObjectName("txtNumWien")
        self.gridLayout_2.addWidget(self.txtNumWien, 3, 1, 1, 1)
        self.btnCreProb = QtWidgets.QPushButton(FullExampSpec)
        self.btnCreProb.setObjectName("btnCreProb")
        self.gridLayout_2.addWidget(self.btnCreProb, 10, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(FullExampSpec)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 8, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnf3 = QtWidgets.QPushButton(FullExampSpec)
        self.btnf3.setObjectName("btnf3")
        self.gridLayout.addWidget(self.btnf3, 2, 2, 1, 1)
        self.btnf1 = QtWidgets.QPushButton(FullExampSpec)
        self.btnf1.setObjectName("btnf1")
        self.gridLayout.addWidget(self.btnf1, 1, 2, 1, 1)
        self.btng1 = QtWidgets.QPushButton(FullExampSpec)
        self.btng1.setObjectName("btng1")
        self.gridLayout.addWidget(self.btng1, 1, 3, 1, 1)
        self.btnf2 = QtWidgets.QPushButton(FullExampSpec)
        self.btnf2.setObjectName("btnf2")
        self.gridLayout.addWidget(self.btnf2, 2, 0, 1, 1)
        self.btng2 = QtWidgets.QPushButton(FullExampSpec)
        self.btng2.setObjectName("btng2")
        self.gridLayout.addWidget(self.btng2, 2, 1, 1, 1)
        self.btnf = QtWidgets.QPushButton(FullExampSpec)
        self.btnf.setObjectName("btnf")
        self.gridLayout.addWidget(self.btnf, 1, 0, 1, 1)
        self.btng = QtWidgets.QPushButton(FullExampSpec)
        self.btng.setObjectName("btng")
        self.gridLayout.addWidget(self.btng, 1, 1, 1, 1)
        self.btng3 = QtWidgets.QPushButton(FullExampSpec)
        self.btng3.setObjectName("btng3")
        self.gridLayout.addWidget(self.btng3, 2, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 9, 0, 1, 2)
        self.gInput = QtWidgets.QPushButton(FullExampSpec)
        self.gInput.setObjectName("gInput")
        self.gridLayout_2.addWidget(self.gInput, 5, 1, 1, 1)
        self.btnParDescr = QtWidgets.QPushButton(FullExampSpec)
        self.btnParDescr.setObjectName("btnParDescr")
        self.gridLayout_2.addWidget(self.btnParDescr, 2, 0, 1, 2)

        self.retranslateUi(FullExampSpec)
        QtCore.QMetaObject.connectSlotsByName(FullExampSpec)
        FullExampSpec.setTabOrder(self.cbProbSpec, self.leDimdX)
        FullExampSpec.setTabOrder(self.leDimdX, self.leNumWien)
        FullExampSpec.setTabOrder(self.leNumWien, self.btnf)
        FullExampSpec.setTabOrder(self.btnf, self.btng)
        FullExampSpec.setTabOrder(self.btng, self.btnf1)
        FullExampSpec.setTabOrder(self.btnf1, self.btng1)
        FullExampSpec.setTabOrder(self.btng1, self.btnf2)
        FullExampSpec.setTabOrder(self.btnf2, self.btng2)
        FullExampSpec.setTabOrder(self.btng2, self.btnf3)
        FullExampSpec.setTabOrder(self.btnf3, self.btng3)
        FullExampSpec.setTabOrder(self.btng3, self.btnCreProb)

    def retranslateUi(self, FullExampSpec):
        _translate = QtCore.QCoreApplication.translate
        FullExampSpec.setWindowTitle(_translate("FullExampSpec", "Full example problem specification."))
        self.fInput.setText(_translate("FullExampSpec", "Input f function"))
        self.txtHeader.setText(_translate("FullExampSpec", "Choose problem specification of dX = f(X,t)dt+g(X,t)dW from list:"))
        self.cbProbSpec.setItemText(0, _translate("FullExampSpec", "Constant coefficients"))
        self.cbProbSpec.setItemText(1, _translate("FullExampSpec", "Langevin equation"))
        self.cbProbSpec.setItemText(2, _translate("FullExampSpec", "Brownian bridge"))
        self.cbProbSpec.setItemText(3, _translate("FullExampSpec", "Stock model"))
        self.cbProbSpec.setItemText(4, _translate("FullExampSpec", "Ohrstein-Uhlenbeck"))
        self.cbProbSpec.setItemText(5, _translate("FullExampSpec", "Random harmonic oscillations"))
        self.txtDimdX.setText(_translate("FullExampSpec", "Dimension of dX:"))
        self.txtNumWien.setText(_translate("FullExampSpec", "Number of Wiener processes:"))
        self.btnCreProb.setText(_translate("FullExampSpec", "Create problem specification"))
        self.label_4.setText(_translate("FullExampSpec", "Open internal functions:"))
        self.btnf3.setText(_translate("FullExampSpec", "f\'\'\'"))
        self.btnf1.setText(_translate("FullExampSpec", "f\'"))
        self.btng1.setText(_translate("FullExampSpec", "g\'"))
        self.btnf2.setText(_translate("FullExampSpec", "f\'\'"))
        self.btng2.setText(_translate("FullExampSpec", "g\'\'"))
        self.btnf.setText(_translate("FullExampSpec", "f"))
        self.btng.setText(_translate("FullExampSpec", "g"))
        self.btng3.setText(_translate("FullExampSpec", "g\'\'\'"))
        self.gInput.setText(_translate("FullExampSpec", "Input g function"))
        self.btnParDescr.setText(_translate("FullExampSpec", "Description of chosen problem specification"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FullExampSpec = QtWidgets.QWidget()
    ui = Ui_FullExampSpec()
    ui.setupUi(FullExampSpec)
    FullExampSpec.show()
    sys.exit(app.exec_())

