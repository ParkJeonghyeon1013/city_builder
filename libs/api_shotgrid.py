'''

asset 에 등록 ..?
'''

import shotgun_api3

SERVER_PATH = 'https://rapa.shotgrid.autodesk.com'
SCRIPT_NAME = 'script_pjh_api'
SERVER_KEY = 'dzybujumsUdhoo(luevaacl5o'

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SERVER_KEY)

project_lst = sg.find("Project", [], ['name', 'id'])
for project in project_lst:
    print(project['name'])


# shot grid에서 어떤 사용자들이 있는지 combobox에 넣어주기
# 