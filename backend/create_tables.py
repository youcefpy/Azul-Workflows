# run once only
import asyncio

from backend.database import Base, engine


async def init_models():
    print("Connecting to DB...")
    async with engine.begin() as conn:
        print("Creating tables...")
        await conn.run_sync(Base.metadata.create_all)
    print("Done.")


if __name__ == "__main__":
    asyncio.run(init_models())
