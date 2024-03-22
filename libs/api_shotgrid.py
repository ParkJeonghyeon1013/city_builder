#-*- coding:utf-8 -*-

import shotgun_api3
from datetime import datetime

SERVER_PATH = 'https://rapa.shotgrid.autodesk.com'
SCRIPT_NAME = 'script_pjh_api'
SERVER_KEY = 'dzybujumsUdhoo(luevaacl5o'

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SERVER_KEY)

class SgAPI:
    def __init__(self):
        self.people_lst = self.get_user_info()
        self.publish_usr_id = 0

    @staticmethod
    def get_project_info() -> list(dict()):
        project_lst = sg.find("Project", [], ['name', 'id'])
        for project in project_lst:
            print(project['name'], project['id'])

    @staticmethod
    def get_asset_info() -> list(dict()):
        filters = [['project', 'is', {'type': 'Project', 'id': 320}]]
        asset_lst = sg.find("Asset", filters, ['code', 'id'])
        return asset_lst

    @staticmethod
    def get_user_info() -> list[{'type': 'HumanUser', 'id': '' , 'name': ''}]:
        people_lst = sg.find("HumanUser", [], ["name", "id"])
        return people_lst

    @staticmethod
    def create_field(entity_type, data_type, display_name):
        properties = {"name": display_name}
        sg.schema_field_create(entity_type, data_type, display_name, properties)

    @staticmethod
    def publish2assetlibrary(city_name, dir_path, usr_id):
        # thumnail 설정 / path 지정
        asset_data = {
            "project": {"type": "Project", "id": 320},
            "code": city_name,  # Asset 이름
            "sg_asset_type": "Environment",  # Asset 유형
            "sg_status_list": "wtg",  # Asset 상태
            "sg_sg_version": "1",  # Asset 버전
            "sg_sg_file_path": dir_path,  # Asset 파일 경로
            "created_by": {"type": "HumanUser", "id": usr_id},  # Asset 제작자
            "created_at": datetime.now(),  # Asset 생성일
            "updated_at": datetime.now()  # Asset 수정일
        }

        # ShotGrid에 Asset 생성
        asset = sg.create("Asset", asset_data)
    @staticmethod
    def upload_thumbnail(asset_id, thumbnail_path):
        sg.upload_thumbnail("Asset", asset_id, thumbnail_path)

    @staticmethod
    def set_assignee():
        a = "assets.Asset.step_0$task_assignees"

    def find_usr_id(self, usr_name) -> list:
        for person_info in self.people_lst:
            if usr_name == person_info["name"]:
                return person_info["id"]
        return []

    def find_asset_id(self, asset_name) -> list:
        asset_lst = self.get_asset_info()
        for asset_info in asset_lst:
            if asset_info["code"] == asset_name:
                return asset_info["id"]
        return []

if __name__ == "__main__":
    # create_field("Asset", "text", "sg_version", properties)
    # create_field("Asset", "text", "sg_file_path")

    # set_field()
    # get_project_info()
    _sg = SgAPI()
    # sg.find_usr_id("Jeonghyeon Park")
    # _sg.find_asset_id("city_test")
    # sg.get_asset_info()
    # publish2assetlibrary("city_test", "/home/rapa", 121)

