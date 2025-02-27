import sys, math
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ScientificCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific Calculator")
        self.setGeometry(100, 100, 400, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.display = QLineEdit(self, readOnly=True, alignment=Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Arial", 24))
        layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            ('(', ')', 'sin', 'cos', 'tan'), ('^', 'sqrt', 'log', 'ln', 'pi'),
            ('7', '8', '9', '!', '%'), ('4', '5', '6', '/', '*'),
            ('1', '2', '3', '-', '+'), ('0', '.', '=', 'DEL', 'AC')
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = QPushButton(text, clicked=self.on_button_click)
                btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
                btn.setMinimumSize(70, 70)
                grid.addWidget(btn, r, c)

        layout.addLayout(grid)
        self.setLayout(layout)

    def on_button_click(self):
        sender = self.sender().text()
        if sender == 'AC':
            self.display.clear()
        elif sender == 'DEL':
            self.display.setText(self.display.text()[:-1])
        elif sender == '=':
            try:
                exp = self.display.text().replace('sqrt', 'math.sqrt').replace('^', '**')
                exp = exp.replace('log', 'math.log10').replace('ln', 'math.log')
                exp = exp.replace('pi', 'math.pi').replace('!', 'math.factorial')
                exp = exp.replace('sin', 'math.sin(math.radians').replace('cos', 'math.cos(math.radians')
                exp = exp.replace('tan', 'math.tan(math.radians') + ')' if 'math.radians' in exp else exp
                self.display.setText(str(eval(exp)))
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + sender)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScientificCalculator()
    window.show()
    sys.exit(app.exec())
