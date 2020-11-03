__author__ = 'Cuetin' #Tu nombre o el del autor
# Let's start with some default (for me) imports...
import sys
from cx_Freeze import setup, Executable


build_exe_options = {
"include_msvcr": True   #skip error msvcr100.dll missing
}
# Process the includes, excludes and packages first

carpeta = 'Marcianitos'  #nombre de la carpeta donde se instalara el programa

if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', 'C:\Program File\\ ' + carpeta]

includes = ['pygame', 'sys', 'os', 'random', 'pygame.locals'] #librerias que lleva tu proyecto separadas por comas entre comillas
excludes = []
packages = []
path = []
include_files = ['Musica', 'Imagenes'] #carpetas que lleva tu aplicacion separadas por comas entre comillas
include_msvcr = ['networkChanger.exe.manifest']

if sys.platform == 'win32':
    base = 'Win32GUI'
if sys.platform == 'linux' or sys.platform == 'linux2':
    base = None

marcianitos = Executable(
    # what to build
    script = "main.py", #archivo que ejecuta todo el programa
    initScript = None,
    base = base,
    icon = 'Imagenes\Marciano2A.ico', #ruta del icono del programa
    #shortcutName="DHCP",
    #shortcutDir="ProgramMenuFolder"
    )

setup(

    version = "1.0", # version
    description = "Juego retro de nave espacial contra marcianitos.", #pequeña descripcion
    author = "Cuetin", #autor
    name = "Marcianitos", #nombre del programa

    options = {"build_exe": {"includes": includes,
                 "excludes": excludes,
                 "packages": packages,
                 "path": path,
                 "include_files": include_files,
                 "include_msvcr": include_msvcr,

                 }
           },

    executables=[marcianitos]
    )
