import pytest

@pytest.fixture
def sample_data():
    return "my best friend"

def test_together(sample_data):
    print("I and " + sample_data)