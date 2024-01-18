from main import datetime as dt, json, json_f, os

def write_to_file(currency, result):
    '''
    Функция записи полученных данных в файл
    '''
    now = dt.datetime.utcnow()
    moscow_now = now + dt.timedelta(hours=3)
    data = {
        'time': f'{moscow_now.hour} : {moscow_now.minute} : {moscow_now.second}',
        'currency': currency,
        'exchange': result
    }
    with open(json_f, 'a') as f:
        if os.stat(json_f).st_size == 0:
            json.dump([data], f)
        else:
            with open(json_f) as f_:
                list_ = json.load(f_)
                list_.append(data)
            with open(json_f, 'w') as f_1:
                json.dump(list_, f_1)

