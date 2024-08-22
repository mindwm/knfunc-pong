import asyncio
import uvicorn
import os

async def serve():
    port=os.getenv("PORT", 8080)
    config = uvicorn.Config("knfunc.func:app", host="0.0.0.0", port=int(port), log_level=os.getenv("LOG_LEVEL", "INFO"))
    server = uvicorn.Server(config)
    await server.serve()

def run():
    asyncio.run(serve())
