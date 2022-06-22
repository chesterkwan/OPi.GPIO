# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull
# See LICENSE.md for details.

import functools
from copy import deepcopy
from OPi.constants import BOARD, BCM, SUNXI, CUSTOM


class _sunXi(object):

    def __getitem__(self, value):

        offset = ord(value[1]) - 65
        pin = int(value[2:])

        assert value[0] == "P"
        assert 0 <= offset <= 25
        assert 0 <= pin <= 31

        return (offset * 32) + pin


_pin_map = {
    # Physical pin to actual GPIO pin
    BOARD: {
        3: 12,
        5: 11,
        7: 6,
        8: 198,
        10: 199,
        11: 1,
        12: 7,
        13: 0,
        15: 3,
        16: 19,
        18: 18,
        19: 15,
        21: 16,
        22: 2,
        23: 14,
        24: 13,
        26: 10
    },

    # BCM pin to actual GPIO pin
    BCM: {
        2: 12,
        3: 11,
        4: 6,
        7: 10,
        8: 13,
        9: 16,
        10: 15,
        11: 14,
        14: 198,
        15: 199,
        17: 1,
        18: 7,
        22: 3,
        23: 19,
        24: 18,
        25: 2,
        27: 0
    },

    SUNXI: _sunXi(),

    # Orange Pi - i96
    CUSTOM: {
        3: 40,
        5: 104,
        7: 103,
        8: 2,
        9: 41,
        10: 4,
        11: 14,
        12: 6,
        13: 102,
        14: 3,
        15: 0,
        16: 10,
        17: 1,
        18: 9,
        19: 38,
        20: 13,
        21: 39,
        22: 11,
        23: 15,
        24: 20,
        25: 56,
        26: 66,
        27: 67,
        28: 22,
        29: 30,
        30: 29,
        31: 28,
        32: 27,
        33: 26,
        34: 25
    }
}


def set_custom_pin_mappings(mappings):
    _pin_map[CUSTOM] = deepcopy(mappings)


def get_gpio_pin(mode, channel):
    assert mode in [BOARD, BCM, SUNXI, CUSTOM]
    return _pin_map[mode][channel]


bcm = functools.partial(get_gpio_pin, BCM)
board = functools.partial(get_gpio_pin, BOARD)
sunxi = functools.partial(get_gpio_pin, SUNXI)
custom = functools.partial(get_gpio_pin, CUSTOM)
