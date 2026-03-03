from abc import ABC, abstractmethod


class Magical(ABC):
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass

    cast_spell = abstractmethod(cast_spell)
    channel_mana = abstractmethod(channel_mana)
    get_magic_stats = abstractmethod(get_magic_stats)
