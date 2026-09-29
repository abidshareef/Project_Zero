from hindsight_client import Hindsight
from backend.services.config import settings


class HindsightMemory:
    def __init__(self) -> None:
        self.client = Hindsight(
            base_url=settings.hindsight_base_url,
            api_key=settings.hindsight_api_key,
        )
        self.bank_id = settings.hindsight_bank_id

    def ensure_bank(self) -> None:
        try:
            self.client.create_bank(
                bank_id=self.bank_id,
                name="Project Zero Diagnostic Memory",
            )
        except Exception as exc:
            # A pre-existing bank is expected during normal development.
            if "already exists" not in str(exc).lower():
                raise

    def retain(self, content: str, context: str | None = None) -> None:
        kwargs = {"bank_id": self.bank_id, "content": content}
        if context:
            kwargs["context"] = context
        self.client.retain(**kwargs)

    def recall(self, query: str, budget: str = "mid"):
        return self.client.recall(
            bank_id=self.bank_id,
            query=query,
            budget=budget,
        )

    def reflect(self, query: str, budget: str = "mid"):
        return self.client.reflect(
            bank_id=self.bank_id,
            query=query,
            budget=budget,
            include={"facts": {}},
        )


memory = HindsightMemory()
