#!/usr/bin/env python3

import os

class PWM(object):

    def __init__(self, ch=0):
        self._ch = ch
        self.base = '/sys/class/pwm/pwmchip0'
        self.path = self.base + '/pwm{:d}'.format(self._ch)

        if not os.path.isdir(self.base):
            raise FileNotFoundError('Directory not found: ' + self.base)

    def export(self):
        if not os.path.isdir(self.path):
            f = open('/sys/class/pwm/pwmchip0/export', 'w')
            f.write('{:d}'.format(self._ch))
            f.close()

    def unexport(self):
        if os.path.isdir(self.path):
            f = open('/sys/class/pwm/pwmchip0/unexport', 'w')
            f.write('{:d}'.format(self._ch))
            f.close()

    @property
    def channel(self):
        return self._ch

    @property
    def period(self):
        f = open(self.path + '/period', 'r')
        value = f.readline().strip()
        f.close()
        return int(value)

    @period.setter
    def period(self, value):
        f = open(self.path + '/period', 'w')
        f.write('{:d}'.format(value))
        f.close()
                
    @property
    def duty_cycle(self):
        f = open(self.path + '/duty_cycle', 'r')
        value = f.readline().strip()
        f.close()
        return int(value)

    @duty_cycle.setter
    def duty_cycle(self, value):
        f = open(self.path + '/duty_cycle', 'w')
        f.write('{:d}'.format(value))
        f.close()
 
    @property
    def enable(self):
        f = open(self.path + '/enable', 'r')
        value = f.readline().strip()
        f.close()
        return True if value == '1' else False

    @enable.setter
    def enable(self, value):
        f = open(self.path + '/enable', 'w')
        if value:
            f.write('1')
        else:
            f.write('0')
        f.close()

