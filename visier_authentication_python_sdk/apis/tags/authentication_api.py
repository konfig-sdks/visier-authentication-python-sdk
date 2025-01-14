# coding: utf-8

"""
    Visier Authentication APIs

    Visier APIs for generating authentication tokens

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from visier_authentication_python_sdk.paths.v1_admin_visier_secure_token.post import ASidTokenAuthentication
from visier_authentication_python_sdk.paths.v1_auth_oauth2_authorize.get import OAuth2Authorize
from visier_authentication_python_sdk.paths.v1_auth_oauth2_token.post import OAuth2Token
from visier_authentication_python_sdk.paths.v1_admin_visier_secure_ticket.post import TicketAuthentication
from visier_authentication_python_sdk.apis.tags.authentication_api_raw import AuthenticationApiRaw


class AuthenticationApi(
    ASidTokenAuthentication,
    OAuth2Authorize,
    OAuth2Token,
    TicketAuthentication,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AuthenticationApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AuthenticationApiRaw(api_client)
