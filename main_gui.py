# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_vote_app(object):
    def setupUi(self, vote_app):
        vote_app.setObjectName("vote_app")
        vote_app.resize(500, 400)
        vote_app.setMinimumSize(QtCore.QSize(500, 400))
        vote_app.setMaximumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtWidgets.QWidget(parent=vote_app)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.stackedWidget.setMinimumSize(QtCore.QSize(500, 400))
        self.stackedWidget.setMaximumSize(QtCore.QSize(500, 400))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.email_text_box = QtWidgets.QLineEdit(parent=self.page)
        self.email_text_box.setGeometry(QtCore.QRect(170, 170, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.email_text_box.setFont(font)
        self.email_text_box.setObjectName("email_text_box")
        self.label_title = QtWidgets.QLabel(parent=self.page)
        self.label_title.setGeometry(QtCore.QRect(-10, 0, 521, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(23)
        font.setUnderline(False)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_phone = QtWidgets.QLabel(parent=self.page)
        self.label_phone.setGeometry(QtCore.QRect(110, 210, 61, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.label_phone.setFont(font)
        self.label_phone.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_phone.setObjectName("label_phone")
        self.exit_button = QtWidgets.QPushButton(parent=self.page)
        self.exit_button.setGeometry(QtCore.QRect(390, 340, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.name_text_box = QtWidgets.QLineEdit(parent=self.page)
        self.name_text_box.setGeometry(QtCore.QRect(170, 130, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.name_text_box.setFont(font)
        self.name_text_box.setObjectName("name_text_box")
        self.phone_text_box = QtWidgets.QLineEdit(parent=self.page)
        self.phone_text_box.setGeometry(QtCore.QRect(170, 210, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.phone_text_box.setFont(font)
        self.phone_text_box.setText("")
        self.phone_text_box.setObjectName("phone_text_box")
        self.label_email = QtWidgets.QLabel(parent=self.page)
        self.label_email.setGeometry(QtCore.QRect(110, 170, 61, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.label_email.setFont(font)
        self.label_email.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_email.setObjectName("label_email")
        self.reset_button = QtWidgets.QPushButton(parent=self.page)
        self.reset_button.setGeometry(QtCore.QRect(170, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.reset_button.setFont(font)
        self.reset_button.setObjectName("reset_button")
        self.label_name = QtWidgets.QLabel(parent=self.page)
        self.label_name.setGeometry(QtCore.QRect(110, 130, 61, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.submit_button = QtWidgets.QPushButton(parent=self.page)
        self.submit_button.setGeometry(QtCore.QRect(270, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.label_info = QtWidgets.QLabel(parent=self.page)
        self.label_info.setGeometry(QtCore.QRect(90, 60, 321, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.label_info.setFont(font)
        self.label_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(360, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.radio_jane = QtWidgets.QRadioButton(parent=self.page_2)
        self.radio_jane.setGeometry(QtCore.QRect(210, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radio_jane.setFont(font)
        self.radio_jane.setObjectName("radio_jane")
        self.label_title2 = QtWidgets.QLabel(parent=self.page_2)
        self.label_title2.setGeometry(QtCore.QRect(-10, 0, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setUnderline(False)
        self.label_title2.setFont(font)
        self.label_title2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title2.setObjectName("label_title2")
        self.vote_button = QtWidgets.QPushButton(parent=self.page_2)
        self.vote_button.setGeometry(QtCore.QRect(200, 190, 81, 41))
        self.vote_button.setObjectName("vote_button")
        self.label_info2 = QtWidgets.QLabel(parent=self.page_2)
        self.label_info2.setGeometry(QtCore.QRect(0, 60, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_info2.setFont(font)
        self.label_info2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info2.setObjectName("label_info2")
        self.radio_john = QtWidgets.QRadioButton(parent=self.page_2)
        self.radio_john.setGeometry(QtCore.QRect(210, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radio_john.setFont(font)
        self.radio_john.setChecked(False)
        self.radio_john.setObjectName("radio_john")
        self.stackedWidget.addWidget(self.page_2)
        vote_app.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=vote_app)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        vote_app.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=vote_app)
        self.statusbar.setObjectName("statusbar")
        vote_app.setStatusBar(self.statusbar)

        self.retranslateUi(vote_app)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(vote_app)
        QtWidgets.QWidget.setTabOrder(self.name_text_box, self.email_text_box)
        QtWidgets.QWidget.setTabOrder(self.email_text_box, self.phone_text_box)

    def retranslateUi(self, vote_app):
        _translate = QtCore.QCoreApplication.translate
        vote_app.setWindowTitle(_translate("vote_app", "Voting Application"))
        self.label_title.setText(_translate("vote_app", "Welcome to the vote application!"))
        self.label_phone.setText(_translate("vote_app", "Phone"))
        self.exit_button.setText(_translate("vote_app", "exit"))
        self.label_email.setText(_translate("vote_app", "Email"))
        self.reset_button.setText(_translate("vote_app", "RESET"))
        self.label_name.setText(_translate("vote_app", "Name"))
        self.submit_button.setText(_translate("vote_app", "SUBMIT"))
        self.label_info.setText(_translate("vote_app", "Please enter: Name, Email and Phone number"))
        self.pushButton.setText(_translate("vote_app", "BACK"))
        self.radio_jane.setText(_translate("vote_app", "Jane"))
        self.label_title2.setText(_translate("vote_app", "Who will you vote for?"))
        self.vote_button.setText(_translate("vote_app", "VOTE"))
        self.label_info2.setText(_translate("vote_app", "Welcome! Please select a candidate!"))
        self.radio_john.setText(_translate("vote_app", "John"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vote_app = QtWidgets.QMainWindow()
    ui = Ui_vote_app()
    ui.setupUi(vote_app)
    vote_app.show()
    sys.exit(app.exec())
