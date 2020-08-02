from typing import Dict, Any
import abc


class KingdomRepositoryService(metaclass=abc.ABCMeta):
    """ A class to handle getting southeros kingdoms from kingdoms.json file.
    """

    @abc.abstractmethod
    def get_all_southeros_kingdoms(self) -> Dict[str, Dict[str, Any]]:
        """
        get_all_southeros_kingdoms() -> This function will return a dictionary of the form
        {"rulers": [Ruler], "kingdoms": [kingdoms1, .... kingdomN]}
        :return: Returns a dictionary mapping of ruler and kingdom objects.
        """

        pass
