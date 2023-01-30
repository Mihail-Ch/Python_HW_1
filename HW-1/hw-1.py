#Задача 2: Найдите сумму цифр трехзначного числа.
#123 -> 6 (1 + 2 + 3) 
# 100 -> 1 (1 + 0 + 0)

number = int(input("Input number: "))

def sumNumber(a):
    result = 0
    for i in str(a):
        result = result + int(i)
    print(result)

sumNumber(number)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4 
# 60 -> 10 40 10

allBird = int(input("input all count bird: "))
katy = None
pety = None
sereja = None

def everyStudent(all):
    katy = all//2
    pety = katy//2
    sereja = pety
    print(f'Katy have {katy} birds\nPety have {pety} birds\nSereja have {sereja} birds')

everyStudent(allBird)

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# .
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета
# 385916 -> yes
# 123456 -> no

ticketNumber = input("Input ticket number: ")

def happy(ticket):
    firstHalf = 0
    secondHalf = 0
    for i in ticket[:3]:
        firstHalf = firstHalf + int(i)
    for i in ticket[3:]:
        secondHalf = secondHalf + int(i)
    if firstHalf == secondHalf:
        print(f'Ticket with number {ticketNumber} is happy 🎉')
    else:
        print(f'Ticket with number {ticketNumber} is not happy 😔')

happy(ticketNumber)


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes 
# 3 2 1 -> no

sizeN = int(input("Input size N: "))
sizeM = int(input("Input size M: "))
sliceK = int(input("Input slice K: "))

def sliceChokolate(sizeN, sizeM, sliceK):
    if sliceK < sizeM * sizeN and (sliceK % sizeM == 0 or sliceK % sizeN == 0):
     print("Yes")
    else:
     print("No")

sliceChokolate(sizeN, sizeM, sliceK)