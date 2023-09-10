import pytest
import requests

class TestHotels:
#1
    def test_UponLisbonPrimeResidences(self):
        self.response = requests.get('https://run.mocky.io/v3/b505a79c-0280-4a09-bba0-b984e1eed188')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#2
    def test_ContentisTemporarilyUnavailable(self):
        self.response = requests.get('https://run.mocky.io/v3/64f4ecc6-368e-414e-b6fe-8a059affe1ca')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 404
#3
    def test_DisneyDreams(self):
        self.response = requests.get('https://run.mocky.io/v3/82aded74-373e-4b9e-b721-ebb938e9ac19')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#4
    def test_FloraChiadoApartments(self):
        self.response = requests.get('https://run.mocky.io/v3/e08e35df-77a2-436a-9eb5-1dca46e0da00')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#5
    def test_GoldenRatio(self):
        self.response = requests.get('https://run.mocky.io/v3/ff14a060-abab-4305-8c1e-cd768036f6ef')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#6
    def test_GrandOrlandoResort(self):
        self.response = requests.get('https://run.mocky.io/v3/35344e37-ca0e-41a8-9c87-b13141d3e816')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#7
    def test_HolidayInnandSuitesOrlando(self):
        self.response = requests.get('https://run.mocky.io/v3/0dd3c4e1-fb37-4348-aa06-7a2afc81c16a')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#8
    def test_MotelOneBrussels(self):
        self.response = requests.get('https://run.mocky.io/v3/3a4dea4b-17c2-4c5a-8cb2-556af5c7091b')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#9
    def test_NewRomeHouse(self):
        self.response = requests.get('https://run.mocky.io/v3/ac1f829d-ffce-49d1-8ce6-9778559c98e5')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#10
    def test_OscarHotel(self):
        self.response = requests.get('https://run.mocky.io/v3/44c84d52-a815-40f6-a47c-1b8782b3de6e')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#11
    def test_P17Hotel(self):
        self.response = requests.get('https://run.mocky.io/v3/be338e29-d3dd-4298-924e-5604e8a7b350')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#12
    def test_ParkwayInternational(self):
        self.response = requests.get('https://run.mocky.io/v3/85af46cd-ed99-4c9f-ba22-6e34ea5bb8da')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#13
    def test_StradomApartments(self):
        self.response = requests.get('https://run.mocky.io/v3/7fcd8e0c-fd4a-4146-bada-700e8790b69a')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200
#14
    def test_UponLisbonPrimeResidences(self):
        self.response = requests.get('https://run.mocky.io/v3/b505a79c-0280-4a09-bba0-b984e1eed188')
        print(self.response)
        print(self.response.headers)
        print(self.response.text)
        assert self.response.status_code == 200