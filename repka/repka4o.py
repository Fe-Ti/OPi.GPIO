# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Repka Pi 4 Optimal

**Note:** Pin function depend on pinout variant, which is software defined.
Only UART0-TX/RX and PWM0 are shared between pinouts.

Usage:

.. code:: python
   import repka.repka4o
   from OPi import GPIO

   GPIO.setmode(repka.repka4o.BOARD) or GPIO.setmode(repka.repka4o.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Repka Pi 4 Optimal physical board pin to GPIO pin
BOARD = {
    3: 122,  # PD26
    5: 121,  # PD25
    7: 362,  # PL10
    8: 224,  # PH0/UART0-TX
    10: 225,  # PH1/UART0-RX
    11: 111,  # PD15
    12: 203,  # PH11
    13: 112,  # PD16
    15: 113,  # PD17
    16: 354,  # PL2
    18: 355,  # PL3
    19: 229,  # PH2
    21: 230,  # PH6
    22: 359,  # PL7
    23: 228,  # PH4
    24: 227,  # PH3
    26: 226,  # PH2
    27: 120,  # PD24
    28: 119,  # PD23
    29: 356,  # PL4
    31: 357,  # PL5
    32: 360,  # PL8
    33: 118,  # PD22/PWM0
    35: 202,  # PG10
    36: 231,  # PH7
    37: 358,  # PL6
    38: 205,  # PG13
    40: 204,  # PG12
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
