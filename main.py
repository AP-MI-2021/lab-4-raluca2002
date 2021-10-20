def show_menu():
   print('1. Citire listei')
   print('2. Afisare numere intregi')
   print('3. Exit')

def read_list():
   floats_as_str = input('Dati o lista de float-uri separate prin spatii: ')
   floats_as_list_of_str = floats_as_str.split(' ')
   floats = []
   for floats_str in floats_as_list_of_str:
       floats.append(float(floats_str))
   return floats

def get_integers(lst):
   """
   Determina numerele intregi din lista
   lst: lista de float-uri
   return: o lista cu numere intregi din lista
   """
   result = []
   for num in lst:
       if int(num) == num:
          result.append(num)
   return result


def test_get_integers():
   assert get_integers([1.2, 5.3, 3, 4, 12.0]) == [3, 4, 12.0]
   assert get_integers([]) == []
   assert get_integers([5.3,5.64]) == []

def show_integers(lst):
   result = get_integers(lst)
   print(f'Numerele intregi din lista: {lst} sunt: {result}')


def main():
   lst = []
   while True:
      show_menu()
      option = input('Alegeti optiunea: ')
      if option == '1':
         lst=read_list()
      elif option == '2':
         show_integers(lst)
      elif option == 'x':
         break
      else:
         print('Optiune invalida, reincercati!')

if __name__ == '__main__':
      test_get_integers()
      main()



