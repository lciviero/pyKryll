# -*- coding: utf-8 -*-
"""Module defining KryllApi class"""

import requests
import json
from typing import Union

from .KryllWallet import KryllWallet
from .KryllCrypto import KryllCrypto


def api_connexion_needed(method):
    """Decorator checking if the connection is established, if not established it before the use of the function"""
    def wraper(self, *arg, **kargs):
        if not self.connected:
            self.connect()

        return method(self, *arg, **kargs)

    return wraper


class KryllApi:
    """Class to manage Kryll api connexion"""

    def __init__(self, api_url: str, api_user: str, api_pass: str, api_2fa: str = ""):
        """Instanciate a KryllApi object

        Args:
            api_url (str): url of the Kryll api endpoint
            api_user: api user
            api_pass: api password
            api_2fa: api 2 factor authentification code

        Returns:
            KryllApi:

        """

        # adding trailing "/" if needed
        if not api_url.endswith("/"):
            api_url += "/"

        self._api_url = api_url         # url of the Kryll api endpoint
        self._api_user = api_user       # api user
        self._api_pass = api_pass       # api password
        self._api_2fa = api_2fa         # api 2 factor authentification code
        self._token = str()             # api authentification token
        self._connected = False         # are we connected to the api

    @property
    def connected(self):
        return self._connected

    def _send_request(self, url: str, method: str = "GET", headers: dict = None, data: dict = None):
        """send a request to the api

        Args:
            url: api function url (without base url)
            method: http method to use
            headers: header to send
            data: data to send
        """

        if not headers:
            headers = dict()

        if not data:
            data = dict()

        # adding authentification token to header
        if self._token != "":
            headers["x-access-token"] = self._token

        # adding content type
        headers["content-type"] = "application/json"

        # adding base url
        url = self._api_url + url

        # sending request
        if method.upper() == "GET":
            res = requests.get(url, headers=headers)
        elif method.upper() == "POST":
            res = requests.post(url, headers=headers, json=data)
        else:
            raise ValueError(method + " is an incorrect value for method parameter")

        return res

    def connect(self):
        """Connect to Kryll api"""
        if self.connected:
            return True

        auth_body = {"email": self._api_user,
                     "password": self._api_pass,
                     "token_2fa": self._api_2fa,
                     "trusted": False,
                     "preferred_lang": "fr"}

        res = self._send_request("users/auth", "POST", data=auth_body)

        if res.status_code != 200:
            raise RuntimeError("Unable to connect to Kryll API: {} - {}:{}".format(res.status_code,
                                                                                   res.reason,
                                                                                   res.text))

        tmp = json.loads(res.text)
        self._token = tmp["data"]["auth_token"]
        self._connected = True

    @api_connexion_needed
    def get_wallet_detail(self) -> KryllWallet:
        """Return à list of KryllCoin object representing each coin in the wallet
        """
        res = self._send_request("users/me/wallet?force=true")
        if res.status_code != 200:
            return list()

        tmp = json.loads(res.text)

        # parsing data for wallet detail
        wallet = KryllWallet()
        for balance, lst in tmp["data"]["balance"].items():
            for curr in lst:
                tmp = KryllCrypto(curr["currency"], curr["locked"], curr["available"], curr["free"])
                wallet.add_crypto(balance, tmp)

        return wallet

    @api_connexion_needed
    def get_rates_for_currencies(self, fsyms: Union[set, list, str], tsyms: Union[set, list, str]):
        """Refresh rates from Kryll API, seems to always include USB

        Args:
            fsyms (set, str): coins to retreive price details for.
            tsyms (set, str): how price should be reported for fsyms.
        """

        # Dealing with differents parameters type
        # We use set to avoid duplicate value
        # converting str to set
        if isinstance(fsyms, str):
            fsyms = set([fsyms])
        if isinstance(tsyms, str):
            tsyms = set([tsyms])
        # converting list to set
        if isinstance(fsyms, list):
            fsyms = set([fsyms])
        if isinstance(tsyms, list):
            tsyms = set([tsyms])

        # we need to send list for json conversion
        fsyms = list(fsyms)
        tsyms = list(tsyms)

        headers = dict()
        headers["fsyms"] = fsyms
        headers["tsyms"] = tsyms

        res = self._send_request("exchanges/rates", "POST", data=headers)
        if res.status_code != 200:
            return {}

        tmp = json.loads(res.text)

        return tmp["data"]

