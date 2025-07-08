import os
from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity
from bot_logic import MyTeamsBot

APP_ID = os.getenv("MicrosoftAppId", "")
APP_PASSWORD = os.getenv("MicrosoftAppPassword", "")

bot = MyTeamsBot()
adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter_settings.disable_authentication = True     # ✅ désactive l'auth pour l'émulateur local
adapter = BotFrameworkAdapter(adapter_settings)

async def messages(req):
    print("✅ Called /api/messages endpoint")

    try:
        body = await req.json()
        print("Body received:", body)
    except Exception as e:
        print("❌ Error reading JSON:", e)
        return web.Response(status=400, text=f"JSON error: {e}")

    activity = Activity().deserialize(body)
    auth_header = req.headers.get("Authorization", "")

    try:
        response = await adapter.process_activity(activity, auth_header, bot.on_turn)
        if response:
            return web.json_response(data=response.body, status=response.status)
    except Exception as e:
        print("❌ Error processing activity:", e)
        return web.Response(status=500, text=f"Processing error: {e}")

    return web.Response(status=201)

app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=3978)
