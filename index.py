import sys
import math
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt


class ScientificCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Scientific Calculator")
        self.setGeometry(100, 100, 450, 680)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setFont(QFont("Arial", 14))
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet("background-color: #AAAAAA; color: black; padding: 30px 12px; border-radius: 5px;")
        layout.addWidget(self.display)

        grid_layout = QGridLayout()
        buttons = [
            ('(', 0, 0, "#6666FF"), (')', 0, 1, "#6666FF"), ('sin', 0, 2, "#6666FF"), ('cos', 0, 3, "#6666FF"),
            ('tan', 0, 4, "#6666FF"),
            ('^', 1, 0, "#6666FF"),('sqrt',1,1,"#6666FF"), ('log', 1, 2, "#6666FF"), ('ln', 1, 3, "#6666FF"),('pi', 1, 4, "#6666FF"),
            ('7', 2, 0, "#2F3F4F"), ('8', 2, 1, "#2F3F4F"), ('9', 2, 2, "#2F3F4F"),('!', 2, 3, "#A27BBF"),('%', 2, 4, "#A27BBF"),
            ('4', 3, 0, "#2F3F4F"), ('5', 3, 1, "#2F3F4F"), ('6', 3, 2, "#2F3F4F"),('/', 3, 3, "#A27BBF"),
            ('*', 3, 4, "#A27BBF"),
            ('1', 4, 0, "#2F3F4F"), ('2', 4, 1, "#2F3F4F"), ('3', 4, 2, "#2F3F4F"), ('-', 4, 3, "#A27BBF"),
            ('+', 4, 4, "#A27BBF"),
            ('0', 5, 0, "#2F3F4F"), ('.', 5, 1, "#2F3F4F"), ('=', 5, 2, "#FF2900"), ('DEL', 5, 3, "#FF2900"),
            ('C', 5, 4,"#FF2900")
            ]


        for text, row, col, color in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Arial", 18,QFont.Weight.Bold))
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color}; 
                    color: white; 
                    border-radius: 10px; 
                    padding: 15px;
                }}
                QPushButton:hover {{
                    background-color: #555;
                }}
                QPushButton:pressed {{
                    background-color: #777;
                }}
            """)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(self.on_button_click)
            button.setMinimumSize(70, 70)
            grid_layout.addWidget(button, row, col)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def on_button_click(self):
        sender = self.sender().text()
        if sender == 'C':
            self.display.clear()
        elif sender == 'DEL':
            self.display.setText(self.display.text()[:-1])
        elif sender == '=':
            try:
                expression = self.display.text()

                # Replace other mathematical functions with Python equivalents
                expression = expression.replace('sqrt', 'math.sqrt')  # Handle exponentiation
                expression = expression.replace('^', '**')
                expression = expression.replace('invs', 'math.')
                expression = expression.replace('log', 'math.log10').replace('ln', 'math.log')
                expression = expression.replace('pi', 'math.pi').replace('e', 'math.e')
                expression = expression.replace('sin', 'math.sin(math.radians').replace('cos','math.cos(math.radians').replace('tan', 'math.tan(math.radians')
                expression = expression.replace(')', '))') if 'math.radians' in expression else expression

                # Evaluate the expression safely
                result = eval(expression)
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        elif sender == '!':
            # Handle the factorial function
            try:
                number = int(self.display.text())
                if number < 0:
                    self.display.setText("Error")
                else:
                    result = math.factorial(number)
                    self.display.setText(str(result))
            except ValueError:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + sender)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScientificCalculator()
    window.show()
    sys.exit(app.exec())
