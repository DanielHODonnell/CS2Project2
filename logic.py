from PyQt6.QtWidgets import *
from main_gui import *
import re
import os
import csv


class Logic(QMainWindow, Ui_vote_app):
    """
    This is the main logic class for the voting application.
    """
    def __init__(self):
        """
        Initializes the Logic class.
        """
        super().__init__()
        self.main_ui = Ui_vote_app()
        self.main_ui.setupUi(self)

        self.main_ui.submit_button.clicked.connect(self.next_screen)

        self.main_ui.pushButton.clicked.connect(
            lambda: self.main_ui.stackedWidget.setCurrentWidget(self.main_ui.page))

        self.main_ui.exit_button.clicked.connect(self.close)
        self.main_ui.reset_button.clicked.connect(self.clear_input)
        self.main_ui.vote_button.clicked.connect(self.import_to_csv)

    def is_valid_email(self, email: str) -> bool:
        """
        Checks if the given email address is valid.
        :param email: The email address to validate.
        :return: True if the email is valid, False if not.
        """
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def is_valid_phone(self, phone: str) -> bool:
        """
        Checks if the given phone number is valid.
        :param phone: The phone number to validate.
        :return: True if the phone number is valid, False if not.
        """
        pattern = r'^\d{10}$'
        pattern2 = r'^\d{3}-\d{3}-\d{4}$'
        return re.match(pattern, phone) is not None or re.match(pattern2, phone)

    def email_exists(self, email: str) -> bool:
        """
        Checks if the given email already exists in the CSV file.
        :param email: The email address to check.
        :return: True if the email exists, False if not.
        """
        if not os.path.exists('voting_results.csv'):
            return False

        with open('voting_results.csv', 'r+', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if email == row[1]:
                    return True
        return False

    def next_screen(self):
        """
        Processes user information and changes screens.
        :return: None and a tuple containing user's name, email, and phone number.
        """
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

    def import_to_csv(self) -> None:
        """
        Takes the user's info plus their candidate choice and stores it in a CSV file.
        :return: None
        """
        row_one = ['Name', 'Email', 'Phone', 'Choice']
        name_input, email_input, phone_input = self.next_screen()
        try:
            if not self.main_ui.radio_jane.isChecked() or not self.main_ui.radio_john.isChecked():
                choice = 'Jane' if self.main_ui.radio_jane.isChecked() else 'John'
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
                        f"Thank you {name_input} for voting for {choice}!"
                    )
                    self.close()
            else:
                raise ValueError('Please select a candidate.')

        except ValueError as e:
            QtWidgets.QMessageBox.warning(
                None,
                "Warning!",
                str(e)
            )
            return

        print(f'done')

    def clear_input(self) -> None:
        """
        Clears all text boxes in application.
        :return: None
        """
        self.main_ui.name_text_box.clear()
        self.main_ui.email_text_box.clear()
        self.main_ui.phone_text_box.clear()
