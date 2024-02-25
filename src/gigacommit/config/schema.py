from typing import List, Literal

from pydantic.v1 import BaseModel
from gigachat.settings import Settings
from gigachat.models import Chat, MessagesRole, Messages


SCOPE = Literal["GIGACHAT_API_PERS", "GIGACHAT_API_CORP"]

class ModelSettings(Settings):
    scope: SCOPE = "GIGACHAT_API_PERS"


class ModelChat(Chat):
    messages: List[Messages] = [
        Messages(
            role=MessagesRole.USER,
            content="Message text",
        )
    ]


class Model(BaseModel):
    settings: ModelSettings = ModelSettings()
    chat: ModelChat = ModelChat()


class AppSchema(BaseModel):
    gigachat: Model = Model()
