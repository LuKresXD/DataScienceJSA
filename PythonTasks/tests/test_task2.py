import pytest
from PythonTasks.task2 import is_palindrome


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal, Panama") == True
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("") == True
    assert is_palindrome("A") == True
    assert is_palindrome("aa") == True
    assert is_palindrome("ab") == False


if __name__ == "__main__":
    pytest.main()
