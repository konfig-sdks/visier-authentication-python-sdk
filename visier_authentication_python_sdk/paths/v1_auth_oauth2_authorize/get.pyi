# coding: utf-8

"""
    Visier Authentication APIs

    Visier APIs for generating authentication tokens

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from visier_authentication_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from visier_authentication_python_sdk.api_response import AsyncGeneratorResponse
from visier_authentication_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from visier_authentication_python_sdk import schemas  # noqa: F401

from visier_authentication_python_sdk.model.status import Status as StatusSchema

from visier_authentication_python_sdk.type.status import Status

from ...api_client import Dictionary
from visier_authentication_python_sdk.pydantic.status import Status as StatusPydantic

# Query params
RedirectUriSchema = schemas.StrSchema
ResponseTypeSchema = schemas.StrSchema
ClientIdSchema = schemas.StrSchema
ScopeSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'response_type': typing.Union[ResponseTypeSchema, str, ],
        'client_id': typing.Union[ClientIdSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'redirect_uri': typing.Union[RedirectUriSchema, str, ],
        'scope': typing.Union[ScopeSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_redirect_uri = api_client.QueryParameter(
    name="redirect_uri",
    style=api_client.ParameterStyle.FORM,
    schema=RedirectUriSchema,
    explode=True,
)
request_query_response_type = api_client.QueryParameter(
    name="response_type",
    style=api_client.ParameterStyle.FORM,
    schema=ResponseTypeSchema,
    required=True,
    explode=True,
)
request_query_client_id = api_client.QueryParameter(
    name="client_id",
    style=api_client.ParameterStyle.FORM,
    schema=ClientIdSchema,
    required=True,
    explode=True,
)
request_query_scope = api_client.QueryParameter(
    name="scope",
    style=api_client.ParameterStyle.FORM,
    schema=ScopeSchema,
    explode=True,
)


@dataclass
class ApiResponseFor3XX(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor3XXAsync(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_3XX = api_client.OpenApiResponse(
    response_cls=ApiResponseFor3XX,
    response_cls_async=ApiResponseFor3XXAsync,
)
SchemaFor0ResponseBodyApplicationJson = StatusSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Status


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Status


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _o_auth2_authorize_mapped_args(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if redirect_uri is not None:
            _query_params["redirect_uri"] = redirect_uri
        if response_type is not None:
            _query_params["response_type"] = response_type
        if client_id is not None:
            _query_params["client_id"] = client_id
        if scope is not None:
            _query_params["scope"] = scope
        args.query = _query_params
        return args

    async def _ao_auth2_authorize_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_redirect_uri,
            request_query_response_type,
            request_query_client_id,
            request_query_scope,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/auth/oauth2/authorize',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _o_auth2_authorize_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_redirect_uri,
            request_query_response_type,
            request_query_client_id,
            request_query_scope,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/auth/oauth2/authorize',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class OAuth2AuthorizeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ao_auth2_authorize(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._o_auth2_authorize_mapped_args(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
        )
        return await self._ao_auth2_authorize_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def o_auth2_authorize(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._o_auth2_authorize_mapped_args(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
        )
        return self._o_auth2_authorize_oapg(
            query_params=args.query,
        )

class OAuth2Authorize(BaseApi):

    async def ao_auth2_authorize(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> StatusPydantic:
        raw_response = await self.raw.ao_auth2_authorize(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
            **kwargs,
        )
        if validate:
            return StatusPydantic(**raw_response.body)
        return api_client.construct_model_instance(StatusPydantic, raw_response.body)
    
    
    def o_auth2_authorize(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        validate: bool = False,
    ) -> StatusPydantic:
        raw_response = self.raw.o_auth2_authorize(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
        )
        if validate:
            return StatusPydantic(**raw_response.body)
        return api_client.construct_model_instance(StatusPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._o_auth2_authorize_mapped_args(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
        )
        return await self._ao_auth2_authorize_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._o_auth2_authorize_mapped_args(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
        )
        return self._o_auth2_authorize_oapg(
            query_params=args.query,
        )

