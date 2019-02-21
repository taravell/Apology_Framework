#Apology Framework V.01
#
#!/usr/bin/python3
# - * - codificação: utf-8 - * -

#blibliotecas
import sys
import os

#inicio

def main ():
        try:
            print('''



   ###    ########   #######  ##        #######   ######   ##    ##
  ## ##   ##     ## ##     ## ##       ##     ## ##    ##   ##  ##
 ##   ##  ##     ## ##     ## ##       ##     ## ##          ####
##     ## ########  ##     ## ##       ##     ## ##   ####    ##
######### ##        ##     ## ##       ##     ## ##    ##     ##
##     ## ##        ##     ## ##       ##     ## ##    ##     ##
##     ## ##         #######  ########  #######   ######      ##




                    ''')
                def inicio1():
                            while True:
                                print('''

[1]Scanner
                ''')

#selecioona as opções que o Framework disponibliza

                    aca = input("1")
                    while aca == "1":
print('''

1-Nmap
2-Nikto
0-exit
''')

                    inst = input("Selecione a ferramenta desejada?")

                        if  inst == "1":
                            cmd1N = os.system("apt-get install nmap")

                        elif inst =="2":
                            cmd2N = os.system("apt-get install Nikto")
                        else inst =="0":
                            cmd3N = os.system("exit")
