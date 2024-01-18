from main import requests, json, key, symbols


def get_apilayer_symbols():
    '''выводит все доступные валюты'''
    headers = {'apikey': key}
    response = requests.get(f'https://api.apilayer.com/exchangerates_data/symbols', headers=headers)
    data = json.loads(response.text)
    list_ = []
    list_result = []
    for i in data['symbols']:
        if len(list_) <= 17:
            list_.append(i)
        else:
            list_result.append(','.join(list_))
            list_ = []
            continue
    return list_result


def get_apilayer_latest(base):
    '''получает курс указанной валюты по отношению к symbols=RUB в init-main'''
    headers = {'apikey': key}
    response = requests.get(f'https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}', headers=headers)
    data = json.loads(response.text)
    if 'error' in data:
        return [0, f'\nЛибо ошибочно указана валюта - либо ошибка на сервере\nпоробуйте еще раз!']
    else:
        str_ = round(data['rates'][symbols], 2)
        list_ = str(str_).split('.')
        return [1, f'{list_[0]} rub : {list_[1]} kop']