from enum import Enum

from ex0.Card import Card


class SpellEffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(effect_type, str) or not effect_type.strip():
            raise ValueError("Effect type must be a non-empty string")

        normalized_effect = effect_type.strip().lower()
        self.effect_type: str = normalized_effect

        if not self._validate_effect_type():
            raise ValueError(
                "Effect type must be one of: damage, heal, buff, debuff"
            )

    def _validate_effect_type(self) -> bool:
        allowed = {effect.value for effect in SpellEffectType}
        return self.effect_type in allowed

    def play(self, game_state: dict) -> dict:
        effect_map = {
            SpellEffectType.DAMAGE.value: "Deal 3 damage to target",
            SpellEffectType.HEAL.value: "Restore 3 health to target",
            SpellEffectType.BUFF.value: "Increase target stats",
            SpellEffectType.DEBUFF.value: "Reduce target stats",
        }

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_map[self.effect_type],
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True,
        }
