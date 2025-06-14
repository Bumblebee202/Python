from PySide6.QtWidgets import QApplication
from Views.MainWindow import MainWindow



app = QApplication([])

widget = MainWindow()
widget.resize(480, 320)
widget.show()

app.exec()