from PyQt6.QtWidgets import QApplication
from controller import BMIController

if __name__ == "__main__":
    app = QApplication([])
    controller = BMIController()
    app.exec()


