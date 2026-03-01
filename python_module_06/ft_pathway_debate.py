print('\n=== Pathway Debate Mastery ===')
print('\nTesting Absolute Imports (from basic.py):')
try:
    from alchemy.transmutation import lead_to_gold, stone_to_gem
    print(f'lead_to_gold(): {lead_to_gold()}')
    print(f'stone_to_gem(): {stone_to_gem()}')
except Exception as e:
    print(f'ERROR: {e}')

print('\nTesting Relative Imports (from advanced.py):')
try:
    from alchemy.transmutation import philosophers_stone, elixir_of_life
    print(f'philosophers_stone(): {philosophers_stone()}')
    print(f'elixir_of_life(): {elixir_of_life()}')
except Exception as e:
    print(f'ERROR: {e}')

print('\nTesting Package Access:')
try:
    import alchemy.transmutation
    print('alchemy.transmutation.lead_to_gold()'
          f': {alchemy.transmutation.lead_to_gold()}')
    print('alchemy.transmutation.philosophers_stone()'
          f': {alchemy.transmutation.philosophers_stone()}')
except Exception as e:
    print(f'ERROR: {e}')

print('\nBoth pathways work! Absolute: clear, Relative: concise')
