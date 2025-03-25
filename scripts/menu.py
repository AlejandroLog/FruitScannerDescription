import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class FruitRecognitionApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle("Sistema de Reconocimiento de Frutas")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Widget central y layout principal
        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)
        mainLayout = QtWidgets.QVBoxLayout()
        centralWidget.setLayout(mainLayout)

        # Título con estilo
        title = QtWidgets.QLabel("Sistema de Reconocimiento de Frutas")
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setFont(QtGui.QFont("Comic Sans MS", 22, QtGui.QFont.Bold))
        title.setStyleSheet("color: #333333; margin: 20px;")
        mainLayout.addWidget(title)

        # Layout para los botones principales
        btnLayout = QtWidgets.QHBoxLayout()
        self.btnCelular = QtWidgets.QPushButton("Con Celular")
        self.btnCelular.setFixedSize(200, 50)
        self.btnCelular.setStyleSheet("""
            QPushButton {
                background-color: #ffcc00;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                color: #333333;
            }
            QPushButton:hover {
                background-color: #ffdd33;
            }
        """)
        self.btnWebcam = QtWidgets.QPushButton("Con Cámara Web")
        self.btnWebcam.setFixedSize(200, 50)
        self.btnWebcam.setStyleSheet("""
            QPushButton {
                background-color: #66ccff;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                color: #333333;
            }
            QPushButton:hover {
                background-color: #88d0ff;
            }
        """)
        # Agregar botones centrados
        btnLayout.addStretch()
        btnLayout.addWidget(self.btnCelular)
        btnLayout.addSpacing(40)
        btnLayout.addWidget(self.btnWebcam)
        btnLayout.addStretch()
        mainLayout.addLayout(btnLayout)

        # Línea separadora
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        mainLayout.addWidget(separator)

        # Layout para la información de las frutas
        infoLayout = QtWidgets.QHBoxLayout()

        # Lista de frutas
        self.listFruits = QtWidgets.QListWidget()
        self.listFruits.addItems(["Plátano", "Mango", "Piña", "Manzana"])
        self.listFruits.setFixedWidth(150)
        self.listFruits.setStyleSheet("font-size: 16px; padding: 5px;")
        infoLayout.addWidget(self.listFruits)

        # Widget de detalle para mostrar información
        self.detailWidget = QtWidgets.QTextEdit()
        self.detailWidget.setReadOnly(True)
        self.detailWidget.setStyleSheet("""
            font-size: 14px;
            background-color: #ffffff;
            padding: 10px;
            border: 1px solid #cccccc;
        """)
        infoLayout.addWidget(self.detailWidget)

        mainLayout.addLayout(infoLayout)

        # Datos de ejemplo para cada fruta
        self.fruitData = {
            "Plátano": "Información nutrimental:\n- Calorías: 89 kcal\n\nPrecio: $1.00 c/u\n\nReceta: Batido de plátano y avena.",
            "Mango": "Información nutrimental:\n- Calorías: 60 kcal\n\nPrecio: $1.50 c/u\n\nReceta: Ensalada tropical de mango.",
            "Piña": "Información nutrimental:\n- Calorías: 50 kcal\n\nPrecio: $2.00 c/u\n\nReceta: Piña colada light.",
            "Manzana": "Información nutrimental:\n- Calorías: 52 kcal\n\nPrecio: $1.20 c/u\n\nReceta: Manzana asada con canela."
        }

        # Selección por defecto
        self.listFruits.setCurrentRow(0)
        self.displayFruitInfo(self.listFruits.currentItem(), None)

        # Conectar señales
        self.listFruits.currentItemChanged.connect(self.displayFruitInfo)
        self.btnCelular.clicked.connect(self.useCelular)
        self.btnWebcam.clicked.connect(self.useWebcam)

        # Barra de estado
        self.statusBar().showMessage("Listo")

    def displayFruitInfo(self, current, previous):
        if current:
            fruit = current.text()
            self.detailWidget.setText(self.fruitData.get(fruit, "Sin información disponible."))

    def useCelular(self):
        QtWidgets.QMessageBox.information(self, "Con Celular",
                                          "Funcionalidad para reconocimiento con celular no implementada.")

    def useWebcam(self):
        QtWidgets.QMessageBox.information(self, "Con Cámara Web",
                                          "Funcionalidad para reconocimiento con cámara web no implementada.")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = FruitRecognitionApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
