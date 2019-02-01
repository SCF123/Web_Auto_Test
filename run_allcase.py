from public.common import send_mail  # 引入public.common中邮件发送功能
from BeautifulReport import BeautifulReport
import unittest, time, os, threading
import schedule

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 获取当前时间，并转化成我们想要的格式
now_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
# 拼接测试报告名，固定名TestReport + 当前时间
report_name = 'TestReport_' + now_time + '.html'
# 拼接测试报告存放路径
report_path = os.path.join(os.getcwd(), 'result\\testreport')


# 使用discover方法加载所有test_开头的测试用例
def add_suite():
    case_file = os.path.join(os.getcwd(), 'testcase')
    discover = unittest.defaultTestLoader.discover(
        case_file,
        pattern='test_*.py',
        top_level_dir=None
    )
    return discover


# 调用BeautifulReport模块执行测试用例并生成测试报告
def run_case(suites):
    result = BeautifulReport(suites)
    result.report(filename=report_name,
                  tester='非攻',
                  title='自动化测试报告',
                  description='百度、CSDN、慕课用例批量执行测试',
                  log_path=report_path
                  )


# 使用多线程去执行测试用例
def start_thread(suites):
    threads = []
    for test_case in suites:
        t = threading.Thread(target=run_case, args=(test_case,))
        t.start()
        threads.append(t)

    # 等所有线程完成用例执行
    for t in threads:
        t.join()


# 封装一个主函数
def main():
    test_suites = add_suite()
    start_thread(test_suites)

    # 所有用例执行完成后，将生成的测试报告通过邮件发送
    # filename = '{}\\{}'.format(report_path, report_name)
    # text = "最新Web自动化测试报告请接收，见附件。"
    # send_mail(text, filename)


if __name__ == "__main__":
    # schedule.every().monday.at("08:00").do(main)  # 每周一08:00执行用例
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    main()
