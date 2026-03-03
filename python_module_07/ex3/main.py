import random

from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    engine = GameEngine()
    factory = FantasyCardFactory(rng=random.Random(42))
    strategy = AggressiveStrategy(starting_mana=6)

    engine.configure_engine(factory, strategy)

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")
    print()
    print("Simulating aggressive turn...")
    result = engine.simulate_turn()
    print("Hand:", result["hand"])
    print()
    print("Turn execution:")
    print(f"Strategy: {result['turn_execution']['strategy']}")
    print(f"Actions: {result['turn_execution']['actions']}")
    print()
    print("Game Report:")
    print(result["game_report"])
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
