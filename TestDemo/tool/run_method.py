import requests

class RunMain(object):
    def send_get(self,url,data= None):
        report = requests.get(url= url, params= data)
        return report

    def send_post(self,url,data= None):
        report = requests.post(url= url, data= data)
        return report

    def run_main(self,method,url,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res