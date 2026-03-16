import functools
import time
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def timed_call(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()

        output = func(*args, **kwargs)

        duration = time.time() - start
        print(f"Spell completed in {duration:.3f} seconds")
        return output

    return timed_call


def power_validator(min_power: int) -> Callable:
    def validator(func: Callable) -> Callable:
        @functools.wraps(func)
        def guarded_call(*args: Any, **kwargs: Any) -> Any:

            power_value = kwargs.get("power")

            if power_value is None:
                for item in args:
                    if isinstance(item, int):
                        power_value = item
                        break

            if power_value is not None and power_value < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return guarded_call

    return validator


def retry_spell(max_attempts: int) -> Callable:
    def retry_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def attempt_call(*args: Any, **kwargs: Any) -> Any:

            tries = 1
            while tries <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {tries}/{max_attempts})")
                    tries += 1

            return f"Spell casting failed after {max_attempts} attempts"

        return attempt_call

    return retry_decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(ch.isalpha() or ch.isspace() for ch in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print("Result:", result)

    print("\nTesting MageGuild...")

    guild = MageGuild()

    print(MageGuild.validate_mage_name("Alex The Great"))
    print(MageGuild.validate_mage_name("M@g3!"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
