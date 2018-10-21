from components.ai import ConfusedMonster
from game_messages import Message

def drink(*args, **kwargs):
    entity = args[0]
    colors = args[1]
    amount = kwargs.get('amount')

    results = []

    if entity.fighter.hp == entity.fighter.max_hp:
        results.append({'consumed': False, 'message': Message('You are already at full alertness.', colors.get('yellow'))})
    else:
        entity.fighter.heal(amount)
        results.append({'consumed': True, 'message': Message('You feel a rush of energy!', colors.get('green'))})

    return results

def backtrace(*args, **kwargs):
    caster = args[0]
    colors = args[1]
    entities = kwargs.get('entities')
    game_map = kwargs.get('game_map')
    damage = kwargs.get('damage')
    maximum_range = kwargs.get('maximum_range')

    results = []

    target = None
    closest_distance = maximum_range + 1

    for entity in entities:
        if entity.fighter and entity != caster and game_map.fov[entity.x, entity.y]:
            distance = caster.distance_to(entity)

            if distance < closest_distance:
                target = entity
                closest_distance = distance
    if target:
        results.append({'consumed':True, 'target':target, 'message': Message('You backtrace the {0} with a scrutinizing gaze! The damage is {1}'.format(target.name, damage))})
        results.extend(target.fighter.take_damage(damage))
    else:
        result.append({'consumed': False, 'target': None, 'message': Message('No error is present.', colors.get('red'))})

    return results

def search_stack(*args, **kwargs):
    colors = args[1]
    entities = kwargs.get('entities')
    game_map = kwargs.get('game_map')
    damage = kwargs.get('damage')
    radius = kwargs.get('radius')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')

    results = []

    if not game_map.fov[target_x, target_y]:
        results.append({'consumed': False, 'message': Message("You cannot search an error that doesn't exist.",
                                                              colors.get('yellow'))})
        return results

    results.append({'consumed': True,
                    'message': Message('Stack Overflow helps solve every error within {0} tiles!'.format(radius),
                                       colors.get('orange'))})

    for entity in entities:
        if entity.distance(target_x, target_y) <= radius and entity.fighter:
            results.append({'message': Message('The {0} gets solved for {1} hit points.'.format(entity.name, damage),
                                               colors.get('orange'))})
            results.extend(entity.fighter.take_damage(damage))

    return results

def confuse_error(*args, **kwargs):
    colors = args[1]
    entities = kwargs.get('entities')
    game_map = kwargs.get('game_map')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')

    results = []

    if not game_map.fov[target_x, target_y]:
        results.append({'consumed': False, 'message': Message("You cannot target an error that doesn't exist.",
                                                              colors.get('yellow'))})
        return results

    for entity in entities:
        if entity.x == target_x and entity.y == target_y and entity.ai:
            confused_ai = ConfusedMonster(entity.ai, 10)

            confused_ai.owner = entity
            entity.ai = confused_ai

            results.append({'consumed': True, 'message': Message('The {0} itself looks confused!.'.format(entity.name),
                                                                 colors.get('light_green'))})

            break
    else:
        results.append({'consumed': False, 'message': Message('There is no targetable error at that location.',
                                                              colors.get('yellow'))})

    return results
