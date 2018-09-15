import urllib, progressbar
from time import strftime
from PIL import Image
from make_gif import *

def download_image(year, month, day, hour, minute, second, level):
  # download all image pieces, put them in temp folder
  for x in range(level):
    for y in range(level):
      while True:
        try:
          download_image_block(year, month, day, hour, minute, second, level, x, y)
          break
        except:
          pass
  # stitch together images
  new_im = Image.new('RGB', (550*level, 550*level))
  for x in range(level):
    for y in range(level):
      new_im.paste(Image.open('img/temp/'+str(x)+'_'+str(y)+'.png'), (x*550, y*550))
  new_im.save(strftime("img/%Y%m%d%H%M%S.png", (year, month, day, hour, minute, second, 0, 0, 0)))

def download_image_block(year, month, day, hour, minute, second, level, x, y):
  url_format = 'http://himawari8.nict.go.jp/img/D531106/{}d/{}/{}_{}_{}.png'
  url = url_format.format(level, 550, strftime("%Y/%m/%d/%H%M%S", (year, month, day, hour, minute, second, 0, 0, 0)), x, y)
  filepath = 'img/temp/'+str(x)+'_'+str(y)+'.png'
  urllib.urlretrieve(url, filepath)

def main1():
  download_image(17,2,6,3,00,00,20)

def main2():
  bar = progressbar.ProgressBar()
  daysInMo = [31,28,31,30,31,30,31,31,30,31,30,31]
  days = []
  for d in range(len(daysInMo)):
    for i in range(daysInMo[d]):
      days.append((d+1,i+1))
  for d in bar(days):
    download_image(16,d[0],d[1],3,0,0,4)
  makeGif()

if __name__ == '__main__':
  main2()
