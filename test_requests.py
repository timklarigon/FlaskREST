import requests, random, string, time, datetime, json

def strTimeProp(start, end, format, prop):
    stime = time.mktime(start.timetuple()) + start.microsecond / 1E6
    etime = time.mktime(end.timetuple()) + end.microsecond / 1E6

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(prop):
    return strTimeProp(datetime.datetime(2018, 1, 1), datetime.datetime.now(), '%d/%m/%Y', prop)

def request_data_post():
    data = json.dumps({"fullname":''.join(random.choice(string.ascii_lowercase) for x in range(10)),
            "birthdate": randomDate(random.random()),
            "gender": 'male' if random.randint(0,1) else 'female'})

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post('http://127.0.0.1:5000', headers=headers, data=data)

    if response.status_code == 200:
        return response.content
    else:
        raise Exception

if __name__ == '__main__':
    for _ in range(100):
        request_data_post()