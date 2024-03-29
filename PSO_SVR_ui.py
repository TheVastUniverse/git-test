# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PSO_SVR_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_PSO_SVR_ui(QWidget):
    def setupUi(self, PSO_SVR_ui):
        PSO_SVR_ui.setObjectName("PSO_SVR_ui")
        PSO_SVR_ui.resize(693, 733)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        PSO_SVR_ui.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(PSO_SVR_ui)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 69, 641, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_maxiter = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_maxiter.setObjectName("lineEdit_maxiter")
        self.horizontalLayout.addWidget(self.lineEdit_maxiter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_phip = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_phip.setObjectName("lineEdit_phip")
        self.horizontalLayout_3.addWidget(self.lineEdit_phip)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_swarmsize = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_swarmsize.setObjectName("lineEdit_swarmsize")
        self.horizontalLayout_4.addWidget(self.lineEdit_swarmsize)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEdit_minfunc = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_minfunc.setObjectName("lineEdit_minfunc")
        self.horizontalLayout_5.addWidget(self.lineEdit_minfunc)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(PSO_SVR_ui)
        self.label.setGeometry(QtCore.QRect(20, 10, 651, 65))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(PSO_SVR_ui)
        QtCore.QMetaObject.connectSlotsByName(PSO_SVR_ui)

    def retranslateUi(self, PSO_SVR_ui):
        _translate = QtCore.QCoreApplication.translate
        PSO_SVR_ui.setWindowTitle(_translate("PSO_SVR_ui", "PSO-SVR参数设置"))
        self.label_2.setText(_translate("PSO_SVR_ui", "参数说明\n"
"SVR参数：\n"
"C：正则化参数,正则化的强度与C成反比 \n"
"ε：它指定了在训练损失函数中预测值与实际值之间距离为ε的ε-tube\n"
"mape:损失函数\n"
"\n"
"PSO参数：\n"
"maxiter:PSO最大迭代次数，默认值:100\n"
"phip：粒子朝p_best（当前粒子的历史最优位置）方向飞行的权重，默认值：2\n"
"swarmsize：粒子的个数，默认值：20\n"
"minfunc：函数的最小改变值，默认值：1e-4\n"
"\n"
"\n"
"\n"
"参数设置（不设置则为默认值）"))
        self.label_3.setText(_translate("PSO_SVR_ui", "maxiter:  "))
        self.label_4.setText(_translate("PSO_SVR_ui", "phip:     "))
        self.label_5.setText(_translate("PSO_SVR_ui", "swarmsize:"))
        self.label_6.setText(_translate("PSO_SVR_ui", "minfunc:  "))
        self.pushButton.setText(_translate("PSO_SVR_ui", "开始"))
        self.label.setText(_translate("PSO_SVR_ui", "PSO-SVR参数设置"))
