__author__ = 'g8y3e'

from layer_1.common.driver_handler_base import DriverHandlerBase

class PolatisDriverHandler(DriverHandlerBase):
    def __init__(self):
        DriverHandlerBase.__init__(self)

        self._ctag = 1
        self._switch_name = ''

    def _incrCTAG(self):
        self._ctag += 1
        return self._ctag

    def login(self, address, username, password):
        self._session.connect(address, username, password, port=None, re_string=self._prompt)

        command = 'ACT-USER::{0}:1::{1};'.format(username, password)
        command_result = self._session.hardware_expect(command, re_string=self._prompt)

        command = 'RTRV-HDR:::{0}:;'.format(self._incrCTAG())
        command_result = self._session.hardware_expect(command, re_string=self._prompt)

        #fixme parse switch name