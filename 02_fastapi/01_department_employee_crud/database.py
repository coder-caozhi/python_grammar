import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# 从项目目录读取本机配置；现有环境变量优先，便于测试和部署。
load_dotenv(Path(__file__).parent / ".env")
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("请在 .env 中设置 DATABASE_URL，参考 .env.example")
engine = create_engine(
    DATABASE_URL,
    echo=os.getenv("SQL_ECHO", "false").lower() == "true",
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
class Base(DeclarativeBase):
    pass

def get_db():
    # 每个请求使用独立会话，发生异常时回滚，结束后关闭。
    with SessionLocal() as session:
        try:
            yield session
        except Exception:
            session.rollback()
            raise
