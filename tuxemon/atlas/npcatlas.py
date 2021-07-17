# NOTICE THIS IS EXTREMELY BETA CODE AND IS SUBJECT TO CHANGE

# Use pillow direcctly? (Not implemented yet)
USEPIL = False

# Disables rotations
# may need to be turned off
NORT = False

# Mod dir (If you want to change the mod this atlases)
ADIR = "tuxemon"

if(USEPIL == 1):
    from PIL import Image
elif(USEPIL == 0):
    from PyTexturePacker import Packer
import sys



def createatlas(inpcdat):
    if(USEPIL == 1):
        print("Sorry PIL only mode doesn't exist yet")
        return
    elif(USEPIL == 0):
        if(NORT == 0):
            packer = Packer.create(atlas_format="json", bg_color=0x00000000, max_width=512, max_height=512)
            packer.pack("mods/" + ADIR + "/sprites/", "mods/" + ADIR + "/sprites/npc%d.atlas")
            return
        elif(NORT == 1):
            packer = Packer.create(enable_rotated=True, atlas_format="json", bg_color=0x00000000, max_width=512, max_height=512)
            packer.pack("mods/" + ADIR + "/sprites/", "mods/" + ADIR + "/sprites/npc%d.atlas")
            return
def make():
    print("Making Atlas")
    if(USEPIL == 1):
        #TODO put stuff here
        sys.exit
        return

    elif(USEPIL == 0):
        createatlas("")
        return
