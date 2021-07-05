# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'discount.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(196, 343)
        Form.setMinimumSize(QtCore.QSize(196, 343))
        Form.setMaximumSize(QtCore.QSize(196, 343))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, -10, 181, 81))
        self.widget.setObjectName("widget")
        self.orignal_priceinput = QtWidgets.QSpinBox(self.widget)
        self.orignal_priceinput.setGeometry(QtCore.QRect(10, 50, 161, 27))
        self.orignal_priceinput.setMaximum(999999999)
        self.orignal_priceinput.setObjectName("orignal_priceinput")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 19))
        self.label.setObjectName("label")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(10, 80, 181, 81))
        self.widget_2.setObjectName("widget_2")
        self.disocunt_input = QtWidgets.QSpinBox(self.widget_2)
        self.disocunt_input.setGeometry(QtCore.QRect(10, 50, 161, 27))
        self.disocunt_input.setMaximum(100)
        self.disocunt_input.setObjectName("disocunt_input")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 101, 19))
        self.label_2.setObjectName("label_2")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(10, 170, 181, 81))
        self.widget_3.setObjectName("widget_3")
        self.final_price = QtWidgets.QLabel(self.widget_3)
        self.final_price.setGeometry(QtCore.QRect(10, 50, 161, 27))
        self.final_price.setStyleSheet("background-color: rgb(39, 42, 52);\n"
"border-color: rgb(25, 26, 33);\n"
"border:1px solid rgb(25, 26, 33);")
        self.final_price.setObjectName("final_price")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 101, 19))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(56, 300, 67, 19))
        self.label_5.setStyleSheet("color: rgb(134, 134, 134);")
        self.label_5.setObjectName("label_5")
        self.you_save = QtWidgets.QLabel(Form)
        self.you_save.setGeometry(QtCore.QRect(120, 300, 41, 19))
        self.you_save.setStyleSheet("color: rgb(134, 134, 134);")
        self.you_save.setObjectName("you_save")
        self.calculate = QtWidgets.QPushButton(Form)
        self.calculate.setGeometry(QtCore.QRect(50, 260, 88, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.calculate.setFont(font)
        self.calculate.setStyleSheet("color: rgb(0, 255, 0);")
        self.calculate.setFlat(True)
        self.calculate.setObjectName("calculate")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.calculate.clicked.connect(self.discount_calc)

    def discount_calc(self):
        original_price = self.orignal_priceinput.value()
        discount = self.disocunt_input.value()
        result = original_price*(discount/100)
        self.you_save.setText(str(result))
        self.final_price.setText(str(original_price-result))




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Discount"))
        self.label.setText(_translate("Form", "Oringinal Price"))
        self.label_2.setText(_translate("Form", "Discount"))
        self.final_price.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "Final Price"))
        self.label_5.setText(_translate("Form", "you save"))
        self.you_save.setText(_translate("Form", "0"))
        self.calculate.setText(_translate("Form", "Calculate"))