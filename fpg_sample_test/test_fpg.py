import pytest
import logging
from pytest_testrail.plugin import pytestrail

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@pytestrail.case('C1')
def test_add():
    logger.info('Logged INFO message1')
    logger.warning('Logged WARNING message1')
    logger.error('Logged ERROR message1')
    print("Test Add")
    a = 5
    b = 10
    assert (a+b) == 15
    print("Success - Test Add")


@pytestrail.case('C2')
def test_sub():
    logger.info('Logged INFO message2')
    logger.warning('Logged WARNING message2')
    logger.error('Logged ERROR message2')
    print("Test Sub")
    a = 5
    b = 10
    assert (b-a) == 5
    print("Success - Test Sub")