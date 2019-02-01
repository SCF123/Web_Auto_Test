# function: 封装日志
from datetime import datetime
import logging
import os


class MyLog(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # 每次调用handler之前先清除已存在的handler，避免日志的重复打印
        self.logger.handlers.clear()
        self.logger.setLevel(level=logging.DEBUG)
        self.log_file = None

        formatter = logging.Formatter(
            fmt='[%(asctime)s] [%(levelname)s] %(message)s'
        )

        # 拼接日志文件api.log的输出路径
        log_path = os.path.join(
            os.path.split(os.path.realpath(__file__))[0][:-6],
            "result\\log"
        )
        # 若日志目录不存在，则创建一个
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        log_file = os.path.join(log_path, 'web_')
        now_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_file = log_file + str(now_time) + '.log'

        # FileHandler, 将日志输出到api.log文件
        file_handler = logging.FileHandler(self.log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # streamHandler，将日志输出到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def get_logger(self):
        return self.logger


# 测试用代码
if __name__ == '__main__':
    logger = MyLog().get_logger()
    logger.info('你好，世界！')

