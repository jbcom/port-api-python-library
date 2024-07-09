import json
from typing import Any, Dict, List, Optional

import httpx

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_blueprint_scorecards(
    blueprint_identifier: str, api_config_override: Optional[APIConfig] = None
) -> List[Dict[str, Any]]:
    """
    Retrieve all scorecards for the specified blueprint.

    Args:
        blueprint_identifier (str): The identifier of the blueprint.
        api_config_override (Optional[APIConfig], optional): API configuration override. Defaults to None.

    Raises:
        HTTPException: If the API request fails.

    Returns:
        List[Dict[str, Any]]: A list of scorecards.
    """

    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/blueprints/{blueprint_identifier}/scorecards"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}"
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return response.json()


async def create_blueprint_scorecard(
    blueprint_identifier: str, data: Dict[str, Any], api_config_override: Optional[APIConfig] = None
) -> Dict[str, Any]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/blueprints/{blueprint_identifier}/scorecards"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}"
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data)

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return response.json()


async def update_blueprint_scorecards(
    blueprint_identifier: str, data: List[Dict[str, Any]], api_config_override: Optional[APIConfig] = None
) -> Dict[str, Any]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/blueprints/{blueprint_identifier}/scorecards"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}"
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "put", httpx.URL(path), headers=headers, params=query_params, json=[i.dict() for i in data]
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return response.json()


async def get_blueprint_scorecard(
    scorecard_identifier: str, blueprint_identifier: str, api_config_override: Optional[APIConfig] = None
) -> Dict[str, Any]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/blueprints/{blueprint_identifier}/scorecards/{scorecard_identifier}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}"
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return response.json()


async def update_blueprint_scorecard(
    scorecard_identifier: str,
    blueprint_identifier: str,
    data: Dict[str, Any],
    api_config_override: Optional[APIConfig] = None,
) -> Dict[str, Any]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/blueprints/{blueprint_identifier}/scorecards/{scorecard_identifier}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}"
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request("put", httpx.URL(path), headers=headers, params=query_params, json=data)

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return response.json()


async def delete_blueprint_scorecard(
    scorecard_identifier: str, blueprint_identifier: str, api_config_override: Optional[APIConfig] = None
) -> Dict[str, Any]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/blueprints/{blueprint_identifier}/scorecards/{scorecard_identifier}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}"
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "delete",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return response.json()


async def get_scorecards(api_config_override: Optional[APIConfig] = None) -> List[Dict[str, Any]]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/scorecards"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_config.get_access_token()}"
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "get",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return response.json()
