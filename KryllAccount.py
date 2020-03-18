# -*- coding: utf-8 -*-
"""Module defining KryllAccount class"""


class KryllAccount:
    """Class representing a Krill account"""
    def __init__(self, datas: dict):
        """
        Args:
            datas: dictionnary of attribute to populate
        """

        self._email = datas.get("email", "")
        self._username = datas.get("username", "")
        self._has_accepted_terms = datas.get("has_accepted_terms", False)
        self._is_funder = datas.get("is_funder", False)
        self._is_admin = datas.get("is_admin", False)
        self._is_beta_tester = datas.get("is_beta_tester", False)
        self._access_smarttrading = datas.get("access_smarttrading", False)
        self._access_referral = datas.get("access_referral", False)
        self._holding_program_tier = datas.get("holding_program_tier", 0)
        self._need_kyc = datas.get("need_kyc", False)
        self._is_secured = datas.get("is_secured", False)
        self._ref_link = datas.get("ref_link", "")
        self._missing_security_question = datas.get("missing_security_question", False)
        self._avatar = datas.get("avatar", "")
        # TODO self._krl =
        # TODO self._api_config =
        # TODO self._holding_program =

    def __repr__(self):
        return "{}({})".format(self.username, self.email)

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = str(value)

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str):
        self._username = str(value)

    @property
    def has_accepted_terms(self) -> bool:
        return self._has_accepted_terms

    @has_accepted_terms.setter
    def has_accepted_terms(self, value: bool):
        self._has_accepted_terms = bool(value)

    @property
    def is_funder(self) -> bool:
        return self._is_funder

    @is_funder.setter
    def is_funder(self, value: bool):
        self._is_funder = bool(value)

    @property
    def is_admin(self) -> bool:
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value: bool):
        self._is_admin = bool(value)

    @property
    def is_beta_tester(self) -> bool:
        return self._is_beta_tester

    @is_beta_tester.setter
    def is_beta_tester(self, value: bool):
        self._is_beta_tester = bool(value)

    @property
    def access_smarttrading(self) -> bool:
        return self._access_smarttrading

    @access_smarttrading.setter
    def access_smarttrading(self, value: bool):
        self._access_smarttrading = bool(value)

    @property
    def access_referral(self) -> bool:
        return self._access_referral

    @access_referral.setter
    def access_referral(self, value: bool):
        self._access_referral = bool(value)

    @property
    def holding_program_tier(self) -> int:
        return self._holding_program_tier

    @holding_program_tier.setter
    def holding_program_tier(self, value: int):
        self._holding_program_tier = int(value)

    @property
    def need_kyc(self) -> bool:
        return self._need_kyc

    @need_kyc.setter
    def need_kyc(self, value: bool):
        self._need_kyc = bool(value)

    @property
    def is_secured(self) -> bool:
        return self._is_secured

    @is_secured.setter
    def is_secured(self, value: bool):
        self._is_secured = bool(value)

    @property
    def ref_link(self) -> str:
        return self._ref_link

    @ref_link.setter
    def ref_link(self, value: str):
        self._ref_link = str(value)

    @property
    def missing_security_question(self) -> bool:
        return self._missing_security_question

    @missing_security_question.setter
    def missing_security_question(self, value: bool):
        self._missing_security_question = bool(value)

    @property
    def avatar(self) -> str:
        return self._email

    @avatar.setter
    def avatar(self, value: str):
        self._email = str(value)
