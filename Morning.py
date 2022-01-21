import pyautogui as p

# open Chrome
p.moveTo(164, 1063, 0.5)
p.leftClick()

# stack tabs for HOME
p.moveTo(360, 12, 1)
p.leftClick()
with p.hold('shift'):
    p.move(-233, 0)
    p.leftClick()
p.rightClick()
p.move(10, 60, 0.15)
p.leftClick()
p.write('HOME')
p.move(-84, 24, 0.15)
p.leftClick()

# Stack tabs for SCHOOL
p.moveTo(1127, 12)
p.leftClick()
with p.hold('shift'):
    p.move(-515, 0)
    p.leftClick()
p.rightClick()
p.move(0, 60, 0.15)
p.move(280, 0, 0.15)
p.leftClick()
p.write('SCHOOL')
p.move(-300, 30, 0.15)
p.leftClick()

# Stack tabs for ML
p.moveTo(1460, 12)
p.rightClick()
p.move(0, 60, 0.15)
p.move(280, 0, 0.15)
p.leftClick()
p.write('ML')
p.move(-300, 30, 0.15)
p.leftClick()

# end of program
p.hotkey('ctrl','t')
p.write('Good morning, Jack. :D')
p.moveTo(1225, 12)
p.leftClick()
p.moveTo(578, 12)
p.leftClick()
p.moveTo(79, 12)
p.leftClick()
