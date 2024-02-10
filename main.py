from art import logo
import random

def afisare_carti(carti):
    return ", ".join(str(c) for c in carti)

def calcul_puncte(carti):
    suma = sum(carti)
    if suma > 21 and 11 in carti:
        suma -= 10  
    return suma

def joc_blackjack():
    print(logo)

    carti = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    random.shuffle(carti)

    carti_jucator = [carti.pop(), carti.pop()]
    carti_calculator = [carti.pop(), carti.pop()]

    print(f"Cartile tale: {afisare_carti(carti_jucator)}, puncte: {calcul_puncte(carti_jucator)}")
    print(f"Cartile calculatorului: {carti_calculator[0]}")

    while True:
        actiune = input("Doresti sa tragi o carte? (da/nu): ").lower()
        if actiune == 'da':
            carti_jucator.append(carti.pop())
            print(f"Ai tras o carte: {carti_jucator[-1]}")
            print(f"Cartile tale: {afisare_carti(carti_jucator)}, puncte: {calcul_puncte(carti_jucator)}")
            if calcul_puncte(carti_jucator) > 21:
                print("Ai depasit 21 de puncte! Ai pierdut!")
                break
        else:
            puncte_calculator = calcul_puncte(carti_calculator)
            while puncte_calculator < 17:
                carti_calculator.append(carti.pop())
                puncte_calculator = calcul_puncte(carti_calculator)

            print(f"Cartile calculatorului: {afisare_carti(carti_calculator)}, puncte: {puncte_calculator}")

            puncte_jucator = calcul_puncte(carti_jucator)
            if puncte_calculator > 21 or puncte_jucator > puncte_calculator:
                print("Ai castigat!")
            elif puncte_jucator == puncte_calculator:
                print("Egalitate!")
            else:
                print("Ai pierdut!")
            break

joc_blackjack()

intrebare = input("Doriti sa mai jucati odata? (da/nu)\n")
while intrebare == 'da':
  joc_blackjack()
  break

  
