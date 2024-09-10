import pytest
from gendiff.scripts.gendiff import generate_diff
from gendiff.parse_file import parse_file
from gendiff.formatters.stylish import make_stylish


def get_fixture_name(filename):
    return f"tests/fixtures/{filename}"

test_data = [
    ('file1.json', 'file2.json', 'expect_file1_file2.txt'),
    ('file1.yaml', 'file2.yaml', 'expect_file1_file2.txt'),
    ('file1_tree.json', 'file2_tree.json', 'expect_file1_file2_tree.txt'),
    ('file1_tree.yaml', 'file2_tree.yaml', 'expect_file1_file2_tree.txt')
]


@pytest.mark.parametrize("input1, input2, expected", test_data)
def test_add(input1, input2, expected):
    file_1 = get_fixture_name(input1)
    file_2 = get_fixture_name(input2)
    expected_file = get_fixture_name(expected)
    with open(expected_file) as f:
        expected_result = f.read()
    parse_file1 = parse_file(file_1)
    parse_file2 = parse_file(file_2)
    result = generate_diff(parse_file1, parse_file2) 
    assert result == expected_result
