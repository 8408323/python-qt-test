class DataModel:
    """
    The Model class that handles data storage and business logic.
    """

    def __init__(self) -> None:
        """
        Initializes the data model with default values.
        """
        self.message = "Click a button to interact"

    def get_message(self) -> str:
        """
        Retrieves the current message.

        Returns:
            str: The current message stored in the model.
        """
        return self.message

    def set_message(self, message: str) -> None:
        """
        Updates the message in the model.

        Args:
            message (str): The message to be stored in the model.
        """
        self.message = message

    def reset_message(self) -> None:
        """
        Resets the message to the default value.
        """
        self.message = "Click a button to interact"
