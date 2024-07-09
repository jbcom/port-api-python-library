from typing import *

from pydantic import BaseModel, Field


class def_2(BaseModel):
    """
    /schemas/grouperWidget model

    """

    id: Optional[str] = Field(alias="id", default=None)

    updatedAt: Optional[str] = Field(alias="updatedAt", default=None)

    updatedBy: Optional[str] = Field(alias="updatedBy", default=None)

    createdAt: Optional[str] = Field(alias="createdAt", default=None)

    createdBy: Optional[str] = Field(alias="createdBy", default=None)

    type: str = Field(alias="type")

    title: Optional[str] = Field(alias="title", default=None)

    displayMode: str = Field(alias="displayMode")

    activeGroupUrlParam: Optional[str] = Field(alias="activeGroupUrlParam", default=None)

    groupsOrder: Optional[List[str]] = Field(alias="groupsOrder", default=None)

    groups: List[Dict[str, Any]] = Field(alias="groups")