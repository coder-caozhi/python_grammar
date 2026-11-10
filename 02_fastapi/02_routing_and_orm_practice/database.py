import os
from pathlib import Path
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(Path(__file__).with_name(".env"))
DATABASE_URL = os.environ["DATABASE_URL"]

# 创建engine
engine = create_engine(
    DATABASE_URL,
    echo=True, # 是否启用日志输出 开发环境启用，生产环境关闭
    pool_pre_ping=True # 连接前检查有效性，避免连接失效
)

# 创建会话工厂
SessionLocal = sessionmaker(
    autoflush=False, # 关闭自动提交，需手动 commit()
    bind=engine
)

