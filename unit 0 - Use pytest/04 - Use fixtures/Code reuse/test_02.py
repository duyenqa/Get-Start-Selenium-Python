import pytest

@pytest.fixture
def setup():
    print("Set up the environment before running the test.")
    yield
    print("Clean up after testing is complete.")


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_case_1(self):
        print("Run test case 1")
        assert True

    def test_case_2(self):
        print("Run test case 2")
        assert True

'''
Trong Pytest, @pytest.mark.usefixtures("setup") là một cách để sử dụng fixtures trong các test case mà không cần phải truyền 
fixture đó vào như tham số cho mỗi hàm kiểm thử. Thay vì truyền trực tiếp tên fixture vào hàm test, bạn có thể chỉ định fixture đó
bằng cách sử dụng decorator @pytest.mark.usefixtures.

Result:
Set up the environment before running the test.
Run test case 1
Clean up after testing is complete.

Set up the environment before running the test.
Run test case 2
Clean up after testing is complete.
'''