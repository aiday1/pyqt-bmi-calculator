class BMIModel:
    def calculate_bmi(self, weight, height):
        """Calculate BMI using the formula: BMI = weight (kg) / [height (m)]²"""
        return weight / (height ** 2)

    def get_bmi_status(self, bmi):
        """Determine BMI category based on standard ranges."""
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

