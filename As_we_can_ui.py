# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'As_we_can.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)
# import pics_ui_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(722, 398)
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 10, 431, 281))
        self.Button = QPushButton(Form)
        self.Button.setObjectName(u"Button")
        self.Button.setGeometry(QRect(120, 330, 75, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(490, 60, 171, 171))
        self.label.setPixmap(QPixmap(u":/pics/mur\u732b.png"))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"As we can", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u987e\u9526\u5802", None))
        self.Button.setText(QCoreApplication.translate("Form", u"\u987e\u9526\u5802", None))
        self.label.setText("")
    # retranslateUi

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# version 3
