import os
import pytest
from requests import Session


env = os.getenv('ENV')
host = os.getenv('HOST')


@pytest.fixture()
def init(request):
    bs = Session()
    bs.headers['Authorization'] = 'admin'
    request.cls.bs = bs
    request.cls.env = env
    if env == 'loc':
        request.cls.url = f'http://127.0.0.1:8002'
    else:
        request.cls.url = f'http://test-demo.atop:8002'
