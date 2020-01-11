import pytest
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C1')
def test_add():
    a = 5
    b = 10
    assert (a+b) == 15


@pytestrail.case('C2')
def test_sub():
    a = 5
    b = 10
    assert (b-a) == 5