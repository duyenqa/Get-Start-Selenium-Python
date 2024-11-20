import pytest

@pytest.fixture(params=[
    {"username": "tester1", "password": "123456"},
    {"username": "tester2", "password": "123456"}
])
def user_credentials(request):
    return request.param

def test_login(user_credentials):
    username = user_credentials["username"]
    password = user_credentials["password"]

    assert username == "tester1" or username == "tester2"
    assert password == "123456"