import datetime
import hashlib


def get_password() -> str:
    encode = 'c0210sovsecontej2022' + datetime.datetime.now(tz=None).strftime("%Y%m%d")
    hash = hashlib.md5(str(encode).encode('utf-8')).hexdigest()
    master_password = str(hash)[22:]
    return master_password