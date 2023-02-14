activity_costs = {1: 100, 2: 60, 3: 180, 4: 200, -1: 60, -2: 150, -3: 500}
total_energy = 1000
spent_energy = 0
recovered_energy = 0
while total_energy > 0:
    print("Текущая энергия:", total_energy)
    print("1. Спорт (100) 2. Домашняя деятельность (60) 3. Уроки (180) 4. Слушайте жалобы (200)")
    print("-1. Слушать музыку (+60) -2. Есть (+150) -3. Спать (+500)")
    choice = input("Выберите занятие: ")
    if choice in activity_costs:
        energy_change = activity_costs
        if choice > 0:
            spent_energy += energy_change
            total_energy -= energy_change
        else:
            recovered_energy += energy_change
            total_energy += energy_change
else:
    print("Неверный выбор, попробуйте еще раз")
print("Затраченная энергия:", spent_energy)
print("Восстановленная энергия:", recovered_energy)