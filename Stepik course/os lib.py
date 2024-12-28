import os
import os.path
import shutil

print(os.getcwd())
print(os.listdir())
print("-------------------")
print(os.path.exists("ancestors.py"))
print(os.path.exists("ancertors.py"))
print("-------------------")
print(os.path.isfile("Fibonnaci.py"))
print(os.path.isfile("../Tinkoff"))
print("-------------------")
print(os.path.isdir("../Tinkoff"))
print(os.path.isdir("Fibonnaci.py"))
print("-------------------")
for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)
print("-------------------")
print(os.path.abspath("r and w.py"))
print("-------------------")
os.chdir("../Tinkoff")
print(os.getcwd())
print("-------------------")
shutil.copy("../Stepik course/test1.txt", "../Stepik course/test2.txt")
# shutil.copytree("из какой папки копировать", "в какую") - копирование из одной папки в другую
