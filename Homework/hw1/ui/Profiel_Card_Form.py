# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Profile_Card_Form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Profile_Card(object):
    def setupUi(self, Profile_Card):
        if not Profile_Card.objectName():
            Profile_Card.setObjectName(u"Profile_Card")
        Profile_Card.resize(350, 300)
        Profile_Card.setMaximumSize(QSize(450, 16777215))
        self.verticalLayout = QVBoxLayout(Profile_Card)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelLastName = QLabel(Profile_Card)
        self.labelLastName.setObjectName(u"labelLastName")
        self.labelLastName.setMinimumSize(QSize(80, 35))
        font = QFont()
        font.setPointSize(12)
        self.labelLastName.setFont(font)

        self.horizontalLayout.addWidget(self.labelLastName)

        self.lineEditLastName = QLineEdit(Profile_Card)
        self.lineEditLastName.setObjectName(u"lineEditLastName")
        self.lineEditLastName.setMinimumSize(QSize(200, 25))
        self.lineEditLastName.setMaximumSize(QSize(350, 35))
        self.lineEditLastName.setFont(font)

        self.horizontalLayout.addWidget(self.lineEditLastName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelFirstName = QLabel(Profile_Card)
        self.labelFirstName.setObjectName(u"labelFirstName")
        self.labelFirstName.setMinimumSize(QSize(80, 35))
        self.labelFirstName.setFont(font)

        self.horizontalLayout_2.addWidget(self.labelFirstName)

        self.lineEditFirstName = QLineEdit(Profile_Card)
        self.lineEditFirstName.setObjectName(u"lineEditFirstName")
        self.lineEditFirstName.setMinimumSize(QSize(200, 25))
        self.lineEditFirstName.setMaximumSize(QSize(350, 35))
        self.lineEditFirstName.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEditFirstName)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelSecondName = QLabel(Profile_Card)
        self.labelSecondName.setObjectName(u"labelSecondName")
        self.labelSecondName.setMinimumSize(QSize(80, 35))
        self.labelSecondName.setFont(font)

        self.horizontalLayout_3.addWidget(self.labelSecondName)

        self.lineEditSecondName = QLineEdit(Profile_Card)
        self.lineEditSecondName.setObjectName(u"lineEditSecondName")
        self.lineEditSecondName.setMinimumSize(QSize(200, 25))
        self.lineEditSecondName.setMaximumSize(QSize(350, 35))
        self.lineEditSecondName.setFont(font)

        self.horizontalLayout_3.addWidget(self.lineEditSecondName)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelPhone = QLabel(Profile_Card)
        self.labelPhone.setObjectName(u"labelPhone")
        self.labelPhone.setMinimumSize(QSize(80, 35))
        self.labelPhone.setFont(font)

        self.horizontalLayout_4.addWidget(self.labelPhone)

        self.lineEditPhone = QLineEdit(Profile_Card)
        self.lineEditPhone.setObjectName(u"lineEditPhone")
        self.lineEditPhone.setMinimumSize(QSize(200, 25))
        self.lineEditPhone.setMaximumSize(QSize(350, 35))
        self.lineEditPhone.setFont(font)

        self.horizontalLayout_4.addWidget(self.lineEditPhone)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(Profile_Card)

        QMetaObject.connectSlotsByName(Profile_Card)
    # setupUi

    def retranslateUi(self, Profile_Card):
        Profile_Card.setWindowTitle(QCoreApplication.translate("Profile_Card", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.labelLastName.setText(QCoreApplication.translate("Profile_Card", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.lineEditLastName.setPlaceholderText(QCoreApplication.translate("Profile_Card", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0443 \u0444\u0430\u043c\u0438\u043b\u0438\u044e", None))
        self.labelFirstName.setText(QCoreApplication.translate("Profile_Card", u"\u0418\u043c\u044f:", None))
        self.lineEditFirstName.setPlaceholderText(QCoreApplication.translate("Profile_Card", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0438\u043c\u044f", None))
        self.labelSecondName.setText(QCoreApplication.translate("Profile_Card", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.lineEditSecondName.setPlaceholderText(QCoreApplication.translate("Profile_Card", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.labelPhone.setText(QCoreApplication.translate("Profile_Card", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.lineEditPhone.setPlaceholderText(QCoreApplication.translate("Profile_Card", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
    # retranslateUi

