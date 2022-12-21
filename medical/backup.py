import os
import shutil
import datetime


if not os.path.isdir("backup"):
     os.mkdir("backup")

path_1 = os.path.abspath('db.sqlite3')
path_2 = os.path.abspath('backup')

shutil.copy(
    os.path.join('', 'db.sqlite3'),
    os.path.join('backup')
)

date = str(datetime.datetime.now()).replace('.', '-').replace(' ', '-').replace(':', '-')
os.rename(path_2 + '\\db.sqlite3', path_2 + '\\' + date + 'db.sqlite3')
