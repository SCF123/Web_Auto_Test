from selenium.webdriver.common.action_chains import ActionChains


# CSDN账号退出
def exit_csdn(driver):
    above = driver.find_element_by_class_name('login_img')
    ActionChains(driver).move_to_element(above).pause(2).perform()
    driver.find_element_by_link_text('退出').click()


# 慕课网账号退出
def exit_immoc(driver):
    above = driver.find_element_by_css_selector("#header-avator > img")
    ActionChains(driver).move_to_element(above).pause(2).perform()
    driver.find_element_by_link_text("安全退出").click()

