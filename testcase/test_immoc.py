from testcase.common.Login import login_immoc
from testcase.common.Exit import exit_immoc
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest


class TestImmoc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.imooc.com/")
        self.driver.maximize_window()

    # 测试慕课网的搜索功能
    def test_search(self):
        """测试慕课网的搜索功能"""
        driver = self.driver
        # 登陆账号
        login_immoc(driver)

        # 执行搜索用例
        time.sleep(3)
        driver.find_element_by_class_name('search-input').clear()
        driver.find_element_by_class_name('search-input').send_keys('Python')
        driver.find_element_by_xpath('//i[@class="icon-search"]').click()

        # 通过查看页面title中是否包含搜索内容来验证
        time.sleep(3)
        self.assertIn('python', driver.title)

        # 退出账号
        exit_immoc(driver)

    def test_collect(self):
        """测试收藏课程功能"""
        driver = self.driver
        # 登陆账号
        login_immoc(driver)

        # 执行搜藏课程用例
        # 进入个人中心
        driver.find_element_by_id('header-avator').click()
        driver.find_element_by_xpath('//div[@class="slider"]/ul/li[2]/a').click()
        # 先到[我的收藏]列表，统计之前已收藏的课程总数
        driver.find_element_by_link_text('我的收藏').click()
        old_collects = driver.find_elements_by_xpath('//li[@class="course-one"]')
        # 切换到[最近学习]列表，对最近学习的第一个课程进行点击收藏
        driver.find_element_by_link_text('最近学习').click()
        time.sleep(2)
        above = driver.find_element_by_xpath('//ul[@class="clearfix"]/li/div[2]/h3/div/div[1]')
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(2)
        driver.find_element_by_xpath('//ul[@class="clearfix"]/li/div[2]/h3/div/div[2]/a[1]').click()

        # 校验：切换到[我的收藏]列表，统计当前已收藏的课程总数是否比之前的多一个
        driver.find_element_by_link_text('我的收藏').click()
        time.sleep(2)
        new_collects = driver.find_elements_by_xpath('//li[@class="course-one"]')
        self.assertEqual(len(new_collects), (len(old_collects) + 1))


        # 退出账号
        exit_immoc(driver)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
