from PyQt6.QtWidgets import *
from main_gui import *
import re
import csv


class Logic(QMainWindow, Ui_vote_app):
    def __init__(self):
        super().__init__()
        self.main_ui = Ui_vote_app()
        self.main_ui.setupUi(self)

        self.main_ui.submit_button.clicked.connect(self.next_screen)

        self.main_ui.pushButton.clicked.connect(
            lambda: self.main_ui.stackedWidget.setCurrentWidget(self.main_ui.page))

        self.main_ui.exit_button.clicked.connect(self.close)
        self.main_ui.reset_button.clicked.connect(self.clear_input)

    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def is_valid_phone(self, phone):
        pattern = r'^\d{10}$'
        return re.match(pattern, phone) is not None

    def next_screen(self):
        input_text1 = self.main_ui.name_text_box.text().strip()
        input_text2 = self.main_ui.email_text_box.text().strip()
        input_text3 = self.main_ui.phone_text_box.text().strip()

        if input_text1 and input_text2 and input_text3:
            try:
                name = str(input_text1)
                email = str(input_text2)
                phone = str(input_text3)

                if any(char.isdigit() for char in name):
                    raise ValueError('Name should not contain numbers.')

                if not self.is_valid_email(email):
                    raise ValueError('Invalid email format.')

                if not self.is_valid_phone(phone):
                    raise ValueError('Invalid phone number format.')

                next_ui = lambda: self.main_ui.stackedWidget.setCurrentWidget(self.main_ui.page_2)
                next_ui()

            except ValueError as e:
                QtWidgets.QMessageBox.warning(
                    None,
                    'Warning',
                    str(e)
                )
                return
        else:
            if not input_text1 or not input_text2 or not input_text3:
                QtWidgets.QMessageBox.warning(
                    None,
                    "Warning",
                    "Please enter in your information"
                )
                return

    def clear_input(self):
        self.main_ui.name_text_box.clear()
        self.main_ui.email_text_box.clear()
        self.main_ui.phone_text_box.clear()
