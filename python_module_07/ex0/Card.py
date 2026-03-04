from abc import ABC, abstractmethod
from enum import Enum


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"
    ELITE = "Elite"
    TOURNAMENT = "Tournament"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost if cost > 0 else 0
        self.rarity = rarity

    def play(self, game_state: dict) -> dict:
        pass

    play = abstractmethod(play)

    def _get_card_type(self) -> str:
        class_name = self.__class__.__name__
        mapping = {
            "CreatureCard": CardType.CREATURE.value,
            "SpellCard": CardType.SPELL.value,
            "ArtifactCard": CardType.ARTIFACT.value,
            "EliteCard": CardType.ELITE.value,
            "TournamentCard": CardType.TOURNAMENT.value,
        }
        return mapping.get(class_name, class_name.replace("Card", ""))

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self._get_card_type()
        }

    def is_playable(self, available_mana: int) -> bool:
        if isinstance(available_mana, int):
            return available_mana >= self.cost
        raise ValueError("int Error")
