class InputParsingError:
    """ Exception raised when an Input Validator is provided with invalid data.
    """

    def __init__(self, message):
        """
        :param message: a helpful message to indicate the error.
        """

        super().__init__(message)


class InputValidatorNotImplemented:
    """ Exception raised when a custom input validator to check input data has not been defined.
    """

    def __init__(self, message: str):
        """
        :param message: a helpful message to indicate the error.
        """

        super().__init__(message)
