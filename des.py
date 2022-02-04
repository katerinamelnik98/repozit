# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import math
from pyqtgraph import PlotWidget
import os
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QTextEdit, QAction, QLabel, QPushButton
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from scipy.ndimage.filters import gaussian_filter1d


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 556)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 741, 541))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.pushButton = QtWidgets.QPushButton(self.tab_9)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 301, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_9)
        self.textEdit_6.setGeometry(QtCore.QRect(320, 50, 371, 70))
        self.textEdit_6.setObjectName("textEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 180, 251, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_9)
        self.textEdit_7.setGeometry(QtCore.QRect(320, 150, 371, 70))
        self.textEdit_7.setObjectName("textEdit_7")
        self.comboBox = QtWidgets.QComboBox(self.tab_9)
        self.comboBox.setGeometry(QtCore.QRect(320, 250, 371, 25))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.tab_9)
        self.label_3.setGeometry(QtCore.QRect(40, 250, 241, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_9)
        self.label_4.setGeometry(QtCore.QRect(440, 350, 221, 141))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(190, 10, 311, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(40, 40, 641, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Наименование")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        file = open('info.txt', 'rt')
        s = {}
        q = {}
        d1 = {}
        d2 = {}
        k = 0
        t = 0
        for line in file:
            for i in range(0, 12):
                s = line.split(':', 1)
                d1 = s[0]
                self.tableWidget.setItem(k, 0, QTableWidgetItem(d1))
            k = k + 1
            for i in range(0, 12):
                q = line.split(':', 1)
                d2 = q[1]
                d2 = d2.lstrip()
                self.tableWidget.setItem(t, 1, QTableWidgetItem(d2))
            t = t + 1
        file.close()
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(220, 240, 311, 31))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(20, 280, 701, 211))
        self.textEdit.setObjectName("textEdit")
        file = open('fs_info.txt', 'rt')
        r=[]
        file1 = open('name_fs.txt', 'rt')
        for line in file1:
            r = line.split()
        t = r[0] +':         ' + r[1]
        s = ''
        s1 = ''
        k = 1

        for line in file:
            s = line
            s1 = s1 + s
            k = k + 1
            if k > 10:
                break
        file.close()
        self.textEdit.setText(t +'\n'+ s1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 971, 611))
        self.tabWidget_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget_2.setAcceptDrops(False)
        self.tabWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_2.setIconSize(QtCore.QSize(20, 25))
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_4.sizePolicy().hasHeightForWidth())
        self.tab_4.setSizePolicy(sizePolicy)
        self.tab_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tab_4.setObjectName("tab_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 20, 671, 301))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 340, 651, 111))
        self.textEdit_3.setObjectName("textEdit_3")
        file = open('all.txt', 'rt')
        s =''
        s1=''
        k = 0
        for line in file:
            s = line
            s1 = s1 + '\n' + s
            k=k+1
            if k > 2:
                break
        file.close()
        self.textEdit_3.setText(s1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 691, 321))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(27)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        file = open('attributes.txt', 'rt')
        q = {}
        k = 0
        for line in file:
            q = line.split()
            a = q[0]
            b = q[1]
            c = q[3]
            d = q[4]
            e = q[5]
            l = q[8]
            n = q[9]
            self.tableWidget_2.setItem(k, 0, QTableWidgetItem(a))
            self.tableWidget_2.setItem(k, 1, QTableWidgetItem(b))
            self.tableWidget_2.setItem(k, 2, QTableWidgetItem(c))
            self.tableWidget_2.setItem(k, 3, QTableWidgetItem(d))
            self.tableWidget_2.setItem(k, 4, QTableWidgetItem(e))
            self.tableWidget_2.setItem(k, 5, QTableWidgetItem(l))
            self.tableWidget_2.setItem(k, 6, QTableWidgetItem(n))
            k = k+1
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_3.setGeometry(QtCore.QRect(10, 10, 721, 491))
        self.tabWidget_3.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 30, 161, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit_1 = QtWidgets.QTextEdit(self.tab_7)
        self.textEdit_1.setGeometry(QtCore.QRect(30, 110, 651, 311))
        self.textEdit_1.setObjectName("textEdit_2")
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 60, 161, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit.setGeometry(QtCore.QRect(220, 60, 441, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(100, 140, 511, 151))
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_4.setGeometry(QtCore.QRect(40, 320, 661, 111))
        self.textEdit_4.setObjectName("textEdit_4")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.graphicsView = PlotWidget(self.tab_6)
        self.graphicsView.setGeometry(QtCore.QRect(220, 110, 441, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 130, 181, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AnomalFS"))
        self.pushButton.setText(_translate("MainWindow", "Определить файловую систему"))
        self.pushButton_2.setText(_translate("MainWindow", "Поиск дисков"))
        self.label_3.setText(_translate("MainWindow", "Выбор диска для проверки:"))
        self.label_4.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Главная"))
        self.tabWidget.setCurrentWidget
        self.label.setText(_translate("MainWindow", "Информация о жёстком диске"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Информация"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "Информация о файловой системе"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "О системе"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget_2.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget_2.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget_2.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget_2.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget_2.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.tableWidget_2.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.tableWidget_2.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "18"))
        item = self.tableWidget_2.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "19"))
        item = self.tableWidget_2.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "20"))
        item = self.tableWidget_2.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "21"))
        item = self.tableWidget_2.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "22"))
        item = self.tableWidget_2.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", "23"))
        item = self.tableWidget_2.verticalHeaderItem(23)
        item.setText(_translate("MainWindow", "24"))
        item = self.tableWidget_2.verticalHeaderItem(24)
        item.setText(_translate("MainWindow", "25"))
        item = self.tableWidget_2.verticalHeaderItem(25)
        item.setText(_translate("MainWindow", "26"))
        item = self.tableWidget_2.verticalHeaderItem(26)
        item.setText(_translate("MainWindow", "27"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Наименов."))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Текущ.знач."))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Миним.знач."))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Порог.знач."))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Ошибки"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Знач."))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Сканирование состояния диска"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Мониторинг состояния жесткого диска"))
        self.pushButton_5.setText(_translate("MainWindow", "Сканировать"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("MainWindow", "Сканирование файловой системы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Анализ состояния файловой системы"))
        self.pushButton_3.setText(_translate("MainWindow", "Открыть файл"))
        self.pushButton_4.setText(_translate("MainWindow", "Построить график"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "Проверка энтропии файла"))

    def add_function(self):
        self.pushButton.clicked.connect(lambda: self.fs())
        self.pushButton_2.clicked.connect(lambda: self.disk())
        self.pushButton_3.clicked.connect(lambda: self.showDialog())
        self.pushButton_5.clicked.connect(lambda: self.sh_fail())
        self.pushButton_5.clicked.connect(lambda: self.razreg_fail())

    def fs(self):
        d=[]
        cmd = 'findmnt /dev/sdb3'
        data = os.popen(cmd).read()
        res = data.splitlines()
        res=res[1]
        res=res.split(' ')
        res ='файловая система:' + res[7]
        self.textEdit_6.setText(res)

    def disk(self):
        cmd = 'smartctl --scan'
        data = os.popen(cmd)
        res = data.read()
        temp = res.split('\n')
        res1 = temp[0]
        temp1 = res1.split(' ')
        temp1 = temp1[0].split('/')
        name1 = temp1[2]
        d1=''
        d = 'Диск1:' + name1
        d1 = 'Диск1:' + name1
        self.textEdit_7.setText(d)
        self.comboBox.addItem(d1)


    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'home')[0]
        self.lineEdit.setText(fname)
        with open(fname, 'rb') as f:
            byteArr = list(f.read())
            fileSize = len(byteArr)
            entropY = []
            entropX = []
            self.textEdit_4.setText('Размер файла в байтах: {}'.format(fileSize))
            freqList = []
            k = 0
            for b in range(256):
                ctr = 0
                for byte in byteArr:
                    if byte == b:
                        ctr += 1
                freqList.append(float(ctr) / fileSize)
        ent = 0.0
        l = 0.0
        t = ''
        for freq in freqList:
            if freq > 0:
                ent = ent + freq * math.log(freq, 2)
                l = -(ent)
                k += 1
        ent = -ent
        if ent > 7:
            t = 'Файл запакован'
        else:
            t = 'Файл не запакован'
        k = 0
        entI = 0
        for byte in byteArr:
            entI = ent + float(freqList[byte]) * math.log(float(freqList[byte]), 2)
            entropX.append(k)
            entropY.append(entI)
            k += 1
        self.textEdit_4.append('Энтропия файла: {}'.format(ent))
        self.textEdit_4.append(t)
        self.pushButton_4.clicked.connect(lambda: self.draw(entropX, entropY))


    def draw(self,x1 , y1):
        X_Y_Spline = make_interp_spline(x1, y1)
        X_ = np.linspace(min(x1), max(x1), 300)
        Y_ = X_Y_Spline(X_)
        ysmoothed = gaussian_filter1d(Y_, sigma=2)
        self.graphicsView.clear()
        self.graphicsView.setYRange(0, 8.5, padding=0)
        self.graphicsView.plot(X_, ysmoothed)

    def sh_fail(self):
        cmd = 'find / -name "*.sh" -mount -print'
        data = os.popen(cmd).read()
        res = data.splitlines()
        with open(r"sh_fail.txt", "w") as file:
            for i in range(len(res)):
                line = res[i]
                temp = line.split('\n')
                a = temp[0]
                file.write(a + '\n')
        file.close()
        f1 = open(r"scan.txt", "w")
        with open(r"sh_fail.txt", "r") as file:
            a = 'rm -rf / '
            b='sudo dd if=/dev/zero of=/dev/sda bs=8m'
            c='shred /'
            d='mkfs.ext3 /'
            e='chmod -Rv 000 /'
            h='chown -R nobody:nobody /'
            g=':(){ :|:& };:'
            k='> file.conf'
            n='chmod -R 777 /'
            for i in range(len(res)):
                line = res[i]
                with open(line, "r") as f:
                    for line1 in f:
                        if (a in line1) or (b in line1) or (c in line1) or (d in line1) or (e in line1) or (h in line1) or (g in line1) or (k in line1) or (n in line1):
                            f1.write(line +'   '+'Статус: пакетный файл'+'\n')
                            break
                f.close()
        file.close()
        f1.close()
        with open (r"scan.txt", "r") as file:
            for line2 in file:
                d =line2
                self.textEdit_1.append(d)

    def razreg_fail(self):
        cmd = 'ls /home/katushka69 -lhs --block-size=K'
        data = os.popen(cmd).read()
        res = data.splitlines()
        line2=[]
        line3=[]
        d=[]
        t=[]
        line4=[]
        for i in range(1, len(res)):
            line = res[i]
            line1= line.split(" ")
            line1=list(filter(None, line1))
            for j in range(len(line1)):
                if j==0:
                    d=line1[j]
                    d=str(d)
                    if'K' in d:
                        d=d[:-1]
                        line2.append(d)
                elif j==5:
                    t = line1[j]
                    t = str(t)
                    if 'K' in t:
                        t = t[:-1]
                        line3.append(t)
                elif j==9:
                    k=line1[9]
                    line4.append(k)
        r=0
        s=0
        n=[]
        for i in range(len(line2)):
            r=int(line2[i])
            s=int(line3[i])
            if ((s > r) and (r !=0)):
                k=s//r
                if k>1:
                    d =line4[i]
                    d = str(d)
                    filename = d
                    for root, dirnames, filenames in os.walk('/home/katushka69/'):
                        for file in filenames:
                            if file == filename:
                                d = os.path.join(root, file)
                                d = d + '  Статус: разреженный файл\n'
                                d=str(d)
                                n.append(d)
            elif r == 0:
                if s>500:
                    d=line4[i]
                    d=str(d)
                    filename = d
                    for root, dirnames, filenames in os.walk('/home/katushka69/'):
                        for file in filenames:
                            if file == filename:
                                d = os.path.join(root, file)
                                d= d + '  Статус: разреженный файл\n'
                                d=str(d)
                                n.append(d)
        for i in range(len(n)):
            g = n[i]
            self.textEdit_1.append(g)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
