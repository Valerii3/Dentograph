from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QMessageBox


class DiagnosticDetailsWindow(QMainWindow):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.media_player = QMediaPlayer(self)
        self.video_widget = QVideoWidget(self)
        self.init_ui()

    def init_ui(self):
        # Set up video widget
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.file_path)))

        # Set up play and stop actions
        play_action = QAction('Play', self)
        play_action.triggered.connect(self.media_player.play)

        stop_action = QAction('Stop', self)
        stop_action.triggered.connect(self.media_player.stop)

        # Add actions to menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(play_action)
        file_menu.addAction(stop_action)

        # Add video widget to central widget
        self.setCentralWidget(self.video_widget)

        # Set window properties
        self.setWindowTitle('Video Player')
        self.setGeometry(100, 100, 800, 600)
        self.show()