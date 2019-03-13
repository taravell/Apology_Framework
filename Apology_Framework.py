#Apology Framework V.01
#
#!/usr/bin/python3
# - * - codificação: utf-8 - * -

#blibliotecas
import sys
import os

#inicio

                    inst = input("Selecione a ferramenta desejada?")

                        if  inst == "1":
                            cmd1N = os.system("apt-get install nmap")

                        elif inst =="2":
                            cmd2N = os.system("apt-get htop ; htop")
                        else inst =="0":
                            cmd3N = os.system("exit")
