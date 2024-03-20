# coding: utf-8

"""
    Visier Authentication APIs

    Visier APIs for generating authentication tokens

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


RequiredGoogleProtobufAny = TypedDict("RequiredGoogleProtobufAny", {
    })

OptionalGoogleProtobufAny = TypedDict("OptionalGoogleProtobufAny", {
    # The type of the serialized message.
    "@type": str,
    }, total=False)

class GoogleProtobufAny(RequiredGoogleProtobufAny, OptionalGoogleProtobufAny):
    pass
