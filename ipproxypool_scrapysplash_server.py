import os
import sys

exp10it_module_path = os.path.expanduser("~")+"/mypypi"
sys.path.insert(0, exp10it_module_path)

from exp10it import start_ipproxypool
from exp10it import start_scrapy_splash

start_ipproxypool()

start_scrapy_splash()
