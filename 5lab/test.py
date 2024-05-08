import pytest
from os import path, listdir

test_dir_path = "/home/user/Desktop/Computational-mathematics/5lab/tests"
list_tests = [
        path.join(test_dir_path, f)
        for f in listdir(test_dir_path)
        if path.isfile(path.join(test_dir_path, f))
    ]

@pytest.mark.parametrize("/home/user/Desktop/Computational-mathematics/5lab/tests", list_tests)
def test_empty_input(test_file_path):
    file = open(test_file_path, "r")
    ent = file.readline()
    if ent == "1":
        pass
    elif ent == "2":
        pass
    elif ent == "3":
        pass
    else:
        assert 0 == "Такого варианта ввода нет"