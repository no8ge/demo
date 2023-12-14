import pytest


@pytest.mark.usefixtures('init')
class TestDemo():

    payload = {
        'name': "admin",
        'password': "admin"
    }

    def test_read_root(self):
        resp = self.bs.get(f'{self.url}/demo/')

        assert resp.status_code == 200

    def test_read_item(self):
        resp = self.bs.get(f'{self.url}/demo/404')
        assert resp.status_code == 200

    def test_anythings(self):
        resp = self.bs.post(
            f'{self.url}/demo/items', json=self.payload)
        assert resp.status_code == 200
