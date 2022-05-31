# -*- coding=utf-8 -*-

__version__ = "0.0.4"

__doc__ = \
"""
// script by MineClever @ LLStudio for project ZHJ
// This Script was designed to translate Engine Camera into AfterEffect Camera in purpose

// first is target, second is reference source ,others are attachments
// Matrix is most effective method transforming all

// should work @ maya version >= 2016

// HOW TO USE ?
:::::::::::::::

1.select Target Object
2.select Referenced Object
3.(option) select Objects following Referenced one
4.run script

:::::::::::::::

... ... ... ... ... ... ... ... ,,----~~”'¯¯¯¯¯¯”'~~
... ... ... ... ... ...,,-~”¯::::::::::::::::::::::::::::::::::¯”'~
... ... ... ... ..,,~”::::::::::::::::::::::::::::::::::::::::::::::::::::”~
... ... ... ..,,-“:::::::::::::::/::::::/::::::::::::::::\::::::::::::\:::::::::\
... ... ...,-“:::::,-“:::/:::::/::::::/:|::::::::::::::::\::::::::::::\:::::::::\
... ... .,-“:::::::/:::::|:::::|:::::::|:|:::::::|:::::::\\:::::::::::|:|:::::\::\
... ... /::::::/:::|::::::|:::::|::|::::\:\:::::/\::::/:::||:::::::::|:/::::::|:::|
... .../::::::|:::::\::::::\::::\::\::::/\:\,::/::\::/::::|:|:::::::/\/::::::/::::|
... ../::::::/::::::'\::::::\-,:::\/\::/: :\-,”/ : :\/:\:::/: |:::::/::/::::::|::::/
... ./::::::|:::::::::\::::::\|::/: \/: : : \/: : : : : \,/: \/::_/\//:\:::::/:::/
... /::::::/::/:::::::|::/,__/:/: :__/ . .: : : : : : :\__. \/: \:::::/::/:::/
... |:::|::::::::::::/::/::::/;/ ;/ ,. .,\: : : : : : : / ,._., \ /::::::|::/:|
...|:::/:::/::::::::/::/|:::|.\: |.|❤||; : : : : : :|.|.❤||;|::|:::\/:/::/
...|::|:::|::::::::/:::\|:::'\,|: \."'" /: : : : : : : :'\." '"/ : \: |:::|::\
...|::|:::|:::::::/:::::|::::|/: : “¯': : : : : : : : : :"¯'' : : :\ : :/::::'\
...|::|:::|::::::/:::::/:::::'\: : : : : : : : : : : : : : :': : : : :| :/::::::|
... \:|:::|:::::|::::::|::::::|,: : : : : : :~,___,~: : : : : :,-“:::::::|::|
... .'\|::|:::::|::::::||::::::\'~,: : : : : : '~--~': : : : ,,~”\:::::::::|:/
... ...'\:|:::::|::::::/.|::::::|: : “~,: : : : : : : : ,,-~,”::::::'\::::::::/
... ... .\\:::::|”~,/-,|:::::::|: : : : ¯”~,-,,,-~”:::,,-'\::::::::\-,,_::|
... ... ..',\,::|~--'-~\:::::::|: : : : : : |::|,,-~”¯___\::::::::\... .'|
... ..,~”': : \|: : : : : \::::::|: : : : : : |¯”'~~”~,”,: : \:::::::|... /
..,-“: : : : : :|: : : : : :\::::::|: : : : : : \: : : : : : “~'-,:\::::::|\,/
..|: : : : : : : |: : : : : : |::::|,\,: : : : : : : : : : : : : :”-,-\::::|: \
..| : : : : : : : : : : : : : |::::|:'-,\: : : : : : : : : : : : : : :”-'\,|: :|
...\ : : : : : : : : : :'\: : :\:::|: : '\'\: : : : :~,,: : : : : : : : : “~-
...| : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :”-'\,,
...\: : : : : : : : : : :'\: : : : : : : : : : : : : :~,,: : : : : : : : : “~-.,_
....\ : : : : : : : : : : :\: /: : : : : : : : : : : : : : : “,: : : : : : : : : : :"~,_
... .\: : : : : : : : : : :\|: : : : : : : : :_._ : : : : : : \: : : : : : : : : : : : :”- .
... ...\: : : : : : : : : : \: : : : : : : : ( O ) : : : : : : \: : : : : : : : : : : : : : '\._
... ... .\ : : : : : : : : : '\': : : : : : : :"*": : : : : : : :|: : : : : : : : : : : : : : : |0)
... ... ...\ : : : : : : : : : '\: : : : : : : : : : : : : : : :/: : : : : : : : : : : : : : : /
... ... .....\ : : : : : : : : : \: : : : : : : : : : : : : ,-“: : : : : : : : : : : : : : : :/
... ... ... ...\ : : : : : : : : : \: : : : : : : : : _=" : : : : : ',_.: : : : : : : :,-“ '
... ... ... ... \,: : : : : : : : : \: :"”'~---~”" : : : : : : : : : : : : = :"”~~ '
... ... ... ... ..'\,: : : : : : : : : \: : : : : : : : : : : : : : : : : : : '\: : : \ :
... ... ... ... ... .\, : : : : : : : : '\: : : : : : : : : : : : : : : : : : :|: : ::\:
... ... ... ... ... ...\,: : : : : : : : : \: : : : : : : : : : : : : : : : : :I : : :|
... ... ... ... ... ... ..\ : : : : : : : : \: : : : : : : : : : : : : : : : :|: : : :|
... ... ... ... ... ... ...\\,: : : : : : : , \: : : : : : : : : : : : : : : I: : : : |
... ... ... ... ... ... ... .\\ : : : : : : : :'\ : : : : : : : : : : : : : :|: : : : |
... ... ... ... ... ... ... ./:\: : : : : : : : :'\, : : : : : : : : : : : : |: : : ::|
... ... ... ... ... ... .../: : : '\: : : : : : : : : :'\,: : : : : : : : : :|: : : ::|
... ... ... ... ... ... ../: : : : :\: : : : : : : : : : ,\ : : : : : : : : :|: : : ::|
... ... ... ... ... ... ,/: : : : : : :\: : : : : : : : : : '\,: : : : : : : |: : : ::|
... ... ... ... ... ..,-“: : : : : : : :“-,: : : : : : : : : : \: : : : : : I: : : ::|
... ... ... ... ... ,/ : : : : : : : : : :”-, : : : : : : : : : :\: : : : : I: : : :/
... ... ... ... ..,/ : : : : : : : : : : : : :”-, : : : : : : : : :'\: : : :I : : : /
... ... ... ... ,/ : : : : : : : : : : : : : : : “-,: : : : : : : : :'\: : :I : : : /
... ... ... .../: : : : : : : : : : : : : : : : : : “-,: : : : : : : : '\: :I : : : /
... ... ... ../: : : : : : : : : : : : : : : : : : : : :“-,: : : : : : : \,:I : : :/
... ... ... ,/: : : : : : : : : : : : : : : : : : : : : : :“-,: : : : : : :\: : : :/
... ... .../-,-,”,,-,~-,,_: : : : : : : : : : : : : : : : : “-,: : : : : :'\: : /
... ... ..|',/,/:||:\,\: : ::: ""~,,~~---,,,_: : : : : : : : : :'\: : : : : ,:\ :
... ... ..|: :”: ||: :”: : : : : : :”-,........ ¯¯”''~~~-----~|\: : : : : : \ : '
... ... ..|: : : ||: : : : : : : : : : :”-,..........................|: : : : : : :\
... ... ..| : : : : : : : : : : : : : : : :”-,.......................\: : : : : : : :\
... ... ..| : : : : : : : : : : : : : : : :”-,\....................,-“\: : : : : : : :':\
... ... ..| : : : : : : : : : : : : : : : : : :”-\...............,/: : :\:

"""

import sys
import re
import math
import maya.cmds as cmds
import maya.api.OpenMaya as api # api 2.0
import maya.mel as mel
# dont use pymel , maya 2022 have some problem with it

class MayaMatrixTools (object):
    """
        the first in sel_list is [target];
        the second in sel_list is [reference];

        setSelectList(list) : set current process list;
        ret matrix makeEmptyGPMatrix(void) : get the origin point matrix of current workspace
        ret matrix getWorldMatrix(string) : get a world matrix by name;
        ret matrix getInvWorldMatrix(string) : get a Inverse world matrix by name;
    """

    def __init__ (self):
        self.empty_matrix = self.makeEmptyGPMatrix()
        self.sel_list = []
        self.length_of_sel_list = 0

    def setSelectList(self, input_list):
        self.sel_list = input_list
        self.length_of_sel_list = len(self.sel_list)

    def getWorldMatrix (self, name):
        matrix = api.MMatrix(cmds.getAttr("{}.worldMatrix".format(name)))
        return matrix

    def getInvWorldMatrix (self, name):
        matrix = api.MMatrix(cmds.getAttr("{}.worldInverseMatrix".format(name)))
        return matrix

    def computeOffsetMatrix(self):
        warning = u"Select 2 objects or more\n"
        if self.length_of_sel_list < 2 : sys.stderr.write(warning); raise (Exception(warning))
        matrix_product = self.getInvWorldMatrix(self.sel_list[1]) * self.getWorldMatrix(self.sel_list[0])
        return matrix_product

    def transOffsetMethod(self):
        """virtual method"""
        raise (NotImplementedError(u"You need an implementation of {}".format(sys._getframe().f_code.co_name)))

    def makeEmptyGPMatrix(self):
        # make a empty origin transform node, to get the matrix of current software origin
        # empty_group = cmds.group( empty=True, world=True, name="EMPETY_ORIGIN_POINT_01" )
        # empty_matrix = self.getWorldMatrix(empty_group)
        # cmds.delete(empty_group)
        """Create a empty matrix"""
        _empty_matrix =[1.0, 0.0, 0.0, 0.0,
                        0.0, 1.0, 0.0, 0.0,
                        0.0, 0.0, 1.0, 0.0,
                        0.0, 0.0, 0.0, 1.0]
        empty_matrix = api.MMatrix(_empty_matrix)
        return empty_matrix

    def removeOffsetMatrix(self):
        warning = u"Select One object at least\n"
        if self.length_of_sel_list < 1 : sys.stderr.write(warning); raise (Exception(warning))
        for i in range(self.length_of_sel_list):
            cmds.setAttr("{}.offsetParentMatrix".format(self.sel_list[i]), self.empty_matrix ,type='matrix')

class MayaMatrixToolsGroupMode (MayaMatrixTools) :
    def __init__(self):
        # MayaMatrixTools.__init__(self)
        super(MayaMatrixToolsGroupMode,self).__init__()

    def transOffsetMethod(self):
        # override
        """method make How to trans our referenced object to target object"""

        self.removeOffsetMatrix()
        matrix_product = self.computeOffsetMatrix()

        # use cmds.ls fix the bug of object input
        offset_group = cmds.ls(cmds.group(empty=True, world=True, name = "{}_OffsetGP_01".format(self.sel_list[1])))[0]

        for i in range(1,self.length_of_sel_list):
            # if i < 1: continue
            cmds.parent(self.sel_list[i], offset_group)
        # use xform method to use matrix easily
        cmds.xform(offset_group , m=matrix_product)

class MayaMatrixToolsMatrixMode (MayaMatrixTools):
    def __init__(self):
        # MayaMatrixTools.__init__(self)
        super(MayaMatrixToolsMatrixMode,self).__init__()

    def transOffsetMethod(self):
        # override
        """method make How to trans our referenced object to target object"""

        self.removeOffsetMatrix()
        matrix_product = self.computeOffsetMatrix()
        # use offsetParentMatrix
        for i in range(self.length_of_sel_list):
            if (i < 1): continue
            cmds.setAttr("{}.offsetParentMatrix".format(self.sel_list[i]), matrix_product ,type='matrix')

class MayaMatrixToolsModeFactory ():
    """use factory to product our class"""
    def __init__(self,class_override):
        for cls in MayaMatrixTools.__subclasses__() :
            if cls.__name__ == class_override :
                self.methodClass = cls()
                break
        else :
            raise (NotImplementedError("unknown class name"))

class CamToolBase (MayaMatrixTools):
    """
    derived from Class MayaMatrixTools;Brige method by factory
    """
    def __init__(self,class_override):
        self.global_time_slider = mel.eval('$tempGlobalTimeSlider=$gPlayBackSlider')

        # a factory
        self.methodClass = MayaMatrixToolsModeFactory(class_override).methodClass

        self.cam_transform = None
        self.cam_shape = None
        self.rebuild_cam_transform = None
        self.rebuild_cam_shape = None
        self.rebuild_cam_matrix = None

    def transOffsetMethod (self):
        self.methodClass.transOffsetMethod()

    def setSelectList(self,input_list):
        self.methodClass.setSelectList(input_list)
        self.__dict__.update(self.methodClass.__dict__)

    def buildLocatorByJointName (self,matched_name_rule=r"locator_root$"):
        """
            find all joint in sel_list

            [loop]

            if some joint named "locator_root";

            will create a locator naming "null_{the name of inputted one which in sel_list}_#index#"
        """
        match = matched_name_rule
        for current in self.sel_list :
            joints = cmds.listRelatives(current, allDescendents=1, type="joint",fullPath=1)
            if (joints):
                for joint in joints :
                    if (re.search(match , joint, re.I)):
                        joint_parent_name= cmds.listRelatives(joint, parent=1,fullPath=1)[0]
                        joint_location_matrix = self.getWorldMatrix(joint_parent_name)
                        joint_locator = cmds.ls(cmds.spaceLocator(name="null_{}_01".format(current), position=(0,0,0)))[0]
                        cmds.xform(joint_locator, m=joint_location_matrix)

    def connectAttrByName(self,input_from,input_to,attr_name):
        """
            wrap cmds.connectAttr();

            will connect the [attr_name] from [input_from] to [input_to]
        """
        cmds.connectAttr (  "{}.{}".format(input_from,attr_name),
                            "{}.{}".format(input_to,attr_name),
                            force=True)


    def createBaseCameraTools (self, cam_shape):
        """
            build copy camera then move to the location of current camera

            then you can use :
                current camera:
                    self.cam_shape
                    self.cam_transform
                rebuilt camera:
                    self.rebuild_cam_transform
                    self.rebuild_cam_shape
                    self.rebuild_cam_matrix : same as the matrix of current
        """
        self.cam_shape = cam_shape
        self.cam_transform = cmds.ls(cmds.listRelatives(cam_shape, parent=1,fullPath=1)[0])[0]
        rebuild_cam = cmds.camera (n="Cam_{}_Baked_".format(self.cam_transform))
        self.rebuild_cam_transform = rebuild_cam[0]
        self.rebuild_cam_shape = rebuild_cam[1]
        self.rebuild_cam_matrix = self.getWorldMatrix(self.cam_transform)
        cmds.xform(self.rebuild_cam_transform, m=self.rebuild_cam_matrix)


    def copyCameraAttrsByList (self,input_from,input_to,attrs_list):
        attr_connectable_list = cmds.listAttr(input_to,connectable=1)
        for attr_name in attrs_list :
            if attr_name in attr_connectable_list :
                self.connectAttrByName(input_from,input_to,attr_name)

    # interface
    def copyCameraAttrs (self,input_from,input_to):
        """virtual method"""
        raise (NotImplementedError(u"You need an implementation of {}".format(sys._getframe().f_code.co_name)))

    # interface
    def rebuildCameraByCameraMainProcess (self, cam_shape, use_target_filmsize = True):
        """virtual method"""
        raise (NotImplementedError(u"You need an implementation of {}".format(sys._getframe().f_code.co_name)))

    def rebuildCameraByCamera (self, use_target_filmsize=True):
        """Automate create and bake copy of ue camera by free camera"""

        # filter cameras
        for current in self.sel_list :
            if current == self.sel_list[0] : continue # skip target
            cameras = cmds.listRelatives(current, allDescendents=1, type="camera")
            # loop
            if (cameras) :
                for cam_shape in cameras :
                    ls_cam_shape = cmds.ls(cam_shape)[0] # safe method
                    self.rebuildCameraByCameraMainProcess(ls_cam_shape,use_target_filmsize)

    def getObjectKeyframeTimeRange (self, object_name):
        """get interage time range from inputted object"""
        key_time_list = cmds.keyframe(object_name, q=1, timeChange=1)
        key_start_time = math.floor(min(key_time_list))
        key_end_time = math.ceil(max(key_time_list))
        return {"start":key_start_time,"end":key_end_time}

class TransMatrixFreeCam (CamToolBase):

    """Rebuild the camera infomation as a free camera"""
    def __init__(self,class_override):
        CamToolBase.__init__(self,class_override)

    # -- implement
    def copyCameraAttrs (self,input_from,input_to):
        """ Sync beteew two cameras  """
        attrs_list =["nearClipPlane","farClipPlane","focusRegionScale","locatorScale",
                    "clippingPlanes","orthographicWidth","orthographic",
                    "shutterAngle","focalLength","bestFitClippingPlanes",
                    "fStop","cameraScale","lensSqueezeRatio","cameraAperture",
                    "verticalFilmAperture","horizontalFilmAperture"]

        self.copyCameraAttrsByList(input_from,input_to,attrs_list)

        # free cam only
        for attr in ["centerOfInterest","horizontalFilmOffset","verticalFilmOffset"] :
            self.connectAttrByName(self.cam_shape, input_to,attr)

    # -- implement
    def rebuildCameraByCameraMainProcess (self, current_cam_shape, use_target_filmsize=True):

        self.createBaseCameraTools(current_cam_shape)

        # connect attributes
        attr_source =   (cmds.listRelatives(self.sel_list[0], children=1, type="camera",path=1)[0]) \
                        if (use_target_filmsize) else self.cam_shape
        self.copyCameraAttrs(attr_source , self.rebuild_cam_shape)

        # get interage time range from current camera
        key_time_dict = self.getObjectKeyframeTimeRange(self.cam_transform)

        # fix timeline
        cmds.timeControl(self.global_time_slider, edit=True, snap=True)
        cmds.playbackOptions(min=key_time_dict["start"], max=key_time_dict["end"],
                                ast=key_time_dict["start"], aet=key_time_dict["end"])

        # make parent constrain
        rebuild_cam_constraint_name = cmds.parentConstraint(self.cam_transform, self.rebuild_cam_transform,maintainOffset=1)[0]

        # bake copy camera
        cmds.bakeResults(self.rebuild_cam_transform,
                        time=(key_time_dict["start"],key_time_dict["end"]),
                        removeBakedAttributeFromLayer=1,shape=1,sampleBy=1.0,
                        removeBakedAnimFromLayer=1,disableImplicitControl=1)
        # delete constraint
        cmds.delete(rebuild_cam_constraint_name)

class TransMatrixAimCam (CamToolBase):
    """Rebuild the camera information as a aim camera"""
    def __init__(self,class_override):
        CamToolBase.__init__(self,class_override)

    # implement
    def copyCameraAttrs (self,input_from,input_to):
        """ Sync between two cameras  """
        attrs_list =["nearClipPlane","farClipPlane","focusRegionScale",
                    "clippingPlanes","orthographicWidth","orthographic",
                    "shutterAngle","bestFitClippingPlanes","locatorScale",
                    "fStop","cameraScale","lensSqueezeRatio","cameraAperture",
                    "verticalFilmAperture","horizontalFilmAperture"]

        self.copyCameraAttrsByList(input_from,input_to,attrs_list)

    # implement
    def rebuildCameraByCameraMainProcess (self, current_cam_shape, use_target_filmsize=True):

        self.createBaseCameraTools(current_cam_shape)
        # add two locator
        mel.eval("cameraMakeNode 2 \"{}\";".format(self.rebuild_cam_transform)) # magic method , Aim+Up == 3
        aim_locator = cmds.ls(u"{}_aim".format(self.rebuild_cam_transform))[0]
        # aim_locator = cmds.rename(cmds.ls(aim_locator)[0], u"{}FBXASC046Target".format(rebuild_cam_transfrom))
        aim_tool_locator = cmds.spaceLocator(name="AimTool_{}_01".format(self.rebuild_cam_transform), position=(0,0,0))[0]
        cmds.xform(aim_tool_locator, m=self.rebuild_cam_matrix) # move to camera

        # use node subtract
        math_node = cmds.shadingNode("floatMath", asUtility=1)
        cmds.connectAttr(self.rebuild_cam_transform + ".translateZ",math_node + ".floatA",force=1)
        cmds.setAttr(math_node + ".operation",1) # 0=add,1=sub
        cmds.connectAttr(self.cam_shape + ".centerOfInterest",math_node + ".floatB",force=1)
        cmds.connectAttr(math_node + ".outFloat", aim_tool_locator + ".translateZ",force=1)


        # get interage time range from current camera
        key_time_dict = self.getObjectKeyframeTimeRange(self.cam_transform)

        # fix timeline
        cmds.timeControl(self.global_time_slider, edit=True, snap=True)
        cmds.playbackOptions(   min=key_time_dict["start"], max=key_time_dict["end"],
                                ast=key_time_dict["start"], aet=key_time_dict["end"])

        # make parent constrain
        rebuild_cam_constraint_name = cmds.parentConstraint(self.cam_transform, self.rebuild_cam_transform,maintainOffset=1)[0]
        aim_tool_locator_constraint_name = cmds.parentConstraint(self.cam_transform, aim_tool_locator,maintainOffset=1)[0]
        cam_aim_locator_constraint_name = cmds.pointConstraint(aim_tool_locator, aim_locator,maintainOffset=0)[0]

        # connect attributes
        attr_source =   (cmds.listRelatives(self.sel_list[0], children=1, type="camera", path=1)[0]) \
                        if (use_target_filmsize) else self.cam_shape
        self.copyCameraAttrs(attr_source , self.rebuild_cam_shape)

        # bake copy camera
        for job in (self.rebuild_cam_transform, aim_tool_locator,aim_locator) :

            """use maya capsuled method"""
            cmds.bakeResults(   job, time=(key_time_dict["start"], key_time_dict["end"]),
                                at=["tx","ty","tz"],
                                removeBakedAttributeFromLayer=1,shape=1,sampleBy=1.0,
                                removeBakedAnimFromLayer=1,disableImplicitControl=1)
        # delete constraint
        _del_tuple = (  rebuild_cam_constraint_name,
                        aim_tool_locator_constraint_name,
                        cam_aim_locator_constraint_name,
                        aim_tool_locator,math_node   )
        cmds.delete(_del_tuple)

class TransMatrixCamWarper ():
    def __init__(self,rebuild_cam_mode,class_override):
        for cls in CamToolBase.__subclasses__() :
            if cls.__name__ == rebuild_cam_mode:
                self.instance_class = cls(class_override)
                break
        else :
            raise(NotImplementedError("Unknown class name"))

class EnumMatrixToolModes ():
    class TransMode ():
        MatrixMode = "MayaMatrixToolsMatrixMode"
        GroupMode = "MayaMatrixToolsGroupMode"
    class CamMode ():
        AimCam = "TransMatrixAimCam"
        FreeCam = "TransMatrixFreeCam"

class MatrixToolModesManager ():
    def __init__(self,trans_mode=EnumMatrixToolModes.TransMode.MatrixMode,
                 rebuild_cam_mode=EnumMatrixToolModes.CamMode.FreeCam,
                 input_list=["top","persp"]
                 ):

        self.__rebuild_cam_mode =  rebuild_cam_mode
        self.__rebuild_locator = True
        self.__matrix_trans_mode = trans_mode
        self.__sel_list = []
        self.__use_target_filmsize = True
        self.rebuild_locator_joint_search_rule = r"locator_root$"

        self.sel_list = input_list

    @property
    def matrix_trans_mode (self):
        return self.__matrix_trans_mode

    @matrix_trans_mode.setter
    def matrix_trans_mode (self, value):
        if value in [cls.__name__ for cls in MayaMatrixTools.__subclasses__()] :
            self.__matrix_trans_mode = value
        else :
            raise(Exception("unknown class name"))

    @property
    def rebuild_cam_mode (self):
        return self.__rebuild_cam_mode

    @rebuild_cam_mode.setter
    def rebuild_cam_mode(self, value):
        if value in [cls.__name__ for cls in CamToolBase.__subclasses__()] :
            self.__rebuild_cam_mode = value

    @property
    def rebuild_locator(self):
        return self.__rebuild_locator

    @rebuild_locator.setter
    def rebuild_locator (self,value):
        if value in (0,1,True,False) :
            self.__rebuild_locator = value
        else :
            sys.stdout.write("You can only input 0|1|True|False for locator rebuilder,Using default instead\n")

    @property
    def sel_list (self):
        if len(self.__sel_list) > 0 :
            return self.__sel_list

    @sel_list.setter
    def sel_list (self, value):
        if isinstance(value, list) and len(value) > 2 :
            self.__sel_list = value
        else :
            raise(Exception("You have to select two object"))

    @property
    def use_target_filmsize (self):
        """if use target filmsize"""
        return self.__use_target_filmsize

    @use_target_filmsize.setter
    def use_target_filmsize (self, value):
        if value in (0,1,True,False):
            self.__use_target_filmsize = value
        else :
            sys.stdout.write("You can only input 0|1|True|False for film size setter,Using default\n")

    @use_target_filmsize.deleter
    def use_target_filmsize (self):
        self.__use_target_filmsize = True

    def run(self):
        matrix_tool = TransMatrixCamWarper(self.rebuild_cam_mode,self.matrix_trans_mode).instance_class
        matrix_tool.setSelectList(self.sel_list)
        matrix_tool.transOffsetMethod()
        if (self.rebuild_locator):
            matrix_tool.buildLocatorByJointName(self.rebuild_locator_joint_search_rule)
        matrix_tool.rebuildCameraByCamera(use_target_filmsize=self.use_target_filmsize)
        matrix_tool.removeOffsetMatrix()
        del (matrix_tool)

class QTUICameraTransTool ():
    """_summary_

    Make UI Here
    """

    def __init__ (self):
        pass

    def loadUI (self):
        pass

    def showMe (self):
        pass

def tempJobs (*args, **kw):
    matrix_tool = MatrixToolModesManager(
                    input_list=cmds.ls(sl=1),
                    rebuild_cam_mode=EnumMatrixToolModes.CamMode.AimCam)
    # using regex to search bone
    matrix_tool.rebuild_locator_joint_search_rule = r"locator_root$"
    matrix_tool.use_target_filmsize = False
    matrix_tool.run()

# easily run script

def runScript (*args, **kw):
    tempJobs(*args, **kw)

def onMayaDroppedPythonFile (*args,**kw):
    """Maya Dropped"""
    runScript (*args,**kw)

if __name__ == "__main__":
    runScript()
