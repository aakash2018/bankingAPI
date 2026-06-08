from typing import AsyncGenerator
from .config import settings
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from .logging import get_logger


logger = get_logger()

engine  = create_async_engine(settings.DATABASE_URL, echo=False, future=True)
async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_session()->AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Error occurred while getting database using session: {e}")
            raise
        finally:
            await session.close()

async def init_db()->None:
    pass
    
    