import sys
import os
import yaml

class ReadYaml(object):
    def __init__(self, yaml):
        if os.path.exists(yaml):
            self.yaml = yaml
        else:
            print("Error")
        with open(self.yaml, 'r', encoding='utf-8') as f:
            file_data = f.read()
        self.f = file_data

    def getData(self):
        all_data = yaml.full_load(self.f)
        return all_data

    def getDatas(self, key):
        all_data = yaml.full_load_all(self.f)
        d = None
        for data in all_data:
            if data.get(key):
                d = data.get(key)
        return d

if __name__ == "__main__":
    a = ReadYaml(r"E:\PY_demo\TestDemo\data\data.yaml").getDatas('qiantao')
    print(a)