# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sample_window5.ui'
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
        MainWindow.resize(1290, 631)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 173, 389))
        self.gridLayout_18 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.groupBox__grayscale = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox__grayscale.setObjectName(u"groupBox__grayscale")
        self.gridLayout_2 = QGridLayout(self.groupBox__grayscale)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label__grid = QLabel(self.groupBox__grayscale)
        self.label__grid.setObjectName(u"label__grid")

        self.verticalLayout_2.addWidget(self.label__grid)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit__grid_path = QLineEdit(self.groupBox__grayscale)
        self.lineEdit__grid_path.setObjectName(u"lineEdit__grid_path")

        self.horizontalLayout_2.addWidget(self.lineEdit__grid_path)

        self.toolButton__gird_path = QToolButton(self.groupBox__grayscale)
        self.toolButton__gird_path.setObjectName(u"toolButton__gird_path")

        self.horizontalLayout_2.addWidget(self.toolButton__gird_path)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout__dragdrop = QHBoxLayout()
        self.horizontalLayout__dragdrop.setObjectName(u"horizontalLayout__dragdrop")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout__dragdrop.addItem(self.verticalSpacer_7)

        self.label_18 = QLabel(self.groupBox__grayscale)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout__dragdrop.addWidget(self.label_18)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout__dragdrop.addItem(self.verticalSpacer_6)


        self.gridLayout_2.addLayout(self.horizontalLayout__dragdrop, 1, 0, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox__grayscale, 0, 0, 1, 1)

        self.groupBox__osm = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox__osm.setObjectName(u"groupBox__osm")
        self.gridLayout_16 = QGridLayout(self.groupBox__osm)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label__OSM = QLabel(self.groupBox__osm)
        self.label__OSM.setObjectName(u"label__OSM")

        self.verticalLayout_5.addWidget(self.label__OSM)

        self.horizontalLayout__osm = QHBoxLayout()
        self.horizontalLayout__osm.setObjectName(u"horizontalLayout__osm")
        self.lineEdit__osm = QLineEdit(self.groupBox__osm)
        self.lineEdit__osm.setObjectName(u"lineEdit__osm")

        self.horizontalLayout__osm.addWidget(self.lineEdit__osm)

        self.toolButton__osm = QToolButton(self.groupBox__osm)
        self.toolButton__osm.setObjectName(u"toolButton__osm")

        self.horizontalLayout__osm.addWidget(self.toolButton__osm)


        self.verticalLayout_5.addLayout(self.horizontalLayout__osm)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout__osm_2 = QHBoxLayout()
        self.horizontalLayout__osm_2.setObjectName(u"horizontalLayout__osm_2")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout__osm_2.addItem(self.verticalSpacer_9)

        self.label_19 = QLabel(self.groupBox__osm)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout__osm_2.addWidget(self.label_19)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout__osm_2.addItem(self.verticalSpacer_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout__osm_2)


        self.gridLayout_16.addLayout(self.verticalLayout_6, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox__osm, 1, 0, 1, 1)

        self.groupBox__name = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox__name.setObjectName(u"groupBox__name")
        self.gridLayout_17 = QGridLayout(self.groupBox__name)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalLayout__name = QVBoxLayout()
        self.verticalLayout__name.setObjectName(u"verticalLayout__name")
        self.label_2 = QLabel(self.groupBox__name)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout__name.addWidget(self.label_2)

        self.lineEdit__city_name = QLineEdit(self.groupBox__name)
        self.lineEdit__city_name.setObjectName(u"lineEdit__city_name")

        self.verticalLayout__name.addWidget(self.lineEdit__city_name)


        self.gridLayout_17.addLayout(self.verticalLayout__name, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox__name, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_8.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.frame__image = QFrame(self.tab1)
        self.frame__image.setObjectName(u"frame__image")
        self.frame__image.setFrameShape(QFrame.StyledPanel)
        self.frame__image.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame__image)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox__image = QGroupBox(self.frame__image)
        self.groupBox__image.setObjectName(u"groupBox__image")
        self.gridLayout_6 = QGridLayout(self.groupBox__image)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame__img2 = QFrame(self.groupBox__image)
        self.frame__img2.setObjectName(u"frame__img2")
        self.frame__img2.setFrameShape(QFrame.StyledPanel)
        self.frame__img2.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame__img2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_13 = QLabel(self.frame__img2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setBaseSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(36)
        self.label_13.setFont(font)

        self.gridLayout_11.addWidget(self.label_13, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame__img2, 0, 1, 1, 1)

        self.frame__img4 = QFrame(self.groupBox__image)
        self.frame__img4.setObjectName(u"frame__img4")
        self.frame__img4.setFrameShape(QFrame.StyledPanel)
        self.frame__img4.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame__img4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_12 = QLabel(self.frame__img4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setBaseSize(QSize(50, 50))
        self.label_12.setFont(font)

        self.gridLayout_12.addWidget(self.label_12, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame__img4, 1, 1, 1, 1)

        self.frame__img3 = QFrame(self.groupBox__image)
        self.frame__img3.setObjectName(u"frame__img3")
        self.frame__img3.setFrameShape(QFrame.StyledPanel)
        self.frame__img3.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame__img3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label__img3 = QLabel(self.frame__img3)
        self.label__img3.setObjectName(u"label__img3")
        self.label__img3.setBaseSize(QSize(50, 50))
        self.label__img3.setFont(font)

        self.gridLayout_10.addWidget(self.label__img3, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame__img3, 1, 0, 1, 1)

        self.frame__img1 = QFrame(self.groupBox__image)
        self.frame__img1.setObjectName(u"frame__img1")
        self.frame__img1.setFrameShape(QFrame.StyledPanel)
        self.frame__img1.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame__img1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label = QLabel(self.frame__img1)
        self.label.setObjectName(u"label")
        self.label.setBaseSize(QSize(50, 50))
        self.label.setFont(font)

        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame__img1, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox__image, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame__image, 0, 1, 1, 1)

        self.groupBox__build = QGroupBox(self.tab1)
        self.groupBox__build.setObjectName(u"groupBox__build")
        self.gridLayout_24 = QGridLayout(self.groupBox__build)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.progressBar__build = QProgressBar(self.groupBox__build)
        self.progressBar__build.setObjectName(u"progressBar__build")
        self.progressBar__build.setValue(0)

        self.gridLayout_24.addWidget(self.progressBar__build, 0, 0, 1, 1)

        self.pushButton__start = QPushButton(self.groupBox__build)
        self.pushButton__start.setObjectName(u"pushButton__start")

        self.gridLayout_24.addWidget(self.pushButton__start, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox__build, 1, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.tab1)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_23 = QGridLayout(self.groupBox_10)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.horizontalLayout__open = QHBoxLayout()
        self.horizontalLayout__open.setObjectName(u"horizontalLayout__open")
        self.label_7 = QLabel(self.groupBox_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout__open.addWidget(self.label_7)

        self.lineEdit__open = QLineEdit(self.groupBox_10)
        self.lineEdit__open.setObjectName(u"lineEdit__open")
        self.lineEdit__open.setEnabled(False)
        self.lineEdit__open.setReadOnly(True)

        self.horizontalLayout__open.addWidget(self.lineEdit__open)

        self.toolButton__open = QToolButton(self.groupBox_10)
        self.toolButton__open.setObjectName(u"toolButton__open")

        self.horizontalLayout__open.addWidget(self.toolButton__open)

        self.pushButton__open = QPushButton(self.groupBox_10)
        self.pushButton__open.setObjectName(u"pushButton__open")

        self.horizontalLayout__open.addWidget(self.pushButton__open)


        self.gridLayout_23.addLayout(self.horizontalLayout__open, 0, 0, 1, 1)

        self.horizontalLayout__publish = QHBoxLayout()
        self.horizontalLayout__publish.setObjectName(u"horizontalLayout__publish")
        self.label__publish = QLabel(self.groupBox_10)
        self.label__publish.setObjectName(u"label__publish")

        self.horizontalLayout__publish.addWidget(self.label__publish)

        self.comboBox__usr = QComboBox(self.groupBox_10)
        self.comboBox__usr.setObjectName(u"comboBox__usr")

        self.horizontalLayout__publish.addWidget(self.comboBox__usr)

        self.pushButton__publish = QPushButton(self.groupBox_10)
        self.pushButton__publish.setObjectName(u"pushButton__publish")

        self.horizontalLayout__publish.addWidget(self.pushButton__publish)


        self.gridLayout_23.addLayout(self.horizontalLayout__publish, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_10, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2__variation = QWidget()
        self.tab2__variation.setObjectName(u"tab2__variation")
        self.gridLayout_13 = QGridLayout(self.tab2__variation)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox_12 = QGroupBox(self.tab2__variation)
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

        self.scrollArea_2 = QScrollArea(self.tab2__variation)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 198, 389))
        self.gridLayout_14 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
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
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_31.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_31.addWidget(self.label_10, 1, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_16)


        self.gridLayout_14.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_13.addWidget(self.scrollArea_2, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.tab2__variation)
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

        self.groupBox_13 = QGroupBox(self.tab2__variation)
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

        self.tabWidget.addTab(self.tab2__variation, "")

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
        self.menubar.setGeometry(QRect(0, 0, 1290, 20))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_9.setTitle("")
        self.groupBox__grayscale.setTitle(QCoreApplication.translate("MainWindow", u"GrayScale", None))
        self.label__grid.setText(QCoreApplication.translate("MainWindow", u"Main Grid source", None))
        self.toolButton__gird_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Drag & Drop", None))
        self.groupBox__osm.setTitle(QCoreApplication.translate("MainWindow", u"OSM", None))
        self.label__OSM.setText(QCoreApplication.translate("MainWindow", u"Main OSM source", None))
        self.toolButton__osm.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Drag & Drop", None))
        self.groupBox__name.setTitle(QCoreApplication.translate("MainWindow", u"City Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"City Name", None))
        self.groupBox__image.setTitle(QCoreApplication.translate("MainWindow", u"Sample Image", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.label__img3.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IMG 1              ", None))
        self.groupBox__build.setTitle("")
        self.pushButton__start.setText(QCoreApplication.translate("MainWindow", u"Build start", None))
        self.groupBox_10.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Save Location", None))
        self.toolButton__open.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton__open.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.label__publish.setText(QCoreApplication.translate("MainWindow", u"csv data\ub85c username", None))
        self.pushButton__publish.setText(QCoreApplication.translate("MainWindow", u"Publish Shotgrid", None))
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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"weather FX", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"building setting", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2__variation), QCoreApplication.translate("MainWindow", u"Exist City Variation", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"City Setting", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"USD hieararchy", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Draw Mode", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Kind", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Variants", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Primitive Type", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Scene Graph Path", None));
    # retranslateUi

