# -*- coding: utf-8 -*-
"""Module defining KryllApi class"""

import requests
import json
from .KryllCoin import KryllCoin


def api_connexion_needed(method):
    """Decorator checking if the connection is established, if not established it before the use of the function"""
    def wraper(self, *arg, **kargs):
        if not self.connected:
            self.connect()

        method(self, *arg, **kargs)

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

        self._api_url = api_url
        self._api_user = api_user
        self._api_pass = api_pass
        self._api_2fa = api_2fa
        self._token = str()
        self._connected = False

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

    @api_connexion_needed
    def get_wallet_detail(self) -> list:
        """return à list of KryllCoin object representing each coin in the wallet"""
        res = self._send_request("users/me/wallet?force=true")
        if res.status_code != 200:
            return list()

        tmp = json.loads(res.text)

        # parsing data for wallet detail
        wallet = list()
        for balance in tmp["data"]["balance"].keys():
            for currency in tmp["data"]["balance"][balance]:
                # adding coin to the list
                wallet.append(KryllCoin(currency["currency"], balance, currency["locked"],
                                        currency["available"], currency["free"]))

        return wallet

    @api_connexion_needed
    def get_rates_for_currencies(self, fsyms: set, tsyms: set):
        """Refresh rates from Kryll API

        Args:
            fsyms: coins to retreive price details for.
            tsyms: how price should be reported for fsyms. Default USD
        """
        headers = dict()
        headers["fsyms"] = fsyms
        headers["tsyms"] = tsyms

        res = self._send_request("exchanges/rates", "POST", data=headers)
        if res.status_code != 200:
            return

        tmp = json.loads(res.text)

    @property
    def connected(self):
        return self._connected
