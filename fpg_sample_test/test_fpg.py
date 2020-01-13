import pytest
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C1')
def test_add():
    print("Test Add")
    a = 5
    b = 10
    assert (a+b) == 15
    print("Success - Test Add")


@pytestrail.case('C2')
def test_sub():
    print("Test Sub")
    a = 5
    b = 10
    assert (b-a) == 5
    print("Success - Test Sub")