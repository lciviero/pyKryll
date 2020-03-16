# -*- coding: utf-8 -*-
"""Module defining KryllWallet class"""

from collections import defaultdict

from .KryllCrypto import KryllCrypto


class KryllWallet:
    """Class representing à Kryll Wallet"""

    def __init__(self):
        self._platform = defaultdict(list)     # dictionary of cryptos held on a platform

    def add_crypto(self, platform: str, crypto: KryllCrypto):
        """Add a KryllCrypto object to the wallet

        Args:
            platform: platform name
            crypto: KryllCrypto object
        """
        self._platform[platform].append(crypto)

    def get_crypto_list(self) -> set:
        """Return a set of (unique) cryptocurrency code in the wallet

        Returns:
            set: set of cryptocurrency code
        """
        res = set()
        for lst in self._platform.values():
            res.update([x.currency for x in lst])

        return res
