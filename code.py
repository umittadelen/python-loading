import sys,random,os
os.system("color a")
os.system("cls")
def progressbar(it, prefix="", size=60, out=sys.stdout):
  count = len(it)
  def show(j):
      x = int(size*j/count)
      print("{}[{}{}] {}/{}".format(prefix, "█"*x, " "*(size-x), j, count), 
              end='\r', file=out, flush=True)
  show(0)
  for i, item in enumerate(it):
      yield item
      show(i+1)
  print("\n", flush=True, file=out)

import time    
num = 1
while True:
  for i in progressbar(range(random.randint(5, 200)), f"downloading virus [{num}/∞]: ", 50):
      time.sleep(0.01)
  num += 1
