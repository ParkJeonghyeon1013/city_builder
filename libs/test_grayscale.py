def align_node_pos(node_name, node_pos, add_x, add_y):
    node_name.setPosition((node_pos[0] + add_x, node_pos[1] + add_y))


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
n_work_viewer1.setDisplayFlag(False)
n_work_viewer2.setDisplayFlag(False)
n_render_viewer1.setDisplayFlag(True)
n_render_viewer2.setDisplayFlag(True)

print("\n렌더 세팅 시작", dir_path)

# camera/ light 세팅
# TODO: :::::::::::::::::::: camera 위치 세팅
n_cam = obj.createNode("cam")
n_light1 = obj.createNode("hlight::2.0", "sunlight")
n_light1.parm("light_type").set(8)
n_light1.parm("vm_envangle").set(2)

n_light2 = obj.createNode("envlight", "skylight")
n_light2.parm("skymap_enable").set(1)
n_light2.parm("light_intensity").set(1.3)

# obj > topnet > mantra renderer 추가
n_part_idx = hou.node("/obj/topnet1/partitionbyindex1")
n_mantra = n_topnet.createNode("ropmantra")
n_mantra.setInput(0, n_part_idx)
n_mantra.parm("pdg_cachemode").set(2)
n_mantra.parm("override_camerares").set(1)
n_mantra.parm("vm_picture").set("$HIP/render/$HIPNAME.$OS.`@wedgenum`.png")

# obj > topnet > overlaytext
n_overlaytext = n_topnet.createNode("ropcomposite")
n_overlaytext.setInput(0, n_mantra)
n_overlaytext.parm("copoutput").set("$HIP/render/$HIPNAME.$OS.`@wedgenum`.png")

n_overlaytext_in = hou.node(n_overlaytext.path() + '/c')
n_pdg_result = hou.node('/obj/topnet1/ropcomposite1/c/pdg_result')

n_font = n_overlaytext_in.createNode("font")
n_font.parm("text").set(
    "Map: `@file_wedge`\nCity Core: `@center_wedge.0`, `@center_wedge.2`\nVariation Seed: `@seed_wedge`")
n_font.parm("textsize").set(30)
n_font.setInput(0, n_pdg_result)

n_dropshadow = n_overlaytext_in.createNode("dropshadow")
n_dropshadow.setInput(0, n_font)

n_over = n_overlaytext_in.createNode("over")
n_over.setInput(0, n_dropshadow)
n_over.setInput(1, n_pdg_result)

# obj > topnet > waitforall
n_wait = n_topnet.createNode("waitforall")
n_wait.setInput(0, n_overlaytext)

n_magick = n_topnet.createNode("imagemagick")
n_magick.setInput(0, n_wait)

# todo ::::::::::: file save > topnet cook > render 순으로 진행
# cook 해주고 render 해주기
print("\nrender 전 저장 후 render 시작")
n_magick.setDisplayFlag(True)
n_topnet.dirtyAllTasks(True)
n_topnet.cookAllOutputWorkItems(True)
