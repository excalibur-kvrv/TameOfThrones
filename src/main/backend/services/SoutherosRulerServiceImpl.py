from src.main.backend.models.Ruler import Ruler
from src.main.backend.services.SoutherosRulerService import SoutherosRulerService
from src.main.backend.repositoryservices.KingdomRepositoryServiceDummyImpl import KingdomRepositoryServiceDummyImpl
from typing import List


class SoutherosRulerServiceImpl(SoutherosRulerService):
    repo_service = KingdomRepositoryServiceDummyImpl()

    def find_all_allies_for_rulers(self, messages) -> List[Ruler]:
        mappings = self.repo_service.get_all_southeros_kingdoms()
        rulers = mappings["ruler"]
        kingdoms = mappings["kingdoms"]

        result = []

        for ruler_name in rulers:
            ruler = rulers[ruler_name]
            for kingdom_name, message in messages:
                if kingdom_name not in kingdoms:
                    continue

                kingdom = kingdoms[kingdom_name]
                encrypted_message = ruler.send_message(message, kingdom.get_emblem())
                will_ally = kingdom.receive_message(encrypted_message)
                if will_ally:
                    ruler.add_ally(kingdom)

            result.append(ruler)

        return result
