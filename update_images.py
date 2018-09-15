import urllib
from time import strftime, mktime, sleep
from PIL import Image
from datetime import datetime, timedelta
from dateutil.tz import tzlocal
import subprocess

def stitchImages(level):
  new_im = Image.new('RGB', (550*level, 550*level))
  for x in range(level):
    for y in range(level):
      try:
        new_im.paste(Image.open('img/temp/'+str(x)+'_'+str(y)+'.png'), (x*550, y*550))
      except:
        pass
  new_im.save("current.png")
  sleep(5)

def main():
  stitchImages(20)

if __name__ == '__main__':
  main()
