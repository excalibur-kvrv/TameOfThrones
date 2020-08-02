from src.main.backend.utils.CryptographyFactory import CryptographyFactory
from src.main.backend.models.Kingdom import Kingdom
from src.main.backend.models.Ruler import Ruler
from src.main.backend.repositoryservices.KingdomRepositoryService import KingdomRepositoryService

from typing import Dict, Any
import json
import os


class KingdomRepositoryServiceDummyImpl(KingdomRepositoryService):
    REPO_PATH = os.path.join("src", "main", "resources", "kingdoms.json")

    def get_all_southeros_kingdoms(self) -> Dict[str, Dict[str, Any]]:
        mappings = {"ruler": {}, "kingdoms": {}}

        with open(self.REPO_PATH) as repository:
            json_data = json.load(repository)

        crypto_type = json_data["cipher_type"].lower()
        crypto_strategy = CryptographyFactory.get_cryptographic_strategy(crypto_type)

        for ruler in json_data["rulers"]:
            emblem = json_data["rulers"][ruler]
            new_ruler = Ruler(ruler, emblem, crypto_strategy)
            mappings["ruler"][ruler] = new_ruler

        for ally in json_data["allies"]:
            emblem = json_data["allies"][ally]
            new_kingdom = Kingdom(ally, emblem, crypto_strategy)
            mappings["kingdoms"][ally] = new_kingdom

        return mappings
