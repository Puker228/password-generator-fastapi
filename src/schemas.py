from pydantic import BaseModel


class SPassword(BaseModel):
    len: int = 8
    nums: bool | None = True
    symbols: bool | None = True
    registry: bool | None = True
