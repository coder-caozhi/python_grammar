import logging

# 日志的基本配置
logging.basicConfig(
    # 配置日志的基本
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
    # 设置日志在日志文件和控制台输出
    handlers=[
        # 在控制台输出
        logging.StreamHandler(),
        # 输出到文件
        logging.FileHandler('app.log', encoding='utf-8')
    ]
)

logger = logging.getLogger(__name__)

logger.info("普通日志")
logger.debug("Debug级别的日志")
logger.error("错误日志")