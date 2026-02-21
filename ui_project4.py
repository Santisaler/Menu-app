# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proyecto4WmlSHk.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1103, 758)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bar_name = QLabel(self.centralwidget)
        self.bar_name.setObjectName(u"bar_name")
        self.bar_name.setGeometry(QRect(100, 20, 961, 41))
        self.bar_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget_11 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(100, 70, 961, 621))
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.template_path = QLineEdit(self.verticalLayoutWidget_11)
        self.template_path.setObjectName(u"template_path")

        self.horizontalLayout_47.addWidget(self.template_path)

        self.pushButton = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_47.addWidget(self.pushButton)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_47)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)

        self.tabWidget = QTabWidget(self.verticalLayoutWidget_11)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.postres_container = QWidget(self.tab)
        self.postres_container.setObjectName(u"postres_container")
        self.postres_container.setGeometry(QRect(160, 20, 281, 131))
        self.verticalLayoutWidget_3 = QWidget(self.postres_container)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 10, 261, 111))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.postres_title = QLabel(self.verticalLayoutWidget_3)
        self.postres_title.setObjectName(u"postres_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.postres_title.sizePolicy().hasHeightForWidth())
        self.postres_title.setSizePolicy(sizePolicy)
        self.postres_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.postres_title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.input_1 = QLineEdit(self.verticalLayoutWidget_3)
        self.input_1.setObjectName(u"input_1")

        self.horizontalLayout.addWidget(self.input_1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.input_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.input_2.setObjectName(u"input_2")

        self.horizontalLayout_2.addWidget(self.input_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.gaseosas_container = QWidget(self.tab)
        self.gaseosas_container.setObjectName(u"gaseosas_container")
        self.gaseosas_container.setGeometry(QRect(160, 170, 281, 311))
        self.verticalLayoutWidget_2 = QWidget(self.gaseosas_container)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 261, 291))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gaseosas_title = QLabel(self.verticalLayoutWidget_2)
        self.gaseosas_title.setObjectName(u"gaseosas_title")
        sizePolicy.setHeightForWidth(self.gaseosas_title.sizePolicy().hasHeightForWidth())
        self.gaseosas_title.setSizePolicy(sizePolicy)
        self.gaseosas_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.gaseosas_title)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.input_3 = QLineEdit(self.verticalLayoutWidget_2)
        self.input_3.setObjectName(u"input_3")

        self.horizontalLayout_3.addWidget(self.input_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.input_4 = QLineEdit(self.verticalLayoutWidget_2)
        self.input_4.setObjectName(u"input_4")

        self.horizontalLayout_4.addWidget(self.input_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.input_5 = QLineEdit(self.verticalLayoutWidget_2)
        self.input_5.setObjectName(u"input_5")

        self.horizontalLayout_5.addWidget(self.input_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.input_6 = QLineEdit(self.verticalLayoutWidget_2)
        self.input_6.setObjectName(u"input_6")

        self.horizontalLayout_6.addWidget(self.input_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.input_7 = QLineEdit(self.verticalLayoutWidget_2)
        self.input_7.setObjectName(u"input_7")

        self.horizontalLayout_7.addWidget(self.input_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.licuados_container = QWidget(self.tab)
        self.licuados_container.setObjectName(u"licuados_container")
        self.licuados_container.setGeometry(QRect(470, 230, 361, 141))
        self.verticalLayoutWidget_4 = QWidget(self.licuados_container)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 10, 341, 121))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.licuados_title = QLabel(self.verticalLayoutWidget_4)
        self.licuados_title.setObjectName(u"licuados_title")
        sizePolicy.setHeightForWidth(self.licuados_title.sizePolicy().hasHeightForWidth())
        self.licuados_title.setSizePolicy(sizePolicy)
        self.licuados_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.licuados_title)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.verticalLayoutWidget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(True)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.input_8 = QLineEdit(self.verticalLayoutWidget_4)
        self.input_8.setObjectName(u"input_8")

        self.horizontalLayout_9.addWidget(self.input_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.verticalLayoutWidget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(True)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.input_9 = QLineEdit(self.verticalLayoutWidget_4)
        self.input_9.setObjectName(u"input_9")

        self.horizontalLayout_8.addWidget(self.input_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.promo_container = QWidget(self.tab)
        self.promo_container.setObjectName(u"promo_container")
        self.promo_container.setGeometry(QRect(470, 20, 361, 181))
        self.verticalLayoutWidget_5 = QWidget(self.promo_container)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 341, 151))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.promo_title = QLabel(self.verticalLayoutWidget_5)
        self.promo_title.setObjectName(u"promo_title")
        sizePolicy.setHeightForWidth(self.promo_title.sizePolicy().hasHeightForWidth())
        self.promo_title.setSizePolicy(sizePolicy)
        self.promo_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.promo_title)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.verticalLayoutWidget_5)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16)

        self.input_10 = QLineEdit(self.verticalLayoutWidget_5)
        self.input_10.setObjectName(u"input_10")

        self.horizontalLayout_10.addWidget(self.input_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_18 = QLabel(self.verticalLayoutWidget_5)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_12.addWidget(self.label_18)

        self.input_11 = QLineEdit(self.verticalLayoutWidget_5)
        self.input_11.setObjectName(u"input_11")

        self.horizontalLayout_12.addWidget(self.input_11)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(self.verticalLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)

        self.input_12 = QLineEdit(self.verticalLayoutWidget_5)
        self.input_12.setObjectName(u"input_12")

        self.horizontalLayout_11.addWidget(self.input_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.cafe_container = QWidget(self.tab_2)
        self.cafe_container.setObjectName(u"cafe_container")
        self.cafe_container.setGeometry(QRect(250, 20, 461, 431))
        self.verticalLayoutWidget_7 = QWidget(self.cafe_container)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 10, 441, 411))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.cafeteria_title = QLabel(self.verticalLayoutWidget_7)
        self.cafeteria_title.setObjectName(u"cafeteria_title")
        sizePolicy.setHeightForWidth(self.cafeteria_title.sizePolicy().hasHeightForWidth())
        self.cafeteria_title.setSizePolicy(sizePolicy)
        self.cafeteria_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.cafeteria_title)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(self.verticalLayoutWidget_7)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_13.addWidget(self.label_20)

        self.input_13 = QLineEdit(self.verticalLayoutWidget_7)
        self.input_13.setObjectName(u"input_13")

        self.horizontalLayout_13.addWidget(self.input_13)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_21 = QLabel(self.verticalLayoutWidget_7)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_14.addWidget(self.label_21)

        self.input_14 = QLineEdit(self.verticalLayoutWidget_7)
        self.input_14.setObjectName(u"input_14")

        self.horizontalLayout_14.addWidget(self.input_14)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_22 = QLabel(self.verticalLayoutWidget_7)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_15.addWidget(self.label_22)

        self.input_15 = QLineEdit(self.verticalLayoutWidget_7)
        self.input_15.setObjectName(u"input_15")

        self.horizontalLayout_15.addWidget(self.input_15)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_23 = QLabel(self.verticalLayoutWidget_7)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_16.addWidget(self.label_23)

        self.input_16 = QLineEdit(self.verticalLayoutWidget_7)
        self.input_16.setObjectName(u"input_16")

        self.horizontalLayout_16.addWidget(self.input_16)


        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_25 = QLabel(self.verticalLayoutWidget_7)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_18.addWidget(self.label_25)

        self.input_17 = QLineEdit(self.verticalLayoutWidget_7)
        self.input_17.setObjectName(u"input_17")

        self.horizontalLayout_18.addWidget(self.input_17)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_24 = QLabel(self.verticalLayoutWidget_7)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_17.addWidget(self.label_24)

        self.input_18 = QLineEdit(self.verticalLayoutWidget_7)
        self.input_18.setObjectName(u"input_18")

        self.horizontalLayout_17.addWidget(self.input_18)


        self.verticalLayout_7.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_27 = QLabel(self.verticalLayoutWidget_7)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_20.addWidget(self.label_27)

        self.input_19 = QLineEdit(self.verticalLayoutWidget_7)
        self.input_19.setObjectName(u"input_19")

        self.horizontalLayout_20.addWidget(self.input_19)


        self.verticalLayout_7.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_26 = QLabel(self.verticalLayoutWidget_7)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_19.addWidget(self.label_26)

        self.input_20 = QLineEdit(self.verticalLayoutWidget_7)
        self.input_20.setObjectName(u"input_20")

        self.horizontalLayout_19.addWidget(self.input_20)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.minutas_container = QWidget(self.tab_3)
        self.minutas_container.setObjectName(u"minutas_container")
        self.minutas_container.setGeometry(QRect(70, 20, 401, 441))
        self.verticalLayoutWidget_6 = QWidget(self.minutas_container)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 10, 381, 391))
        self.Minutas_container = QVBoxLayout(self.verticalLayoutWidget_6)
        self.Minutas_container.setObjectName(u"Minutas_container")
        self.Minutas_container.setContentsMargins(0, 0, 0, 0)
        self.minutas_title = QLabel(self.verticalLayoutWidget_6)
        self.minutas_title.setObjectName(u"minutas_title")
        sizePolicy.setHeightForWidth(self.minutas_title.sizePolicy().hasHeightForWidth())
        self.minutas_title.setSizePolicy(sizePolicy)
        self.minutas_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Minutas_container.addWidget(self.minutas_title)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_33 = QLabel(self.verticalLayoutWidget_6)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_24.addWidget(self.label_33)

        self.input_21 = QLineEdit(self.verticalLayoutWidget_6)
        self.input_21.setObjectName(u"input_21")

        self.horizontalLayout_24.addWidget(self.input_21)


        self.Minutas_container.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_31 = QLabel(self.verticalLayoutWidget_6)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_23.addWidget(self.label_31)

        self.input_22 = QLineEdit(self.verticalLayoutWidget_6)
        self.input_22.setObjectName(u"input_22")

        self.horizontalLayout_23.addWidget(self.input_22)


        self.Minutas_container.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_34 = QLabel(self.verticalLayoutWidget_6)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_25.addWidget(self.label_34)

        self.input_23 = QLineEdit(self.verticalLayoutWidget_6)
        self.input_23.setObjectName(u"input_23")

        self.horizontalLayout_25.addWidget(self.input_23)


        self.Minutas_container.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_40 = QLabel(self.verticalLayoutWidget_6)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_31.addWidget(self.label_40)

        self.input_24 = QLineEdit(self.verticalLayoutWidget_6)
        self.input_24.setObjectName(u"input_24")

        self.horizontalLayout_31.addWidget(self.input_24)


        self.Minutas_container.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_35 = QLabel(self.verticalLayoutWidget_6)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_26.addWidget(self.label_35)

        self.input_25 = QLineEdit(self.verticalLayoutWidget_6)
        self.input_25.setObjectName(u"input_25")

        self.horizontalLayout_26.addWidget(self.input_25)


        self.Minutas_container.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_36 = QLabel(self.verticalLayoutWidget_6)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_27.addWidget(self.label_36)

        self.input_26 = QLineEdit(self.verticalLayoutWidget_6)
        self.input_26.setObjectName(u"input_26")

        self.horizontalLayout_27.addWidget(self.input_26)


        self.Minutas_container.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_37 = QLabel(self.verticalLayoutWidget_6)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_28.addWidget(self.label_37)

        self.input_27 = QLineEdit(self.verticalLayoutWidget_6)
        self.input_27.setObjectName(u"input_27")

        self.horizontalLayout_28.addWidget(self.input_27)


        self.Minutas_container.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_38 = QLabel(self.verticalLayoutWidget_6)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_29.addWidget(self.label_38)

        self.input_28 = QLineEdit(self.verticalLayoutWidget_6)
        self.input_28.setObjectName(u"input_28")

        self.horizontalLayout_29.addWidget(self.input_28)


        self.Minutas_container.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_39 = QLabel(self.verticalLayoutWidget_6)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_30.addWidget(self.label_39)

        self.input_29 = QLineEdit(self.verticalLayoutWidget_6)
        self.input_29.setObjectName(u"input_29")

        self.horizontalLayout_30.addWidget(self.input_29)


        self.Minutas_container.addLayout(self.horizontalLayout_30)

        self.ensaladas_container = QWidget(self.tab_3)
        self.ensaladas_container.setObjectName(u"ensaladas_container")
        self.ensaladas_container.setGeometry(QRect(500, 130, 371, 151))
        self.verticalLayoutWidget_8 = QWidget(self.ensaladas_container)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 10, 351, 131))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ensaladas_title = QLabel(self.verticalLayoutWidget_8)
        self.ensaladas_title.setObjectName(u"ensaladas_title")
        sizePolicy.setHeightForWidth(self.ensaladas_title.sizePolicy().hasHeightForWidth())
        self.ensaladas_title.setSizePolicy(sizePolicy)
        self.ensaladas_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.ensaladas_title)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_28 = QLabel(self.verticalLayoutWidget_8)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_21.addWidget(self.label_28)

        self.input_41 = QLineEdit(self.verticalLayoutWidget_8)
        self.input_41.setObjectName(u"input_41")

        self.horizontalLayout_21.addWidget(self.input_41)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_54 = QLabel(self.tab_4)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(230, 30, 439, 32))
        self.label_54.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sand_caliente_container = QWidget(self.tab_4)
        self.sand_caliente_container.setObjectName(u"sand_caliente_container")
        self.sand_caliente_container.setGeometry(QRect(490, 90, 441, 281))
        self.verticalLayoutWidget_9 = QWidget(self.sand_caliente_container)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 10, 421, 261))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.caliente_title = QLabel(self.verticalLayoutWidget_9)
        self.caliente_title.setObjectName(u"caliente_title")
        sizePolicy.setHeightForWidth(self.caliente_title.sizePolicy().hasHeightForWidth())
        self.caliente_title.setSizePolicy(sizePolicy)
        self.caliente_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.caliente_title)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_49 = QLabel(self.verticalLayoutWidget_9)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_38.addWidget(self.label_49)

        self.input_36 = QLineEdit(self.verticalLayoutWidget_9)
        self.input_36.setObjectName(u"input_36")

        self.horizontalLayout_38.addWidget(self.input_36)


        self.verticalLayout_10.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_50 = QLabel(self.verticalLayoutWidget_9)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_39.addWidget(self.label_50)

        self.input_37 = QLineEdit(self.verticalLayoutWidget_9)
        self.input_37.setObjectName(u"input_37")

        self.horizontalLayout_39.addWidget(self.input_37)


        self.verticalLayout_10.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_51 = QLabel(self.verticalLayoutWidget_9)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_40.addWidget(self.label_51)

        self.input_38 = QLineEdit(self.verticalLayoutWidget_9)
        self.input_38.setObjectName(u"input_38")

        self.horizontalLayout_40.addWidget(self.input_38)


        self.verticalLayout_10.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_52 = QLabel(self.verticalLayoutWidget_9)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_41.addWidget(self.label_52)

        self.input_39 = QLineEdit(self.verticalLayoutWidget_9)
        self.input_39.setObjectName(u"input_39")

        self.horizontalLayout_41.addWidget(self.input_39)


        self.verticalLayout_10.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_53 = QLabel(self.verticalLayoutWidget_9)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_42.addWidget(self.label_53)

        self.input_40 = QLineEdit(self.verticalLayoutWidget_9)
        self.input_40.setObjectName(u"input_40")

        self.horizontalLayout_42.addWidget(self.input_40)


        self.verticalLayout_10.addLayout(self.horizontalLayout_42)

        self.sand_fria_container = QWidget(self.tab_4)
        self.sand_fria_container.setObjectName(u"sand_fria_container")
        self.sand_fria_container.setGeometry(QRect(20, 90, 441, 281))
        self.verticalLayoutWidget = QWidget(self.sand_fria_container)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 421, 261))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.fria_title = QLabel(self.verticalLayoutWidget)
        self.fria_title.setObjectName(u"fria_title")
        sizePolicy.setHeightForWidth(self.fria_title.sizePolicy().hasHeightForWidth())
        self.fria_title.setSizePolicy(sizePolicy)
        self.fria_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.fria_title)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_41 = QLabel(self.verticalLayoutWidget)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_32.addWidget(self.label_41)

        self.input_30 = QLineEdit(self.verticalLayoutWidget)
        self.input_30.setObjectName(u"input_30")

        self.horizontalLayout_32.addWidget(self.input_30)


        self.verticalLayout_9.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_43 = QLabel(self.verticalLayoutWidget)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_33.addWidget(self.label_43)

        self.input_31 = QLineEdit(self.verticalLayoutWidget)
        self.input_31.setObjectName(u"input_31")

        self.horizontalLayout_33.addWidget(self.input_31)


        self.verticalLayout_9.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_44 = QLabel(self.verticalLayoutWidget)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_34.addWidget(self.label_44)

        self.input_32 = QLineEdit(self.verticalLayoutWidget)
        self.input_32.setObjectName(u"input_32")

        self.horizontalLayout_34.addWidget(self.input_32)


        self.verticalLayout_9.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_45 = QLabel(self.verticalLayoutWidget)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_35.addWidget(self.label_45)

        self.input_33 = QLineEdit(self.verticalLayoutWidget)
        self.input_33.setObjectName(u"input_33")

        self.horizontalLayout_35.addWidget(self.input_33)


        self.verticalLayout_9.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_46 = QLabel(self.verticalLayoutWidget)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_36.addWidget(self.label_46)

        self.input_34 = QLineEdit(self.verticalLayoutWidget)
        self.input_34.setObjectName(u"input_34")

        self.horizontalLayout_36.addWidget(self.input_34)


        self.verticalLayout_9.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_47 = QLabel(self.verticalLayoutWidget)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_37.addWidget(self.label_47)

        self.input_35 = QLineEdit(self.verticalLayoutWidget)
        self.input_35.setObjectName(u"input_35")

        self.horizontalLayout_37.addWidget(self.input_35)


        self.verticalLayout_9.addLayout(self.horizontalLayout_37)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.pastas_container = QWidget(self.tab_5)
        self.pastas_container.setObjectName(u"pastas_container")
        self.pastas_container.setGeometry(QRect(210, 60, 561, 321))
        self.verticalLayoutWidget_10 = QWidget(self.pastas_container)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(10, 10, 541, 301))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pastas_title = QLabel(self.verticalLayoutWidget_10)
        self.pastas_title.setObjectName(u"pastas_title")
        sizePolicy.setHeightForWidth(self.pastas_title.sizePolicy().hasHeightForWidth())
        self.pastas_title.setSizePolicy(sizePolicy)
        self.pastas_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.pastas_title)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_56 = QLabel(self.verticalLayoutWidget_10)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_43.addWidget(self.label_56)

        self.input_42 = QLineEdit(self.verticalLayoutWidget_10)
        self.input_42.setObjectName(u"input_42")

        self.horizontalLayout_43.addWidget(self.input_42)


        self.verticalLayout_11.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_57 = QLabel(self.verticalLayoutWidget_10)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_44.addWidget(self.label_57)

        self.input_43 = QLineEdit(self.verticalLayoutWidget_10)
        self.input_43.setObjectName(u"input_43")

        self.horizontalLayout_44.addWidget(self.input_43)


        self.verticalLayout_11.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_58 = QLabel(self.verticalLayoutWidget_10)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_45.addWidget(self.label_58)

        self.input_44 = QLineEdit(self.verticalLayoutWidget_10)
        self.input_44.setObjectName(u"input_44")

        self.horizontalLayout_45.addWidget(self.input_44)


        self.verticalLayout_11.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_59 = QLabel(self.verticalLayoutWidget_10)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_46.addWidget(self.label_59)

        self.input_45 = QLineEdit(self.verticalLayoutWidget_10)
        self.input_45.setObjectName(u"input_45")

        self.horizontalLayout_46.addWidget(self.input_45)


        self.verticalLayout_11.addLayout(self.horizontalLayout_46)

        self.tabWidget.addTab(self.tab_5, "")

        self.verticalLayout_12.addWidget(self.tabWidget)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.generateFile = QPushButton(self.verticalLayoutWidget_11)
        self.generateFile.setObjectName(u"generateFile")

        self.verticalLayout_6.addWidget(self.generateFile)


        self.horizontalLayout_57.addLayout(self.verticalLayout_6)

        self.pdf_checkBox = QCheckBox(self.verticalLayoutWidget_11)
        self.pdf_checkBox.setObjectName(u"pdf_checkBox")
        font = QFont()
        font.setPointSize(12)
        self.pdf_checkBox.setFont(font)

        self.horizontalLayout_57.addWidget(self.pdf_checkBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_57)

        self.label_4 = QLabel(self.verticalLayoutWidget_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1103, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bar_name.setText(QCoreApplication.translate("MainWindow", u"BAR BUENOS AIRES", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.postres_title.setText(QCoreApplication.translate("MainWindow", u"POSTRES", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Helado bomb\u00f3n escoc\u00e9s", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Queso y dulce", None))
        self.gaseosas_title.setText(QCoreApplication.translate("MainWindow", u"GASEOSAS", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gaseosas", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Agua mineral", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cerveza (lata)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Jugo exprimido naranja", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Vino en copa", None))
        self.licuados_title.setText(QCoreApplication.translate("MainWindow", u"LICUADOS", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Banana", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Durazno", None))
        self.promo_title.setText(QCoreApplication.translate("MainWindow", u"PROMOCIONES", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Sandwich jam\u00f3n y queso + gaseosa", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"caf\u00e9 c/ leche + tostado", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Tallarines al fileto + gaseosa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.cafeteria_title.setText(QCoreApplication.translate("MainWindow", u"CAFETER\u00cdA", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Caf\u00e9", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Caf\u00e9 c/ leche", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Capuchino", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Submarino", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"T\u00e9 c/ lim\u00f3n", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"T\u00e9 c/ leche", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Medialunas c/ jam\u00f3n y queso", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Pastafrola o brownie", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.minutas_title.setText(QCoreApplication.translate("MainWindow", u"MINUTAS", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Milanesa de ternera", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Milanesa de ternera c/ ensalada o pur\u00e9", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Milanesa de ternera c/ fritas y huevo", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Milanesa napolitana c/ pur\u00e9 o fritas", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Suprema de pollo", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Suprema de pollo c/ pur\u00e9 o ensalada", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Pechuga de pollo grill\u00e9", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Pechuga de pollo grill\u00e9 c/ fritas o pur\u00e9", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Omelettes jam\u00f3n y queso", None))
        self.ensaladas_title.setText(QCoreApplication.translate("MainWindow", u"ENSALADAS", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Combinaci\u00f3n 3 gustos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"P\u00e1gina", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"SANDWICHER\u00cdA", None))
        self.caliente_title.setText(QCoreApplication.translate("MainWindow", u"CALIENTE", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Especial de milanesa", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Milanesa c/ lechuga y tomate", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Milanesa completa", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Especial de pollo", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Pollo completo", None))
        self.fria_title.setText(QCoreApplication.translate("MainWindow", u"FR\u00cdA", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Jam\u00f3n cocido y queso", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Salame y queso", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"jam\u00f3n cocido-queso, tomate, huevo", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Jam\u00f3n y queso", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Jam\u00f3n, tomate, queso", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"jam\u00f3n, tomate, queso, huevo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"P\u00e1gina", None))
        self.pastas_title.setText(QCoreApplication.translate("MainWindow", u"PASTAS CASERAS", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Ravioles filetto", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Ravioles c/ estofado", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Tallarines filetto", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Tallarines c/ estofado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"P\u00e1gina", None))
        self.generateFile.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
        self.pdf_checkBox.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Designed by Santiago Salerno", None))
    # retranslateUi

