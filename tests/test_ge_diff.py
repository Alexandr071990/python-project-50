from gendiff.gen_diff import generate_diff


def test_gen_diff():
    with open("tests/fixtures/expected_results.txt", "r", encoding='utf8') as file:
        result = file.read().strip("\n")
    assert generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json'
        ) == result