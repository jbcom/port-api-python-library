import json
from typing import *

import httpx

from ..api_config import APIConfig, HTTPException
from ..models import *


def get_v1organization(api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/organization"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return None


def post_v1organization(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/organization"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data)

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return None


def put_v1organization(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> Dict[str, Any]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/organization"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("put", httpx.URL(path), headers=headers, params=query_params, json=data)

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return response.json()


def patch_v1organization(data: Dict[str, Any], api_config_override: Optional[APIConfig] = None) -> Dict[str, Any]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/organization"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    with httpx.Client(base_url=base_path, verify=api_config.verify) as client:
        response = client.request("patch", httpx.URL(path), headers=headers, params=query_params, json=data)

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return response.json()
