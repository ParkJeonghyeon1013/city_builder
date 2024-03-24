import pathlib
import sys, os
import re, importlib, subprocess
import hou as hou




class GrayScaleCity:
    def __init__(self, cityname: str = 'testcity'):
        self.version = 0
        self.__cityname = cityname

    @property
    def cityname(self):
        return self.__cityname
    @cityname.setter
    def cityname(self, val):
        assert isinstance(val, str)
        self.__cityname = val

    @staticmethod
    def align_node(node_lst):
        for node in node_lst:
            node.moveToGoodPosition()

    @staticmethod       # 노드 생성 시 위치 정렬을 위한 메서드
    def align_node_pos(node_name, node_pos, add_x, add_y):
        node_name.setPosition((node_pos[0] + add_x, node_pos[1] + add_y))

    @staticmethod
    def set_hipfile():
        print("\ngrayscale set hipfile")
        # init HOUDINI
        hou.hipFile.clear(suppress_save_prompt=True)

        # set frame range - 5s [1001-1121]

        start_frame: int = 1001
        end_frame: int = 1062
        fps: int = 24
        hou.setFps(fps)
        frame_set = f"`{start_frame -1}/$FPS` `{end_frame}/$FPS`"
        hou.hscript(frame_set)
        hou.playbar.setFrameRange(start_frame, end_frame)
        hou.playbar.setPlaybackRange(start_frame, end_frame)
        hou.setFrame(start_frame)
        # hou.playbar.setTimeRange(int(start_frame), int(end_frame))

################################################################dd##########################
    def render_seq(self,
                   dir_path: str = "D:/git_workspace/usd_IO/build_data/grayscale_testcity"):
        # set Node variable
        obj = hou.node("/obj")

        n_street_grid = hou.node('/obj/STREET_GRID')
        n_work_viewer1 = hou.node('/obj/WORK_Building_VIEWER1')
        n_work_viewer2 = hou.node('/obj/WORK_Building_VIEWER2')
        n_render_viewer1 = hou.node('/obj/RENDER_Building_VIEWER1')
        n_render_viewer2 = hou.node('/obj/RENDER_Building_VIEWER2')
        n_topnet = hou.node('/obj/topnet1')

        n1_file_node = n_render_viewer1.createNode("file")
        n1_file_node.parm("file").set("`@pdg_input`")

        n2_file_node = n_render_viewer2.createNode("file")
        n2_file_node.parm("file").set("`@pdg_input.1`")


        # Render displayFlag set
        n_street_grid.setDisplayFlag(False)
        n_work_viewer1.setDisplayFlag(False)
        n_work_viewer2.setDisplayFlag(False)
        n_render_viewer1.setDisplayFlag(True)
        n_render_viewer2.setDisplayFlag(True)

        print("\n렌더 세팅 시작", dir_path)

        # camera/ light 세팅
        # TODO: :::::::::::::::::::: camera 위치 세팅 -> test render so, just put fixed value

        n_cam = obj.createNode("cam")
        # n_cam.parm("tx").setExpression('ch("../topnet1/hdaprocessor1/hdap_sx1")*3')
        # n_cam.parm("ty").setExpression('ch("../topnet1/hdaprocessor1/hdap_sx1")*2.5')

        n_cam.parm("tx").set(172)
        n_cam.parm("ty").set(150)
        n_cam.parm("tz").set(172)
        n_cam.parm("rx").set(-30)
        n_cam.parm("ry").set(45)


        n_light1 = obj.createNode("hlight::2.0", "sunlight")
        n_light1.parm("light_type").set(8)
        n_light1.parm("vm_envangle").set(2)
        n_light1.parm("vm_samplingquality").set(0.5)

        n_light2 = obj.createNode("envlight", "skylight")
        n_light2.parm("skymap_enable").set(1)
        n_light2.parm("light_intensity").set(1.3)
        n_light2.parm("vm_samplingquality").set(0.5)
        n_light2.parm("skymap_resolution").set(16)
        self.align_node_pos(n_cam, n_work_viewer2.position(), 0, -1)
        self.align_node_pos(n_light1, n_cam.position(), 0, -1)
        self.align_node_pos(n_light2, n_light1.position(), 3, 0)

        # obj > topnet > mantra renderer 추가
        n_part_idx = hou.node("/obj/topnet1/partitionbyindex1")
        n_mantra = n_topnet.createNode("ropmantra")
        n_mantra.setInput(0, n_part_idx)
        n_mantra.parm("pdg_cachemode").set(2)
        n_mantra.parm("override_camerares").set(1)
        n_mantra.parm("vm_picture").set("$HIP/render/$HIPNAME_$OS_`@wedgenum`/$HIPNAME.`@wedgenum`.$F.jpg")

        # 만트라 세팅 렌더시간 줄일 수 있...지는 못했다ㅠ
        # a = hou.node('/obj/topnet1/ropmantra1')
        # >> > a.parm("vm_sssquality").set(0)
        # >> > a.parm("vm_reflectionquality").set(0)
        # >> > a.parm("vm_refractionquality").set(0)
        # >> > a.parm("vm_renderengine").set(0)

        self.align_node_pos(n_mantra, n_part_idx.position(), 0, -2)

        # obj > topnet > overlaytext
        n_overlaytext = n_topnet.createNode("ropcomposite")
        n_overlaytext.setInput(0, n_mantra)
        n_overlaytext.parm("copoutput").set("$HIP/render/$HIPNAME_$OS_`@wedgenum`/$HIPNAME.$OS.`@wedgenum`.$F.jpg")
        self.align_node_pos(n_overlaytext, n_mantra.position(), 0, -2)

        n_overlaytext_in = hou.node(n_overlaytext.path() + '/c')
        n_pdg_result = hou.node('/obj/topnet1/ropcomposite1/c/pdg_result')

        n_font = n_overlaytext_in.createNode("font")
        n_font.parm("text").set(
            "Map: `@file_wedge`\nCity Core: `@center_wedge.0`, `@center_wedge.2`\nVariation Seed: `@seed_wedge`")
        n_font.parm("textsize").set(18)
        n_font.setInput(0, n_pdg_result)
        self.align_node_pos(n_font, n_pdg_result.position(), -2, -2)

        n_dropshadow = n_overlaytext_in.createNode("dropshadow")
        n_dropshadow.setInput(0, n_font)
        self.align_node_pos(n_dropshadow, n_font.position(), 0, -2)

        n_over = n_overlaytext_in.createNode("over")
        n_over.setInput(0, n_dropshadow)
        n_over.setInput(1, n_pdg_result)
        n_over.setRenderFlag(True)
        self.align_node_pos(n_over, n_dropshadow.position(), 2, -2)


        # obj > topnet > waitforall
        n_wait = n_topnet.createNode("waitforall")
        n_wait.setInput(0, n_overlaytext)
        self.align_node_pos(n_wait, n_overlaytext.position(), 0, -2)

        n_magick = n_topnet.createNode("imagemagick")
        n_magick.setInput(0, n_wait)
        n_magick.setDisplayFlag(True)
        self.align_node_pos(n_magick, n_wait.position(), 0, -2)


        # todo ::::::::::: file save > topnet cook > render 순으로 진행
        # cook 해주고 render 해주기
        print("\nrender 전 저장 후 render 시작")
        self.save_hip(dir_path,'render')
        n_topnet.dirtyAllTasks(True)
        print("\n렌더 시작!!")

        # Mantra render set >> framerange
        # n_mantra.parm("framegeneration").set(1)
        # n_topnet.cookAllOutputWorkItems(True)
        print("\n cook 했다면 seq 뽑을 수 있음!")



    def save_hip(self,
                 dir_path: str = "D:/git_workspace/usd_IO/build_data/grayscale_testcity",
                 task: str = "render"):

        '''

        :param dir_path:
        :param task: overview / render 두 종류 task 구분해서 저장하기 위함.
        :return:
        '''
        hip_path = os.path.join(dir_path, f'grayscale_{self.cityname}_{task}.hip')
        print(f"\n{hip_path}에 저장합니다!")
        # hip save
        hou.hipFile.save(hip_path)
        self.version += 1


    def create_city(self,
                    img_path: str = "D:/git_workspace/usd_IO/hip_practice/script_grayscale/tex/citygrid.jpg",
                    saved_path: str = "D:/git_workspace/usd_IO/build_data/grayscale_testcity"):

        # Create Main Node
        obj = hou.node("/obj")

        n_street_grid = obj.createNode("geo", "STREET_GRID")
        n_work_viewer1 = obj.createNode("geo", "WORK_Building_VIEWER1")
        n_work_viewer2 = obj.createNode("geo", "WORK_Building_VIEWER2")
        n_render_viewer1= obj.createNode("geo", "RENDER_Building_VIEWER1")
        n_render_viewer2= obj.createNode("geo", "RENDER_Building_VIEWER2")
        n_topnet = obj.createNode("topnet")

        n_topnet.setPosition([4, 0])
        n_work_viewer1.setPosition([0, -1])
        n_work_viewer2.setPosition([0, -2])
        n_render_viewer1.setPosition([4, -1])
        n_render_viewer2.setPosition([4, -2])

        print("\n obj 채널 기본 세팅 완료!")

######################################################################################################################
        # n_work_viewer1 노드 안에 file 노드 생성 후 값 세팅
        file_node = n_work_viewer1.createNode("file")
        file_node.parm("file").set("`@pdg_output`")

######################################################################################################################
        # obj > street_grid > subnet
        # TODO : grid size / path 설정하기!!!!!!!!!!!!!!! 일단 절대로 두고, 상대로 변경은 나중에!!!!!!!!!
        n_subnet = n_street_grid.createNode("subnet", "streetgrid_maker")
        n_trace = n_subnet.createNode("trace")

        n_trace.parm("rx").set(-90)
        n_trace.parm("sx").set(1)
        n_trace.parm("sy").setExpression('ch("./sx")')

        # n_trace.parm("file").set("/home/rapa/git_workspace/usd_IO/hip_practice/script_grayscale/tex/citygrid.jpg") # grid 이미지 경로 설정
        print(img_path, type(img_path))
        n_trace.parm("file").set(img_path) # grid 이미지 경로 설정
        print("\n이미지 경로 잘 들어감!")
        n_trace.parm("overridesize").set(1)     # gird size 랑 그냥 relative로 엮어줄까?
        n_trace.parm("imagesize1").set(500)
        n_trace.parm("imagesize2").set(500)

        n_reverse = n_subnet.createNode("reverse")
        n_reverse.setInput(0, n_trace)
        self.align_node_pos(n_reverse, n_trace.position(), 0, -1)


        n_root = n_subnet.createNode("null", "root")
        n_root.setInput(0, n_reverse)
        self.align_node_pos(n_root, n_trace.position(), 0, -1)


        # vex를 사용하여 그리드 각각 사이즈의 평균을 구해 어떤 grid가 오든 유사한 사이즈의 그리드가 생성될 수 있도록 함.
        # root 노드 옆에 새로운 길 팜.
        n_vex = n_subnet.createNode("null", "vex")
        n_vex.setInput(0, n_root)
        self.align_node_pos(n_vex, n_root.position(), 3, 0)


        n_att_wrangle = n_subnet.createNode("attribwrangle")
        n_att_wrangle.parm("class").set(0)
        vex_expression1 = '''int _nprims = nprimitives(0);
        float _sum = 0;
        
        for(int i=0; i<_nprims; i++){
            _sum += primintrinsic(0, "measuredarea", i);
        }

        f@_area = 1.0 / (_sum / float(_nprims));
        '''
        n_att_wrangle.parm("snippet").set(vex_expression1)
        n_att_wrangle.parm("class").set(0)
        n_att_wrangle.setInput(0, n_vex)
        self.align_node_pos(n_att_wrangle, n_vex.position(), 0, -1)


        n_ref_area = n_subnet.createNode("null", "__REF_AREA__")
        n_ref_area.setInput(0, n_att_wrangle)
        self.align_node_pos(n_ref_area, n_att_wrangle.position(), 0, -1)

        ##############################################################################
        n_resample = n_subnet.createNode("resample")
        # todo >> render 시간 오래 걸리는 이유를 vertex 많아서 일 수 있다고 하셔서 resample 넣어줌
        # n_resample.parm("length").set(3)
        n_resample.setInput(0, n_root)
        self.align_node_pos(n_resample, n_root.position(), 0, -1)

        n_att_wrangle2 = n_subnet.createNode("attribwrangle")
        vex_expression2 = """for(int i=0; i<npoints(0); i++){
            int _neighbours[] = neighbours(0, i);
            vector _pos1 = point(0, "P", _neighbours[0]);
            vector _pos2 = point(0, "P", _neighbours[1]);
            vector _p = point(0, "P", i);
            vector _dir1 = _pos1 - _p;
            vector _dir2 = _pos2 - _p;
            _dir1 = normalize(_dir1);
            _dir2 = normalize(_dir2);
            float _angle = abs(dot(_dir1, _dir2));
            if(_angle > 0.99){
                removepoint(geoself(), i);
            }
        }    
        """
        n_att_wrangle2.parm("snippet").set(vex_expression2)
        n_att_wrangle2.parm("class").set(0)
        n_att_wrangle2.setInput(0, n_resample)
        self.align_node_pos(n_att_wrangle2, n_resample.position(), 0 ,-1)


        n_transform = n_subnet.createNode("xform")
        n_transform.parm("scale").setExpression('detail("../__REF_AREA__", "_area", 0)')
        n_transform.setInput(0, n_att_wrangle2)
        self.align_node_pos(n_transform, n_att_wrangle2.position(), 0, -1)


        n_color = n_subnet.createNode("color")
        # n_color.setColor(hou.Color(0,0,0))
        n_color.parm("colorr").set(0)
        n_color.parm("colorg").set(0)
        n_color.parm("colorb").set(0)
        n_color.parm("class").set(1)
        n_color.setInput(0, n_transform)
        self.align_node_pos(n_color, n_transform.position(), 0, -1)


        # city core 제작 위함 = 초록색으로 표시 후 해당 부분을 추출하여 height를 높여주는 원리
        n_sphere = n_subnet.createNode("sphere")
        n_sphere.parm("type").set(1)
        n_sphere.parm("radx").set(0.5)
        n_sphere.parm("rady").set(0.5)
        n_sphere.parm("radz").set(0.5)
        n_sphere.parm("scale").set(5)
        self.align_node_pos(n_sphere, n_trace.position(), 3, -1)


        n_sphere_color = n_subnet.createNode("color")
        n_sphere_color.parm("colorr").set(0)
        n_sphere_color.parm("colorg").set(1)
        n_sphere_color.parm("colorb").set(0)
        n_sphere_color.parm("class").set(1)
        n_sphere_color.setInput(0, n_sphere)
        self.align_node_pos(n_sphere_color, n_sphere.position(), 0, -1)


        n_attribute_transfer = n_subnet.createNode("attribtransfer")
        n_attribute_transfer.setInput(0, n_color)
        n_attribute_transfer.setInput(1, n_sphere_color)
        n_attribute_transfer.parm("pointattribs").set(0)
        n_attribute_transfer.parm("primattriblist").set("Cd")
        n_attribute_transfer.parm("thresholddist").set(0)
        n_attribute_transfer.parm("blendwidth").set(30)
        self.align_node_pos(n_attribute_transfer, n_sphere_color.position(), 0, -2)

        n_output = n_subnet.createNode("output")
        n_output.setInput(0, n_attribute_transfer)
        n_output.setDisplayFlag(True)
        self.align_node_pos(n_output, n_attribute_transfer.position(), 0, -1)
        self.align_node([n_trace, n_reverse, n_root, n_vex, n_att_wrangle, n_ref_area, n_resample, n_att_wrangle2, n_transform, n_color, n_sphere, n_sphere_color, n_attribute_transfer, n_output])


        print("\n hda 제작을 위한 세팅 완료 ")
        ##########################################################################################################

        # subnet을 통해서 HDA를 만들 때 relative로 parmeter 연결해주기 위한 작업!
        # ptg 그룹이 있다. 여기에 넣어주기 위한 parm templete 제작 > ptg 그룹에 넣어주고 > subnet에 set해주면 됨
        # 오마이갓. subent에 set을 해주는 방식이 아니라 hda를 우선 제작한 후 해당 hda의 parmgroup에 넣어주고, definition, option 설정을 해주면 hda processor에서도 보인다!!!!!!!

        n_subnet = hou.node('/obj/STREET_GRID/streetgrid_maker')
        hda_save_path = f"{saved_path}/hda/streetgrid_maker.hda"
        hda = n_subnet.createDigitalAsset(name='Street_maker', description='Street_maker',
                                                 hda_file_name=hda_save_path,
                                                 create_backup=False)
        definition = hda.type().definition()
        ptg = hda.parmTemplateGroup()





        # TODO ::::::::::: parm과 relative로 연결하기 // SETFROMPARM 사용해주면 됨.
        #
        # target_parm = hou.node('/obj/street_grid/subnet1/trace1').parm("file")
        # n_subnet.parm("file").setFromParm(target_parm)
        # >> > p = hou.parm('/obj/topnet1/hdaprocessor1/hdap_img_input')
        # >> > hou.parm('/obj/geo1/trace1/file').setFromParm(hou.parm('/obj/topnet1/hdaprocessor1/hdap_Image_input'))
        # >> > hou.parm('/obj/geo1/trace1/file').setFromParm(p)
        # >> > hou.parm('/obj/geo1/trace1/file').setFromParm(p)
        # >> > hou.parm('/obj/geo1/trace1/file').setFromParm(p)

        hou.parmTuple('/obj/geo1/t')
        '''
        // image input (file) : subnet > trace > image input
        // scale X (sx) : subnet > trace > scale X
        // sphere center (t) : subnet > sphere > center
        // blend width : subnet > attribtransfer > blend width 
        '''


        template1 = hou.FloatParmTemplate(name='s', label='Scale', num_components=2,)
                                          # default_expression=('chs("trace1/sx")'),
                                          # default_expression_language=(hou.scriptLanguage.Hscript,))

        template2 = hou.FloatParmTemplate(name='t', label='Sphere_Center', num_components=3,)
                                          # default_expression=('chs("sphere1/t")'),
                                          # default_expression_language=(hou.scriptLanguage.Hscript,))

        template3 = hou.FloatParmTemplate(name='blendwidth', label='Blend_Width', num_components=1,)
                                          # default_expression=('chs("attribtransfer1/blendwidth")'),
                                          # default_expression_language=(hou.scriptLanguage.Hscript,))

        template4 = hou.StringParmTemplate(name='file', label='Image_input', num_components=1,
                                           file_type=hou.fileType.Image,
                                           # default_value=('put_image_path',),
                                           string_type=hou.stringParmType.FileReference,
                                           default_expression=('chs("trace1/file")',),
                                           default_expression_language=(hou.scriptLanguage.Hscript,))
        # template5 = hou.
        ptg.append(template1)
        ptg.append(template2)
        ptg.append(template3)
        ptg.append(template4)

        # n_subnet.setParmTemplateGroup(ptg)
        definition.setParmTemplateGroup(ptg)

        options = definition.options()
        options.saveSpareParms()
        options.setSaveSpareParms(True)
        options.setSaveInitialParmsAndContents(True)
        definition.setOptions(options)
        hda_fpath = definition.libraryFilePath()
        definition.save(hda_fpath, template_node=hda, options=options, create_backup=False)
        definition.updateFromNode(hda)

        n_subnet = hou.node('/obj/STREET_GRID/streetgrid_maker')
        n_null = n_street_grid.createNode("null", "CITYBLOCKS_OUT")
        n_null.setInput(0, n_subnet)
        self.align_node_pos(n_null, n_subnet.position(), 0, -1)
        print('\nHDA 제작 완료')


##########################################################################################################
        # obj > topnet > localscheduler
        n_localscheduler = n_topnet.node('localscheduler')
        n_localscheduler.parm('maxprocsmenu').set(-1)

        print("\ntopnet 작업을 통해 wedge 및 렌더 세팅")

        # topnet 작업 > wedge 노드 세팅
        # 몇 가지의 variation 줄지 설정
        n_wedge = n_topnet.createNode("wedge")
        n_wedge.setPosition([0, -1])
        n_wedge.parm("wedgecount").set(4)
        n_wedge.parm("wedgeattributes").set(3)

        # attribute 1 = center_wedge
        n_wedge.parm("name1").set("center_wedge")
        n_wedge.parm("type1").set(1)
        n_wedge.parm("random1").set(1)
        n_wedge.parm("floatrangestart1x").set(-50)
        n_wedge.parm("floatrangestart1y").set(0)
        n_wedge.parm("floatrangestart1z").set(-50)
        n_wedge.parm("floatrangestart1w").set(0)

        n_wedge.parm("floatrangeend1x").set(50)
        n_wedge.parm("floatrangeend1y").set(0)
        n_wedge.parm("floatrangeend1z").set(50)
        n_wedge.parm("floatrangeend1w").set(0)


        # attribute 2 = seed_wedge
        n_wedge.parm("name2").set("seed_wedge")
        n_wedge.parm("type2").set(0)
        n_wedge.parm("random2").set(1)
        n_wedge.parm("floatrange2x").set(0)
        n_wedge.parm("floatrange2y").set(1000)


        # attribute 3 = file_wedge
        n_wedge.parm("name3").set("file_wedge")
        n_wedge.parm("type3").set(0)
        n_wedge.parm("random3").set(0)
        n_wedge.parm("floatrange3x").set(1)
        n_wedge.parm("floatrange3y").set(4)


        # hdaProcessor 1 = make_cirygrid
        # Write file location and Just call callback func

        n_hdaprocessor = n_topnet.createNode("hdaprocessor")
        n_hdaprocessor.setInput(0, n_wedge)
        n_hdaprocessor.setName("make_citygrid")
        n_hdaprocessor.parm("inputfile").set(hda_save_path)
        # hda parm update callback method
        print("call back method")
        n_hdaprocessor.hdaModule().hdaFileChanged({'node':n_hdaprocessor})

        # TODO: PUT relative parms to HDA parameters
        # NEEEEEEEEDDDDDDD to fix
        # n_hdaprocessor.parm("operatortype").set("Sop/USER::streetgrid_maker::1.0")
        n_hdaprocessor.parm("outputfile1").set("$HIP/geo/$OS.`@pdg_name`.`@wedgenum`.0.bgeo.sc")
        n_hdaprocessor.parm("outputtag1").set("file/geo")

        n_hdaprocessor.parm("hdap_sy").setExpression('ch("hdap_sx")')
        # n_hdaprocessor.parm("hdap_blendwidth").setExpression('ch("hdap_sx")')
        n_hdaprocessor.parm("hdap_tx").setExpression("@center_wedge.0")
        n_hdaprocessor.parm("hdap_ty").setExpression("@center_wedge.1")
        n_hdaprocessor.parm("hdap_tz").setExpression("@center_wedge.2")

        # image input은 연결되어있음! 그리드 사이즈는 고정되어있어서 image 사이즈가 커지면 grid (= 도시 사이즈) 도 함께 커질 수 있게 만들어주기
        self.align_node_pos(n_hdaprocessor, n_wedge.position(), 0, -1)

        print("\ntopnet 에서 height / core 변수값 세팅 시작!!")

        # obj > topnet > geometryimport
        n_geometryimport = n_topnet.createNode("geometryimport", "cityblocks")
        # n_geometryimport.setName("cityblocks")
        n_geometryimport.parm("geometrysource").set(0)
        n_geometryimport.parm("pdg_workitemgeneration").set(0)
        n_geometryimport.parm("geometrysource").set(1)
        n_geometryimport.parm("externalpath").set("$HIP/geo/$HIPNAME.$OS.`@pdg_index`.`@wedgenum`.bgeo.sc")
        n_geometryimport.parm("class").set(2)
        n_geometryimport.setInput(0, n_hdaprocessor)
        self.align_node_pos(n_geometryimport, n_hdaprocessor.position(), -2, -1)


        # obj > topnet > attributecreate1 = attr_core
        n_att_create1 = n_topnet.createNode("attributecreate", "attributecreate_core")
        n_att_create1.parm("pdg_workitemgeneration").set(0)
        n_att_create1.parm("floatattribs").set(2)
        n_att_create1.parm("floatname1").set("base_height")
        n_att_create1.parm("floatvalue11").set(10)
        n_att_create1.parm("floatname2").set("height_variation")
        n_att_create1.parm("floatvalue21").setExpression("rand(@pdg_index*@seed_wedge)*15 + @Cd.g*30")
        n_att_create1.setInput(0, n_geometryimport)
        self.align_node_pos(n_att_create1, n_geometryimport.position(), 2, -1)


        # obj > topnet > attributecreate2 = attr_isolate
        n_att_create2 = n_topnet.createNode("attributecreate", "attributecreate_isolate")
        n_att_create2.parm("usecondition").set(1)
        # todo!!!!!!!!!!!!!!!!!!!! ADD create when expresssion

        n_att_create2.parm("floatattribs").set(2)
        n_att_create2.parm("floatname1").set("base_heigiht")
        n_att_create2.parm("floatvalue11").set(50)
        n_att_create2.parm("floatname2").set("height_variation")
        n_att_create2.setInput(0, n_att_create1)
        self.align_node_pos(n_att_create2, n_att_create1.position(), -4, -1)


        n_rop_geo = n_topnet.createNode("ropgeometry")
        n_rop_geo.setName("create_buildings")
        n_rop_geo.parm("usesoppath").set(0)
        n_rop_geo.parm("sopoutput").set("$HIP/geo/$HIPNAME.$OS.`@pdg_index`.`@wedgenum`.bgeo.sc")
        n_rop_geo.parm("pdg_cachemode").set(2)
        n_rop_geo.parm("pdg_cooktype").set(3)
        n_rop_geo.setInput(0, n_att_create2)
        self.align_node_pos(n_rop_geo, n_att_create2.position(), 4, -1)

#########################################################################################################################
        # obj > topnet > ropgeometry = create_building
        # ropgeometry 노드의 경우 Lock 이 걸려있어서 그런지 세부 경로를 타고 가야 했음.
        print("\nbuilding 짓기 시작!!")
        n_rop_in = hou.node(n_rop_geo.path()+'/s/s')
        n_out = hou.node('/obj/topnet1/create_buildings/s/s/output1')
        n_out.setInput(0, None)

        n_file = hou.node('/obj/topnet1/create_buildings/s/s/incoming')
        n_file.parm("file").set("`@pdg_input`")
        n_file.setTemplateFlag(False)
        self.align_node_pos(n_out, n_file.position(), 0, -10)


        n_extrude1 = n_rop_in.createNode("polyextrude::2.0")
        n_extrude1.setName("block_offset")
        n_extrude1.parm("outputfront").set(1)
        n_extrude1.parm("outputback").set(0)
        n_extrude1.parm("outputside").set(0)
        n_extrude1.setInput(0, n_file)
        self.align_node_pos(n_extrude1, n_file.position(), 0, -1)

        n_fuse = n_rop_in.createNode("fuse")
        n_fuse.parm("tol3d").set(0.2)
        n_fuse.setInput(0, n_extrude1)
        self.align_node_pos(n_fuse, n_extrude1.position(), 0, -1)

        n_extrude2 = n_rop_in.createNode("polyextrude::2.0", "building_height")
        n_extrude2.parm("dist").setExpression("@base_height+@height_variation")
        n_extrude2.parm("divs").setExpression('ch("dist")/2')
        n_extrude2.parm("outputfrontgrp").set(1)
        n_extrude2.parm("outputsidegrp").set(1)
        n_extrude2.parm("frontgrp").set("building_top")
        n_extrude2.parm("sidegrp").set("building_side")
        n_extrude2.setInput(0, n_fuse)
        self.align_node_pos(n_extrude2, n_fuse.position(), 0, -1)

        n_extrude3 = n_rop_in.createNode("polyextrude::2.0", "window_frames")
        n_extrude3.parm("inset").set(0.05)
        n_extrude3.parm("group").set("building_side")
        n_extrude3.parm("splittype").set(0)
        n_extrude3.parm("outputfront").set(1)
        n_extrude3.parm("outputback").set(0)
        n_extrude3.parm("outputside").set(1)
        n_extrude3.parm("outputfrontgrp").set(1)
        n_extrude3.parm("frontgrp").set("window_out")
        n_extrude3.setInput(0, n_extrude2)
        self.align_node_pos(n_extrude3, n_extrude2.position(), 0, -1)

        n_extrude4 = n_rop_in.createNode("polyextrude::2.0", "window")
        n_extrude4.parm("dist").set(-0.05)
        n_extrude4.parm("group").set("window_out")
        n_extrude4.setInput(0, n_extrude3)
        self.align_node_pos(n_extrude4, n_extrude3.position(), 0, -1)

        n_extrude5 = n_rop_in.createNode("polyextrude::2.0", "extend_roof")
        n_extrude5.parm("group").set("building_top")
        n_extrude5.parm("dist").set(0.5)
        n_extrude5.setInput(0,n_extrude4)
        self.align_node_pos(n_extrude5, n_extrude4.position(), 0, -1)

        n_extrude6 = n_rop_in.createNode("polyextrude::2.0")
        n_extrude6.setName("roof_edge")
        n_extrude6.parm("group").set("building_top")
        n_extrude6.parm("inset").set(0.3)
        n_extrude6.parm("outputfront").set(1)
        n_extrude6.parm("outputback").set(0)
        n_extrude6.parm("outputside").set(1)
        n_extrude6.parm("outputfrontgrp").set(1)
        n_extrude6.parm("frontgrp").set("roof_out")
        n_extrude6.setInput(0, n_extrude5)
        self.align_node_pos(n_extrude6, n_extrude5.position(), 0, -1)

        n_extrude7 = n_rop_in.createNode("polyextrude::2.0", "roof_edge_in")
        n_extrude7.parm("group").set("roof_out")
        n_extrude7.parm("dist").set(-0.25)
        n_extrude7.setInput(0, n_extrude6)
        self.align_node_pos(n_extrude7, n_extrude6.position(), 0, -1)

        n_color = n_rop_in.createNode("color")
        n_color.parm("group").set("window_out")
        n_color.parm("colorr").set(0)
        n_color.parm("colorg").set(0)
        n_color.parm("colorb").set(0)
        n_color.setInput(0, n_extrude7)
        self.align_node_pos(n_color, n_extrude7.position(), 0, -1)

        n_out.setInput(0, n_color)
        n_out.setDisplayFlag(True)

##########################################################################################################################
        # obj > topnet > partitionbyatrribute
        print("\nwedge 및 street 만들기")
        n_part_att = n_topnet.createNode("partitionbyattribute")
        n_part_att.parm("attributes").set(1)
        n_part_att.parm("name1").set("wedgenum")
        n_part_att.setInput(0, n_rop_geo)
        self.align_node_pos(n_part_att, n_rop_geo.position(), -4, -1)

        # obj > topnet > geometryimport
        n_rop_geo2 = n_topnet.createNode("geometryimport", "building_merge")
        n_rop_geo2.parm("mergeinput").set(1)
        n_rop_geo2.parm("externalpath").set("$HIP/geo/$HIPNAME.$OS.`@pdg_index`.`@wedgenum`.bgeo.sc")
        n_rop_geo2.setInput(0, n_part_att)
        self.align_node_pos(n_rop_geo2, n_part_att.position(), 4, -1)

        # obj > topnet
        n_rop_import2 = n_topnet.createNode("ropgeometry", "build_streets")
        n_rop_import2.parm("usesoppath").set(0)
        n_rop_import2.parm("sopoutput").set("$HIP/geo/$HIPNAME.$OS.`@wedgenum`.bgeo.sc1")
        n_rop_import2.parm("pdg_cachemode").set(2)
        n_rop_import2.parm("pdg_cooktype").set(3)
        n_rop_import2.setInput(0, n_hdaprocessor)
        self.align_node_pos(n_rop_import2, n_geometryimport.position(), 4, 0)


        # obj > topnet > ropgeometryimport
        n_rop2_in = hou.node(n_rop_import2.path()+'/s/s')
        n_file2 = hou.node('/obj/topnet1/build_streets/s/s/incoming')
        n_out2 = hou.node('/obj/topnet1/build_streets/s/s/output1')
        n_out2.setInput(0, None)
        self.align_node_pos(n_out2, n_file2.position(), 0, -7)

        n2_extrude1 = n_rop2_in.createNode("polyextrude::2.0")
        n2_extrude1.parm("dist").set(-0.05)
        n2_extrude1.parm("outputfront").set(0)
        n2_extrude1.parm("outputback").set(1)
        n2_extrude1.parm("outputside").set(1)
        n2_extrude1.setInput(0, n_file2)
        self.align_node_pos(n2_extrude1, n_file2.position(), 0, -10)

        n2_reverse = n_rop2_in.createNode("reverse")
        n2_reverse.setInput(0, n2_extrude1)
        self.align_node_pos(n2_reverse, n2_extrude1.position(), 0, -1)

        n2_color = n_rop2_in.createNode("color")
        n2_color.setInput(0, n2_reverse)
        self.align_node_pos(n2_color, n2_reverse.position(), 0, -1)

        n2_merge = n_rop2_in.createNode("merge")
        n2_merge.setInput(0, n2_color)
        self.align_node_pos(n2_merge, n2_color.position(), 0, -1)

        n2_box = n_rop2_in.createNode("box")
        n2_box.parm("type").set(1)
        n2_box.parm("divrate1").set(2)
        n2_box.parm("divrate2").set(2)
        n2_box.parm("divrate3").set(2)
        n2_box.setInput(0, n2_extrude1)
        self.align_node_pos(n2_box, n2_extrude1.position(), 3, -1)

        n2_blast = n_rop2_in.createNode("blast")
        n2_blast.parm("group").set("2")
        n2_blast.parm("negate").set(1)
        n2_blast.setInput(0, n2_box)
        self.align_node_pos(n2_blast, n2_box.position(), 0, -1)


        n2_transform = n_rop2_in.createNode("xform")
        n2_transform.parm("ty").set(-0.05)
        n2_transform.parm("sx").set(1.05)
        n2_transform.parm("sy").set(1)
        n2_transform.parm("sz").set(1.05)
        n2_transform.setInput(0, n2_blast)
        self.align_node_pos(n2_transform, n2_blast.position(), 0, -1)


        n2_color2 = n_rop2_in.createNode("color")
        n2_color2.parm("colorr").set(0.33)
        n2_color2.parm("colorg").set(0.33)
        n2_color2.parm("colorb").set(0.33)
        n2_color2.setInput(0, n2_transform)
        self.align_node_pos(n2_color2, n2_transform.position(), 0, -1)

        n2_merge.setInput(1, n2_color2)
        n_out2.setInput(0, n2_merge)
        self.align_node_pos(n2_merge, n2_color.position(), 0, -3)

##########################################################################################
        # obj > topnet > patitionbyindex
        n_partition_idx = n_topnet.createNode("partitionbyindex")
        n_partition_idx.setInput(0, n_rop_geo2)
        n_partition_idx.setInput(1, n_rop_import2)
        self.align_node_pos(n_partition_idx, n_rop_geo2.position(), 0, -1)

###########################################################################################################
        # n_work_viewer2 노드 안에 file 노드 생성 후 값 세팅
        file_node = n_work_viewer2.createNode("file")
        file_node.parm("file").set("`@pdg_output.1`")

#####################################################################
        # null 노드를 통해 turntable 만들어주기
        # 돌아가는 속도는 f 단위로 곱해지는 값을 올려주면 됨.
        print("\n턴테이블 위한 컨트롤러 null 노드 제작")
        n_ctrl = obj.createNode("null", "_ctrl")
        turn_speed = 6
        n_ctrl.parm("ry").setExpression(f"($F-1000) * {turn_speed}")
        n_ctrl_ry = n_ctrl.parm("ry")
        n_render_viewer1.parm("ry").setFromParm(n_ctrl_ry)
        n_render_viewer2.parm("ry").setFromParm(n_ctrl_ry)
        n_ctrl.setDisplayFlag(False)
        self.align_node_pos(n_ctrl, n_work_viewer1.position(), -4, 0)

        #####################################################################
        # display mode on 해주기
        print("\nTopnet의 마지막 n_partition_idx 노드 output켬")
        n_partition_idx.setDisplayFlag(True)
        n_topnet.cookAllOutputWorkItems(True)


        print("cook 해주고 work 켜주면 사용자가 건물 확인할 수 있음!")
        print("근데 지금은 hda 뭔가 이상하게 생성되어서 가장 큰 문제는 grid 이미지와 연결이 안되는 것!! 일단 절댓값으로 넣고 진행")
        n_street_grid.setDisplayFlag(False)
        n_work_viewer1.setDisplayFlag(True)
        n_work_viewer2.setDisplayFlag(True)
        n_render_viewer1.setDisplayFlag(False)
        n_render_viewer2.setDisplayFlag(False)

        self.save_hip(saved_path, 'overview')







# when people wanna watch viewport -> topnet 에서 partitionby index 를 ouput으로 두고 recook 한 후 work viewer 로 보기


if __name__ == '__main__':
    city = GrayScaleCity('seoul')
    city.set_hipfile()
    city.create_city()
    city.render_seq()


