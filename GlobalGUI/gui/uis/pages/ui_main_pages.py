# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesXtDFID.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1137, 818)
        self.verticalLayout_25 = QVBoxLayout(MainPages)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.Maintenance = QWidget()
        self.Maintenance.setObjectName(u"Maintenance")
        self.horizontalLayout_20 = QHBoxLayout(self.Maintenance)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.Maintenance)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setPointSize(50)
        self.label_15.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_15)

        self.pages.addWidget(self.Maintenance)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton = QPushButton(self.page_1)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_6.addWidget(self.pushButton)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_4 = QPushButton(self.page_1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_14.addWidget(self.pushButton_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_14.addLayout(self.verticalLayout_7)

        self.pushButton_5 = QPushButton(self.page_1)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_14.addWidget(self.pushButton_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.horizontalLayout_14.addLayout(self.verticalLayout_8)

        self.pushButton_6 = QPushButton(self.page_1)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_14.addWidget(self.pushButton_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.horizontalLayout_14.addLayout(self.verticalLayout_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.pushButton_3 = QPushButton(self.page_1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_6.addWidget(self.pushButton_3)


        self.page_1_layout.addLayout(self.verticalLayout_6)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 215, 266))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_p3 = QLabel(self.page_3)
        self.label_p3.setObjectName(u"label_p3")

        self.horizontalLayout.addWidget(self.label_p3)

        self.zabercon_p3 = QPushButton(self.page_3)
        self.zabercon_p3.setObjectName(u"zabercon_p3")

        self.horizontalLayout.addWidget(self.zabercon_p3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.n_devices_p3 = QLabel(self.page_3)
        self.n_devices_p3.setObjectName(u"n_devices_p3")
        self.n_devices_p3.setFont(font1)

        self.horizontalLayout.addWidget(self.n_devices_p3)

        self.check_p3 = QRadioButton(self.page_3)
        self.check_p3.setObjectName(u"check_p3")
        self.check_p3.setCheckable(False)
        self.check_p3.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.check_p3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.globalhome_p3 = QPushButton(self.page_3)
        self.globalhome_p3.setObjectName(u"globalhome_p3")

        self.horizontalLayout_2.addWidget(self.globalhome_p3)

        self.home1_p3 = QPushButton(self.page_3)
        self.home1_p3.setObjectName(u"home1_p3")

        self.horizontalLayout_2.addWidget(self.home1_p3)

        self.home2_p3 = QPushButton(self.page_3)
        self.home2_p3.setObjectName(u"home2_p3")

        self.horizontalLayout_2.addWidget(self.home2_p3)

        self.home3_p3 = QPushButton(self.page_3)
        self.home3_p3.setObjectName(u"home3_p3")

        self.horizontalLayout_2.addWidget(self.home3_p3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.z1_Relative = QCheckBox(self.page_3)
        self.z1_Relative.setObjectName(u"z1_Relative")

        self.horizontalLayout_10.addWidget(self.z1_Relative)

        self.z1_Absolute = QCheckBox(self.page_3)
        self.z1_Absolute.setObjectName(u"z1_Absolute")

        self.horizontalLayout_10.addWidget(self.z1_Absolute)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.z1_cm = QCheckBox(self.page_3)
        self.z1_cm.setObjectName(u"z1_cm")

        self.horizontalLayout_4.addWidget(self.z1_cm)

        self.z1_mm = QCheckBox(self.page_3)
        self.z1_mm.setObjectName(u"z1_mm")

        self.horizontalLayout_4.addWidget(self.z1_mm)

        self.z1_um = QCheckBox(self.page_3)
        self.z1_um.setObjectName(u"z1_um")

        self.horizontalLayout_4.addWidget(self.z1_um)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.z1_data = QLineEdit(self.page_3)
        self.z1_data.setObjectName(u"z1_data")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z1_data.sizePolicy().hasHeightForWidth())
        self.z1_data.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.z1_data)

        self.z1_set = QPushButton(self.page_3)
        self.z1_set.setObjectName(u"z1_set")

        self.horizontalLayout_7.addWidget(self.z1_set)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.z1_slider = QSlider(self.page_3)
        self.z1_slider.setObjectName(u"z1_slider")
        self.z1_slider.setValue(50)
        self.z1_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.z1_slider)

        self.line_3 = QFrame(self.page_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_7)

        self.line_6 = QFrame(self.page_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.z1speed = QLineEdit(self.page_3)
        self.z1speed.setObjectName(u"z1speed")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.z1speed.sizePolicy().hasHeightForWidth())
        self.z1speed.setSizePolicy(sizePolicy1)
        self.z1speed.setMaxLength(200)

        self.horizontalLayout_13.addWidget(self.z1speed)

        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.z1_left = QPushButton(self.page_3)
        self.z1_left.setObjectName(u"z1_left")

        self.horizontalLayout_13.addWidget(self.z1_left)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.z1_right = QPushButton(self.page_3)
        self.z1_right.setObjectName(u"z1_right")

        self.horizontalLayout_13.addWidget(self.z1_right)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.z1_Stop = QPushButton(self.page_3)
        self.z1_Stop.setObjectName(u"z1_Stop")

        self.verticalLayout_3.addWidget(self.z1_Stop)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.line = QFrame(self.page_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.z2_Relative = QCheckBox(self.page_3)
        self.z2_Relative.setObjectName(u"z2_Relative")

        self.horizontalLayout_11.addWidget(self.z2_Relative)

        self.z2_Absolute = QCheckBox(self.page_3)
        self.z2_Absolute.setObjectName(u"z2_Absolute")

        self.horizontalLayout_11.addWidget(self.z2_Absolute)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.z2_cm = QCheckBox(self.page_3)
        self.z2_cm.setObjectName(u"z2_cm")

        self.horizontalLayout_5.addWidget(self.z2_cm)

        self.z2_mm = QCheckBox(self.page_3)
        self.z2_mm.setObjectName(u"z2_mm")

        self.horizontalLayout_5.addWidget(self.z2_mm)

        self.z2_um = QCheckBox(self.page_3)
        self.z2_um.setObjectName(u"z2_um")

        self.horizontalLayout_5.addWidget(self.z2_um)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.z2_data = QLineEdit(self.page_3)
        self.z2_data.setObjectName(u"z2_data")
        sizePolicy.setHeightForWidth(self.z2_data.sizePolicy().hasHeightForWidth())
        self.z2_data.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.z2_data)

        self.z2_Set = QPushButton(self.page_3)
        self.z2_Set.setObjectName(u"z2_Set")

        self.horizontalLayout_8.addWidget(self.z2_Set)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.z2_slider = QSlider(self.page_3)
        self.z2_slider.setObjectName(u"z2_slider")
        self.z2_slider.setValue(50)
        self.z2_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.z2_slider)

        self.line_4 = QFrame(self.page_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)

        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.line_7 = QFrame(self.page_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_7)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.z2speed = QLineEdit(self.page_3)
        self.z2speed.setObjectName(u"z2speed")

        self.horizontalLayout_15.addWidget(self.z2speed)

        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_15.addWidget(self.label_11)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)

        self.z2_left = QPushButton(self.page_3)
        self.z2_left.setObjectName(u"z2_left")

        self.horizontalLayout_15.addWidget(self.z2_left)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)

        self.z2_right = QPushButton(self.page_3)
        self.z2_right.setObjectName(u"z2_right")

        self.horizontalLayout_15.addWidget(self.z2_right)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.z2_Stop = QPushButton(self.page_3)
        self.z2_Stop.setObjectName(u"z2_Stop")

        self.verticalLayout_4.addWidget(self.z2_Stop)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.line_2 = QFrame(self.page_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.z3_Relative = QCheckBox(self.page_3)
        self.z3_Relative.setObjectName(u"z3_Relative")

        self.horizontalLayout_12.addWidget(self.z3_Relative)

        self.z3_Absolute = QCheckBox(self.page_3)
        self.z3_Absolute.setObjectName(u"z3_Absolute")

        self.horizontalLayout_12.addWidget(self.z3_Absolute)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.z3_cm = QCheckBox(self.page_3)
        self.z3_cm.setObjectName(u"z3_cm")

        self.horizontalLayout_6.addWidget(self.z3_cm)

        self.z3_mm = QCheckBox(self.page_3)
        self.z3_mm.setObjectName(u"z3_mm")

        self.horizontalLayout_6.addWidget(self.z3_mm)

        self.z3_um = QCheckBox(self.page_3)
        self.z3_um.setObjectName(u"z3_um")

        self.horizontalLayout_6.addWidget(self.z3_um)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.z3_data = QLineEdit(self.page_3)
        self.z3_data.setObjectName(u"z3_data")
        sizePolicy.setHeightForWidth(self.z3_data.sizePolicy().hasHeightForWidth())
        self.z3_data.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.z3_data)

        self.z3_Set = QPushButton(self.page_3)
        self.z3_Set.setObjectName(u"z3_Set")

        self.horizontalLayout_9.addWidget(self.z3_Set)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.z3_slider = QSlider(self.page_3)
        self.z3_slider.setObjectName(u"z3_slider")
        self.z3_slider.setValue(50)
        self.z3_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.z3_slider)

        self.line_5 = QFrame(self.page_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_5)

        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.line_8 = QFrame(self.page_3)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_8)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.z3speed = QLineEdit(self.page_3)
        self.z3speed.setObjectName(u"z3speed")

        self.horizontalLayout_16.addWidget(self.z3speed)

        self.label_12 = QLabel(self.page_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.z3_left = QPushButton(self.page_3)
        self.z3_left.setObjectName(u"z3_left")

        self.horizontalLayout_16.addWidget(self.z3_left)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)

        self.z3_right = QPushButton(self.page_3)
        self.z3_right.setObjectName(u"z3_right")

        self.horizontalLayout_16.addWidget(self.z3_right)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.z3_Stop = QPushButton(self.page_3)
        self.z3_Stop.setObjectName(u"z3_Stop")

        self.verticalLayout_5.addWidget(self.z3_Stop)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.Daq_Signal = QHBoxLayout()
        self.Daq_Signal.setObjectName(u"Daq_Signal")

        self.verticalLayout_2.addLayout(self.Daq_Signal)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.Keyboard_p3 = QPushButton(self.page_3)
        self.Keyboard_p3.setObjectName(u"Keyboard_p3")

        self.verticalLayout_2.addWidget(self.Keyboard_p3)


        self.page_3_layout.addLayout(self.verticalLayout_2)

        self.pages.addWidget(self.page_3)
        self.page_calib = QWidget()
        self.page_calib.setObjectName(u"page_calib")
        self.verticalLayout_11 = QVBoxLayout(self.page_calib)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_13 = QLabel(self.page_calib)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.label_13)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_8)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.but_start_weight = QPushButton(self.page_calib)
        self.but_start_weight.setObjectName(u"but_start_weight")

        self.gridLayout_9.addWidget(self.but_start_weight, 4, 0, 1, 1)

        self.label_32 = QLabel(self.page_calib)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_9.addWidget(self.label_32, 1, 0, 1, 1)

        self.label_29 = QLabel(self.page_calib)
        self.label_29.setObjectName(u"label_29")
        sizePolicy2.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy2)

        self.gridLayout_9.addWidget(self.label_29, 0, 0, 1, 1)

        self.label_33 = QLabel(self.page_calib)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_9.addWidget(self.label_33, 6, 0, 1, 1)

        self.label_36 = QLabel(self.page_calib)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_9.addWidget(self.label_36, 8, 0, 1, 1)

        self.label_grams = QLabel(self.page_calib)
        self.label_grams.setObjectName(u"label_grams")
        sizePolicy2.setHeightForWidth(self.label_grams.sizePolicy().hasHeightForWidth())
        self.label_grams.setSizePolicy(sizePolicy2)

        self.gridLayout_9.addWidget(self.label_grams, 0, 1, 1, 1)

        self.comboBox_weight_Format = QComboBox(self.page_calib)
        self.comboBox_weight_Format.addItem("")
        self.comboBox_weight_Format.addItem("")
        self.comboBox_weight_Format.setObjectName(u"comboBox_weight_Format")

        self.gridLayout_9.addWidget(self.comboBox_weight_Format, 9, 0, 1, 1)

        self.label_31 = QLabel(self.page_calib)
        self.label_31.setObjectName(u"label_31")
        sizePolicy2.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy2)

        self.gridLayout_9.addWidget(self.label_31, 0, 2, 1, 1)

        self.label_30 = QLabel(self.page_calib)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_9.addWidget(self.label_30, 1, 2, 1, 1)

        self.comboBox_weight_port = QComboBox(self.page_calib)
        self.comboBox_weight_port.addItem("")
        self.comboBox_weight_port.addItem("")
        self.comboBox_weight_port.addItem("")
        self.comboBox_weight_port.addItem("")
        self.comboBox_weight_port.addItem("")
        self.comboBox_weight_port.addItem("")
        self.comboBox_weight_port.addItem("")
        self.comboBox_weight_port.addItem("")
        self.comboBox_weight_port.addItem("")
        self.comboBox_weight_port.setObjectName(u"comboBox_weight_port")

        self.gridLayout_9.addWidget(self.comboBox_weight_port, 7, 0, 1, 1)

        self.label_flowrate = QLabel(self.page_calib)
        self.label_flowrate.setObjectName(u"label_flowrate")

        self.gridLayout_9.addWidget(self.label_flowrate, 1, 1, 1, 1)

        self.Reset_zero_but = QPushButton(self.page_calib)
        self.Reset_zero_but.setObjectName(u"Reset_zero_but")

        self.gridLayout_9.addWidget(self.Reset_zero_but, 4, 1, 1, 1)

        self.but_stop_weight = QPushButton(self.page_calib)
        self.but_stop_weight.setObjectName(u"but_stop_weight")

        self.gridLayout_9.addWidget(self.but_stop_weight, 4, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_9, 10, 0, 1, 1)

        self.line_9 = QFrame(self.page_calib)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_9, 2, 0, 1, 1)

        self.line_10 = QFrame(self.page_calib)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_10, 2, 1, 1, 1)

        self.line_11 = QFrame(self.page_calib)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_11, 2, 2, 1, 1)

        self.lineEdit_weight_directory = QLineEdit(self.page_calib)
        self.lineEdit_weight_directory.setObjectName(u"lineEdit_weight_directory")
        sizePolicy.setHeightForWidth(self.lineEdit_weight_directory.sizePolicy().hasHeightForWidth())
        self.lineEdit_weight_directory.setSizePolicy(sizePolicy)

        self.gridLayout_9.addWidget(self.lineEdit_weight_directory, 9, 1, 1, 1)

        self.but_confirm_weight = QPushButton(self.page_calib)
        self.but_confirm_weight.setObjectName(u"but_confirm_weight")

        self.gridLayout_9.addWidget(self.but_confirm_weight, 7, 1, 1, 1)

        self.label_34 = QLabel(self.page_calib)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_9.addWidget(self.label_34, 8, 1, 1, 1)

        self.lineEdit_weight_FileName = QLineEdit(self.page_calib)
        self.lineEdit_weight_FileName.setObjectName(u"lineEdit_weight_FileName")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_weight_FileName.sizePolicy().hasHeightForWidth())
        self.lineEdit_weight_FileName.setSizePolicy(sizePolicy3)

        self.gridLayout_9.addWidget(self.lineEdit_weight_FileName, 9, 2, 1, 1)

        self.label_35 = QLabel(self.page_calib)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_9.addWidget(self.label_35, 8, 2, 1, 1)


        self.verticalLayout_34.addLayout(self.gridLayout_9)


        self.horizontalLayout_17.addLayout(self.verticalLayout_34)

        self.Weigh_Layout = QVBoxLayout()
        self.Weigh_Layout.setObjectName(u"Weigh_Layout")
        self.Weigh_Layout.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_17.addLayout(self.Weigh_Layout)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.pages.addWidget(self.page_calib)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_5 = QGridLayout(self.page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Page_Name = QLabel(self.page)
        self.Page_Name.setObjectName(u"Page_Name")
        self.Page_Name.setMaximumSize(QSize(500, 16777215))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.Page_Name.setFont(font2)

        self.gridLayout_5.addWidget(self.Page_Name, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.page)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.widget_4 = QWidget(self.widget_6)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(550, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.widget_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.Parameters = QWidget(self.widget_4)
        self.Parameters.setObjectName(u"Parameters")
        self.Parameters.setMaximumSize(QSize(926, 370))
        self.gridLayout = QGridLayout(self.Parameters)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_outputFormat_2 = QWidget(self.Parameters)
        self.widget_outputFormat_2.setObjectName(u"widget_outputFormat_2")
        self.verticalLayout_21 = QVBoxLayout(self.widget_outputFormat_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_format_2 = QLabel(self.widget_outputFormat_2)
        self.label_format_2.setObjectName(u"label_format_2")

        self.verticalLayout_21.addWidget(self.label_format_2)

        self.textEdit_DAQ_Device = QTextEdit(self.widget_outputFormat_2)
        self.textEdit_DAQ_Device.setObjectName(u"textEdit_DAQ_Device")

        self.verticalLayout_21.addWidget(self.textEdit_DAQ_Device)


        self.gridLayout.addWidget(self.widget_outputFormat_2, 2, 1, 1, 1)

        self.widget_numberSamples = QWidget(self.Parameters)
        self.widget_numberSamples.setObjectName(u"widget_numberSamples")
        self.verticalLayout_15 = QVBoxLayout(self.widget_numberSamples)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_samples = QLabel(self.widget_numberSamples)
        self.label_samples.setObjectName(u"label_samples")

        self.verticalLayout_15.addWidget(self.label_samples)

        self.textEdit = QTextEdit(self.widget_numberSamples)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_15.addWidget(self.textEdit)


        self.gridLayout.addWidget(self.widget_numberSamples, 4, 2, 1, 1)

        self.widget_SampleFrequency = QWidget(self.Parameters)
        self.widget_SampleFrequency.setObjectName(u"widget_SampleFrequency")
        self.verticalLayout_13 = QVBoxLayout(self.widget_SampleFrequency)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_freq = QLabel(self.widget_SampleFrequency)
        self.label_freq.setObjectName(u"label_freq")

        self.verticalLayout_13.addWidget(self.label_freq)

        self.textEdit_SampleFrequency = QTextEdit(self.widget_SampleFrequency)
        self.textEdit_SampleFrequency.setObjectName(u"textEdit_SampleFrequency")

        self.verticalLayout_13.addWidget(self.textEdit_SampleFrequency)


        self.gridLayout.addWidget(self.widget_SampleFrequency, 4, 1, 1, 1)

        self.widget_outputFormat_3 = QWidget(self.Parameters)
        self.widget_outputFormat_3.setObjectName(u"widget_outputFormat_3")
        self.verticalLayout_22 = QVBoxLayout(self.widget_outputFormat_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_Port_Arduino = QLabel(self.widget_outputFormat_3)
        self.label_Port_Arduino.setObjectName(u"label_Port_Arduino")

        self.verticalLayout_22.addWidget(self.label_Port_Arduino)

        self.comboBox_3 = QComboBox(self.widget_outputFormat_3)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_22.addWidget(self.comboBox_3)


        self.gridLayout.addWidget(self.widget_outputFormat_3, 2, 2, 1, 1)

        self.widget_lowfreq = QWidget(self.Parameters)
        self.widget_lowfreq.setObjectName(u"widget_lowfreq")
        self.verticalLayout_14 = QVBoxLayout(self.widget_lowfreq)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_lowfreq = QLabel(self.widget_lowfreq)
        self.label_lowfreq.setObjectName(u"label_lowfreq")

        self.verticalLayout_14.addWidget(self.label_lowfreq)

        self.textEdit_lowfreq = QTextEdit(self.widget_lowfreq)
        self.textEdit_lowfreq.setObjectName(u"textEdit_lowfreq")

        self.verticalLayout_14.addWidget(self.textEdit_lowfreq)


        self.gridLayout.addWidget(self.widget_lowfreq, 5, 2, 1, 2)

        self.widget_outputFormat = QWidget(self.Parameters)
        self.widget_outputFormat.setObjectName(u"widget_outputFormat")
        self.verticalLayout_17 = QVBoxLayout(self.widget_outputFormat)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_format = QLabel(self.widget_outputFormat)
        self.label_format.setObjectName(u"label_format")

        self.verticalLayout_17.addWidget(self.label_format)

        self.comboBox = QComboBox(self.widget_outputFormat)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_17.addWidget(self.comboBox)


        self.gridLayout.addWidget(self.widget_outputFormat, 6, 4, 1, 1)

        self.widget_highfreq = QWidget(self.Parameters)
        self.widget_highfreq.setObjectName(u"widget_highfreq")
        self.verticalLayout_18 = QVBoxLayout(self.widget_highfreq)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_highfreq = QLabel(self.widget_highfreq)
        self.label_highfreq.setObjectName(u"label_highfreq")

        self.verticalLayout_18.addWidget(self.label_highfreq)

        self.textEdit_highfreq = QTextEdit(self.widget_highfreq)
        self.textEdit_highfreq.setObjectName(u"textEdit_highfreq")

        self.verticalLayout_18.addWidget(self.textEdit_highfreq)


        self.gridLayout.addWidget(self.widget_highfreq, 5, 4, 1, 1)

        self.widget_namefile = QWidget(self.Parameters)
        self.widget_namefile.setObjectName(u"widget_namefile")
        self.verticalLayout_16 = QVBoxLayout(self.widget_namefile)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_file = QLabel(self.widget_namefile)
        self.label_file.setObjectName(u"label_file")

        self.verticalLayout_16.addWidget(self.label_file)

        self.textEdit_numberSamples_2 = QTextEdit(self.widget_namefile)
        self.textEdit_numberSamples_2.setObjectName(u"textEdit_numberSamples_2")

        self.verticalLayout_16.addWidget(self.textEdit_numberSamples_2)


        self.gridLayout.addWidget(self.widget_namefile, 6, 2, 1, 2)

        self.widget_Luminosity = QWidget(self.Parameters)
        self.widget_Luminosity.setObjectName(u"widget_Luminosity")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_Luminosity)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_intensity = QLabel(self.widget_Luminosity)
        self.label_intensity.setObjectName(u"label_intensity")

        self.horizontalLayout_19.addWidget(self.label_intensity)

        self.intensity_spin_box = QSpinBox(self.widget_Luminosity)
        self.intensity_spin_box.setObjectName(u"intensity_spin_box")
        self.intensity_spin_box.setMaximum(20)
        self.intensity_spin_box.setValue(1)

        self.horizontalLayout_19.addWidget(self.intensity_spin_box)


        self.gridLayout.addWidget(self.widget_Luminosity, 4, 3, 1, 2)

        self.widget_mean = QWidget(self.Parameters)
        self.widget_mean.setObjectName(u"widget_mean")
        self.verticalLayout_20 = QVBoxLayout(self.widget_mean)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_mean = QLabel(self.widget_mean)
        self.label_mean.setObjectName(u"label_mean")

        self.verticalLayout_20.addWidget(self.label_mean)

        self.textEdit_mean = QTextEdit(self.widget_mean)
        self.textEdit_mean.setObjectName(u"textEdit_mean")

        self.verticalLayout_20.addWidget(self.textEdit_mean)


        self.gridLayout.addWidget(self.widget_mean, 5, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_13, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 4, 5, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 6, 5, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 8, 4, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 8, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 1, 4, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 8, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 5, 5, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 4, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 5, 0, 1, 1)

        self.widget_directoryFile = QWidget(self.Parameters)
        self.widget_directoryFile.setObjectName(u"widget_directoryFile")
        self.verticalLayout_19 = QVBoxLayout(self.widget_directoryFile)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_directory = QLabel(self.widget_directoryFile)
        self.label_directory.setObjectName(u"label_directory")

        self.verticalLayout_19.addWidget(self.label_directory)

        self.textEdit_numberSamples_3 = QTextEdit(self.widget_directoryFile)
        self.textEdit_numberSamples_3.setObjectName(u"textEdit_numberSamples_3")

        self.verticalLayout_19.addWidget(self.textEdit_numberSamples_3)


        self.gridLayout.addWidget(self.widget_directoryFile, 7, 1, 1, 1)

        self.widget_outputFormat_4 = QWidget(self.Parameters)
        self.widget_outputFormat_4.setObjectName(u"widget_outputFormat_4")
        self.verticalLayout_23 = QVBoxLayout(self.widget_outputFormat_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_format_3 = QLabel(self.widget_outputFormat_4)
        self.label_format_3.setObjectName(u"label_format_3")

        self.verticalLayout_23.addWidget(self.label_format_3)

        self.textEdit_Bauds = QTextEdit(self.widget_outputFormat_4)
        self.textEdit_Bauds.setObjectName(u"textEdit_Bauds")

        self.verticalLayout_23.addWidget(self.textEdit_Bauds)


        self.gridLayout.addWidget(self.widget_outputFormat_4, 6, 1, 1, 1)

        self.portsButton = QPushButton(self.Parameters)
        self.portsButton.setObjectName(u"portsButton")
        self.portsButton.setMaximumSize(QSize(200, 25))

        self.gridLayout.addWidget(self.portsButton, 3, 4, 1, 1)

        self.widget_outputFormat_5 = QWidget(self.Parameters)
        self.widget_outputFormat_5.setObjectName(u"widget_outputFormat_5")
        self.verticalLayout_24 = QVBoxLayout(self.widget_outputFormat_5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_format_4 = QLabel(self.widget_outputFormat_5)
        self.label_format_4.setObjectName(u"label_format_4")

        self.verticalLayout_24.addWidget(self.label_format_4)

        self.textEdit_DAQ_Device_2 = QTextEdit(self.widget_outputFormat_5)
        self.textEdit_DAQ_Device_2.setObjectName(u"textEdit_DAQ_Device_2")

        self.verticalLayout_24.addWidget(self.textEdit_DAQ_Device_2)


        self.gridLayout.addWidget(self.widget_outputFormat_5, 2, 4, 1, 1)


        self.verticalLayout_12.addWidget(self.Parameters)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Ok_Button = QPushButton(self.widget_5)
        self.Ok_Button.setObjectName(u"Ok_Button")
        self.Ok_Button.setMaximumSize(QSize(100, 25))

        self.gridLayout_4.addWidget(self.Ok_Button, 0, 4, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_17, 0, 2, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(197, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_14, 2, 4, 2, 1)

        self.horizontalSpacer_15 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_15, 2, 1, 2, 1)

        self.Save_Data = QPushButton(self.widget_5)
        self.Save_Data.setObjectName(u"Save_Data")
        self.Save_Data.setMaximumSize(QSize(80, 25))

        self.gridLayout_4.addWidget(self.Save_Data, 0, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.widget_5)

        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.LayoutColor = QHBoxLayout()
        self.LayoutColor.setObjectName(u"LayoutColor")

        self.gridLayout_2.addLayout(self.LayoutColor, 1, 0, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.widget)


        self.horizontalLayout_18.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.widget_6)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.LayoutLaser = QVBoxLayout()
        self.LayoutLaser.setObjectName(u"LayoutLaser")

        self.gridLayout_3.addLayout(self.LayoutLaser, 0, 0, 1, 1)

        self.widget_19 = QWidget(self.widget_3)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(200, 0))
        self.widget_19.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton_Reference = QPushButton(self.widget_19)
        self.pushButton_Reference.setObjectName(u"pushButton_Reference")
        self.pushButton_Reference.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_28.addWidget(self.pushButton_Reference)

        self.pushButton_Clear = QPushButton(self.widget_19)
        self.pushButton_Clear.setObjectName(u"pushButton_Clear")
        self.pushButton_Clear.setMinimumSize(QSize(100, 0))
        self.pushButton_Clear.setMaximumSize(QSize(130, 30))

        self.horizontalLayout_28.addWidget(self.pushButton_Clear)


        self.gridLayout_3.addWidget(self.widget_19, 1, 0, 1, 1)

        self.label_reference = QLabel(self.widget_3)
        self.label_reference.setObjectName(u"label_reference")
        self.label_reference.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_3.addWidget(self.label_reference, 2, 0, 1, 1)


        self.horizontalLayout_18.addWidget(self.widget_3)


        self.gridLayout_5.addWidget(self.widget_6, 1, 0, 1, 1)

        self.pages.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_32 = QVBoxLayout(self.page_4)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_28 = QLabel(self.page_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(150, 50))
        self.label_28.setMaximumSize(QSize(200, 50))
        font3 = QFont()
        font3.setPointSize(29)
        self.label_28.setFont(font3)

        self.verticalLayout_32.addWidget(self.label_28)

        self.widget_10 = QWidget(self.page_4)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.pushButton_8 = QPushButton(self.widget_10)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_24.addWidget(self.pushButton_8)

        self.horizontalSpacer_16 = QSpacerItem(414, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_16)

        self.pushButton_7 = QPushButton(self.widget_10)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_24.addWidget(self.pushButton_7)

        self.horizontalSpacer_17 = QSpacerItem(414, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_17)

        self.pushButton_11 = QPushButton(self.widget_10)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_24.addWidget(self.pushButton_11)


        self.verticalLayout_32.addWidget(self.widget_10)

        self.widget_9 = QWidget(self.page_4)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.widget_2 = QWidget(self.widget_9)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(290, 150))
        self.widget_2.setMaximumSize(QSize(250, 120))
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(90, 50))
        self.widget_7.setMaximumSize(QSize(130, 50))
        self.verticalLayout_26 = QVBoxLayout(self.widget_7)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_16 = QLabel(self.widget_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(71, 16))

        self.verticalLayout_26.addWidget(self.label_16)

        self.label_17 = QLabel(self.widget_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(71, 16))

        self.verticalLayout_26.addWidget(self.label_17)


        self.gridLayout_6.addWidget(self.widget_7, 0, 2, 1, 1)

        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(90, 50))
        self.widget_8.setMaximumSize(QSize(130, 50))
        self.verticalLayout_27 = QVBoxLayout(self.widget_8)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_18 = QLabel(self.widget_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(100, 16))

        self.verticalLayout_27.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget_8)
        self.label_19.setObjectName(u"label_19")
        font4 = QFont()
        font4.setPointSize(8)
        self.label_19.setFont(font4)
        self.label_19.setCursor(QCursor(Qt.ArrowCursor))

        self.verticalLayout_27.addWidget(self.label_19)


        self.gridLayout_6.addWidget(self.widget_8, 1, 2, 1, 1)

        self.radioButton = QRadioButton(self.widget_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMaximumSize(QSize(120, 20))

        self.gridLayout_6.addWidget(self.radioButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_6.addWidget(self.pushButton_2, 2, 2, 1, 1)

        self.verticalSlider = QSlider(self.widget_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(200)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_6.addWidget(self.verticalSlider, 0, 1, 3, 1)


        self.horizontalLayout_25.addWidget(self.widget_2)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")

        self.horizontalLayout_25.addLayout(self.horizontalLayout_21)


        self.verticalLayout_32.addWidget(self.widget_9)

        self.widget_11 = QWidget(self.page_4)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(290, 150))
        self.widget_12.setMaximumSize(QSize(250, 120))
        self.gridLayout_7 = QGridLayout(self.widget_12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(90, 50))
        self.widget_13.setMaximumSize(QSize(130, 50))
        self.verticalLayout_28 = QVBoxLayout(self.widget_13)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_20 = QLabel(self.widget_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(71, 16))

        self.verticalLayout_28.addWidget(self.label_20)

        self.label_21 = QLabel(self.widget_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(71, 16))

        self.verticalLayout_28.addWidget(self.label_21)


        self.gridLayout_7.addWidget(self.widget_13, 0, 2, 1, 1)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(90, 50))
        self.widget_14.setMaximumSize(QSize(130, 50))
        self.verticalLayout_29 = QVBoxLayout(self.widget_14)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_22 = QLabel(self.widget_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(100, 16))

        self.verticalLayout_29.addWidget(self.label_22)

        self.label_23 = QLabel(self.widget_14)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_29.addWidget(self.label_23)


        self.gridLayout_7.addWidget(self.widget_14, 1, 2, 1, 1)

        self.radioButton_2 = QRadioButton(self.widget_12)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMaximumSize(QSize(120, 20))

        self.gridLayout_7.addWidget(self.radioButton_2, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.widget_12)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_7.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.verticalSlider_2 = QSlider(self.widget_12)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setMaximum(200)
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.gridLayout_7.addWidget(self.verticalSlider_2, 0, 1, 3, 1)


        self.horizontalLayout_26.addWidget(self.widget_12)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")

        self.horizontalLayout_26.addLayout(self.horizontalLayout_22)


        self.verticalLayout_32.addWidget(self.widget_11)

        self.widget_15 = QWidget(self.page_4)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(290, 150))
        self.widget_16.setMaximumSize(QSize(250, 120))
        self.gridLayout_8 = QGridLayout(self.widget_16)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(90, 50))
        self.widget_17.setMaximumSize(QSize(130, 50))
        self.verticalLayout_30 = QVBoxLayout(self.widget_17)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_24 = QLabel(self.widget_17)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(71, 16))

        self.verticalLayout_30.addWidget(self.label_24)

        self.label_25 = QLabel(self.widget_17)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(71, 16))

        self.verticalLayout_30.addWidget(self.label_25)


        self.gridLayout_8.addWidget(self.widget_17, 0, 2, 1, 1)

        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(90, 50))
        self.widget_18.setMaximumSize(QSize(130, 50))
        self.verticalLayout_31 = QVBoxLayout(self.widget_18)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_26 = QLabel(self.widget_18)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(100, 16))

        self.verticalLayout_31.addWidget(self.label_26)

        self.label_27 = QLabel(self.widget_18)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_31.addWidget(self.label_27)


        self.gridLayout_8.addWidget(self.widget_18, 1, 2, 1, 1)

        self.radioButton_3 = QRadioButton(self.widget_16)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMaximumSize(QSize(120, 20))

        self.gridLayout_8.addWidget(self.radioButton_3, 0, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.widget_16)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_8.addWidget(self.pushButton_10, 2, 2, 1, 1)

        self.verticalSlider_3 = QSlider(self.widget_16)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setMaximum(200)
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.gridLayout_8.addWidget(self.verticalSlider_3, 0, 1, 3, 1)


        self.horizontalLayout_27.addWidget(self.widget_16)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")

        self.horizontalLayout_27.addLayout(self.horizontalLayout_23)


        self.verticalLayout_32.addWidget(self.widget_15)

        self.pages.addWidget(self.page_4)

        self.verticalLayout_25.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_15.setText(QCoreApplication.translate("MainPages", u"In maintenance", None))
        self.pushButton.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.label_p3.setText(QCoreApplication.translate("MainPages", u"CHECK CONNECTION", None))
        self.zabercon_p3.setText(QCoreApplication.translate("MainPages", u"CONNECT", None))
        self.n_devices_p3.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:10pt;\"># Devices</span></p></body></html>", None))
        self.check_p3.setText(QCoreApplication.translate("MainPages", u"Available", None))
        self.globalhome_p3.setText(QCoreApplication.translate("MainPages", u"Reset Connection", None))
        self.home1_p3.setText(QCoreApplication.translate("MainPages", u"Home 1", None))
        self.home2_p3.setText(QCoreApplication.translate("MainPages", u"Home 2", None))
        self.home3_p3.setText(QCoreApplication.translate("MainPages", u"Home 3", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p align=\"center\">Zaber 1</p></body></html>", None))
        self.z1_Relative.setText(QCoreApplication.translate("MainPages", u"Relative", None))
        self.z1_Absolute.setText(QCoreApplication.translate("MainPages", u"Absolute", None))
        self.z1_cm.setText(QCoreApplication.translate("MainPages", u"cm", None))
        self.z1_mm.setText(QCoreApplication.translate("MainPages", u"mm", None))
        self.z1_um.setText(QCoreApplication.translate("MainPages", u"um", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:9pt;\">Distance: </span></p></body></html>", None))
        self.z1_set.setText(QCoreApplication.translate("MainPages", u"SET", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Move at constant speed</span></p></body></html>", None))
        self.z1speed.setText(QCoreApplication.translate("MainPages", u"0.2", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:10pt;\">mm/s</span></p></body></html>", None))
        self.z1_left.setText(QCoreApplication.translate("MainPages", u"<<", None))
        self.z1_right.setText(QCoreApplication.translate("MainPages", u">>", None))
        self.z1_Stop.setText(QCoreApplication.translate("MainPages", u"STOP", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p align=\"center\">Zaber 2</p></body></html>", None))
        self.z2_Relative.setText(QCoreApplication.translate("MainPages", u"Relative", None))
        self.z2_Absolute.setText(QCoreApplication.translate("MainPages", u"Absolute", None))
        self.z2_cm.setText(QCoreApplication.translate("MainPages", u"cm", None))
        self.z2_mm.setText(QCoreApplication.translate("MainPages", u"mm", None))
        self.z2_um.setText(QCoreApplication.translate("MainPages", u"um", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:9pt;\">Distance</span></p></body></html>", None))
        self.z2_Set.setText(QCoreApplication.translate("MainPages", u"Set", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Move at constant speed</span></p></body></html>", None))
        self.z2speed.setText(QCoreApplication.translate("MainPages", u"0.2", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:10pt;\">mm/s</span></p></body></html>", None))
        self.z2_left.setText(QCoreApplication.translate("MainPages", u"<<", None))
        self.z2_right.setText(QCoreApplication.translate("MainPages", u">>", None))
        self.z2_Stop.setText(QCoreApplication.translate("MainPages", u"STOP", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p align=\"center\">Zaber 3</p></body></html>", None))
        self.z3_Relative.setText(QCoreApplication.translate("MainPages", u"Relative", None))
        self.z3_Absolute.setText(QCoreApplication.translate("MainPages", u"Absolute", None))
        self.z3_cm.setText(QCoreApplication.translate("MainPages", u"cm", None))
        self.z3_mm.setText(QCoreApplication.translate("MainPages", u"mm", None))
        self.z3_um.setText(QCoreApplication.translate("MainPages", u"um", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:9pt;\">Distance</span></p></body></html>", None))
        self.z3_Set.setText(QCoreApplication.translate("MainPages", u"Set", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Move at constant speed</span></p></body></html>", None))
        self.z3speed.setText(QCoreApplication.translate("MainPages", u"0.2", None))
        self.label_12.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:10pt;\">mm/s</span></p></body></html>", None))
        self.z3_left.setText(QCoreApplication.translate("MainPages", u"<<", None))
        self.z3_right.setText(QCoreApplication.translate("MainPages", u">>", None))
        self.z3_Stop.setText(QCoreApplication.translate("MainPages", u"STOP", None))
        self.Keyboard_p3.setText(QCoreApplication.translate("MainPages", u"Keyboard", None))
        self.label_13.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Weight Analysis</span></p></body></html>", None))
        self.but_start_weight.setText(QCoreApplication.translate("MainPages", u"Start", None))
        self.label_32.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Rate of change:</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Grams:</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainPages", u"Channel port", None))
        self.label_36.setText(QCoreApplication.translate("MainPages", u"Format", None))
        self.label_grams.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:12pt;\">0.00</span></p></body></html>", None))
        self.comboBox_weight_Format.setItemText(0, QCoreApplication.translate("MainPages", u".mat", None))
        self.comboBox_weight_Format.setItemText(1, QCoreApplication.translate("MainPages", u".csv", None))

        self.label_31.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:12pt;\">[g]</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:12pt;\">[mL/s]</span></p></body></html>", None))
        self.comboBox_weight_port.setItemText(0, QCoreApplication.translate("MainPages", u"COM1", None))
        self.comboBox_weight_port.setItemText(1, QCoreApplication.translate("MainPages", u"COM2", None))
        self.comboBox_weight_port.setItemText(2, QCoreApplication.translate("MainPages", u"COM3", None))
        self.comboBox_weight_port.setItemText(3, QCoreApplication.translate("MainPages", u"COM4", None))
        self.comboBox_weight_port.setItemText(4, QCoreApplication.translate("MainPages", u"COM5", None))
        self.comboBox_weight_port.setItemText(5, QCoreApplication.translate("MainPages", u"COM6", None))
        self.comboBox_weight_port.setItemText(6, QCoreApplication.translate("MainPages", u"COM7", None))
        self.comboBox_weight_port.setItemText(7, QCoreApplication.translate("MainPages", u"COM8", None))
        self.comboBox_weight_port.setItemText(8, QCoreApplication.translate("MainPages", u"COM9", None))

        self.label_flowrate.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:12pt;\">0.00</span></p></body></html>", None))
        self.Reset_zero_but.setText(QCoreApplication.translate("MainPages", u"Reset to Zero", None))
        self.but_stop_weight.setText(QCoreApplication.translate("MainPages", u"Stop", None))
        self.but_confirm_weight.setText(QCoreApplication.translate("MainPages", u"Confirm", None))
        self.label_34.setText(QCoreApplication.translate("MainPages", u"File Directory", None))
        self.label_35.setText(QCoreApplication.translate("MainPages", u"File Name", None))
        self.Page_Name.setText(QCoreApplication.translate("MainPages", u"Lasercito", None))
        self.label_format_2.setText(QCoreApplication.translate("MainPages", u"Select device Laser", None))
        self.textEdit_DAQ_Device.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">Dev1/ai0</span></p></body></html>", None))
        self.label_samples.setText(QCoreApplication.translate("MainPages", u"Number of samples", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">4096</span></p></body></html>", None))
        self.label_freq.setText(QCoreApplication.translate("MainPages", u"Sample Frequency:", None))
        self.textEdit_SampleFrequency.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">500000</span></p></body></html>", None))
        self.label_Port_Arduino.setText(QCoreApplication.translate("MainPages", u"Select Arduino Port", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainPages", u"com1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainPages", u"com2", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainPages", u"com3", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainPages", u"com4", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainPages", u"com5", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainPages", u"com6", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainPages", u"com7", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainPages", u"com8", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainPages", u"com9", None))

        self.label_lowfreq.setText(QCoreApplication.translate("MainPages", u"Low frequency filter", None))
        self.textEdit_lowfreq.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">100</span></p></body></html>", None))
        self.label_format.setText(QCoreApplication.translate("MainPages", u"Output Format", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainPages", u".mat", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainPages", u".txt", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainPages", u".csv", None))

        self.label_highfreq.setText(QCoreApplication.translate("MainPages", u"High frequency filter", None))
        self.textEdit_highfreq.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">8000</span></p></body></html>", None))
        self.label_file.setText(QCoreApplication.translate("MainPages", u"Name File", None))
        self.textEdit_numberSamples_2.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">data_try</span></p></body></html>", None))
        self.label_intensity.setText(QCoreApplication.translate("MainPages", u"luminosity", None))
        self.label_mean.setText(QCoreApplication.translate("MainPages", u"Number to mean", None))
        self.textEdit_mean.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">3</span></p></body></html>", None))
        self.label_directory.setText(QCoreApplication.translate("MainPages", u"Directory File", None))
        self.textEdit_numberSamples_3.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.label_format_3.setText(QCoreApplication.translate("MainPages", u"Enter number of data to save", None))
        self.textEdit_Bauds.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">20</span></p></body></html>", None))
        self.portsButton.setText(QCoreApplication.translate("MainPages", u"Confirm Ports", None))
        self.label_format_4.setText(QCoreApplication.translate("MainPages", u"Select device Photo Diode", None))
        self.textEdit_DAQ_Device_2.setHtml(QCoreApplication.translate("MainPages", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">Dev1/ai1</span></p></body></html>", None))
        self.Ok_Button.setText(QCoreApplication.translate("MainPages", u"Confirm", None))
        self.Save_Data.setText(QCoreApplication.translate("MainPages", u"Save Data", None))
        self.label_14.setText(QCoreApplication.translate("MainPages", u"HGB ratio:", None))
        self.pushButton_Reference.setText(QCoreApplication.translate("MainPages", u"Reference", None))
        self.pushButton_Clear.setText(QCoreApplication.translate("MainPages", u"Clear reference", None))
        self.label_reference.setText(QCoreApplication.translate("MainPages", u"Welcome", None))
        self.label_28.setText(QCoreApplication.translate("MainPages", u"Fluigent", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainPages", u"Opcion 2", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainPages", u"Calibration", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainPages", u"Stop", None))
        self.label_16.setText(QCoreApplication.translate("MainPages", u"Mesurement:", None))
        self.label_17.setText(QCoreApplication.translate("MainPages", u"RES....", None))
        self.label_18.setText(QCoreApplication.translate("MainPages", u"Set presure (uL/min)", None))
        self.label_19.setText(QCoreApplication.translate("MainPages", u"0.0", None))
        self.radioButton.setText(QCoreApplication.translate("MainPages", u"Primera presion", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainPages", u"Confirm", None))
        self.label_20.setText(QCoreApplication.translate("MainPages", u"Mesurement:", None))
        self.label_21.setText(QCoreApplication.translate("MainPages", u"RES....", None))
        self.label_22.setText(QCoreApplication.translate("MainPages", u"Set presure (uL/min)", None))
        self.label_23.setText(QCoreApplication.translate("MainPages", u"0.0", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainPages", u"Segunda presion", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainPages", u"Confirm", None))
        self.label_24.setText(QCoreApplication.translate("MainPages", u"Mesurement:", None))
        self.label_25.setText(QCoreApplication.translate("MainPages", u"RES....", None))
        self.label_26.setText(QCoreApplication.translate("MainPages", u"Set presure (uL/min)", None))
        self.label_27.setText(QCoreApplication.translate("MainPages", u"0.0", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainPages", u"Tercera presion", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainPages", u"Confirm", None))
    # retranslateUi

