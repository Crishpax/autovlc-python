import os
import vlc
from fileRoute import fileRoute
from folderRoute import folderRoute
from getch import getch
from inputListener import inputListener


mockFolder = r'D:\TARDIS\TV series\The Office US S01-S09 (2005-)\The Office US S02 (360p re-webrip)'


mockObj = folderRoute(mockFolder)
instance = vlc.Instance(["--no-sub-autodetect-file"])
player = instance.media_player_new()
player.set_mrl(mockObj.files[1].path)
player.play()
inputListener(player)
