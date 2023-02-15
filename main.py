from PySide6.QtWidgets import QWidget, QApplication, QMainWindow,QVBoxLayout, QLabel, QFormLayout, QPushButton, QFileDialog, QHBoxLayout
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtCore import QSize, Qt, QUrl
from PIL import Image
import sys, os

class MainWindow(QMainWindow):
	filename = ""
	folder = ""
	buton_sytle = '''
	border-style: solid;
	background-color: #537FE7;
	border-width: 0px;
	border-radius: 5px;
	'''
	def __init__(self):
		super().__init__()
		self.setContentsMargins(0,0,0,0)
		self.setWindowTitle("Compresor de Imágenes")
		self.setWindowIcon(QIcon("imagen.png"))
		self.setFixedSize(QSize(600, 400))
		self.interface()
		self.setStyleSheet('''
		margin:0;
		background-color:#C0EEF2;
		font-family:"Montserrat"
		''')
		
	def interface(self):
		titulo = QLabel('Compresor de Imágenes');titulo.setStyleSheet('background-color:#E9F8F9; margin: 0; font-size:26px')
		titulo.setAlignment(Qt.AlignCenter)
		self.bFile = QPushButton("Seleccionar un archivo");self.bFile.setFixedSize(160, 50);self.bFile.setStyleSheet(self.buton_sytle)
		self.fileSelected = QLabel("Archivo seleccionado: ")
		self.bOutput = QPushButton("Selecionar una carpeta de salida");self.bOutput.setFixedSize(250,50);self.bOutput.setStyleSheet(self.buton_sytle)
		self.folderSelected = QLabel("Carpeta de Salida seleccionada:")
		self.bCompress = QPushButton("Comprimir!");self.bCompress.setFixedSize(150,50);compress_layout = QVBoxLayout(); compress_layout.addWidget(self.bCompress); compress_layout.setAlignment(Qt.AlignCenter); self.bCompress.setStyleSheet(self.buton_sytle)
		footer = QLabel('<a href="https://www.instagram.com/augusto_silva.py/">AugustoSilva</a>');footer.setOpenExternalLinks(True);footer.setAlignment(Qt.AlignCenter); footer.setStyleSheet('background-color:#181823;color:#fff; font-size:20px;')

		def handleLinkClick(url):
			QDesktopServices.openUrl(QUrl(url))

		footer.linkActivated.connect(handleLinkClick)

		hLayoutFile = QHBoxLayout()
		hLayoutFile.addWidget(self.bFile)
		hLayoutFile.addWidget(self.fileSelected)

		hLayoutFolder = QHBoxLayout()
		hLayoutFolder.addWidget(self.bOutput)
		hLayoutFolder.addWidget(self.folderSelected)
		

		layout = QVBoxLayout()
		layout.addWidget(titulo)
		layout.addLayout(hLayoutFile)
		layout.addLayout(hLayoutFolder)
		layout.addLayout(compress_layout)
		layout.addWidget(footer)


		widget = QWidget()
		widget.setLayout(layout)

		self.setCentralWidget(widget)

		self.bFile.clicked.connect(self.selector_file)
		self.bOutput.clicked.connect(self.select_output)
		self.bCompress.clicked.connect(self.compress_image)

	def selector_file(self):
		self.filename, _ = QFileDialog.getOpenFileName(self,"Seleciona un archivo", "", "Archivos de imagen (*.jpg *.jpeg *.png)")
		self.fileSelected.setText(f"Archivo selecionado: {self.filename}")

	def select_output(self):
		self.folder = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta", "")
		self.folderSelected.setText(f"Carpeta de Salida seleccionada: {self.folder}")
	
	def compress_image(self):
		print(f"comprimiendo a {self.filename} para ponerlo en {self.folder}")
		filename = self.filename[2:] 
		folder = self.folder[2:]+ '/'
		print(f"\n comprimiendo a {filename} para ponerlo en {folder}")
		image = Image.open(filename)
		imageName = os.path.basename(filename)
		print(f"\n {imageName}")
		image.save(folder +'compressed_'+  imageName, optimize=True, quality=60)

if __name__ == '__main__':
	app = QApplication()
	app.setStyle("Fusion")
	window = MainWindow()
	window.show()
	app.exec()
