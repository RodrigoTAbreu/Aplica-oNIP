from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication #importa os widgets



app = QApplication()

loader = QUiLoader()
window = loader.load('login.ui')
window.show()


app.exec()