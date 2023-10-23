from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# .envファイルの読み込み
load_dotenv("/app/backend/.env")

# .envファイルからpostgreSQLのユーザー名とパスワードを取得
username = os.getenv("POSTGRES_USERNAME")
password = os.getenv("POSTGRES_PASSWORD")


DATABASE_URL = f"postgresql+asyncpg://{username}:{password}@postgresql/maindb"

# SQLAlchemyエンジンの作成
async_engine = create_async_engine(DATABASE_URL)

# セッションファクトリの作成
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

# SQLAlchemyモデルのベースクラス
Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session
