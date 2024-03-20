import typing_extensions

from visier_authentication_python_sdk.paths import PathValues
from visier_authentication_python_sdk.apis.paths.v1_admin_visier_secure_ticket import V1AdminVisierSecureTicket
from visier_authentication_python_sdk.apis.paths.v1_admin_visier_secure_token import V1AdminVisierSecureToken
from visier_authentication_python_sdk.apis.paths.v1_auth_oauth2_authorize import V1AuthOauth2Authorize
from visier_authentication_python_sdk.apis.paths.v1_auth_oauth2_token import V1AuthOauth2Token

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ADMIN_VISIER_SECURE_TICKET: V1AdminVisierSecureTicket,
        PathValues.V1_ADMIN_VISIER_SECURE_TOKEN: V1AdminVisierSecureToken,
        PathValues.V1_AUTH_OAUTH2_AUTHORIZE: V1AuthOauth2Authorize,
        PathValues.V1_AUTH_OAUTH2_TOKEN: V1AuthOauth2Token,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ADMIN_VISIER_SECURE_TICKET: V1AdminVisierSecureTicket,
        PathValues.V1_ADMIN_VISIER_SECURE_TOKEN: V1AdminVisierSecureToken,
        PathValues.V1_AUTH_OAUTH2_AUTHORIZE: V1AuthOauth2Authorize,
        PathValues.V1_AUTH_OAUTH2_TOKEN: V1AuthOauth2Token,
    }
)
