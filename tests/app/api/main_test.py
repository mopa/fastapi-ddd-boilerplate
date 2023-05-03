from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

class TestFizzBuzz:

    def test_fizzbuzz_returns_fizzbuzz_when_divisible_by_3_and_5(self):
        response = client.get("/fizzbuzz/15")
        assert response.status_code == 200
        assert response.json() == "FizzBuzz"

    def test_fizzbuzz_returns_fizz_when_divisible_by_3(self):
        response = client.get("/fizzbuzz/9")
        assert response.status_code == 200
        assert response.json() == "Fizz"

    def test_fizzbuzz_returns_buzz_when_divisible_by_5(self):
        response = client.get("/fizzbuzz/10")
        assert response.status_code == 200
        assert response.json() == "Buzz"

    def test_fizzbuzz_returns_number_when_not_divisible_by_3_or_5(self):
        response = client.get("/fizzbuzz/7")
        assert response.status_code == 200
        assert response.json() == 7

    def test_fizzbuzz_returns_error_when_input_is_not_integer(self):
        response = client.get("/fizzbuzz/abc")
        assert response.status_code == 422
        assert response.json() == {"detail": [{"loc": ["path", "number"], "msg": "value is not a valid integer", "type": "type_error.integer"}]}


