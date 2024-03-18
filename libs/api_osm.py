import pathlib
import sys, os
import re, importlib, subprocess
import hou as hou

class OSMCity:
    def __init__(self, cityname: str = 'testcity'):
        self.version = 0
        self.__cityname = cityname

    @property
    def cityname(self):
        return self.__cityname

    # 노드 생성 시 위치 정렬을 위한 메서드
    def align_node_pos(self, node_name, node_pos, add_x, add_y):
        node_name.setPosition((node_pos[0] + add_x, node_pos[1] + add_y))

    @staticmethod
    def set_hipfile():
        print("\ngrayscale set hipfile")
        # init HOUDINI
        hou.hipFile.clear(suppress_save_prompt=True)

        # set frame range - 5s [1001-1121]

        start_frame: int = 1001
        end_frame: int = 1120
        fps: int = 24
        hou.setFps(fps)
        frame_set = f"`{start_frame -1}/$FPS` `{end_frame}/$FPS`"
        hou.hscript(frame_set)
        hou.playbar.setFrameRange(start_frame, end_frame)
        hou.playbar.setPlaybackRange(start_frame, end_frame)
        hou.setFrame(start_frame)
        # hou.playbar.setTimeRange(int(start_frame), int(end_frame))




    def render_seq(self,
                    dir_path: str = "D:/git_workspace/usd_IO/build_data/osm_testcity"):

        pass


    def save_hip(self,
                 dir_path: str = "D:/git_workspace/usd_IO/build_data/grayscale_testcity",
                 task: str = "render"):

        '''

        :param dir_path:
        :param task: overview / render 두 종류 task 구분해서 저장하기 위함.
        :return:
        '''
        hip_path = os.path.join(dir_path, f'osm_{self.cityname}_{task}.hip')
        # hip save
        hou.hipFile.save(hip_path)
        self.version += 1





    def create_city(self,
                    osm_path='D:/git_workspace/usd_IO/hip_practice/based_osm/osm_img/mokdong.osm',
                    saved_path: str = "D:/git_workspace/usd_IO/build_data/osm_testcity"):

        obj = hou.node('/obj')
        n_geo = obj.createNode("geo", "OSM_CITY")
        n_geo.setDisplayFlag(True)

        print("\nosm 작업 시작 ")
        n_osm_import = n_geo.createNode('labs::osm_import')
        n_osm_import.parm('osm_file').set(osm_path)

        n_osm_filter = n_geo.createNode('labs::osm_filter')
        n_osm_filter.setInput(0, n_osm_import)
        self.align_node_pos(n_osm_filter, n_osm_import.position(), 0, -2)

        n_osm_building = n_geo.createNode('labs::osm_buildings')
        n_osm_building.parm('gen_nodata').set(1)
        n_osm_building.setInput(0, n_osm_filter)
        self.align_node_pos(n_osm_building, n_osm_filter.position(), 0, -2)

        n_xform = n_geo.createNode('xform', "turnTable")
        n_xform.parm('ry').setExpression('$F')
        n_xform.parm('px').setExpression("centroid(0, D_X)")
        n_xform.parm('py').setExpression("centroid(0, D_Y)")
        n_xform.parm('pz').setExpression("centroid(0, D_Z)")
        n_xform.setInput(0, n_osm_building)
        n_xform.setDisplayFlag(True)
        self.align_node_pos(n_xform, n_osm_building.position(), 0, -2)

        self.save_hip(saved_path, "overview")



if __name__ == '__main__':
    city = OSMCity()
    city.set_hipfile()
    city.create_city()
    pass
