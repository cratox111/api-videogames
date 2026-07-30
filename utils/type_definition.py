from typing import TypedDict

class TokenAcces(TypedDict):
    access_token: str
    token_type: str


class ReturnMessage(TypedDict):
    msg: str