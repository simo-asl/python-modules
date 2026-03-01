def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "earth", "air"]
    for word in ingredients.split():
        if word not in valid_ingredients:
            return f'{ingredients} - INVALID'
    return f'{ingredients} - VALID'
