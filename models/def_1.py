from typing import *

from pydantic import BaseModel, Field


class def_1(BaseModel):
    """
    /schemas/dashboardWidget model

    """

    id: Optional[str] = Field(alias="id", default=None)

    updatedAt: Optional[str] = Field(alias="updatedAt", default=None)

    updatedBy: Optional[str] = Field(alias="updatedBy", default=None)

    createdAt: Optional[str] = Field(alias="createdAt", default=None)

    createdBy: Optional[str] = Field(alias="createdBy", default=None)

    type: str = Field(alias="type")

    layout: List[Dict[str, Any]] = Field(alias="layout")

    widgets: List[
        Union[
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Tuple[Any, Any, Any, Any, Any],
            Any,
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            Dict[str, Any],
            def_1,
            def_2,
        ]
    ] = Field(alias="widgets")
