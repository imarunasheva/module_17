per_cent = {
    'ТКБ': 5.6, 'СКБ': 5.9,
    'ВТБ': 4.28, 'СБЕР': 4.0
}
deposit = []
money = float(input("Сумма вклада, руб.: "))
if money < 0:
    raise ValueError('Пожалуйста, введите положительное значение ;)')
deposit.extend([money*per_cent['ТКБ']/100,
                money*per_cent['СКБ']/100,
                money*per_cent['ВТБ']/100,
                money*per_cent['СБЕР']/100]
               )
print("Накопленные средства за год: ", [f'{cur:,.2f} руб.' for cur in deposit])
print("Максимальная сумма, которую вы можете заработать — ",
      max([f'{cur:,.2f} руб.' for cur in deposit])
      )

