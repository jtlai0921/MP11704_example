import sys
import logging

old = sys.stderr					#記下原輸出目的地
fp = open('log_test.txt', 'a')		#建立日誌檔
sys.stderr = fp					#把訊息輸出到指定檔案

logging.debug('Debugging information')	#輸出訊息到檔案
logging.info('Informational message')	#一般會忽略debug()和info()的訊息
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

sys.stderr = old					#恢復成標準輸出
fp.close()						#關閉檔案
