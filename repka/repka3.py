# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Repka Pi 3

Usage:

.. code:: python
   import repka.repka3
   from OPi import GPIO

   GPIO.setmode(repka.repka3.BOARD) or GPIO.setmode(repka.repka3.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Repka Pi 3 physical board pin to GPIO pin
BOARD = {
    3:  12,
    5:  11,
    7:  7,
    8:  4,
    10: 5,
    11: 8,  
    12: 6,
    13: 9,
    15: 10, 
    16: 354,
    18: 355,
    19: 64,
    21: 65,
    22: 2,
    23: 66,
    24: 67,
    26: 3,
    27: 19,
    28: 18,
    29: 0,
    31: 1,
    32: 363,
    33: 362,
    35: 16,
    36: 13,
    37: 21,
    38: 15,
    40: 14
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
