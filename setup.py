import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "shutil", "tkinter", "tkinter.messagebox"], "include_files": ["System32\\Windows.ApplicationModel.Store.dll", "SysWOW64\\Windows.ApplicationModel.Store.dll"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "PermissionsAndFilesReplacement",
    version = "0.1",
    description = "Simple GUI for applying permissions and replacing files",
    options = {"build_exe": build_exe_options},
    executables = [Executable("gui_app.py", base=base)]
)
