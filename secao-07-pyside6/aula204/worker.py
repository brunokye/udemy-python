# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worker.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_myWidget(object):
    def setupUi(self, myWidget):
        if not myWidget.objectName():
            myWidget.setObjectName(u"myWidget")
        myWidget.resize(400, 300)
        font = QFont()
        font.setPointSize(40)
        myWidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(myWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label02 = QLabel(myWidget)
        self.label02.setObjectName(u"label02")
        self.label02.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label02, 0, 1, 1, 1)

        self.label01 = QLabel(myWidget)
        self.label01.setObjectName(u"label01")
        self.label01.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label01, 0, 0, 1, 1)

        self.button01 = QPushButton(myWidget)
        self.button01.setObjectName(u"button01")

        self.gridLayout.addWidget(self.button01, 1, 0, 1, 1)

        self.button02 = QPushButton(myWidget)
        self.button02.setObjectName(u"button02")

        self.gridLayout.addWidget(self.button02, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(myWidget)

        QMetaObject.connectSlotsByName(myWidget)
    # setupUi

    def retranslateUi(self, myWidget):
        myWidget.setWindowTitle(QCoreApplication.translate("myWidget", u"Form", None))
        self.label02.setText(QCoreApplication.translate("myWidget", u"L2", None))
        self.label01.setText(QCoreApplication.translate("myWidget", u"L1", None))
        self.button01.setText(QCoreApplication.translate("myWidget", u"B1", None))
        self.button02.setText(QCoreApplication.translate("myWidget", u"B2", None))
    # retranslateUi

