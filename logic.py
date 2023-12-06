from PyQt6.QtWidgets import *
from main_gui import *
import re
import os
import csv


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


def is_valid_phone(phone):
    pattern = r'^\d{10}$'
    return re.match(pattern, phone) is not None


def email_exists(email):
    if not os.path.exists('voting_results.csv'):
        return False

    with open('voting_results.csv', 'r+', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if email == row[1]:
                return True
    return False


class Logic(QMainWindow, Ui_vote_app):
    def __init__(self):
        self.radio_john = False
        self.radio_jane = False
        super().__init__()
        self.main_ui = Ui_vote_app()
        self.main_ui.setupUi(self)

        self.main_ui.submit_button.clicked.connect(self.next_screen)

        self.main_ui.pushButton.clicked.connect(
            lambda: self.main_ui.stackedWidget.setCurrentWidget(self.main_ui.page))

        self.main_ui.exit_button.clicked.connect(self.close)
        self.main_ui.reset_button.clicked.connect(self.clear_input)
        self.main_ui.vote_button.clicked.connect(self.import_to_csv)

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

                if not is_valid_email(email):
                    raise ValueError('Invalid email format.')

                if not is_valid_phone(phone):
                    raise ValueError('Invalid phone number format.')

                next_ui = lambda: self.main_ui.stackedWidget.setCurrentWidget(self.main_ui.page_2)
                next_ui()

            except ValueError as e:
                QtWidgets.QMessageBox.warning(
                    None,
                    'Warning!',
                    str(e)
                )
                return
        else:
            if not input_text1 or not input_text2 or not input_text3:
                QtWidgets.QMessageBox.warning(
                    None,
                    "Warning!",
                    "Please enter in your information"
                )
                return
        return input_text1, input_text2, input_text3

    def import_to_csv(self):
        row_one = ['Name', 'Email', 'Phone', 'Choice']
        name_input, email_input, phone_input = self.next_screen()
        try:
            if not self.radio_jane or not self.radio_john:
                choice = 'Jane' if not self.radio_jane else 'John'
                info_list = [name_input, email_input, phone_input, choice]

                if email_exists(email_input):
                    raise ValueError('You have already voted.')

                with open('voting_results.csv', 'a', newline='') as csvfile:
                    content = csv.writer(csvfile)
                    if csvfile.tell() == 0:
                        content.writerow(row_one)

                    content.writerow(info_list)

                    QtWidgets.QMessageBox.information(
                        None,
                        "Thank you!",
                        f"Thank you {name_input} for voting!"
                    )
                    self.close()
            else:
                raise ValueError('Please select a candidate.')

        except Exception as e:
            QtWidgets.QMessageBox.warning(
                None,
                "Warning!",
                str(e)
            )
            return

        print(f'done')

    def clear_input(self):
        self.main_ui.name_text_box.clear()
        self.main_ui.email_text_box.clear()
        self.main_ui.phone_text_box.clear()
