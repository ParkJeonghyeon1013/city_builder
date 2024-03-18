# -*- coding: utf-8 -*-

import sys
import os
import importlib

from PySide2 import QtCore, QtWidgets

sys.path.append("D:/git_workspace/usd_IO")
# sys.path.append("/")

# from main.resource.ui.sample_window4_ui import Ui_MainWindow
from resource.ui.qt_city_builder_ui import Ui_MainWindow
from libs.api_osm import OSMCity
from libs.api_grayscale import GrayScaleCity
import libs.api_mov

# importlib.reload(Ui_MainWindow)
# import qdarktheme


'''

'''

class Signals(QtWidgets.QApplication):
    update_progress = QtCore.Signal(int)

# TODO ::::::::::::::::: Qframe 별 Default사이즈 조작 위함.
class FrameScale:
    pass

class LineEdit:
    grid_path = 'lineEdit__grid_path'
    osm_path = 'lineEdit__osm_path'


class CityBuilder(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parnet=None):
        super().__init__(parnet)
        self.setWindowTitle("CityBuilder_ver.1.0")

        # variable
        self.__grid_path = ''
        self.__osm_path = ''
        self.__img_source_path = ''
        self.__save_path = 'D:/git_workspace/usd_IO/build_data'
        self.__form = {'hip': '', 'tex': '', 'mov': '', 'usd': ''}
        self.__save_path_lst = list()
        self.__render_img_path = dict()
        self.__task_type = ''
        self.__cityname = ''
        self.build_grayscale = GrayScaleCity()
        self.build_osm = OSMCity()


        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setBaseSize(1000, 1000)
        self.__init()
        self.resize(1000, 1000)
        self.setupUi(self)
        self.__connection()

    @property
    def grid_path(self):
        return self.__grid_path
    @grid_path.setter
    def grid_path(self, val):
        # assert isinstance(val, pathlib.path)
        self.__grid_path = val

    @property
    def osm_path(self):
        return self.__osm_path
    @osm_path.setter
    def osm_path(self, val):
        # assert isinstance(val, pathlib.path)
        self.__osm_path = val


    # 초기상태 저장
    def __init(self):
        # self.pushButton__save.setEnabled(0)
        pass

    def __connection(self):
        self.toolButton__grid.clicked.connect(lambda x: self.file_dialog('grid_path'))
        self.toolButton__osm.clicked.connect(lambda x: self.file_dialog('osm_path'))
        self.pushButton__build.clicked.connect(self.__slot_btn_build)
        self.pushButton__open.clicked.connect(self.__slot_btn_open)

        self.frame__img1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame__img2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame__img3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame__img4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame__img1.customContextMenuRequested.connect(self.showContextMenu)
        self.frame__img2.customContextMenuRequested.connect(self.showContextMenu)
        self.frame__img3.customContextMenuRequested.connect(self.showContextMenu)
        self.frame__img4.customContextMenuRequested.connect(self.showContextMenu)


        # self.frame__img2.rightclicked.connect(lambda x: self.__slot_image_Rclick("mov 경로"))
        # self.

    # def mousePressEvent(self, event):
    #     print(type(event))
    #     if event.type() == QtCore.QEvent.MouseButtonPress:
    #         if event.button() == QtCore.Qt.RightButton:
    #             print('특정범위에서 우클릭을 잡아네야 하는디...;')
    #             return
    #         else:
    #             print('image frame 외의 공간에서 클릭..?')

    def showContextMenu(self, pos):
        # 현재 우클릭한 레이블을 확인
        frame_data = self.sender()
        frame_data: QtWidgets.QFrame
        index = self.frame__img1.sender()
        print(frame_data, type(frame_data))
        print(frame_data.objectName())
        print(index, type(index), 'asdfsafdjk')

        # 서브 메뉴 생성
        context_menu = QtWidgets.QMenu(self)
        # context_menu.popup(frame_data.metaObject())
        # context_menu.popup(pos)
        a1 = context_menu.addAction('OverView City MOV')
        a2 = context_menu.addAction('Open Output Folder')

        a1.triggered.connect(self.overview_player)
        a2.triggered.connect(self.open_folder)

        # 서브 메뉴 표시
        frame_data.mapToGlobal(pos)
        # cursor_pos = self.mapTo(label, pos)
        # print(pos, type(pos))
        # context_menu.exec_(cursor_pos)
        action = context_menu.exec_(self.mapToGlobal(pos))


    # WHEN Right click on the label
    # then MOV player come up
    # def contextMenuEvent(self, event):
    #     # todo : 범위 지정해주기 현재는 어디든 다 적용됨.
    #     context_menu = QtWidgets.QMenu(self)
    #
    #     a1 = context_menu.addAction('OverView City MOV')
    #     a2 = context_menu.addAction('action 2')
    #
    #     a1.triggered.connect(self.overview_player)
    #     a2.triggered.connect(self.action2_trigger)
    #
    #     context_menu.exec_(event.globalPos())


    def __slot_btn_open(self):
        saved_path = self.lineEdit__open.text()
        self.dir_dialog(saved_path)


    def __slot_btn_build(self):
        self.__cityname = self.lineEdit__city_name.text()
        self.mk_dir()
        # self.progressBar__build.setValue()
        print('progress bar setting 해주기 ')

        print("\n City build start ! 본격 후디니 작업!")

        # osm data일 경우
        if self.__task_type == "osm_path":
            print("osm 데이터 기반 city build를 시작합니다 ... ")
            self.textEdit__log.setText("hip 파일 init 프레임설정")
            self.build_osm.set_hipfile()

            self.textEdit__log.setText("")
            self.build_osm.create_city()

            self.textEdit__log.setText("hip 파일 저장")
            self.build_osm.save_hip(self.__form['hip'])

            self.textEdit__log.setText("Rendering 시작합니다!")
            self.build_osm.render_seq()
            self.set_img_path()

        # grayscale grid일 경우
        if self.__task_type == "grid_path":
            print("grayscale grid 기반 city build를 시작합니다 ... ")
            self.textEdit__log.setText("create city in HOUDINI")
            self.build_grayscale.set_hipfile()
            self.build_grayscale.create_city(self.__img_source_path, self.__form['hip'])

            self.textEdit__log.setText("hip 파일 저장")
            self.build_grayscale.cityname = self.__cityname
            print(self.__form['hip'], "overview")
            self.build_grayscale.save_hip(self.__form['hip'], "overview")

            self.textEdit__log.setText("Rendering 시작합니다!")
            self.build_grayscale.render_seq(self.__form['hip'])
            self.set_img_path()



    def __slot_image_Rclick(self, mov_path):
        print(mov_path)
        pass

    def overview_player(self):
        print('mov play hereeeee')
    def open_folder(self):
        print('open folder ')
        pass

    def control_log(self):
        self.textEdit__log.setText("Grid / OSM 이미지를 넣어주세요!")

    def send_email(self):
        pass

    # output 받기 위한 directory 트리구조 제작
    # [base path] / [city name] / [jpg, mov, hip, usd]
    def mk_dir(self):
        city_dpath = f'{self.__save_path}/{self.__task_type}_{self.__cityname}'
        self.lineEdit__open.setText(city_dpath)
        try:
            os.makedirs(city_dpath)
            for form in self.__form.keys():
                fpath = f'{city_dpath}/{form}'
                if form == 'hip':
                    fpath = city_dpath
                self.__form[form] = fpath
                if not os.path.exists(fpath):
                    os.makedirs(fpath)
            self.textEdit__log.setText("[Task1] >> Build data를 저장할 directory tree를 만듦니다!")
        except OSError:
            print('Cant make dir >> ', )

    # dir dialog 띄우기
    def dir_dialog(self, dir_path, parent=None):
        dirc = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open File',
            # dir='/home/rapa/git_workspace/usd_IO/build_data/'
            dir=dir_path
        )
        print(dirc)

    # grid / osm file import 위한 file dialog
    def file_dialog(self, lineedit_type, parent=None):
        files = QtWidgets.QFileDialog.getOpenFileName(
            self,
            caption='Get File',
            # filter='.jpg',
            dir='~/'
        )
        print(lineedit_type)
        if lineedit_type == '':
            self.textEdit__log.setText("이미지 파일을 넣어주세요!")
            return

        if lineedit_type == 'grid_path':
            self.__img_source_path = files[0]
            self.lineEdit__grid.setText(files[0])
            self.lineEdit__osm.setEnabled(False)
            self.toolButton__osm.setEnabled(False)
            self.__task_type = "grid_path"

        if lineedit_type == 'osm_path':
            self.__img_source_path = files[0]
            self.lineEdit__osm.setText(files[0])
            self.lineEdit__grid.setEnabled(False)
            self.toolButton__grid.setEnabled(False)
            self.__task_type = "osm_path"
        self.lineEdit__city_name.setEnabled(True)
        self.pushButton__build.setEnabled(True)

    def set_img_path(self, img_cnt: int =4):
        for cnt in range(img_cnt):
            img_version = 'img'+str(cnt+1)
            self.__render_img_path[img_version] = r"D:\git_workspace\usd_IO\build_data\grid_path_t1106\render"
        print(self.__render_img_path)

    def slot_set_image_to_label(self, img_cnt: int = 4):
        print('일단 set text 로 구현해두고 render 성공하면 이미지 넣는걸로!')
        for cnt in range(img_cnt):
            img_version = 'img'+str(cnt+1)
            self.label__img1.setText(self.set_img_path[img_version])


    # drag and drop 구현
    def slot_drag_drop(self):
        pass




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    citybuild = CityBuilder()
    citybuild.resize(2000, 1500)
    citybuild.setWindowTitle("adlfk")
    citybuild.show()
    app.exec_()

