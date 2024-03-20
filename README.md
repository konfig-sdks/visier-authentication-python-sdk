<div align="center">

[![Visit Visier](./header.png)](https://visier.com)

# Visier<a id="visier"></a>

Visier APIs for generating authentication tokens


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`visierauthentication.authentication.a_sid_token_authentication`](#visierauthenticationauthenticationa_sid_token_authentication)
  * [`visierauthentication.authentication.o_auth2_authorize`](#visierauthenticationauthenticationo_auth2_authorize)
  * [`visierauthentication.authentication.o_auth2_token`](#visierauthenticationauthenticationo_auth2_token)
  * [`visierauthentication.authentication.ticket_authentication`](#visierauthenticationauthenticationticket_authentication)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Visier&serviceName=Authentication&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from visier_authentication_python_sdk import VisierAuthentication, ApiException

visierauthentication = VisierAuthentication()

try:
    a_sid_token_authentication_response = (
        visierauthentication.authentication.a_sid_token_authentication(
            username="string_example",
            password="string_example",
        )
    )
except ApiException as e:
    print(
        "Exception when calling AuthenticationApi.a_sid_token_authentication: %s\n" % e
    )
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from visier_authentication_python_sdk import VisierAuthentication, ApiException

visierauthentication = VisierAuthentication()


async def main():
    try:
        a_sid_token_authentication_response = (
            await visierauthentication.authentication.aa_sid_token_authentication(
                username="string_example",
                password="string_example",
            )
        )
    except ApiException as e:
        print(
            "Exception when calling AuthenticationApi.a_sid_token_authentication: %s\n"
            % e
        )
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from visier_authentication_python_sdk import VisierAuthentication, ApiException

visierauthentication = VisierAuthentication()

try:
    a_sid_token_authentication_response = (
        visierauthentication.authentication.raw.a_sid_token_authentication(
            username="string_example",
            password="string_example",
        )
    )
    pprint(a_sid_token_authentication_response.headers)
    pprint(a_sid_token_authentication_response.status)
    pprint(a_sid_token_authentication_response.round_trip_time)
except ApiException as e:
    print(
        "Exception when calling AuthenticationApi.a_sid_token_authentication: %s\n" % e
    )
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `visierauthentication.authentication.a_sid_token_authentication`<a id="visierauthenticationauthenticationa_sid_token_authentication"></a>

Generate a Visier authentication token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
a_sid_token_authentication_response = (
    visierauthentication.authentication.a_sid_token_authentication(
        username="string_example",
        password="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

##### password: `str`<a id="password-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationRequest`](./visier_authentication_python_sdk/type/authentication_request.py)
Authentication token request body

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/visierSecureToken` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierauthentication.authentication.o_auth2_authorize`<a id="visierauthenticationauthenticationo_auth2_authorize"></a>

Initiate an OAuth2 authorization code flow.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
o_auth2_authorize_response = visierauthentication.authentication.o_auth2_authorize(
    response_type="response_type_example",
    client_id="client_id_example",
    redirect_uri="string_example",
    scope="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### response_type: `str`<a id="response_type-str"></a>

The response type. Must be `code`.

##### client_id: `str`<a id="client_id-str"></a>

The ID of the pre-registered client application.

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The optional URI to redirect to after authorization.

##### scope: `str`<a id="scope-str"></a>

The OAuth 2.0 scope of the authorization request. Defaults to `read`.

#### 🔄 Return<a id="🔄-return"></a>

[`Status`](./visier_authentication_python_sdk/pydantic/status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/auth/oauth2/authorize` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierauthentication.authentication.o_auth2_token`<a id="visierauthenticationauthenticationo_auth2_token"></a>

Generate a JSON Web Token (JWT) for the specified user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
o_auth2_token_response = visierauthentication.authentication.o_auth2_token(
    grant_type="string_example",
    client_id="string_example",
    redirect_uri="string_example",
    code="string_example",
    username="string_example",
    password="string_example",
    asid_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### grant_type: `str`<a id="grant_type-str"></a>

The grant type. Supported values: - `authorization_code`: The authorization code grant type. - `password`: The password grant type. - `urn:visier:params:oauth:grant-type:asid-token`: The ASID token grant type.

##### client_id: `str`<a id="client_id-str"></a>

The ID of the pre-registered client application.

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The optional URI to redirect to after authorization.

##### code: `str`<a id="code-str"></a>

The authorization code. Applicable only for authorization code grant type.

##### username: `str`<a id="username-str"></a>

The username of the user to authenticate. Applicable only for password grant type.

##### password: `str`<a id="password-str"></a>

The password of the user to authenticate. Applicable only for password grant type.

##### asid_token: `str`<a id="asid_token-str"></a>

The ASID token. Applicable only for ASID token grant type.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TokenRequestBody`](./visier_authentication_python_sdk/type/token_request_body.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/auth/oauth2/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierauthentication.authentication.ticket_authentication`<a id="visierauthenticationauthenticationticket_authentication"></a>

Generate a legacy Visier secure ticket

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ticket_authentication_response = (
    visierauthentication.authentication.ticket_authentication(
        username="string_example",
        password="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

##### password: `str`<a id="password-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationRequest`](./visier_authentication_python_sdk/type/authentication_request.py)
Secure ticket request body

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/visierSecureTicket` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
