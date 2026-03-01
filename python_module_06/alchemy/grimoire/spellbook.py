def record_spell(spell_name: str, ingredients: str) -> str:
    import alchemy.grimoire as grimoire
    validation_result = grimoire.validate_ingredients(ingredients)
    if validation_result.endswith(" - VALID"):
        return f'Spell recorded: {spell_name} ({validation_result})'
    else:
        return f'Spell rejected: {spell_name} ({validation_result})'


def record_spell_injected(
        spell_name: str,
        ingredients: str,
        validator_func
        ) -> str:
    validation_result = validator_func(ingredients)
    if validation_result.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"
