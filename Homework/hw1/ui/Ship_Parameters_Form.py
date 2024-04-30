# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ship_Parameters_Form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Ship_Parameters(object):
    def setupUi(self, Ship_Parameters):
        if not Ship_Parameters.objectName():
            Ship_Parameters.setObjectName(u"Ship_Parameters")
        Ship_Parameters.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Ship_Parameters)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Ship_Parameters)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelTemperature = QLabel(self.groupBox)
        self.labelTemperature.setObjectName(u"labelTemperature")
        self.labelTemperature.setMinimumSize(QSize(170, 0))
        font = QFont()
        font.setPointSize(12)
        self.labelTemperature.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelTemperature)

        self.lineEditTemperature = QLineEdit(self.groupBox)
        self.lineEditTemperature.setObjectName(u"lineEditTemperature")
        self.lineEditTemperature.setMinimumSize(QSize(130, 25))
        self.lineEditTemperature.setStyleSheet(u"color: rgb(255, 170, 0);")

        self.horizontalLayout_2.addWidget(self.lineEditTemperature)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Hermetization = QLabel(self.groupBox)
        self.Hermetization.setObjectName(u"Hermetization")
        self.Hermetization.setMinimumSize(QSize(170, 0))
        self.Hermetization.setFont(font)

        self.horizontalLayout_3.addWidget(self.Hermetization)

        self.lineEditHermetization = QLineEdit(self.groupBox)
        self.lineEditHermetization.setObjectName(u"lineEditHermetization")
        self.lineEditHermetization.setMinimumSize(QSize(130, 25))
        self.lineEditHermetization.setStyleSheet(u"color: rgb(0, 255, 0);")

        self.horizontalLayout_3.addWidget(self.lineEditHermetization)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelBarrel1 = QLabel(self.groupBox)
        self.labelBarrel1.setObjectName(u"labelBarrel1")
        self.labelBarrel1.setMinimumSize(QSize(170, 0))
        self.labelBarrel1.setFont(font)

        self.horizontalLayout_4.addWidget(self.labelBarrel1)

        self.lineEditBarrel1 = QLineEdit(self.groupBox)
        self.lineEditBarrel1.setObjectName(u"lineEditBarrel1")
        self.lineEditBarrel1.setMinimumSize(QSize(130, 25))
        self.lineEditBarrel1.setStyleSheet(u"color: rgb(0, 255, 0);")

        self.horizontalLayout_4.addWidget(self.lineEditBarrel1)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelBarrel2 = QLabel(self.groupBox)
        self.labelBarrel2.setObjectName(u"labelBarrel2")
        self.labelBarrel2.setMinimumSize(QSize(170, 0))
        self.labelBarrel2.setFont(font)

        self.horizontalLayout_5.addWidget(self.labelBarrel2)

        self.lineEditBarrel2 = QLineEdit(self.groupBox)
        self.lineEditBarrel2.setObjectName(u"lineEditBarrel2")
        self.lineEditBarrel2.setMinimumSize(QSize(130, 25))
        self.lineEditBarrel2.setStyleSheet(u"color: rgb(0, 255, 0)")

        self.horizontalLayout_5.addWidget(self.lineEditBarrel2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelBarrel3 = QLabel(self.groupBox)
        self.labelBarrel3.setObjectName(u"labelBarrel3")
        self.labelBarrel3.setMinimumSize(QSize(170, 0))
        self.labelBarrel3.setFont(font)

        self.horizontalLayout_6.addWidget(self.labelBarrel3)

        self.lineEditBarrel3 = QLineEdit(self.groupBox)
        self.lineEditBarrel3.setObjectName(u"lineEditBarrel3")
        self.lineEditBarrel3.setMinimumSize(QSize(130, 25))
        self.lineEditBarrel3.setStyleSheet(u"color: rgb(0, 255, 0);")

        self.horizontalLayout_6.addWidget(self.lineEditBarrel3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(Ship_Parameters)

        QMetaObject.connectSlotsByName(Ship_Parameters)
    # setupUi

    def retranslateUi(self, Ship_Parameters):
        Ship_Parameters.setWindowTitle(QCoreApplication.translate("Ship_Parameters", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("Ship_Parameters", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.labelTemperature.setText(QCoreApplication.translate("Ship_Parameters", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443:", None))
        self.lineEditTemperature.setText(QCoreApplication.translate("Ship_Parameters", u"22 \u00b0C", None))
        self.Hermetization.setText(QCoreApplication.translate("Ship_Parameters", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f:", None))
        self.lineEditHermetization.setText(QCoreApplication.translate("Ship_Parameters", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.labelBarrel1.setText(QCoreApplication.translate("Ship_Parameters", u"\u0411\u0430\u043a \u21161:", None))
        self.lineEditBarrel1.setText(QCoreApplication.translate("Ship_Parameters", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.labelBarrel2.setText(QCoreApplication.translate("Ship_Parameters", u"\u0411\u0430\u043a \u21162:", None))
        self.lineEditBarrel2.setText(QCoreApplication.translate("Ship_Parameters", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.labelBarrel3.setText(QCoreApplication.translate("Ship_Parameters", u"\u0411\u0430\u043a \u21163:", None))
        self.lineEditBarrel3.setText(QCoreApplication.translate("Ship_Parameters", u"\u041d\u043e\u0440\u043c\u0430", None))
    # retranslateUi

