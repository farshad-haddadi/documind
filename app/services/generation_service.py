from openai import OpenAI
from app.core.config import get_settings


class GenerationService:
    def __init__(self):
        settings = get_settings()

        self.client = OpenAI(
            api_key=settings.openai_api_key
        )

        self.model = settings.openai_model

    def generate_answer(
        self,
        query: str,
        contexts: list[str],
    ) -> str:

        if not contexts:
            return (
                "I could not find enough information "
                "in the uploaded documents."
            )

        context_text = "\n\n".join(contexts)

        prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

Context:
{context_text}

Question:
{query}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Answer questions using only the supplied context."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content