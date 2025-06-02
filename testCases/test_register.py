import unittest

import pytest

from utilities.custom_logger import LogGen


class Test_001_Register(unittest.TestCase):
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self, setUp):
        self.driver = setUp

    