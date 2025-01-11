# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Repka Pi 4 Optimal
(https://linux-sunxi.org/images/5/50/OrangePi_3_Schematics_v1.5.pdf)

Usage:

.. code:: python
   import repka.repka4
   from OPi import GPIO

   GPIO.setmode(repka.repka4.BOARD) or GPIO.setmode(repka.repka4.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Repka Pi 4 Optimal physical board pin to GPIO pin
BOARD = {
    3: 122,
    5: 121,
    7: 362,
    8: 224,
    10: 225,
    11: 111,
    12: 203,
    13: 112,
    15: 113,
    16: 354,
    18: 355,
    19: 229,
    21: 230,
    22: 359,
    23: 228,
    24: 227,
    26: 226,
    27: 120,
    28: 119,
    29: 356,
    31: 357,
    32: 360,
    33: 118,
    35: 202,
    36: 231,
    37: 358,
    38: 205,
    40: 204
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
