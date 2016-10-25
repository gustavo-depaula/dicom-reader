# made by gustavo-depaula
import sys
from cx_Freeze import setup, Executable

setup(
    name = "Project N",
    version = "0.1",
    description = "Primeiro Prototipo",
    executables = [Executable("main.py", base = "Win32GUI")])
Gustavo de Paula:
#     Comecei o protótipo com uma interface gráfica bem simples
#     onde o usuário pode escolher uma pasta para ver o contido
#     e pode selecionar um arquivo DICOM para ler todas as info_
#     rmações possí
