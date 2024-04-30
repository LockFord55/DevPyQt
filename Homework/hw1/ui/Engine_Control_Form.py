# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Engine_Control_Form.ui'
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
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Engine_Control(object):
    def setupUi(self, Engine_Control):
        if not Engine_Control.objectName():
            Engine_Control.setObjectName(u"Engine_Control")
        Engine_Control.resize(603, 187)
        Engine_Control.setMaximumSize(QSize(700, 235))
        self.horizontalLayout = QHBoxLayout(Engine_Control)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Engine_Control)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSliderEngine1 = QSlider(self.groupBox)
        self.verticalSliderEngine1.setObjectName(u"verticalSliderEngine1")
        self.verticalSliderEngine1.setMinimumSize(QSize(20, 100))
        self.verticalSliderEngine1.setMaximumSize(QSize(16777215, 150))
        self.verticalSliderEngine1.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout.addWidget(self.verticalSliderEngine1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelEngine1 = QLabel(self.groupBox)
        self.labelEngine1.setObjectName(u"labelEngine1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelEngine1.sizePolicy().hasHeightForWidth())
        self.labelEngine1.setSizePolicy(sizePolicy)
        self.labelEngine1.setMinimumSize(QSize(100, 25))
        self.labelEngine1.setMaximumSize(QSize(130, 40))
        font = QFont()
        font.setPointSize(10)
        self.labelEngine1.setFont(font)
        self.labelEngine1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelEngine1, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSliderEngine2 = QSlider(self.groupBox)
        self.verticalSliderEngine2.setObjectName(u"verticalSliderEngine2")
        self.verticalSliderEngine2.setMinimumSize(QSize(20, 100))
        self.verticalSliderEngine2.setMaximumSize(QSize(16777215, 150))
        self.verticalSliderEngine2.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_2.addWidget(self.verticalSliderEngine2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelEngine2 = QLabel(self.groupBox)
        self.labelEngine2.setObjectName(u"labelEngine2")
        sizePolicy.setHeightForWidth(self.labelEngine2.sizePolicy().hasHeightForWidth())
        self.labelEngine2.setSizePolicy(sizePolicy)
        self.labelEngine2.setMinimumSize(QSize(100, 25))
        self.labelEngine2.setMaximumSize(QSize(130, 40))
        self.labelEngine2.setFont(font)
        self.labelEngine2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelEngine2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSliderEngine3 = QSlider(self.groupBox)
        self.verticalSliderEngine3.setObjectName(u"verticalSliderEngine3")
        self.verticalSliderEngine3.setMinimumSize(QSize(20, 100))
        self.verticalSliderEngine3.setMaximumSize(QSize(16777215, 150))
        self.verticalSliderEngine3.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_3.addWidget(self.verticalSliderEngine3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelEngine3 = QLabel(self.groupBox)
        self.labelEngine3.setObjectName(u"labelEngine3")
        sizePolicy.setHeightForWidth(self.labelEngine3.sizePolicy().hasHeightForWidth())
        self.labelEngine3.setSizePolicy(sizePolicy)
        self.labelEngine3.setMinimumSize(QSize(100, 25))
        self.labelEngine3.setMaximumSize(QSize(130, 40))
        self.labelEngine3.setFont(font)
        self.labelEngine3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelEngine3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSliderEngine4 = QSlider(self.groupBox)
        self.verticalSliderEngine4.setObjectName(u"verticalSliderEngine4")
        self.verticalSliderEngine4.setMinimumSize(QSize(20, 100))
        self.verticalSliderEngine4.setMaximumSize(QSize(16777215, 150))
        self.verticalSliderEngine4.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_4.addWidget(self.verticalSliderEngine4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelEngine4 = QLabel(self.groupBox)
        self.labelEngine4.setObjectName(u"labelEngine4")
        sizePolicy.setHeightForWidth(self.labelEngine4.sizePolicy().hasHeightForWidth())
        self.labelEngine4.setSizePolicy(sizePolicy)
        self.labelEngine4.setMinimumSize(QSize(100, 25))
        self.labelEngine4.setMaximumSize(QSize(130, 40))
        self.labelEngine4.setFont(font)
        self.labelEngine4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelEngine4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSliderEngine5 = QSlider(self.groupBox)
        self.verticalSliderEngine5.setObjectName(u"verticalSliderEngine5")
        self.verticalSliderEngine5.setMinimumSize(QSize(20, 100))
        self.verticalSliderEngine5.setMaximumSize(QSize(16777215, 150))
        self.verticalSliderEngine5.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_5.addWidget(self.verticalSliderEngine5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelOverall = QLabel(self.groupBox)
        self.labelOverall.setObjectName(u"labelOverall")
        sizePolicy.setHeightForWidth(self.labelOverall.sizePolicy().hasHeightForWidth())
        self.labelOverall.setSizePolicy(sizePolicy)
        self.labelOverall.setMinimumSize(QSize(125, 25))
        self.labelOverall.setMaximumSize(QSize(130, 40))
        self.labelOverall.setFont(font)
        self.labelOverall.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.labelOverall, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(Engine_Control)

        QMetaObject.connectSlotsByName(Engine_Control)
    # setupUi

    def retranslateUi(self, Engine_Control):
        Engine_Control.setWindowTitle(QCoreApplication.translate("Engine_Control", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("Engine_Control", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.labelEngine1.setText(QCoreApplication.translate("Engine_Control", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.labelEngine2.setText(QCoreApplication.translate("Engine_Control", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.labelEngine3.setText(QCoreApplication.translate("Engine_Control", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.labelEngine4.setText(QCoreApplication.translate("Engine_Control", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.labelOverall.setText(QCoreApplication.translate("Engine_Control", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
    # retranslateUi

