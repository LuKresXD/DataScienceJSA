import pytest
from pythonTasks.task1 import AutoListDict


def test_custom_dict_append():
    d = AutoListDict()
    d['not_exist'].append(1)
    assert d['not_exist'] == [1]

    d['not_exist'].append(2)
    assert d['not_exist'] == [1, 2]

    d['another_key'].append('a')
    assert d['another_key'] == ['a']

    d['another_key'].append('b')
    assert d['another_key'] == ['a', 'b']


if __name__ == "__main__":
    pytest.main()
