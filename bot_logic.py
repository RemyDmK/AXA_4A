from botbuilder.core import ActivityHandler, TurnContext
import requests

FASTAPI_URL = "http://127.0.0.1:8000/process-text/"

class MyTeamsBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_message = turn_context.activity.text

        # Appel à ton FastAPI
        response = requests.post(
            FASTAPI_URL,
            json={"text": user_message}
        )
        bot_response = response.json().get("response")

        # Envoie la réponse dans Teams
        await turn_context.send_activity(bot_response)
