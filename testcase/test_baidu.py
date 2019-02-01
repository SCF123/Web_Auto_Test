from BeautifulReport import BeautifulReport  # 引入BeautifulReport模块
from selenium import webdriver
import unittest
import time, os


class TestBaidu(unittest.TestCase):
    img_path = 'result\\img'

    # 截图接口
    # 传入一个img_name(图片名), 并存储到默认的文件路径下（.\web_auto\result\img）
    def save_img(self, img_name):
        self.driver.get_screenshot_as_file(
            '{}/{}.png'.format(os.path.abspath(self.img_path), img_name)
        )

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.baidu.com")

    # 打开百度, 点击新闻按钮前截一次图，在点击新闻按钮后再截一次图
    # 这里add_test_img参数即相应的截图名称，必须要与save_img参数一致
    @BeautifulReport.add_test_img('点击新闻按钮前', '点击新闻按钮后')
    def test_news(self):
        """新闻按钮跳转"""
        self.save_img('点击新闻按钮前')
        self.driver.find_element_by_link_text('新闻').click()
        self.save_img('点击新闻按钮后')
        self.assertIn('百度新闻', self.driver.title)

    # 如果在测试过程中, 出现不确定的错误, 程序会自动截图, 并返回失败。
    # 此时add_test_img参数必须是用例方法名，这个名字也将是截图名
    @BeautifulReport.add_test_img('test_map')
    def test_map(self):
        """地图按钮跳转"""
        # 此处故意设置使定位失败
        self.driver.find_element_by_link_text('地图的').click()
        # 此处故意使校验失败
        self.assertIn('百度地图', self.driver.title)

    # 如果用例没有出现错误, 即使用了错误截图装饰器, 也不会影响用例的使用，也不会截图
    @BeautifulReport.add_test_img('test_academic')
    def test_academic(self):
        """学术按钮跳转"""
        self.driver.find_element_by_link_text('学术').click()
        self.assertIn('百度学术', self.driver.title)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
