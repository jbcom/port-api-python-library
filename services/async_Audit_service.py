import json
from typing import *

import httpx

from ..api_config import APIConfig, HTTPException
from ..models import *


async def get_v1audit_log(
    identifier: Optional[str] = None,
    entity: Optional[str] = None,
    blueprint: Optional[str] = None,
    run_id: Optional[str] = None,
    webhookId: Optional[str] = None,
    webhookEventId: Optional[str] = None,
    origin: Optional[List[str]] = None,
    InstallationId: Optional[str] = None,
    resources: Optional[Union[List[Any], str]] = None,
    includes: Optional[List[Any]] = None,
    from_: Optional[str] = None,
    to: Optional[str] = None,
    action: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[float] = None,
    actionType: Optional[str] = None,
    api_config_override: Optional[APIConfig] = None,
) -> None:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/audit-log"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {
        "identifier": identifier,
        "entity": entity,
        "blueprint": blueprint,
        "run_id": run_id,
        "webhookId": webhookId,
        "webhookEventId": webhookEventId,
        "origin": origin,
        "InstallationId": InstallationId,
        "resources": resources,
        "includes": includes,
        "from": from_,
        "to": to,
        "action": action,
        "status": status,
        "limit": limit,
        "actionType": actionType,
    }

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

    return None
