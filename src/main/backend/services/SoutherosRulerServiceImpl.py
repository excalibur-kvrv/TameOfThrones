from src.main.backend.repositoryservices.KingdomRepositoryServiceDummyImpl import KingdomRepositoryServiceDummyImpl
from src.main.backend.models.Ruler import Ruler
from src.main.backend.services.SoutherosRulerService import SoutherosRulerService

from collections import OrderedDict
from typing import List


class SoutherosRulerServiceImpl(SoutherosRulerService):
    REPO_SERVICE = KingdomRepositoryServiceDummyImpl

    def find_all_allies_for_rulers(self, messages) -> List[Ruler]:
        repo_service = self.REPO_SERVICE()

        mappings = repo_service.get_all_southeros_kingdoms()
        rulers = mappings["ruler"]
        kingdoms = mappings["kingdoms"]

        result = []

        for ruler_name in rulers:
            ruler = rulers[ruler_name]
            allies = OrderedDict()

            for kingdom_name, message in messages:
                if kingdom_name not in kingdoms or kingdom_name in allies:
                    continue

                kingdom = kingdoms[kingdom_name]
                encrypted_message = ruler.send_message(message, kingdom.get_emblem())
                will_ally = kingdom.receive_message(encrypted_message)
                if will_ally:
                    allies[kingdom_name] = kingdom

            for ally in allies.values():
                ruler.add_ally(ally)

            result.append(ruler)

        return result
