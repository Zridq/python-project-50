import pytest
import json
from ..gendiff.scripts.gendiff import generate_diff


def get_fixture_name(filename):
    return f"tests/fixtures/{filename}"

test_data = [
    ('file1.json', 'file2.json', 'expect_file1_file2.txt')
]


@pytest.mark.parametrize("input1, input2, expected", test_data)
def test_add(input1, input2, expected):
    file_1 = get_fixture_name(input1)
    file_2 = get_fixture_name(input2)
    expected_file = get_fixture_name(expected)
    with open(expected_file) as f:
        expected_result = f.read()
    assert generate_diff(file_1, file_2) == expected_result
