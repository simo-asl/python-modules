print('\n=== Import Transmutation Mastery ===')

print('\nMethod 1 - Full module import:')
try:
    import alchemy.elements
    print(f'alchemy.elements.create_fire(): {alchemy.elements.create_fire()}')
except Exception:
    print('Unexpected Error, Program Never Crash')

print('\nMethod 2 - Specific function import:')
try:
    from alchemy.elements import create_water
    print(f'create_water(): {create_water()}')
except Exception:
    print('Unexpected Error, Program Never Crash')

print('\nMethod 3 - Aliased import:')
try:
    from alchemy.potions import healing_potion as heal
    print(f'heal(): {heal()}')
except Exception:
    print('Unexpected Error, Program Never Crash')

print('\nMethod 4 - Multiple imports:')
try:
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion
    print(f'create_earth(): {create_earth()}')
    print(f'create_fire(): {create_fire()}')
    print(f'strength_potion(): {strength_potion()}')
except Exception:
    print('Unexpected Error, Program Never Crash')

print('\nAll import transmutation methods mastered!')
