from abc import ABC, abstractmethod
from enum import Enum


class CombatType(Enum):
    MELEE = "melee"


class Combatable(ABC):
    def attack(self, target: str) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    attack = abstractmethod(attack)
    defend = abstractmethod(defend)
    get_combat_stats = abstractmethod(get_combat_stats)
