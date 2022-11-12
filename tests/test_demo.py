import pytest


@pytest.mark.usefixtures('init')
class TestDemo():

    payload = {
        'name': "admin",
        'password': "admin"
    }

    header = {
        "Authorization": "admin"
    }

    def test_read_root(self):
        resp = self.bs.get('/demo/', headers=self.header)
        assert resp.status_code == 200

    def test_read_item(self):
        resp = self.bs.get('/demo/1', headers=self.header)
        assert resp.status_code == 200

    def test_anythings(self):
        resp = self.bs.post(
            '/demo/items', json=self.payload, headers=self.header)
        assert resp.status_code == 200
