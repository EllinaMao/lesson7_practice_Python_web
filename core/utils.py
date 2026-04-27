import random
from datetime import datetime, timezone

'''
серва есть дейтайм 0 и получаем час
потом превращаем в секунды и превращаем в инт
'''
def get_current_timestamp_id():
        return int(datetime.now(timezone.utc).timestamp())+random.randint(0, 100000)

def get_current_timestamp():
    return int(datetime.now(timezone.utc).timestamp())

def get_readable_timestamp(timestamp: int) -> str:
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
