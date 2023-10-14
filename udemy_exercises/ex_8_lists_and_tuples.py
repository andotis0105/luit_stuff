connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]

route = 0.0
distance = 0.0
for each in connections:
    if each[1] == 'Rome':
        route += 1
        distance += each[2]


print(route, 'connections lead to Rome with an average flight time of', distance/route,'minutes')