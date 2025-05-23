import random, string,sys
def embra(s):
    return "".join(random.sample(s,len(s)))
def sn(res):
    if res == 's' :
        print('certo')
    else:
        sys.exit()
def gerarsenha(num, num2):
    try:
        n = int(num)
        n2 = int(num2)
    except ValueError:
        print("Digite um número válido.")
        sys.exit()
    senha = ''.join(random.choices(string.ascii_letters, k=n)) + ''.join(random.choices(string.digits, k=n2))
    print(f"a senha gerada é: {embra(senha)}")
        
def gerador():
    print('Você quer gerar uma senha? S/N')
    res = input().strip().lower()
    sn(res)
    print('quantas letras?')
    num = input().strip()
    print('quantos numeros?')
    num1 = input().strip()
    gerarsenha(num,num1)
