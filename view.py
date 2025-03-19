from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox,
    QMessageBox, QMenuBar, QMenu
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt


class BMIView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 400, 300)

        # Menu Bar
        self.menu_bar = QMenuBar(self)
        file_menu = QMenu("File", self)
        help_menu = QMenu("Help", self)
        self.menu_bar.addMenu(file_menu)
        self.menu_bar.addMenu(help_menu)

        # File Menu Options
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_fields)
        file_menu.addAction(clear_action)
        file_menu.addAction(exit_action)

        # Help Menu Options
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

        # UI Components
        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Metric (kg, m)", "Imperial (lbs, in)"])

        self.weight_label = QLabel("Weight:")
        self.weight_input = QLineEdit()
        self.height_label = QLabel("Height:")
        self.height_input = QLineEdit()

        self.calculate_button = QPushButton("Calculate BMI")
        self.result_label = QLabel("Your BMI: ")
        self.status_label = QLabel("")

        # Layout
        layout = QVBoxLayout()
        layout.setMenuBar(self.menu_bar)
        layout.addWidget(self.unit_combo)
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

    def update_bmi_display(self, bmi, status):
        """Update the UI with BMI results and color-coded status."""
        self.result_label.setText(f"Your BMI: {bmi:.2f}")
        self.status_label.setText(status)

        # Apply color coding
        if status == "Underweight":
            self.status_label.setStyleSheet("color: orange; font-weight: bold;")
        elif status == "Normal weight":
            self.status_label.setStyleSheet("color: green; font-weight: bold;")
        elif status == "Overweight":
            self.status_label.setStyleSheet("color: darkorange; font-weight: bold;")
        else:
            self.status_label.setStyleSheet("color: red; font-weight: bold;")

    def clear_fields(self):
        """Reset input fields and result labels."""
        self.weight_input.clear()
        self.height_input.clear()
        self.result_label.setText("Your BMI: ")
        self.status_label.setText("")

    def show_error(self, message):
        """Display error messages."""
        QMessageBox.critical(self, "Error", message)

    def show_about(self):
        """Display information about the app."""
        QMessageBox.information(
            self, "About", "BMI Calculator\n\nEnter your weight and height, "
            "select the unit system, and click 'Calculate BMI'."
        )

