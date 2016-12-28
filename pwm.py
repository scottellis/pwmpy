# A class to work with the Linux PWM driver sysfs interface

import os

class PWM(object):

    def __init__(self, channel=0, chip=0):
        self._channel = channel
        self._chip = chip
        self.base = '/sys/class/pwm/pwmchip{:d}'.format(self._chip)
        self.path = self.base + '/pwm{:d}'.format(self._channel)

        if not os.path.isdir(self.base):
            raise FileNotFoundError('Directory not found: ' + self.base)

    def export(self):
        if not os.path.isdir(self.path):
            with open(self.base + '/export', 'w') as f:
                f.write('{:d}'.format(self._channel))

    def unexport(self):
        if os.path.isdir(self.path):
            with open(self.base + '/unexport', 'w') as f:
                f.write('{:d}'.format(self._channel))

    @property
    def channel(self):
        return self._channel

    @property
    def chip(self):
        return self._chip

    @property
    def period(self):
        with open(self.path + '/period', 'r') as f:
            value = f.readline().strip()

        return int(value)

    @period.setter
    def period(self, value):
        with open(self.path + '/period', 'w') as f:
            f.write('{:d}'.format(value))
                
    @property
    def duty_cycle(self):
        with open(self.path + '/duty_cycle', 'r') as f:
            value = f.readline().strip()

        return int(value)

    @duty_cycle.setter
    def duty_cycle(self, value):
        with open(self.path + '/duty_cycle', 'w') as f:
            f.write('{:d}'.format(value))
 
    @property
    def enable(self):
        with open(self.path + '/enable', 'r') as f:
            value = f.readline().strip()

        return True if value == '1' else False

    @enable.setter
    def enable(self, value):
        with open(self.path + '/enable', 'w') as f:
            if value:
                f.write('1')
            else:
                f.write('0')

