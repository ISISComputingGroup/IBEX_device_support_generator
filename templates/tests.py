import unittest
from unittest import skipIf

from utils.channel_access import ChannelAccess
from utils.ioc_launcher import IOCRegister
from utils.testing import get_running_lewis_and_ioc


class _Device_Tests(unittest.TestCase):
    """
    Tests for the _Device_ IOC.
    """

    TEMP_TOLERANCE = 0.005

    def setUp(self):
        self._lewis, self._ioc = get_running_lewis_and_ioc("_device_")
        self.ca = ChannelAccess(device_prefix="_DEVICE__01")

    def test_that_fails(self):
        self.fail("You haven't implemented any tests!")