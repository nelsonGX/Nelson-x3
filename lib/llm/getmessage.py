class claude:
    from lib.llm.claude import generate

    async def generatemessage(message):
        return await claude.generate(
            [
                {
                    "role": "user",
                    "content": message
                },
            ]
        )

class gemini:
    from lib.llm.gemini import generate

    async def generatemessage(message):
        return await gemini.generate(
            [
                {
                    "role": "user",
                    "content": message
                },
            ]
       )