#-*- coding:utf-8 -*-

import sys
import os
import subprocess
import re

from PySide2 import QtCore, QtWidgets, QtGui

sys.path.append("E:/git_workspace/city_builder")
filepath = os.getcwd()
sys.path.append(f"{filepath}/city_builder")

# from main.resource.ui.sample_window4_ui import Ui_MainWindow
from resource.ui.qt_city_builder2_ui import Ui_MainWindow
from libs.api_osm import OSMCity
from libs.api_grayscale import GrayScaleCity
from libs.api_mov import FFmpegAPI, VideoPlayer
from libs.api_shotgrid import SgAPI

# importlib.reload(Ui_MainWindow)
import qdarktheme

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
        filepath = os.getcwd()
        self.__grid_path = ''
        self.__osm_path = ''
        self.__img_source_path = ''
        self.__save_path = os.path.join(filepath, 'build_data')
        print(self.__save_path)
        self.__form = {'hip': '', 'tex': '', 'mov': '', 'usd': ''}
        self.__save_path_lst = list()
        self.__mov_path_lst = list()
        self.__seq_path_lst = list()
        self.__render_img_path = dict()
        self.city_dpath: str = ''
        self.__task_type: str = ''
        self.__cityname: str = ''
        self.__render_fin = False

        # instances
        self.build_grayscale = GrayScaleCity()
        self.build_osm = OSMCity()
        self.ffAPI = FFmpegAPI()
        # self.vp = VideoPlayer()
        self.sg = SgAPI()

        # set init
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # self.setFixedSize(1800, 1200)
        self.setFixedSize(1800, 1000)

        self.setupUi(self)
        self.__init()
        qdarktheme.setup_theme()
        self.setAcceptDrops(True)
        self._ttest_set_image_to_label()
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
        self.scrollAreaWidgetContents.setFixedSize(400, 1000)
        self.set_usr_combobox()
        self.setStyleSheet("groupBox_9 {border: none;}"
                           "horizontalLayout {border: none;}")
        # self.scrollArea.setFixedSize(400, 1000)
        # self.frame__image.setFixedSize(1200, 1000```)
        # self.pushButton__save.setEnabled(0)


    def __connection(self):
        self.toolButton__grid.clicked.connect(lambda x: self.file_dialog('grid_path'))
        self.toolButton__osm.clicked.connect(lambda x: self.file_dialog('osm_path'))
        self.pushButton__build.clicked.connect(self.__slot_btn_build)
        self.pushButton__open.clicked.connect(self.__slot_btn_open)
        self.pushButton__publish.clicked.connect(self.__slot_btn_publish)
        self.comboBox__usr.currentTextChanged.connect(self.__slot_usr_combobox)

        # submenu 띄우기 위함
        self.frame__img1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame__img2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame__img3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame__img4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame__img1.customContextMenuRequested.connect(self.showContextMenu)
        self.frame__img2.customContextMenuRequested.connect(self.showContextMenu)
        self.frame__img3.customContextMenuRequested.connect(self.showContextMenu)
        self.frame__img4.customContextMenuRequested.connect(self.showContextMenu)


    def showContextMenu(self, pos: QtCore.QPoint):
        # 현재 우클릭한 레이블을 확인
        frame_data = self.sender()
        frame_data: QtWidgets.QFrame

        # 서브 메뉴 생성
        context_menu = QtWidgets.QMenu(self)

        a1 = context_menu.addAction('OverView City MOV')
        a2 = context_menu.addAction('Open Output Folder')

        a1.triggered.connect(lambda x: self.overview_player(frame_data.objectName()))
        a2.triggered.connect(lambda x: self.open_folder(frame_data.objectName()))

        # 서브 메뉴 표시
        context_menu.exec_(frame_data.mapToGlobal(pos))


    def __slot_btn_open(self):
        saved_path = self.lineEdit__open.text()
        self.dir_dialog(saved_path)


    def __slot_btn_build(self):

        self.__cityname = self.lineEdit__city_name.text()
        self.mk_dir()
        print('progress bar setting 해주기 ')

        print("\n City build start ! 본격 후디니 작업!")


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
            # 렌더된 이미지 label에 넣어주기 + mov play 준비
            # self.set_img_path()
            # self.__render_fin = True
            # self.set_image_to_label()

        # osm data일 경우
        if self.__task_type == "osm_path":
            print("osm 데이터 기반 city build를 시작합니다 ... ")
            self.textEdit__log.setText("hip 파일 init 프레임설정")
            self.build_osm.set_hipfile()

            self.textEdit__log.setText("")
            self.build_osm.create_city(self.__img_source_path, self.__form['hip'])

            self.textEdit__log.setText("hip 파일 저장")
            self.build_osm.save_hip(self.__form["hip"])

            self.textEdit__log.setText("Rendering 시작합니다!")
            self.build_osm.render_seq(self.__form["hip"])
            # 렌더된 이미지 label에 넣어주기 + mov play 준비
            # self.set_img_path()
            # self.__render_fin = True
            # self.set_image_to_label()

    def __slot_btn_publish(self):
        # combobox 안에 든 사람이 어떤 id를 가진 사람인지 알아야 ID를 넣을 수 있지.
        publisher_id = self.sg.find_usr_id(self.comboBox__usr.currentText())
        self.sg.publish2assetlibrary(self.__cityname, self.__form["hip"], publisher_id)

        asset_id = self.sg.find_asset_id(self.__cityname)
        # thumbnail_path = os.path.join(self.__render_img_path)
        thumbnail_path = fr"{filepath}\build_data\grid_path\d0320_t0750\render\0\grayscale_d0320_t0750_build_city.0.1001.jpg"
        self.sg.upload_thumbnail(asset_id, thumbnail_path)
        self.textEdit__log.setText(f"{self.comboBox__usr.currentText()} 이름으로 shotgrid에 등록 완료!")

    def __slot_usr_combobox(self):
        if self.comboBox__usr.currentText():
            print("해당 사용자 이름으로 asset library에 올리기!")
            self.pushButton__publish.setEnabled(True)


    # TODO >> MOV 만드는거 상대경로로 바꾸기!!!!
    # TODO >> 함수 실행 위치 build btn 클릭 렌더 이후로 바꿀 것!
    def make_mov(self, wedge_num: int = 4):
        # self.ffAPI.make_jpg_to_mov()
        self.__form['hip'] = r"E:\git_workspace\city_builder\build_data\grid_path\d0322_t2009"
        for wedge in range(wedge_num):
            seq_path = os.path.join(self.__form['hip'], "render", str(wedge))
            start_num = "1001"
            seq_name = f"grayscale_d0322_t2009_render.{wedge}.%4d.jpg"
            mov_name = "output.mov"
            self.ffAPI.make_jpg_to_mov(seq_path, start_num, seq_name, mov_name)
            self.__mov_path_lst.append(os.path.join(seq_path, mov_name))
        print(self.__mov_path_lst)


    def overview_player(self, frame_name):
        # self.make_mov()
        self.__mov_path_lst.append(r"E:\git_workspace\city_builder\build_data\grid_path\d0322_t2009\render\0\output.mov")
        self.__mov_path_lst.append(r"E:\git_workspace\city_builder\build_data\grid_path\d0322_t2009\render\1\output.mov")
        self.__mov_path_lst.append(r"E:\git_workspace\city_builder\build_data\grid_path\d0322_t2009\render\2\output.mov")
        self.__mov_path_lst.append(r"E:\git_workspace\city_builder\build_data\grid_path\d0322_t2009\render\3\output.mov")

        if frame_name == "frame__img1":
            self.vp = VideoPlayer()
            self.vp.set_playlist(self.__mov_path_lst)
            frame_name: QtWidgets.QFrame
            self.vp.set_media_num(0)
            # self.vp.set_path(self.__mov_path_lst[0])
            print('img1 mov play hereeeee')

        if frame_name == "frame__img2":
            self.vp = VideoPlayer()
            self.vp.set_playlist(self.__mov_path_lst)
            frame_name: QtWidgets.QFrame
            self.vp.set_media_num(1)
            # self.vp.set_path(self.__mov_path_lst[1])
            print('img2 mov play hereeeee')

        if frame_name == "frame__img3":
            self.vp = VideoPlayer()
            self.vp.set_playlist(self.__mov_path_lst)
            frame_name: QtWidgets.QFrame
            self.vp.set_media_num(2)
            print('img3 mov play hereeee')

        if frame_name == "frame__img4":
            self.vp = VideoPlayer()
            self.vp.set_playlist(self.__mov_path_lst)
            frame_name: QtWidgets.QFrame
            self.vp.set_media_num(3)
            print('img4 mov play hereeeee')

        self.vp.show()


    def open_folder(self, frame_name):
        # Windows에서 파일 탐색기 열기
        self.__seq_path_lst.append(r"E:\git_workspace\city_builder\build_data\grid_path\d0320_t0750\render\0")
        self.__seq_path_lst.append(r"E:\git_workspace\city_builder\build_data\grid_path\d0320_t0750\render\1")
        self.__seq_path_lst.append(r"E:\git_workspace\city_builder\build_data\grid_path\d0320_t0750\render\2")
        self.__seq_path_lst.append(r"E:\git_workspace\city_builder\build_data\grid_path\d0320_t0750\render\3")
        print(frame_name)
        frame_name: QtWidgets.QFrame

        if frame_name == "frame__img1":
            subprocess.Popen(['explorer', self.__seq_path_lst[0]])
            print('img1 file explorer open')

        if frame_name == "frame__img2":
            subprocess.Popen(['explorer', self.__seq_path_lst[1]])
            print('img2 mov play hereeeee')

        if frame_name == "frame__img3":
            subprocess.Popen(['explorer', self.__seq_path_lst[2]])
            print('img3 mov play hereeee')

        if frame_name == "frame__img4":
            subprocess.Popen(['explorer', self.__seq_path_lst[3]])
            print('img4 mov play hereeeee')

    def control_log(self):
        self.textEdit__log.setText("Grid / OSM 이미지를 넣어주세요!")

    # output 받기 위한 directory 트리구조 제작
    # [base path] / [city name] / [jpg, mov, hip, usd]
    def mk_dir(self):
        self.city_dpath = os.path.join(self.__save_path, self.__task_type, self.__cityname)
        self.lineEdit__open.setText(self.city_dpath)
        try:
            os.makedirs(self.city_dpath)
            for form in self.__form.keys():
                fpath = os.path.join(self.city_dpath, form)
                if form == 'hip':
                    fpath = self.city_dpath
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
        if lineedit_type == 'grid_path':
            _filter = ("Image Files (*.png *.jpg *.bmp)")

        if lineedit_type == 'osm_path':
            _filter = ("OSM Files (*.osm)")

        files = QtWidgets.QFileDialog.getOpenFileName(
            self,
            caption='Get File',
            filter=_filter,
            dir='~/'
        )
        print(lineedit_type)
        if lineedit_type == '':
            self.textEdit__log.setText("이미지 파일을 넣어주세요!")

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

    def set_img_path(self, task, wedge_num: int = 4):
        for wedge in range(wedge_num):
            render_img_name = f"{task}_{self.__cityname}_render.{wedge}.1001.jpg"
            # render_dpath = f"{self.__form['hip']}\
            render_img_path = os.path.join(self.__form['hip'], 'render', str(wedge), render_img_name)

            self.__render_img_path[wedge] = render_img_path


    def _ttest_set_image_to_label(self, task="grayscale", wedge_num: int = 4):
        for wedge in range(wedge_num):
            # render_img_name = f"{task}_t0750_render.{wedge}.1001.jpg"
            # render_dpath = f"{self.__form['hip']}\
            # render_img_path = os.path.join(r"E:\git_workspace\city_builder\build_data\grid_path\t1645", 'render', str(wedge), render_img_name)

            render_img_name = f"{task}_d0322_t2009_render.{wedge}.1001.jpg"
            render_img_path = os.path.join(r"E:\git_workspace\city_builder\build_data\grid_path\d0322_t2009", 'render', str(wedge), render_img_name)

            self.__render_img_path[wedge] = render_img_path

            print(render_img_path)
            render_qimg = QtGui.QPixmap(render_img_path)
            self.__render_img_path[wedge] = render_qimg

            if wedge == 0:
                self.label__img1.setPixmap(self.__render_img_path[wedge])
                self.label__img1.setAlignment(QtCore.Qt.AlignCenter)
            if wedge == 1:
                self.label__img2.setPixmap(self.__render_img_path[wedge])
                self.label__img2.setAlignment(QtCore.Qt.AlignCenter)
            if wedge == 2:
                self.label__img3.setPixmap(self.__render_img_path[wedge])
                self.label__img3.setAlignment(QtCore.Qt.AlignCenter)
            if wedge == 3:
                self.label__img4.setPixmap(self.__render_img_path[wedge])
                self.label__img4.setAlignment(QtCore.Qt.AlignCenter)

        print(self.__render_img_path)

    def set_usr_combobox(self):
        self.comboBox__usr.setEnabled(True)
        user_lst = self.sg.people_lst
        # user_lst:  [{'type': 'HumanUser', 'id': '' , 'name': ''}]
        for usr in user_lst:
            self.comboBox__usr.addItem(usr["name"])


    def set_image_to_label(self, img_cnt: int = 4):
        print('일단 set text로 구현해두고 render 성공하면 이미지 넣는걸로!')
        if self.__task_type == "grid_path":
            self.set_img_path("grayscale")
            print(self.__render_img_path)


        if self.__task_type == "osm_path":
            self.set_img_path("osm")
            print(self.__render_img_path)

        for cnt in range(img_cnt):
            # self.label_lst[cnt].setPixmap(self.__render_img_path[])
            self.label__img1.setText(self.set_img_path[img_version])

            # render_qimg = QtGui.QPixmap(render_img_path)
            # self.__render_img_path[wedge] = render_qimg

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            self.label__dd_grayscale.setText(file_path)
            self.label__dd_osm.setText(file_path)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    citybuild = CityBuilder()
    citybuild.setWindowTitle("City_builder")
    citybuild.show()
    app.exec_()

