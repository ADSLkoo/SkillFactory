num_tickets = int(input("При покупке от 4-х билетов действует скидка 10% от стоимости заказа!\n"
"Введите количество билетов: "))
total_cost = 0

for i in range(num_tickets):
    age = int(input(f"Введите возраст посетителя №{i+1}: "))
    if age < 18:
        cost = 0
    elif age < 25:
        cost = 990
    else:
        cost = 1390
    total_cost += cost

if num_tickets > 3:
    total_cost *= 0.9

print(f"Сумма к оплате: {total_cost} руб.")