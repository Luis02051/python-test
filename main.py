#python tst.py
import os,time,senha,chat,sys
hora = time.localtime().tm_hour
minuto = time.localtime().tm_min
if hora < 10:
    hora = "0"+ f"{hora}"
if minuto < 10:
    minuto = "0"+ f"{minuto}"
print("Carregando...")
print("//////////")
time.sleep(0.1)
print("/////////")
time.sleep(0.1)
print("////////")
time.sleep(0.1)
print("///////")
time.sleep(0.1)
print("//////")
time.sleep(0.1)
print("/////")
time.sleep(0.1)
print("////")
time.sleep(0.1)
print("///")
time.sleep(0.1)
print("//")
time.sleep(0.1)
print("/")
time.sleep(0.1)
os.system('cls')
print("Carregado com sucesso")
print("Você quer fazer oque?")
print('abrir cmd"0"')
print('Gerar senha"1"')
print('Ver a hora "2"')
print('Chat personalizado"3"(com a api do gemini do google)')
res = input()
if res.strip() == "1":
    senha.gerador()
elif res.strip() == "2":
    print(f"são {hora}:{minuto}")
elif res.strip() == "0":
    os.system('start cmd /k python "{}"'.format(__file__))
elif res.strip() == "3":
    os.system('cls')
    print("Sua chave api do gemini")
    ap = input()
    if ap == "" or ap == False:
        print("sem a chave api")
        sys.exit()
    print('Você quer que o bot seja algo por exemplo:"Você e o neymar",se quiser so um assitente ia mesmo deixe em branco')
    pes = input()
    os.system("cls")
    chat.germini(ap,pes)