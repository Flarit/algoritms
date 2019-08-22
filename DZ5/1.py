import collections
import random


def sum_tuple(n):

    total = 0
    for sum in n:
        total += sum
        return total


Enterprise = collections.namedtuple('Enterprise', ['q1', 'q2', 'q3', 'q4'])

base_enterprise = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    profit1 = int(input('Прибыль за 1-й квартал: '))
    profit2 = int(input('Прибыль за 2-й квартал: '))
    profit3 = int(input('Прибыль за 3-й квартал: '))
    profit4 = int(input('Прибыль за 4-й квартал: '))
    base_enterprise[name] = Enterprise(
        q1=profit1,
        q2=profit2,
        q3=profit3,
        q4=profit4
    )

base_enterprise['Name1'] = Enterprise(
    q1=random.randint(100, 500),
    q2=random.randint(100, 500),
    q3=random.randint(100, 500),
    q4=random.randint(100, 500)
)

base_enterprise['Name2'] = Enterprise(
    q1=random.randint(100, 500),
    q2=random.randint(100, 500),
    q3=random.randint(100, 500),
    q4=random.randint(100, 500)
)

total = ()

for name, profit in base_enterprise.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total += profit

avg_total = sum(total) / len(base_enterprise)
print(f'Средняя прибыль за год для всех предприятий {avg_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in base_enterprise.items():
    if sum(profit) > avg_total:
        print(f'{name} - {sum(profit)}')

for name, profit in base_enterprise.items():
    if sum(profit) < avg_total:
        print(f'{name} - {sum(profit)}')