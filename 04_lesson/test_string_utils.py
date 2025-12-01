import pytest
from string_utils import StringUtils

stringutils = StringUtils()

@pytest.mark.parametrize(
    "str, result",
    [
        ("cun", "Cun"),
        ("привет", "Привет"),
        ("Moon", "Moon"),
    ])
def test_cap_positive(str, result):
    stringutils = StringUtils()
    assert stringutils.capitalize(str) == result


@pytest.mark.parametrize(
    "str, result",
    [
        (" ", " "),
        ("123", "123")
    ])
def test_cap_negative(str, result):
    stringutils = StringUtils()
    assert stringutils.capitalize(str) == result


@pytest.mark.parametrize(
    "str, result",
    [
        ("   Cun", "Cun"),
        ("   привет", "привет"),
        ("Moon", "Moon"),
        ("   ", ""),
        ("   123", "123"),
    ])
def test_trim_positive(str, result):
    stringutils = StringUtils()
    assert stringutils.trim(str) == result


@pytest.mark.parametrize(
    "str, result",
    [
        ("", ""),
        ("123", "123"),
    ])
def test_trim_negative(str, result):
    stringutils = StringUtils()
    assert stringutils.trim(str) == result


@pytest.mark.parametrize(
    "string, symbol",
    [
        ("cun", "u"),
        ("привет", "и"),
        ("Moon", "f"),
    ])
def test_con_positive(string: str, symbol: str):
    stringutils = StringUtils()
    assert stringutils.contains(string, symbol) > -1


@pytest.mark.parametrize(
    "string, symbol",
    [
        ("", "u"),
        ("   ", "и"),
    ])
def test_con_negative(string: str, symbol: str):
    stringutils = StringUtils()
    assert stringutils.contains(string, symbol) > -1


@pytest.mark.parametrize(
    "string, symbol",
    [
        ("cun", "u"),
        ("привет", "и"),
        ("Moon", "o"),
    ])
def test_del_positive(string, symbol):
    stringutils = StringUtils()
    assert stringutils.delete_symbol(string, symbol) == string.replace(symbol, "")


@pytest.mark.parametrize(
    "string, symbol",
    [
        ("cn", "u"),
        ("првет", "и"),
        ("   ", "o"),
    ])
def test_del_negative(string, symbol):
    stringutils = StringUtils()
    assert stringutils.delete_symbol(string, symbol) == string.replace(symbol, "")
