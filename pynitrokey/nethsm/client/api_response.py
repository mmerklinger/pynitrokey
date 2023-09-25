# coding: utf-8
"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import dataclasses
import typing

import urllib3

from pynitrokey.nethsm.client import schemas


@dataclasses.dataclass
class ApiResponse:
    response: urllib3.HTTPResponse
    body: typing.Union[schemas.Unset, schemas.OUTPUT_BASE_TYPES] = schemas.unset
    headers: typing.Union[schemas.Unset, typing.Mapping[str, schemas.OUTPUT_BASE_TYPES]] = schemas.unset


@dataclasses.dataclass
class ApiResponseWithoutDeserialization(ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset