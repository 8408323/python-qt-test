import sys

from PyQt6.QtCore import pyqtSlot

from model import DataModel
from view import MainView


class MainPresenter:
    """
    The Presenter class that handles logic and interacts with the View and Model.
    """

    def __init__(self, view: MainView, model: DataModel) -> None:
        """
        Initializes the presenter with the provided view and model.

        Args:
            view (MainView): The view instance responsible for displaying the UI.
            model (DataModel): The model instance responsible for handling data and logic.
        """
        self.view = view
        self.model = model

    @pyqtSlot()
    def on_show_message(self, checked: bool) -> None:
        """
        Handles the logic for the 'Show Message' button click.

        Args:
            checked (bool): Not used argument, but required for the signal connection.
        """
        self.model.set_message('Hello! You clicked the Show Message button.')
        self.view.set_label_text(self.model.get_message())

    @pyqtSlot()
    def on_close_app(self, checked: bool) -> None:
        """
        Handles the logic for the 'Close' button click.

        Args:
            checked (bool): Not used argument, but required for the signal connection.
        """
        sys.exit(0)

    @pyqtSlot()
    def on_reset_label(self, checked: bool) -> None:
        """
        Handles the logic for the 'Reset' button click.

        Args:
            checked (bool): Not used argument, but required for the signal connection.
        """
        self.model.reset_message()
        self.view.set_label_text(self.model.get_message())
