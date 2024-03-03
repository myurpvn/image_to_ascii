from typing import Any
import structlog


class Logger:
    def __init__(self) -> Any:
        self.logger = structlog.get_logger()

    # def init_logger()-> Any:
    #     return Logger()
