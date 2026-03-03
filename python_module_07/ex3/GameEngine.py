from typing import Any, Dict, List, Optional

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None

        self.hand: List[Any] = []
        self.battlefield: List[Any] = []

        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy,
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        if self.factory is None or self.strategy is None:
            raise ValueError(
                "GameEngine is not configured: set factory and strategy first."
            )

        self.hand = [
            self.factory.create_creature("Fire Dragon"),
            self.factory.create_creature("Goblin Warrior"),
            self.factory.create_spell("Lightning Bolt"),
        ]
        self.cards_created += 3

        report = self.strategy.execute_turn(self.hand, self.battlefield)

        actions = report.get("actions", {})
        damage = actions.get("damage_dealt", 0)
        if isinstance(damage, int):
            self.total_damage += damage

        self.turns_simulated += 1

        hand_display = ", ".join(
            f"{card.get_card_info()['name']} ({card.get_card_info()['cost']})"
            for card in self.hand
        )

        return {
            "factory": type(self.factory).__name__,
            "strategy": self.strategy.get_strategy_name(),
            "hand": f"[{hand_display}]",
            "turn_execution": report,
            "game_report": self.get_engine_status(),
        }

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": (
                self.strategy.get_strategy_name()
                if self.strategy is not None
                else None
            ),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
