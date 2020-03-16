# -*- coding: utf-8 -*-
"""Module defining KryllCoin class"""


class KryllCoin:
    """Class representing à Kryll cryptocurrency"""

    def __init__(self, currency, platform, locked=0.00, available=0.00, free=0.00):
        """Instanciate a KryllCoin object

        Args:
            currency: currency code
            platform: platform of the coin
            locked: amount of coin locked by Kryll
            available: available amount of coin
            free: free amount of coin
        """
        self._currency = currency
        self._platform = platform
        self._locked = locked
        self._available = available
        self._free = free

    def __repr__(self):
        return "{}({})".format(self._currency, self._platform)

    @property
    def currency(self):
        return self._currency

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        self.locked = float(value)

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = float(value)

    @property
    def free(self):
        return self._free

    @free.setter
    def free(self, value):
        self._free = float(value)

    @property
    def total(self):
        return self._locked + self._available + self._free
