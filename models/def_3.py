from typing import *

from pydantic import BaseModel, Field


class def_3(BaseModel):
    """
    /schemas/searchRelationsEntitiesQuerySchema model

    """

    combinator: Any = Field(alias="combinator")

    rules: List[Union[Dict[str, Any], def_3]] = Field(alias="rules")
