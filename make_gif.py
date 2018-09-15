import imageio,progressbar
from os import listdir
from os.path import isfile, join

def makeGif():
  mypath = 'img'
  bar = progressbar.ProgressBar()
  allImages = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f))]
  allImages.sort()
  images = [imageio.imread(filename) for filename in allImages[::1]]
  imageio.mimsave('movie.gif', bar(images))

if __name__ == '__main__':
  makeGif()
