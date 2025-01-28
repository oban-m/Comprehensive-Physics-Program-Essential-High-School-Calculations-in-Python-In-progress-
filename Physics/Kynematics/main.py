""" 

    PART PRINCIPAL PER TAL QUE L'USUARI ENTRI QUIN MOVIMENT VOL ESTUDIAR I SI NECESSITAR CANVIA EL MOVIMENT.

"""

from mrau import main_mrua
from mrua_caigudalliure import main_caigudallure
from mparabolico import main_parabolico

def opc_mov():
    while True:
        try:
            print("Which movement do you want to study? 1) MRUA 2) Free fall (MRUA where a is gravity) 3) Parabolic movement.")
            ans = int(input())
            if ans not in [1, 2, 3]:
                print('Please, write a correct integer.')
            else:
                return ans
        except ValueError:
            print('Write a correct value.')


def query():
    while True:
        try:
            print("Do you want to study another movement? Y/n")
            ans = input()
            if ans in ['Y', 'y', 'Yes', 'yes']:
                return True
            elif ans in ['N', 'n', 'No', 'no']:
                return False
            else:
                print('Please, write a correct answer.')
        except Exception as e:
            print('An error has occurried, please try again.')

def main():
    while True:
        option = opc_mov()
        if option == 1:
            main_mrua()
        elif option == 2:
            main_caigudallure()
        elif option == 3:
            main_parabolico()
        

        if not query():
            return print("Finishing program.")

    

main()


