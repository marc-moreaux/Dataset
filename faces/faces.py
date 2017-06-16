import wget
import tarfile
import os


class Faces(object):
    """docstring for Faces"""
    def __init__(self, arg):
        super(Faces, self).__init__()
        if not os.path.isdir("./lfw/Gisele_Bundchen/"):
            self._download()

    def _download(self):
        url = 'http://vis-www.cs.umass.edu/lfw/lfw.tgz'
        print 'Downloading Action Event Dataset'
        wget.download(url, out='./')

        print 'Unzipping ...'
        tar = tarfile.open("lfw.tgz")
        tar.extractall()
        tar.close()

    def _get_all_paths(self):
        img_paths = [os.path.join(root, f)
                     for root, dirs, files in os.walk("./")
                     for f in files
                     if f[-4:] == '.jpg']
        return img_paths
