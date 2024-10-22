import sys

from PyQt6.QtWidgets import QApplication

from model import DataModel
from presenter import MainPresenter
from view import MainView


def main() -> None:
    """
    Main function to initialize and run the MVP PyQt6 application.
    This function creates the model, view, and presenter, connects the signals,
    and starts the application loop.
    """
    app = QApplication(sys.argv)

    # Create the model, view, and presenter
    model = DataModel()
    presenter = MainPresenter(view=None, model=model)
    view = MainView(presenter=presenter)

    # Set the presenter view and connect signals
    presenter.view = view
    view.connect_signals()

    # Show the view and start the application
    view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
