import sys
from cx_Freeze import setup, Executable 

build_exe_options = {"packages":["os"], "include": ["tkinter", "pytube"], 'include_files': ['youtube.png']}
base = None
if sys.platform == "win32":
      base = "Win32GUI"
      
setup(
      name = "Baixador de Vídeos do YouTube" , 
      version = "0.1" , 
      description = "Baixador de Vídeos do YouTub",
      options = {"buil_exe": build_exe_options},
      executables = [Executable("youtubeDowloader.py", base=base, icon='yt.ico')]) 