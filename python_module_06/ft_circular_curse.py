import alchemy.grimoire as grimoire

print('\n=== Circular Curse Breaking ===')

print('\nTesting ingredient validation:')
try:
    print('validate_ingredients("fire air")'
          f': {grimoire.validate_ingredients("fire air")}')
    print('validate_ingredients("dragon scales")'
          f': {grimoire.validate_ingredients("dragon scales")}')
except Exception as e:
    print(f'ERROR: {e}')

print('\nTesting spell recording with validation:')
try:
    print('record_spell("Fireball", "fire air")'
          f': {grimoire.record_spell("Fireball", "fire air")}')
    print('record_spell("Dark Magic", "shadow")'
          f': {grimoire.record_spell("Dark Magic", "shadow")}')
except Exception as e:
    print(f'ERROR: {e}')

print('\nTesting late import technique:')
try:
    print('record_spell("Lightning", "air")'
          f': {grimoire.record_spell("Lightning", "air")}')
except Exception as e:
    print(f'ERROR: {e}')

print('\nCircular dependency curse avoided using late imports!')
print('All spells processed safely!')

print('\nTesting dependency injection technique:')
try:
    print('record_spell_injected("Injected Spell", ', end="")
    print('"fire", validate_ingredients)'
          f': {grimoire.record_spell_injected("Injected Spell", "fire",
                                              grimoire.validate_ingredients)}')
    print('record_spell_injected("Bad Injected Spell", ', end="")
    print('"stone", validate_ingredients)'
          f': {grimoire.record_spell_injected("Bad Injected Spell", "stone",
                                              grimoire.validate_ingredients)}')
except Exception as e:
    print(f'ERROR: {e}')
