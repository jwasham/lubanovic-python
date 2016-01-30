import os

os.mkdir('dir1')
os.mkdir('dir1/subdir1')

with open('dir1/subdir1/somefile', 'wt') as fout:
    fout.write('this was a short-lived file')

os.unlink('dir1/subdir1/somefile')

os.rmdir('dir1/subdir1')
os.rmdir('dir1')
