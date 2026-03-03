import random

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self, rng: random.Random | None = None) -> None:
        self._rng = rng or random.Random()

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            if "Dragon" in name_or_power:
                return CreatureCard(name_or_power, 5, "Legendary", 7, 5)
            return CreatureCard(name_or_power, 2, "Common", 3, 2)

        if isinstance(name_or_power, int):
            power = max(1, name_or_power)
            return CreatureCard(
                "Custom Creature",
                max(1, power // 2),
                "Rare",
                power,
                max(1, power - 1),
            )

        if self._rng.random() < 0.5:
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 3, 2)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            if "Lightning" in name_or_power:
                return SpellCard("Lightning Bolt", 3, "Common", "damage")
            return SpellCard("Fireball", 4, "Rare", "damage")

        if isinstance(name_or_power, int):
            return SpellCard("Arcane Blast", 3, "Common", "damage")

        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            return ArtifactCard("Mana Ring", 2, "Rare", 3, "+1 mana per turn")

        if isinstance(name_or_power, int):
            durability = max(1, name_or_power)
            return ArtifactCard(
                "Durability Relic",
                2,
                "Common",
                durability,
                "Permanent: test effect",
            )

        return ArtifactCard("Mana Ring", 2, "Rare", 3, "+1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        if not isinstance(size, int) or size <= 0:
            raise ValueError("size must be a positive integer")

        cards: list[Card] = []

        for _ in range(size):
            roll = self._rng.random()
            if roll < 0.45:
                cards.append(self.create_creature())
            elif roll < 0.75:
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())

        return {
            "theme": "fantasy",
            "size": size,
            "cards": cards,
        }
