# -*- coding: utf-8 -*-
"""Module defining KryllAccount class"""

import json
from typing import Union


class KrillAccount:
    """Class representing a Krill account"""
    def __init__(self, json_datas: Union[str, json]):
        """
        Args:
            json_datas: datas used to populate class
        """
        # Dealing with datas format
        json_datas = json.loads(json_datas)

        self._email = json_datas["email"]
        self._username = json_datas["username"]
        self._has_accepted_terms = json_datas[""]
        self._is_funder = json_datas["is_funder"]
        self._is_admin = json_datas["is_admin"]
        self._is_beta_tester = json_datas["is_beta_tester"]
        self._access_smarttrading = json_datas["access_smarttrading"]
        self._access_referral = json_datas["access_referral"]
        self._holding_program_tier = json_datas["holding_program_tier"]
        self._need_kyc = json_datas["need_kyc"]
        self._is_secured = json_datas["is_secured"]
        self._ref_link = json_datas["ref_link"]
        self._missing_security_question = json_datas["missing_security_question"]
        self._avatar = json_datas["avatar"]
        # TODO self._krl =
        # TODO self._api_config =
        # TODO self._holding_program =

