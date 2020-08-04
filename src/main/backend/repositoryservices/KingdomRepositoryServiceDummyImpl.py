from src.main.backend.globals.constants import KINGDOM_DATA, STRATEGY
from src.main.backend.models.Kingdom import Kingdom
from src.main.backend.models.Ruler import Ruler
from src.main.backend.repositoryservices.KingdomRepositoryService import KingdomRepositoryService
from src.main.backend.utils.CryptographyFactory import CryptographyFactory

from typing import Dict, Any
import json


class KingdomRepositoryServiceDummyImpl(KingdomRepositoryService):
    REPO_PATH = KINGDOM_DATA

    def get_all_southeros_kingdoms(self) -> Dict[str, Dict[str, Any]]:
        mappings = {"ruler": {}, "kingdoms": {}}

        with open(self.REPO_PATH) as repository:
            json_data = json.load(repository)

        crypto_factory = CryptographyFactory()
        crypto_strategy = crypto_factory.get_cryptographic_strategy(STRATEGY)

        for ruler in json_data["rulers"]:
            emblem = json_data["rulers"][ruler]
            new_ruler = Ruler(ruler, emblem, crypto_strategy)
            mappings["ruler"][ruler] = new_ruler

        for ally in json_data["allies"]:
            emblem = json_data["allies"][ally]
            new_kingdom = Kingdom(ally, emblem, crypto_strategy)
            mappings["kingdoms"][ally] = new_kingdom

        return mappings
