import unittest
import json
import sys

sys.path.append('..')
import sabre_dev_studio

'''
Tests for the SabreDevStudio base class
Requires config.json in the same directory for API authentication

{
	"sabre_client_id": -----,
	"sabre_client_secret": -----
}

'''
class TestBasicSabreDevStudio(unittest.TestCase):
    def read_config(self):
        raw_data = open('config.json').read()

        data = json.loads(raw_data)

        client_secret = data['sabre_client_secret']
        client_id = data['sabre_client_id']

        return (client_id, client_secret)

    def setUp(self):
        # Read from config
        self.client_id, self.client_secret = self.read_config()

    def test_auth(self):
        sds = sabre_dev_studio.SabreDevStudio()
        sds.set_credentials(self.client_id, self.client_secret)
        sds.authenticate()

    def test_token_set(self):
        sds = sabre_dev_studio.SabreDevStudio()
        sds.set_credentials(self.client_id, self.client_secret)
        sds.authenticate()

        token = sds.token
        sds2 = sabre_dev_studio.SabreDevStudio()
        sds2.token = token
        sds2.authenticate()

if __name__ == '__main__':
    unittest.main()
