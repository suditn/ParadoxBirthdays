import datetime, random

def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001,1,1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1 :]):
            if birthdayA == birthdayB:
                return birthdayA


print (" Эта программа показывает парадокс дней рождений. Группа из нескольких людей имеет высокий шанс иметь день рождение в один и тот же день")
MONTHS = ('Январь','Февраль','Март','Апрель','Май','Июнь','Июль',
          'Август','Сентябрь','Октябрь','Ноябрь','Декабрь')

while True:
    print("Сколько дней рождений сгенерировать?(Максимально 100)")
    response = input('> ')
    if response.isdecimal() and (0<int(response)<=100):
        numBDays = int(response)
        break
print()


print ('Вот ',numBDays,' дней рождений:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i !=0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()


match = getMatch(birthdays)

print ('В этой симуляции, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('У большенства человек день раждения в ', dateText)

else:
    print('Дни рождения не совпадают')
print()


print('Создаем ', numBDays, ' рандомных деньрождений 100,000 раз')
input('Нажмите любую клавишу')

print('Сгенерируем ещё раз')

simMatch = 0
for i in range(100000):
    if i%10000 == 0:
        print(i, 'Идёт симуляция')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('Прошло 100000 симуляций')

probability = round(simMatch / 100000 * 100, 2)
print('Из 100,000 симуляций всего', numBDays, 'людей ')
print('совпадающий день рождения в этой группе', simMatch, 'раз. Это значит')
print('что', numBDays, ' людей имеют ', probability, '% шанс ')
print('иметь совпадающие дни рождения в группе.')
#print('That\'s probably more than you would think!')
