from typing import *

from pydantic import BaseModel, Field


class EntitiesQuerySchema(BaseModel):
    """
    Entities query schema model
    """

    combinator: Any = Field(alias="combinator")

    rules: List[
        Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], EntitiesQuerySchema]
    ] = Field(alias="rules")
