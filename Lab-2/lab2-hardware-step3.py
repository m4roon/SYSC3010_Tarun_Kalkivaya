from sense_emu import SenseHat

sense = SenseHat()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

state = False

def show_t():
  sense.show_letter("T", back_colour = red)
  state = False

def show_k():
  sense.show_letter("K", back_colour = red)
  state = True
  
def update():
  if (state):
    show_t()
  else:
    show_k()

show_t()

while (True):
  events = sense.stick.get_events()
  if events:
      for event in events:
        if event.action != 'pressed':
            #this is a hold or keyup; move on
            continue
        if (event.direction == 'left' or 
           event.direction == 'right' or
           event.direction == 'up' or
           event.direction == 'down'):
          state = not state
          update()

