from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel


class MainView(QWidget):
    """
    The View class that handles the user interface.
    """

    def __init__(self, presenter) -> None:
        """
        Initializes the View and sets up the UI components.

        Args:
            presenter: The presenter instance responsible for handling user interaction.
        """
        super().__init__()
        self.presenter = presenter
        self._init_ui()

    def _init_ui(self) -> None:
        """
        Initializes and sets up the user interface by creating widgets and layouts.
        """
        self.label = QLabel("Click a button to interact", self)
        self.button_message = QPushButton("Show Message", self)
        self.button_close = QPushButton("Close", self)
        self.button_reset = QPushButton("Reset", self)

        # Set buttons as not checkable (no toggle buttons)
        self.button_message.setCheckable(False)
        self.button_close.setCheckable(False)
        self.button_reset.setCheckable(False)

        # Create layout and add widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button_message)
        self.layout.addWidget(self.button_close)
        self.layout.addWidget(self.button_reset)
        self.setLayout(self.layout)

        self.setWindowTitle("MVP PyQt6 Example")
        self.setGeometry(100, 100, 300, 200)

    def connect_signals(self) -> None:
        """
        Connects button signals to presenter methods.
        Should be called after the presenter is assigned.
        """
        self.button_message.clicked.connect(lambda checked: self.presenter.on_show_message(checked))
        self.button_close.clicked.connect(lambda checked: self.presenter.on_close_app(checked))
        self.button_reset.clicked.connect(lambda checked: self.presenter.on_reset_label(checked))

    def set_label_text(self, text: str) -> None:
        """
        Updates the label text in the view.

        Args:
            text (str): The text to be displayed on the label.
        """
        self.label.setText(text)
