# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sample_window4.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1636, 742)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_9 = QGroupBox(self.centralwidget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_15 = QGridLayout(self.groupBox_9)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.tabWidget = QTabWidget(self.groupBox_9)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.gridLayout_8 = QGridLayout(self.tab1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea = QScrollArea(self.tab1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 295, 564))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
#if QT_CONFIG(statustip)
        self.groupBox_5.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.groupBox_5.setTitle(u"")
        self.groupBox_5.setCheckable(False)
        self.gridLayout_19 = QGridLayout(self.groupBox_5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_19.addWidget(self.label_6, 1, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_14 = QGridLayout(self.groupBox_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_14.addWidget(self.label_10, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_6)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_14.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_6, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_18 = QGridLayout(self.groupBox_4)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.columnView_2 = QColumnView(self.groupBox_4)
        self.columnView_2.setObjectName(u"columnView_2")

        self.gridLayout_18.addWidget(self.columnView_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 4, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_17 = QGridLayout(self.groupBox_8)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.columnView = QColumnView(self.groupBox_8)
        self.columnView.setObjectName(u"columnView")

        self.gridLayout_17.addWidget(self.columnView, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_8, 2, 0, 1, 1)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lineEdit__grid_path = QLineEdit(self.frame_7)
        self.lineEdit__grid_path.setObjectName(u"lineEdit__grid_path")

        self.horizontalLayout_2.addWidget(self.lineEdit__grid_path)

        self.toolButton__gird_path = QToolButton(self.frame_7)
        self.toolButton__gird_path.setObjectName(u"toolButton__gird_path")

        self.horizontalLayout_2.addWidget(self.toolButton__gird_path)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.frame__grid_drag = QFrame(self.frame_7)
        self.frame__grid_drag.setObjectName(u"frame__grid_drag")
        self.frame__grid_drag.setFrameShape(QFrame.StyledPanel)
        self.frame__grid_drag.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame__grid_drag)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_3 = QLabel(self.frame__grid_drag)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_3, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame__grid_drag)


        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_7, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_20 = QGridLayout(self.groupBox_7)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.columnView_3 = QColumnView(self.groupBox_7)
        self.columnView_3.setObjectName(u"columnView_3")

        self.gridLayout_20.addWidget(self.columnView_3, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_7, 5, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_8.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.tab1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_5 = QFrame(self.groupBox_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.checkBox_5 = QCheckBox(self.frame_5)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_11.addWidget(self.checkBox_5, 0, 0, 1, 1)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setBaseSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(36)
        self.label_13.setFont(font)

        self.gridLayout_11.addWidget(self.label_13, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_5, 0, 1, 1, 1)

        self.frame_6 = QFrame(self.groupBox_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.checkBox_4 = QCheckBox(self.frame_6)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_12.addWidget(self.checkBox_4, 0, 0, 1, 1)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setBaseSize(QSize(50, 50))
        self.label_12.setFont(font)

        self.gridLayout_12.addWidget(self.label_12, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_6, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.groupBox_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setBaseSize(QSize(50, 50))
        self.label_2.setFont(font)

        self.gridLayout_10.addWidget(self.label_2, 1, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.frame_4)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_10.addWidget(self.checkBox_2, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.groupBox_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setBaseSize(QSize(50, 50))
        self.label.setFont(font)

        self.gridLayout_9.addWidget(self.label, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.frame_3)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_9.addWidget(self.checkBox, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_3, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_2, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab1)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_24 = QGridLayout(self.groupBox)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_24.addWidget(self.progressBar, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_24.addWidget(self.pushButton, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.tab1)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_23 = QGridLayout(self.groupBox_10)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.groupBox_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.lineEdit_3 = QLineEdit(self.groupBox_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.toolButton_2 = QToolButton(self.groupBox_10)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_3.addWidget(self.toolButton_2)

        self.pushButton_2 = QPushButton(self.groupBox_10)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.gridLayout_23.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.groupBox_10)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.comboBox = QComboBox(self.groupBox_10)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.pushButton_6 = QPushButton(self.groupBox_10)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_6.addWidget(self.pushButton_6)


        self.gridLayout_23.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_10, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.gridLayout_13 = QGridLayout(self.tab2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox_12 = QGroupBox(self.tab2)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_32 = QGridLayout(self.groupBox_12)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_20 = QLabel(self.groupBox_12)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_9.addWidget(self.label_20)

        self.lineEdit_6 = QLineEdit(self.groupBox_12)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_9.addWidget(self.lineEdit_6)

        self.toolButton_5 = QToolButton(self.groupBox_12)
        self.toolButton_5.setObjectName(u"toolButton_5")

        self.horizontalLayout_9.addWidget(self.toolButton_5)

        self.pushButton_8 = QPushButton(self.groupBox_12)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_9.addWidget(self.pushButton_8)


        self.gridLayout_32.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_21 = QLabel(self.groupBox_12)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_10.addWidget(self.label_21)

        self.comboBox_4 = QComboBox(self.groupBox_12)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_10.addWidget(self.comboBox_4)

        self.pushButton_9 = QPushButton(self.groupBox_12)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_10.addWidget(self.pushButton_9)


        self.gridLayout_32.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_12, 3, 1, 1, 1)

        self.scrollArea_2 = QScrollArea(self.tab2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 198, 165))
        self.gridLayout_34 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_9 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_9)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.lineEdit_4 = QLineEdit(self.frame_9)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.toolButton_3 = QToolButton(self.frame_9)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_4.addWidget(self.toolButton_3)


        self.gridLayout_21.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.comboBox_2 = QComboBox(self.frame_9)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_5.addWidget(self.comboBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.gridLayout_21.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_10)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_4, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_10)


        self.gridLayout_21.addLayout(self.verticalLayout_3, 2, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_16)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.verticalSpacer_5 = QSpacerItem(20, 324, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_31.addItem(self.verticalSpacer_5, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_16)


        self.gridLayout_34.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_13.addWidget(self.scrollArea_2, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.tab2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_11)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.groupBox_11 = QGroupBox(self.frame_11)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_26 = QGridLayout(self.groupBox_11)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.frame_12 = QFrame(self.groupBox_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_12)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.checkBox_6 = QCheckBox(self.frame_12)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_27.addWidget(self.checkBox_6, 0, 0, 1, 1)

        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setBaseSize(QSize(50, 50))
        self.label_14.setFont(font)

        self.gridLayout_27.addWidget(self.label_14, 1, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_12, 0, 1, 1, 1)

        self.frame_13 = QFrame(self.groupBox_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_13)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.checkBox_7 = QCheckBox(self.frame_13)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_28.addWidget(self.checkBox_7, 0, 0, 1, 1)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setBaseSize(QSize(50, 50))
        self.label_15.setFont(font)

        self.gridLayout_28.addWidget(self.label_15, 1, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_13, 1, 1, 1, 1)

        self.frame_14 = QFrame(self.groupBox_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_14)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setBaseSize(QSize(50, 50))
        self.label_16.setFont(font)

        self.gridLayout_29.addWidget(self.label_16, 1, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.frame_14)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_29.addWidget(self.checkBox_3, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_29.addItem(self.verticalSpacer_3, 1, 1, 1, 1)


        self.gridLayout_26.addWidget(self.frame_14, 1, 0, 1, 1)

        self.frame_15 = QFrame(self.groupBox_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_15)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_17 = QLabel(self.frame_15)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setBaseSize(QSize(50, 50))
        self.label_17.setFont(font)

        self.gridLayout_30.addWidget(self.label_17, 1, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.frame_15)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_30.addWidget(self.checkBox_8, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_30.addItem(self.verticalSpacer_4, 1, 1, 1, 1)


        self.gridLayout_26.addWidget(self.frame_15, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.groupBox_11, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_11, 1, 1, 1, 1)

        self.groupBox_13 = QGroupBox(self.tab2)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_33 = QGridLayout(self.groupBox_13)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.progressBar_3 = QProgressBar(self.groupBox_13)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setValue(24)

        self.gridLayout_33.addWidget(self.progressBar_3, 0, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.groupBox_13)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_33.addWidget(self.pushButton_10, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_13, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_15.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_9)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_15.addWidget(self.label_22, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_9)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeWidget = QTreeWidget(self.groupBox_2)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setColumnCount(5)

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setBaseSize(QSize(50, 50))

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1636, 20))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_9.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_6.setTitle("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"City Setting", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Building Setting", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Weather FX", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Main Grid source", None))
        self.toolButton__gird_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Drag & Drop", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Weather FX", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Sample Image", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Image 1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Image 1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Image 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Image 1", None))
        self.groupBox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Build start", None))
        self.groupBox_10.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Save Location", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Export Local", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"csv data\ub85c username", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Publish Shotgrid", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"New City Setting", None))
        self.groupBox_12.setTitle("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Save Location", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Export Local", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"csv data\ub85c username", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Publish Shotgrid", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Select City", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Drag & Drop", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Sample Image", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Image 1", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Image 1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Image 1", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Image 1", None))
        self.groupBox_13.setTitle("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Build start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Exist City Variation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"OSM Setting", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"City Setting", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"USD hieararchy", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Draw Mode", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Kind", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Variants", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Primitive Type", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Scene Graph Path", None));
    # retranslateUi

