
import os
import zipfile

root_path = '/tmp/jina/'
demo_name = 'webqa'
workspace = os.path.join(root_path, demo_name)
if not os.path.exists(root_path):
    os.mkdir(root_path)
if not os.path.exists(workspace):
    os.mkdir(workspace)

fz = zipfile.ZipFile(os.path.join(workspace, 'webtext2019_zh.zip'), 'r')

for file in fz.namelist():
    fz.extract(file, workspace)