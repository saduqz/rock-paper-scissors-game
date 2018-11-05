class GenericException(Exception):
    """Class for General API exceptions api exceptions."""

    def __init__(self, message):
        self.custom_message = message

    def __str__(self):
        return repr(self.custom_message)

    @property
    def message(self):
        """
        The user friendly message property
        """
        return self.custom_message
