from PyQt6.QtWidgets import QApplication
from model import BMIModel
from view import BMIView


class BMIController:
    def __init__(self):
        self.model = BMIModel()
        self.view = BMIView()

        # Connect signals
        self.view.calculate_button.clicked.connect(self.calculate_bmi)

        self.view.show()

    def calculate_bmi(self):
        """Calculate BMI based on user input and selected units."""
        try:
            weight = float(self.view.weight_input.text())
            height = float(self.view.height_input.text())

            # Check if user selected Imperial
            if self.view.unit_combo.currentIndex() == 1:  # Imperial system
                weight = weight * 0.453592  # Convert lbs to kg
                height = height * 0.0254  # Convert inches to meters

            # Ensure valid inputs
            if weight <= 0 or height <= 0:
                self.view.show_error("Weight and height must be positive numbers.")
                return

            # Calculate BMI
            bmi = self.model.calculate_bmi(weight, height)

            # Determine BMI status
            status = self.model.get_bmi_status(bmi)

            # Update the view with the results
            self.view.update_bmi_display(bmi, status)

        except ValueError:
            self.view.show_error("Please enter valid numerical values for weight and height.")


if __name__ == "__main__":
    app = QApplication([])
    controller = BMIController()
    app.exec()
