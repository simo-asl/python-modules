from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable, CombatType
from ex2.Magical import Magical


class EliteCard(CreatureCard, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, mana_capacity: int) -> None:
        super().__init__(name, cost, rarity, attack, health)
        self.max_mana = mana_capacity
        self.current_mana = mana_capacity

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_type": CombatType.MELEE.value
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = incoming_damage
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "remaining_health": self.health,
            "survived": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack,
            "health": self.health,
            "mana": self.current_mana
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        spell_cost = len(targets)

        if self.current_mana < spell_cost:
            return {
                "caster": self.name,
                "spell": spell_name,
                "error": "Not enough mana"
            }

        self.current_mana -= spell_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": spell_cost,
            "remaining_mana": self.current_mana
        }

    def restore_mana(self, amount: int) -> int:
        self.current_mana += amount
        if self.current_mana > self.max_mana:
            self.current_mana = self.max_mana
        return self.current_mana
