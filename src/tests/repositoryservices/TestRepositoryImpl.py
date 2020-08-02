from src.main.backend.repositoryservices.KingdomRepositoryServiceDummyImpl import KingdomRepositoryServiceDummyImpl

import unittest


class TestKingdomRepository(unittest.TestCase):
    repo_service = KingdomRepositoryServiceDummyImpl()

    def test_deserialization(self):
        mappings = self.repo_service.get_all_southeros_kingdoms()

        assert "SPACE" in mappings["ruler"], f"Expected SPACE in deserialized object"

        expected_allies = {"LAND", "WATER", "ICE", "FIRE", "AIR"}

        for ally in mappings["kingdoms"]:
            assert ally in expected_allies, f"Expected {ally} to be in {expected_allies}"
            expected_allies.discard(ally)

        assert len(expected_allies) == 0
