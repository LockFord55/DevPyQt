# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Book_Shop_Form.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QLabel,
    QListView, QListWidget, QListWidgetItem, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Book_Shop(object):
    def setupUi(self, Book_Shop):
        if not Book_Shop.objectName():
            Book_Shop.setObjectName(u"Book_Shop")
        Book_Shop.resize(400, 300)
        Book_Shop.setMinimumSize(QSize(400, 300))
        Book_Shop.setMaximumSize(QSize(500, 400))
        self.verticalLayout_2 = QVBoxLayout(Book_Shop)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelChooseBook = QLabel(Book_Shop)
        self.labelChooseBook.setObjectName(u"labelChooseBook")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.labelChooseBook.setFont(font)
        self.labelChooseBook.setStyleSheet(u"color: rgb(170, 0, 127)")

        self.verticalLayout_2.addWidget(self.labelChooseBook)

        self.listWidgetChooseBook = QListWidget(Book_Shop)
        QListWidgetItem(self.listWidgetChooseBook)
        QListWidgetItem(self.listWidgetChooseBook)
        __qlistwidgetitem = QListWidgetItem(self.listWidgetChooseBook)
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate);
        self.listWidgetChooseBook.setObjectName(u"listWidgetChooseBook")
        self.listWidgetChooseBook.setFrameShape(QFrame.Shape.Box)
        self.listWidgetChooseBook.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.listWidgetChooseBook.setMovement(QListView.Movement.Static)
        self.listWidgetChooseBook.setProperty("isWrapping", False)
        self.listWidgetChooseBook.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.listWidgetChooseBook.setViewMode(QListView.ViewMode.ListMode)

        self.verticalLayout_2.addWidget(self.listWidgetChooseBook)

        self.labelChoosePayment = QLabel(Book_Shop)
        self.labelChoosePayment.setObjectName(u"labelChoosePayment")
        self.labelChoosePayment.setFont(font)
        self.labelChoosePayment.setStyleSheet(u"color: rgb(170, 0, 127)")

        self.verticalLayout_2.addWidget(self.labelChoosePayment)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButtonCard = QRadioButton(Book_Shop)
        self.radioButtonCard.setObjectName(u"radioButtonCard")

        self.verticalLayout.addWidget(self.radioButtonCard)

        self.radioButtonQR = QRadioButton(Book_Shop)
        self.radioButtonQR.setObjectName(u"radioButtonQR")

        self.verticalLayout.addWidget(self.radioButtonQR)

        self.radioButtonCash = QRadioButton(Book_Shop)
        self.radioButtonCash.setObjectName(u"radioButtonCash")

        self.verticalLayout.addWidget(self.radioButtonCash)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Book_Shop)

        QMetaObject.connectSlotsByName(Book_Shop)
    # setupUi

    def retranslateUi(self, Book_Shop):
        Book_Shop.setWindowTitle(QCoreApplication.translate("Book_Shop", u"\u041a\u043d\u0438\u0436\u043d\u044b\u0439 \u043c\u0430\u0433\u0430\u0437\u0438\u043d", None))
        self.labelChooseBook.setText(QCoreApplication.translate("Book_Shop", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043d\u0438\u0433\u0443", None))

        __sortingEnabled = self.listWidgetChooseBook.isSortingEnabled()
        self.listWidgetChooseBook.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidgetChooseBook.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Book_Shop", u"\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440 \u0438 \u0443\u0437\u043d\u0438\u043a \u0410\u0437\u043a\u0430\u0431\u0430\u043d\u0430. \u0414\u0436\u043e\u0430\u043d \u0420\u043e\u0443\u043b\u0438\u043d\u0433 ", None));
        ___qlistwidgetitem1 = self.listWidgetChooseBook.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Book_Shop", u"\u0411\u043b\u0430\u0433\u043e\u0441\u043b\u043e\u0432\u0435\u043d\u0438\u0435 \u043d\u0435\u0431\u043e\u0436\u0438\u0442\u0435\u043b\u0435\u0439. \u0422\u043e\u043c 3, \u041c\u043e\u0441\u044f\u043d \u0422\u0443\u043d\u0441\u044e", None));
        ___qlistwidgetitem2 = self.listWidgetChooseBook.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Book_Shop", u"\u0423\u043d\u0435\u0441\u0435\u043d\u043d\u044b\u0435 \u0432\u0435\u0442\u0440\u043e\u043c. \u041c\u0430\u0440\u0433\u0430\u0440\u0435\u0442 \u041c\u0438\u0442\u0447\u0435\u043b\u043b", None));
        self.listWidgetChooseBook.setSortingEnabled(__sortingEnabled)

        self.labelChoosePayment.setText(QCoreApplication.translate("Book_Shop", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u044b", None))
        self.radioButtonCard.setText(QCoreApplication.translate("Book_Shop", u"\u041f\u043e \u043a\u0430\u0440\u0442\u0435", None))
        self.radioButtonQR.setText(QCoreApplication.translate("Book_Shop", u"\u041f\u043e QR", None))
        self.radioButtonCash.setText(QCoreApplication.translate("Book_Shop", u"\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438", None))
    # retranslateUi

