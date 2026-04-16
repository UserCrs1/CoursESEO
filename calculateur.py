def calculer_prix(base, taxe):
    return (base * taxe) * 0.9
print(f"Prix final : {calculer_prix(100, 1.2)}")


def calculer_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

distance = calculer_distance(1, 2, 4, 6)
print(f"Distance entre les deux points : {distance:.2f}")
