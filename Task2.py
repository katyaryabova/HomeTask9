while True:

    def is_year_leap(a):

        if a % 4 == 0:
            if a % 400 == 0:
                print('True')
            elif a % 100 != 0:
                print('True')
            else:
                print('False')
        else:
            print('False')


    is_year_leap(int(input('Введите год: ')))