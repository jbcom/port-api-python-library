from typing import *

from pydantic import BaseModel, Field


class def_0(BaseModel):
    """
    /schemas/entitiesQuery model

    """

    combinator: Any = Field(alias="combinator")

    rules: List[
        Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], def_0]
    ] = Field(alias="rules")
