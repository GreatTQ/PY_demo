import os
from TestDemo.tool.fileRead import ReadYaml

BASH_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASH_PATH, 'config', 'config.yaml')
DATA_FILE = os.path.join(BASH_PATH, 'data', 'data.yaml')
LOG_PATH = os.path.join(BASH_PATH, "log")
REPORT_PATH = os.path.join(BASH_PATH, 'reports')