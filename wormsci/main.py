import pyb

ds = pyb.Pin('X1', pyb.Pin.OUT_PP)
sh = pyb.Pin('X2', pyb.Pin.OUT_PP)
st = pyb.Pin('X3', pyb.Pin.OUT_PP)
sw = pyb.Switch()
lb = pyb.LED(4)
lo = pyb.LED(3)

NUM_LEDS = 24

l = [0] * NUM_LEDS

def show(l):
  st.low()
  for x in l:
    ds.value(x)
    sh.high(); sh.low()
#    pyb.delay(1)
  st.high()

def move(l):
  i = 0
  while l[i] == -1:
    l[i] = 1
    if i < NUM_LEDS-1:
      i += 1
  while i < NUM_LEDS:
    if l[i] == -1:
      l[i-1] = -1
      l[i] = 0
      i += 1
      if i == NUM_LEDS:
        break
    elif l[i] == 1:
      ii = i
      while l[ii] == 1:
        ii += 1
        if ii == NUM_LEDS:
          break
      if ii == NUM_LEDS:
        for ii in range(i,NUM_LEDS):
          l[ii] = -1
        break
      elif l[ii] == -1:
        for i in range(i,ii):
          l[i] = -1
        i += 1
        while l[i] == -1:
          l[i] = 1
          i += 1
          if i == NUM_LEDS:
            break
      else:
        l[i] = 0
        if (ii < NUM_LEDS-1) and l[ii+1] == -1:
          for i in range(i+1, ii+1):
            l[i] = -1
          i += 1
          while l[i] == -1:
            l[i] = 1
            i += 1
            if i == NUM_LEDS:
              break
        else:
          l[ii] = 1
          i = ii + 1
    else:
      i += 1

#      if i < NUM_LEDS-1:
#        if l[i+1] == -1:
#          ii = i
#          while l[ii] == 1:
#            l[ii] = -1
#            if ii > 0:
#              ii -= 1
#            else:
#              break
#          i += 1
#          while l[i] == -1:
#            l[i] = 1
#            if i < NUM_LEDS-1:
#              i += 1
#            else:
#              i += 1
#              break
#        else:
#         l[i+1] = 1
#          i += 1
#      else:
#        while l[i] == 1:
#          l[i] = -1
#          i -= 1
#        break

while True:
  #print(l)
  if sw() and l[0] == 0:
    l[0] = 1
  show(l)
  move(l)
  pyb.delay(60)
  #lb.toggle()