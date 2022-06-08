from maya import cmds

def rename():
    selection = cmds.ls(selection =True)

    if len(selection) == 0:
         selection = cmds.ls(dag = True,long = True)

    selection.sort(key=len,reverse = True)

    for obj in selection:
         shortName = obj.split("|")[-1]

         childrens = cmds.listRelatives(obj,children = True, fullPath = True) or []

         if len(childrens) == 1:

             child = childrens[0]

             objType = cmds.objectType(child)

         else:

             objType = cmds.objectType(obj)

         if objType == "mesh":
             suffix = "geo"
         elif objType == "joint":
             suffix = "jnt"
         elif objType == "camera":
             continue
         else:
             suffix = "grp"

        newName = shortName + "_" + suffix
        cmds.rename(obj,newName)