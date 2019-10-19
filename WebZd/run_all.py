import unittest
from comm import HTMLTestRunner_cn

casePath = "H:\\Codeall\\WebZd\\Case"

rule = "test*.py"

discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)

print(discover)

reportPath = "H:\\Codeall\\WebZd\\report\\"+"report.html"

fp = open(reportPath,'wb')

run = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                       title="报告的名称",
                                       description="描述报告的作用",
                                       retry=1   #失败后重新跑一次
                                       )
run.run(discover)
fp.close()   #结束