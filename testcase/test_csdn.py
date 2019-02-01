from testcase.common.Login import login_csdn
from testcase.common.Exit import exit_csdn
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time


class TestCSDN(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.csdn.net/')
        self.driver.maximize_window()

    @unittest.skip("not run the case")
    def test_search(self):
        """测试CSDN的搜索功能"""
        driver = self.driver
        # 登陆CSDN账号
        login_csdn(driver)

        # 执行搜索用例
        time.sleep(2)
        driver.find_element_by_id('toolber-keyword').clear()
        driver.find_element_by_id('toolber-keyword').send_keys('selenium')
        driver.find_element_by_css_selector('#toolber-keyword + a').click()

        # 通过查看页面title中是否包含搜索内容来验证
        time.sleep(2)
        handls = driver.window_handles
        driver.switch_to.window(handls[1])
        self.assertIn('selenium', driver.title)

        # 退出账号
        exit_csdn(driver)

    @unittest.skip("not run the case")
    def test_button(self):
        """测试CSDN的个人中心按钮跳功能"""
        driver = self.driver
        # 登陆CSDN账号
        login_csdn(driver)

        # 执行点击【个人中心】按钮用例
        time.sleep(2)
        above = driver.find_element_by_class_name('login_img')
        ActionChains(driver).move_to_element(above).pause(2).perform()
        driver.find_element_by_link_text('个人中心').click()

        # 通过查看页面title中是否包含'个人中心'来验证
        time.sleep(3)
        handls = driver.window_handles
        driver.switch_to.window(handls[1])
        self.assertIn('个人中心', driver.title)

        # 退出账号
        exit_csdn(driver)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == "__name__":
    unittest.main()
