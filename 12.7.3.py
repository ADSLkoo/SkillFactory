per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input('Введите сумму, которую вы планируете положить под проценты: '))

deposit = [round(money * per_cent[bank] / 100,2) for bank in per_cent]

max_deposit = max(deposit)

print('Накопленные средства по вкладам в банках:', deposit)
print(f'Максимальная сумма, которую вы можете заработать — {max_deposit}')