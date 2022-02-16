def calculate_calorie_consumption(sex=None, weight=None, height=None, age=None, activity=None):
    '''Рассчет суточной траты калорий'''

    # уровень базального метаболизма (УБМ)
    # сжигание калорий в сутки в состоянии покоя
    if sex == 'male':
        ubm = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        ubm = (10 * weight) + (6.25 * height) - (5 * age) - 161

    # рассчет траты калорий на основе УБМ и образа жизни
    cc = ubm * activity

    # округляю до целых
    return int(cc)


if __name__ == '__main__':
    print('Моя трата калорий:')
    cc = calculate_calorie_consumption(
        sex='female',
        weight=57,
        height=170,
        age=22,
        activity=1.375
    )
    print(cc)