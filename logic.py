from PyQt6.QtWidgets import *
from main_gui import *
from second_gui import *


class Logic(QMainWindow, Ui_vote_app, Ui_second_screen):

    def __init__(self):
        super().__init__()
        self.main_ui = Ui_vote_app()
        self.main_ui.setupUi(self)

        self.second_ui = Ui_second_screen()
        self.second_ui.setupUi(self)

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.main_ui.centralwidget)
        self.stacked_widget.addWidget(self.second_ui.centralwidget)

        self.setCentralWidget(self.stacked_widget)

        self.stacked_widget.setCurrentIndex(0)

        self.main_ui.submit_button.clicked.connect(self.goto_second_screen)

    def goto_second_screen(self):
        self.stacked_widget.setCurrentIndex(1)
