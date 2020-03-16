# -*- coding: utf-8 -*-
"""Module defining KryllCoin class"""

from typing import Union


class KryllCrypto:
    """Class representing à Kryll cryptocurrency"""

    def __init__(self, currency, locked=0.00, available=0.00, free=0.00):
        """Instanciate a KryllCoin object

        Args:
            currency: currency code
            locked: amount of coin locked by Kryll
            available: available amount of coin
            free: free amount of coin
        """
        self._currency = currency
        self._locked = float(locked)
        self._available = float(available)
        self._free = float(free)

    def __repr__(self):
        return "{}({})".format(self._currency, self.total)

    @property
    def currency(self):
        return self._currency

    @property
    def locked(self) -> float:
        return self._locked

    @locked.setter
    def locked(self, value: Union[int, float]):
        self.locked = float(value)

    @property
    def available(self) -> float:
        return self._available

    @available.setter
    def available(self, value: Union[int, float]) -> float:
        self._available = float(value)

    @property
    def free(self) -> float:
        return self._free

    @free.setter
    def free(self, value: Union[int, float]):
        self._free = float(value)

    @property
    def total(self) -> float:
        return self._locked + self._available + self._free
