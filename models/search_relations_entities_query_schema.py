from typing import *

from pydantic import BaseModel, Field


class SearchRelationsEntitiesQuerySchema(BaseModel):
    """
    Search relations entities query schema model
    """

    combinator: Any = Field(alias="combinator")

    rules: List[Union[Dict[str, Any], SearchRelationsEntitiesQuerySchema]] = Field(alias="rules")
