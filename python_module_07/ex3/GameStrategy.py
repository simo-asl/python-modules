from abc import ABC, abstractmethod
from typing import Any, Dict, List


class GameStrategy(ABC):
    def execute_turn(self, hand: List[Any],
                     battlefield: List[Any]) -> Dict[str, Any]:
        pass

    def get_strategy_name(self) -> str:
        pass

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        pass

    execute_turn = abstractmethod(execute_turn)
    get_strategy_name = abstractmethod(get_strategy_name)
    prioritize_targets = abstractmethod(prioritize_targets)
