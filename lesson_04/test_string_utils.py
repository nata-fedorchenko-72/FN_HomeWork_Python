import pytest
from string_utils import StringUtils


utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, output_str", [
    ("users", "Users"),
    ("r", "R"),
    ("человек", "Человек")
    ])
def test_capitilise_positive(input_str, output_str):
    assert utils.capitilize(input_str) == output_str


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, output_str", [
    ("USERS", "Users"),
    ("", ""),
    (".", ".")
    ])
def test_capitilise_negative(input_str, output_str):
    assert utils.capitilize(input_str) == output_str


@pytest.mark.positive_test
@pytest.mark.parametrize("string, corrected", [
    ("   Nata", "Nata"),
    ("  Users", "Users"),
    ("   New house", "New house")
    ])
def test_trim_positive(string, corrected):
    assert utils.trim(string) == corrected


@pytest.mark.negative_test
@pytest.mark.parametrize("string, corrected", [
    (" 1", "1"),
    ("Users", "Users")
    ])
def test_trim_negative(string, corrected):
    assert utils.trim(string) == corrected


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, output_str", [
    ("5,4,6", ["5", "4", "6"]),
    ("стол,стул,кресло", ["стол", "стул", "кресло"]),
    ("привет,привет,привет", ["привет", "привет", "привет"])
    ])
def test_to_list_positive(input_str, output_str):
    assert utils.to_list(input_str) == output_str


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, output_str", [
    ("-896,-8.9,-8.5", ["-896", "-8.9", "-8.5"]),
    ("N,a,T,a", ["N", "a", "T", "a"])
    ])
def test_to_list_negative(input_str, output_str):
    assert utils.to_list(input_str) == output_str


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, result", [
    ("Домик", "о", True),
    ("Natalia", "N", True),
    ("Google", "a", False)
    ])
def test_contains_positive(string, symbol, result):
    assert utils.contains(string, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize("string, symbol, result", [
    ("Домик", "О", True),
    ("Natalia", "N", False),
    ("Google", " ", True)
    ])
@pytest.mark.xfail(reason="Тест ожидаемо падает из-за известной проблемы")
def test_contains_negative(string, symbol, result):
    assert utils.contains(string, symbol) == result


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, result", [
    ("Удочка", "У", "дочка"),
    ("Букварь", "рь", "Буква"),
    ("12345", "2", "1345")
    ])
def test_delite_symbol_positive(string, symbol, result):
    assert utils.delite_symbol(string, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize("string, symbol, result", [
    ("Nata", "Nata", ""),
    ("Test", "", "Test")
    ])
def test_delite_sumbol_negative(string, symbol, result):
    assert utils.delite_symbol(string, symbol) == result


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, result", [
    ("Desktop", "D", True),
    ("Start", "s", False),
    ("Наталья", "Н", True)
    ])
def test_starts_with_positive(string, symbol, result):
    assert utils.starts_with(string, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize("string, sumbol, result", [
    ("Desktop", "d", True),
    ("Start", "S", False),
    ("Наталья", "H", True)
    ])
@pytest.mark.xfail(reason="Тест ожидаемо падает из-за известной проблемы")
def test_starts_with_negative(string, sumbol, result):
    assert utils.starts_with(string, sumbol) == result


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, result", [
    ("123456", "6", True),
    ("-Дом-", "-", True),
    ("Starts", "t", False)
    ])
def test_end_with_positive(string, symbol, result):
    assert utils.end_with(string, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize("string, symbol, result", [
    ("123456", "65", True),
    ("-Start-", "rt", True),
    ("МИР", "Р", False)
    ])
@pytest.mark.xfail(reason="Тест ожидаемо падает из-за известной проблемы")
def test_end_with_negative(string, symbol, result):
    assert utils.end_with(string, symbol) == result


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, output_str", [
    ("", True),
    ("   ", True),
    ("Слово", False)
    ])
def test_is_empty_positive(input_str, output_str):
    assert utils.is_empty(input_str) == output_str


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, output_str", [
    ("___", True),
    (".. .", True),
    ("1", True),
    ("           ", False)
    ])
@pytest.mark.xfail(reason="Тест ожидаемо падает из-за известной проблемы")
def test_is_empty_negative(input_str, output_str):
    assert utils.is_empty(input_str) == output_str


@pytest.mark.positive_test
@pytest.mark.parametrize("list_str, result", [
    ([1, 2, 3, 4, 5], "1, 2, 3, 4, 5"),
    (["Hello", "World"], "Hello, World"),
    (["Мир" " - " "!!!"], "Мир - !!!")
    ])
def test_list_to_string_positive(list_str, result):
    assert utils.list_to_string(list_str) == result


@pytest.mark.negative_test
@pytest.mark.parametrize(" list_str, result", [
    ([-0.2, -8.5, -4], "-0.2, -8.5, -4"),
    (["a", "A", "л"], "a, A, л"),
    ([], "")
    ])
def test_list_to_string_negative(list_str, result):
    assert utils.list_to_string(list_str) == result
