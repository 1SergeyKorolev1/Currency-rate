from utils import api, functions

def app_operation():
    i = True
    while i:
        print('Введите курс какой валюты к рублю вы хотите узнать - из предложенных:\n')

        for currency in api.get_apilayer_symbols():
            print(currency)

        currency = input('\nВведите валюту:').upper()
        check, result = api.get_apilayer_latest(currency)

        if check == 0:
            print(result)
            continue
        else:
            print(result)
            functions.write_to_file(currency, result)
            while True:
                print('\nДля того что бы продолжить введите - 1,\nВыйти - 2')
                input_ = input()
                if input_ == '1':
                    break
                elif input_ == '2':
                    i = False
                    break
                else:
                    print('Введите 1 или 2')




