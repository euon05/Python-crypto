import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('간단 계산기')
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()
        self.input = QLineEdit()
        self.input.setPlaceholderText("예: 10 + 5")
        self.result_label = QLabel("")
        layout.addWidget(self.input)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
        self.input.returnPressed.connect(self.calculate)

    def calculate(self):
        try:
            eq = self.input.text()
            self.result_label.setText(str(eval(eq)))
        except:
            self.result_label.setText("오류: 잘못된 수식")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())