import subprocess
import xmlrpc.client
import xmlrpc.client as xc

# class Hqueue:
# cmd 작성틀
# https://www.sidefx.com/docs/houdini/hqueue/api.html#functions

def set_hrender(self):
        res = {
            "name": "citybuild",
            "shell": "bash",
            "command":(
                "cd /opt/hfs19.5;"
                "source houdini_setup;"
                "hrender -e -f 1001 1200 -v -d /out/[노드 이름] [파일경로];"
            )
        }
        return res

# HQ에 렌더 걸기
def start_render(self):
        hq_server = xc.ServerProxy("http://192.168.5.26:5000") # 서버연결
        hq_server.newjob(self.set_hrender)



try:
    # hq.ping()
    hq_server = xc.ServerProxy("http://192.168.5.26:5000")
    print('hq 연결됨')
    res = {
        "name": "citybuild",
        "shell": "bash",
        "command": (
            "cd /opt/hfs19.5;"
            "source houdini_setup;"
            "hrender -e -f 1001 1200 -v -d /out/mantra1 /192.168.5.10/workspace/d0323_t1218/feedback3.hip;"
        )
    }
    hq_client = xmlrpc.client.ServerProxy('http://192.168.5.26:5000')
    job_num = hq_server.newjob(res)
    print(hq_client)
    print(job_num)
except ConnectionRefusedError:
    print('failed...')
