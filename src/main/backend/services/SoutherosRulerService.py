from src.main.backend.models.Ruler import Ruler
from typing import List
import abc


class SoutherosRulerService(metaclass=abc.ABCMeta):
    """ A class to model the service of finding potential allies for rulers.
    """

    @abc.abstractmethod
    def find_all_allies_for_rulers(self, messages) -> List[Ruler]:
        """
        find_all_allies_for_rulers() -> This method finds all the allies for the rulers in the repository
        :param messages: The messages that are sent by the ruler to each kingdom
        :return: a list of rulers
        """

        pass
