" Generate tokens "
from random import Random
from django.utils import timezone

def generate_token(token_len=30):
    ''' generate verification code '''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    random.seed(timezone.now())
    token = ''
    for _ in range(token_len):
        token += chars[random.randint(0, length)]
    return token