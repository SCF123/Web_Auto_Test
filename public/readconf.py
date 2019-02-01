# function: 封装读取配置文件web_auto.conf的接口
import configparser
import os


class Readconfig(object):
    def __init__(self):
        confpath = os.path.join(
            os.path.split(os.path.realpath(__file__))[0][:-6],
            "web_auto.conf"
        )
        self.cf = configparser.ConfigParser()
        self.cf.read(confpath, encoding='GBK')

    def get_value(self,section, option):
        if self.cf.has_section(section):
            if self.cf.has_option(section, option):
                value = self.cf.get(section, option)
                return value
        return None


if __name__ == "__main__":
    val = Readconfig().get_value('CSDN', 'account')
    print(val)