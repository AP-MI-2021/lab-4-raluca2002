def show_menu():
    print('1. Citirea a doua liste')
    print('2. Afisarea daca cele doua liste au acelasi numar de elemente pare')
    print('3. Afisati o lista cu intersectia listelor citite de la tastatura')
    print('4. Afisati toate palindroamele obtinute prin concatenarea elementelor de pe aceleasi pozitii in lista')
    print('5. Citirea unei a treia liste si inlocuirea elementelor cu oglinditul lor daca elementele sunt divizibile cu toate elemetele din a treia lista')
    print('x. Exit')


def read_list():
    lst = []
    lst_s = input('Dati o lista separate prin spatii: ')
    lst_s_split = lst_s.split(' ')
    for elem in lst_s_split :
        lst.append(int(elem))
    return lst

def nr_pare(lst):
    '''
    Aflam numarul numerelor pare dintr-o lista
    :param lst: lista de numere intregi
    :return: numarul numerelor pare din lista
    '''
    cate = 0
    for elem in lst:
        if elem % 2 == 0:
            cate = cate + 1
    return cate

def test_nr_pare():
    assert nr_pare([12,4,6,7,9]) == 3
    assert nr_pare([3,5,7,9,1]) == 0
    assert nr_pare([4,6,8,22]) == 4

def intersectie(A, B):
    '''
    Intersectia listelor citite de la tastatura
    :param l1: lista de numere intregi
    :param l2: lista de numere intregi
    :return: intersectia
    '''
    result = []
    A.sort()
    B.sort()
    for i in range(len(A)):
        if A[i] in B:
            result.append(A[i])
    return result

def test_intersectie():
   assert intersectie([12,22,36,424], [22,23,36,55,424]) == [22,36,424]
   assert intersectie([2,4,36,78], [15,76,87,9]) == []
   assert intersectie([2,5], [2,7,9]) == [2]

def acelasi_nr_de_nr_pare(A, B):
    if nr_pare(A) == nr_pare(B):
        print('Listele au acelasi numar de elemente pare')
    else:
        print('Listele nu au acelasi numar de elemente pare')


def oglindit(n):
    ogl = 0
    while n:
        ogl = ogl * 10 + n % 10
        n = int(n/10)
    return ogl


def test_oglindit():
    assert oglindit(356) == 653
    assert oglindit(87) == 78
    assert oglindit(567765) == 567765

def palindrom(n):
    return n == oglindit(n)

def concatenare(A, B):
    '''
    Toate palindroamele obtinute prin concatenare
    :param A: lista de numere intregi
    :param B: lista de numere intregi
    :return: afisarea palindroamelor obtinute prin concatenarea celor doua liste
    '''
    if len(A) > len(B):
        aux = A
        A = l2
        B = aux
    result = []
    for i in range(len(A)):
        nr = int(str(A[i]) + str(B[i]))
        if palindrom(nr):
            result.append(nr)
    return result

def divizibil_cu_toate_elementele(n, l):
    '''
    Vedem daca un numar este divizibil cu toate elementele din lista
    :param n: numar intreg
    :param l: lista de numere intregi
    :return: True daca toate elementele sunt divizibile cu n si False in caz contrar
    '''
    for i in range(len(l)):
        if n % l[i] != 0:
            return False
    return True


def test_divizibil_cu_toate_elementele():
    assert divizibil_cu_toate_elementele(2, [16, 24, 22, 8]) == False
    assert divizibil_cu_toate_elementele(3, [3, 9, 7]) == False
    assert divizibil_cu_toate_elementele(5, [3, 7, 15]) == False

def inlocuire_element(l, c):
    for i in range (len(l)):
        if divizibil_cu_toate_elementele(l[i], c):
            l[i] = oglindit(l[i])
    return l
def test_inlocuire_element():
    assert inlocuire_element([12,22,36,363],[1,2,3,4]) == [21,22,63,363]



def main():
    l1 = []
    l2 = []
    c = []
    while True:
        show_menu()
        option = input('Alegeti optiunea: ')
        if option == '1':
            A = read_list()
            B = read_list()
        elif option == '2':
            acelasi_nr_de_nr_pare(A, B)
        elif option == '3':
            intersectie(A, B)
        elif option == '4':
            concatenare(A, B)
        elif option == '5':
            c = read_list(c)
            print(inlocuire_element(A, c))
            print(inlocuire_element(B, c))
        elif option == 'x':
            break
        else:
            print('Optiune invalida. Reincercati!')
if __name__=='__main__':
 test_nr_pare()
 test_intersectie()
 test_oglindit()
 test_divizibil_cu_toate_elementele()
 test_inlocuire_element()
 main()


