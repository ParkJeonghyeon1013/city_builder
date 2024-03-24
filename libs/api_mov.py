import os
import shlex
import subprocess
import re

import qdarktheme

from PySide2 import QtWidgets, QtGui, QtCore, QtMultimediaWidgets, QtMultimedia


class First(QtWidgets.QMainWindow):
    def __init__(self, parnet=None):
        super().__init__(parnet)
        self.btn = QtWidgets.QPushButton("player")
        self.setLayout(self.btn)
        # vbox = QtWidgets.QVBoxLayout()
        # vbox.addWidget(self.btn)
        # self.setLayout(vbox)

        self.btn.clicked.connect(self.slot_popup)

        self.VP = VideoPlayer()

    def slot_popup(self):
        self.VP.show()

class VideoWidget(QtMultimediaWidgets.QVideoWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtCore.Qt.black)
        self.setPalette(palette)
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)

class VideoPlayer(QtWidgets.QWidget):
    def __init__(self, parnet=None):
        super().__init__(parnet)
        # variable
        self.flag_stop = False
        self.url_lst = list()
        self.video_lst = list()
        self.video_path: os.path = ""

        self.setWindowTitle("Video Player")

        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setBaseSize(1000,1000)
        self.__set_player()
        self.__set_ui()
        qdarktheme.setup_theme()
        self.__connection()


    def __set_player(self):
        self.video_widget = VideoWidget()
        self.__player = QtMultimedia.QMediaPlayer()
        self.__player.setVideoOutput(self.video_widget)
        self.playlist = QtMultimedia.QMediaPlaylist(self.__player)

    def __set_ui(self):
        self.__btn_play = QtWidgets.QPushButton("Play")
        self.__btn_stop = QtWidgets.QPushButton("Stop")
        self.__btn_close = QtWidgets.QPushButton("Close")

        hbox_layout_btns = QtWidgets.QHBoxLayout()
        hbox_layout_btns.addWidget(self.__btn_play)
        hbox_layout_btns.addWidget(self.__btn_stop)
        hbox_layout_btns.addWidget(self.__btn_close)

        self.__label_name = QtWidgets.QLabel(f"{self.video_path}")
        self.__label_name.setText(self.video_path)
        self.__label_name.setFixedSize(500, 70)

        self.video_widget.setFixedSize(500, 500)
        vbox_layout = QtWidgets.QVBoxLayout()
        vbox_layout.addWidget(self.__label_name)
        vbox_layout.addWidget(self.video_widget)
        vbox_layout.addLayout(hbox_layout_btns)

        self.setLayout(vbox_layout)

    def set_path(self, vpath):
        self.video_path = vpath

    def __connection(self):
        self.__btn_play.clicked.connect(self.slot_play_btn)
        self.__btn_stop.clicked.connect(self.slot_stop_btn)
        self.__btn_close.clicked.connect(self.slot_close_btn)
        self.__player.stateChanged.connect(self.slot_state)

    # Video play 다 끝나면 다시 재생해주기
    def slot_state(self, state):
        if state == QtMultimedia.QMediaPlayer.State.StoppedState:
            self.__player.play()
            print("한바퀴 끝났다 loop 플래그 켜져있으면 play 해주는 방식으로 loop를 구현하자.")

    # playlist에 콘텐츠 add 하기
    def set_playlist(self, video_lst):
        for video_path in video_lst:
            self.video_lst.append(video_path)
            url = QtCore.QUrl.fromLocalFile(video_path)
            print(url, type(url))
            self.url_lst.append(url)
            self.playlist.addMedia(url)

    def set_media_num(self, num):
        self.__player.setMedia(self.url_lst[num])
        self.__label_name.setText(self.video_lst[1])

    def __check_video_exist(self):
        pass

    def slot_play_btn(self):
        # QT_MULTIMEDIA_PREFERRED_PLUGINS
        # "windowsmediafoundation" or "directshow"

        self.set_playlist([])
        print('add 완료')

        # self.set_media_num
        self.video_widget.setVisible(True)
        self.__player.play()

        a = self.__player.error()
        print(a)

    def slot_stop_btn(self):
        if self.flag_stop is False:
            self.__player.pause()
            self.flag_stop = True
            return
        if self.flag_stop is True:
            self.__player.play()
            self.flag_stop = False
            return

        print("\n재생 정지")

    def slot_close_btn(self):
        self.close()

    def closeEvent(self, event):
        self.__player.pause()

class FFmpegAPI:
    def __init__(self):
        self.output_video_path = ""

    # ffmpeg -f [image2] -framerate [24] -i [C:\seq\%3d.jpg] -c:v [libx264] -r [24] [C:\seq\output.mp4]
    def make_jpg_to_mov(self,
                        output_path: str = r"D:\git_workspace\usd_IO\resource\seq_sample",
                        start_frame: str = "1001",
                        seq_name: str = "%4d.jpg",
                        mov_name: str = "output.mov",
                        ffmpeg_path: str = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"):

        ffmpeg_path = ffmpeg_path
        seq_path = os.path.join(output_path, seq_name)
        video_path = os.path.join(output_path, mov_name)

        # cmd = r'''
        # {ffmpeg_path} -f image2 -start_number {start_frame} -framerate {frame_rate} -i {seq_path} -c:v {codex} -r {frame_rate} {video_path}
        # '''.format(
        #     ffmpeg_path=ffmpeg_path, start_frame=start_frame, frame_rate=24, seq_path=seq_path, codex="libx264", video_path=video_path
        # )
        # D:\git_workspace\usd_IO\resource\seq_sample\ %4d.jpg
        #
        # print(cmd)
        # result = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # out, err = result.communicate()
        # print(out, err)

        try:
            cmd = []
            cmd.append(ffmpeg_path)
            cmd.append("-f")
            cmd.append("image2")
            cmd.append("-start_number")
            cmd.append(start_frame)
            cmd.append("-framerate")
            cmd.append("24")
            cmd.append("-i")
            cmd.append(seq_path)
            cmd.append("-c:v")
            cmd.append("libx264")
            cmd.append("-r")
            cmd.append("24")
            cmd.append(video_path)
            print(cmd)
            print()
            # TODO ::::::::: 이미 동일한 이름의 mov가 있는 경우 overwrite 할지 말지 묻는데 이런 경우 어떻게 해결해야 할까?
            subprocess.run(cmd, shell=True)
        except Exception:
            subprocess.run("y", shell=True)
        self.output_video_path = os.path.join(output_path, mov_name)


    def return_video_path(self):
        return self.output_video_path

if __name__ == "__main__":
    # ffAPI = FFmpegAPI()
    # ffAPI.make_jpg_to_mov(r"D:\git_workspace\city_builder\build_data\grid_path_t1124\render\0",
    #                       "1001", "grayscale_t1124_render.0.%4d.jpg", "output.mov")
    # output_video_path = ffAPI.return_video_path()

    app = QtWidgets.QApplication()
    vp = VideoPlayer()
    vp.set_media_num(0)
    vp.show()
    app.exec_()