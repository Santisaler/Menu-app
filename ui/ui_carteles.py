# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_cartelesmJgIoO.ui'
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
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(825, 543)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.container_carteles = QWidget(self.centralwidget)
        self.container_carteles.setObjectName(u"container_carteles")
        self.container_carteles.setGeometry(QRect(80, 20, 661, 461))
        self.verticalLayoutWidget = QWidget(self.container_carteles)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 601, 421))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.container_title = QLabel(self.verticalLayoutWidget)
        self.container_title.setObjectName(u"container_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container_title.sizePolicy().hasHeightForWidth())
        self.container_title.setSizePolicy(sizePolicy)
        self.container_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.container_title)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.path_sign_1 = QLineEdit(self.verticalLayoutWidget)
        self.path_sign_1.setObjectName(u"path_sign_1")

        self.horizontalLayout_3.addWidget(self.path_sign_1)

        self.load_file_1 = QPushButton(self.verticalLayoutWidget)
        self.load_file_1.setObjectName(u"load_file_1")

        self.horizontalLayout_3.addWidget(self.load_file_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.path_sign_2 = QLineEdit(self.verticalLayoutWidget)
        self.path_sign_2.setObjectName(u"path_sign_2")

        self.horizontalLayout_2.addWidget(self.path_sign_2)

        self.load_file_2 = QPushButton(self.verticalLayoutWidget)
        self.load_file_2.setObjectName(u"load_file_2")

        self.horizontalLayout_2.addWidget(self.load_file_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.path_sign_3 = QLineEdit(self.verticalLayoutWidget)
        self.path_sign_3.setObjectName(u"path_sign_3")

        self.horizontalLayout_4.addWidget(self.path_sign_3)

        self.load_file_3 = QPushButton(self.verticalLayoutWidget)
        self.load_file_3.setObjectName(u"load_file_3")

        self.horizontalLayout_4.addWidget(self.load_file_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.path_sign_4 = QLineEdit(self.verticalLayoutWidget)
        self.path_sign_4.setObjectName(u"path_sign_4")

        self.horizontalLayout.addWidget(self.path_sign_4)

        self.load_file_4 = QPushButton(self.verticalLayoutWidget)
        self.load_file_4.setObjectName(u"load_file_4")

        self.horizontalLayout.addWidget(self.load_file_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.path_sign_5 = QLineEdit(self.verticalLayoutWidget)
        self.path_sign_5.setObjectName(u"path_sign_5")

        self.horizontalLayout_5.addWidget(self.path_sign_5)

        self.load_file_5 = QPushButton(self.verticalLayoutWidget)
        self.load_file_5.setObjectName(u"load_file_5")

        self.horizontalLayout_5.addWidget(self.load_file_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.path_sign_6 = QLineEdit(self.verticalLayoutWidget)
        self.path_sign_6.setObjectName(u"path_sign_6")

        self.horizontalLayout_6.addWidget(self.path_sign_6)

        self.load_file_6 = QPushButton(self.verticalLayoutWidget)
        self.load_file_6.setObjectName(u"load_file_6")

        self.horizontalLayout_6.addWidget(self.load_file_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.generate_button = QPushButton(self.verticalLayoutWidget)
        self.generate_button.setObjectName(u"generate_button")

        self.verticalLayout_2.addWidget(self.generate_button)

        self.pdf_checkBox = QCheckBox(self.verticalLayoutWidget)
        self.pdf_checkBox.setObjectName(u"pdf_checkBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pdf_checkBox.sizePolicy().hasHeightForWidth())
        self.pdf_checkBox.setSizePolicy(sizePolicy1)
        self.pdf_checkBox.setChecked(False)

        self.verticalLayout_2.addWidget(self.pdf_checkBox, 0, Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 825, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.container_title.setText(QCoreApplication.translate("MainWindow", u"Carteles individuales", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Milanesa y ensadala", None))
        self.load_file_1.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pollo Grill\u00e9", None))
        self.load_file_2.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ravioles", None))
        self.load_file_3.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sandwirch mila", None))
        self.load_file_4.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tallarines", None))
        self.load_file_5.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Promo desayuno", None))
        self.load_file_6.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"GENERATE CARTELES", None))
        self.pdf_checkBox.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
    # retranslateUi

