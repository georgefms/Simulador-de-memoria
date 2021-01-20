def Conversor1(n):
    valor = 0
    a = 3
    for x in n:
        y = int(x)*(2**a)
        valor += y
        a -= 1
    return valor

def Conversor2(n):
    return int(n, base=2)

def isBinary(L):
    for i in range(len(L)):
        if (L[i] != '0' and L[i] != '1'):
                return False

L = ['00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000',
     '00000000']
print('='*3, 'Memória Principal', '='*3)
while True:
    print('='*25)
    print('Você pode ler, escrever, ver estado atual, ou sair da memória.')
    print('Use E para escrever, L para apenas ler, A para o estado atual e S para sair.')
    op = input('Operação [E, L, A ou S]: ')
    if (op == 'E'):
        end = input('Digite o endereço (4 bits): ')
        if (len(end) == 4 and isBinary(end) != False):
            número = input('E qual seria o valor a ser substituido? (8 bits) ')
            if (len(número) == 8 and isBinary(end) != False):
                pos = Conversor2(end)
                L[pos] = número
            else:
                print('O valor precisa ser de 8 bits e em binário, tente de novo.')
        else:
            print('O valor do endereço é de 4 bits e em binário, tente de novo.')

    elif (op == 'L'):
        end = input('Digite o endereço (4 bits): ')
        if (len(end) == 4 and isBinary(end) != False):
            pos = Conversor2(end)
            print('O dado no endereço concedido é: {}'.format(L[pos]))
        else:
            print('O valor do endereço é de 4 bits e em binário, tente de novo.')
    elif (op == 'A'):
        print('')
        print('Memória Atual:')
        for z in L :
            print('-'*10, z, '-'*10)
    elif (op == 'S'):
        break
    else:
        print('Operação inválida! Tente de novo.')
