full_dot = '●'
empty_dot = '○'

def validate_name(name):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

def validate_stats(strength, intelligence, charisma):
    # Type checks
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'

    # Minimum value checks
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'

    # Maximum value checks
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'

    # Total points check
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

def create_dots(stat):
    return full_dot * stat + empty_dot * (10 - stat)


def create_character(name, strength, intelligence, charisma):
    name_error = validate_name(name)
    if name_error:
        return name_error

    stats_error = validate_stats(strength, intelligence, charisma)
    if stats_error:
        return stats_error

    return (
        f'{name}\n'
        f'STR {create_dots(strength)}\n'
        f'INT {create_dots(intelligence)}\n'
        f'CHA {create_dots(charisma)}'
    )
