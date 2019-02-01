from public.readconf import Readconfig

# CSDN账号登录
def login_csdn(driver):
    account = Readconfig().get_value('CSDN', 'account')
    pwd = Readconfig().get_value('CSDN', 'password')
    driver.find_element_by_link_text('登录').click()
    # driver.find_element_by_xpath("//a[contains(text(),'帐号登录')]").click()
    driver.find_element_by_link_text('账号登录').click()
    driver.find_element_by_id('all').clear()
    driver.find_element_by_id('all').send_keys(account)
    driver.find_element_by_id('password-number').clear()
    driver.find_element_by_id('password-number').send_keys(pwd)
    driver.find_element_by_css_selector('button[data-type="account"]').click()


# 慕课网账号登录
def login_immoc(driver):
    account = Readconfig().get_value('IMOOC', 'account')
    pwd = Readconfig().get_value('IMOOC', 'password')
    driver.find_element_by_id('js-signin-btn').click()
    driver.find_element_by_name('email').clear()
    driver.find_element_by_name('email').send_keys(account)
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys(pwd)
    driver.find_element_by_css_selector('input[type="button"]').click()
