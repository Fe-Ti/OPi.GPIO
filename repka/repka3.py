# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Repka Pi 3

**Note:** Pin function depend on pinout variant, which is software defined.
Only UART0-TX/RX and PWM0 are shared between pinouts.

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
    3:  12,     # PA12
    5:  11,     # PA11
    7:  7,      # PA7
    8:  4,      # PA4/UART0-TX
    10: 5,      # PA5/UART0-RX
    11: 8,      # PA8
    12: 6,      # PA6
    13: 9,      # PA9
    15: 10,     # PA10
    16: 354,    # PL2
    18: 355,    # PL3
    19: 64,     # PC0
    21: 65,     # PC1
    22: 2,      # PA2
    23: 66,     # PC2
    24: 67,     # PC3
    26: 3,      # PA3
    27: 19,     # PA19
    28: 18,     # PA18
    29: 0,      # PA0
    31: 1,      # PA1
    32: 363,    # PL11
    33: 362,    # PL10
    35: 16,     # PA16
    36: 13,     # PA13
    37: 21,     # PA21
    38: 15,     # PA15
    40: 14      # PA14
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
