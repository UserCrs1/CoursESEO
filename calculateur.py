def calculer_prix(base, taxe):
    return round((base * taxe)*0.9, 2)
print(f"Prix final : {calculer_prix(100, 1.2)}")