import pyautogui as p

# close all windows
p.moveTo(1895, 7)
p.leftClick()
p.moveTo(-26, 10)
p.leftClick()
p.moveTo(3816, 176)
p.leftClick()

# empty Recycle Bin
p.moveTo(40, 35, 0.3)
p.doubleClick()
p.sleep(2)
p.getWindowsWithTitle('Recycle Bin')[0].maximize()
p.moveTo(284, 31, 0.5)
p.leftClick()
p.moveTo(31, 77, 0.5)
p.leftClick()
p.moveTo(1028, 554, 0.5)
p.leftClick()
p.sleep(30)
p.moveTo(1895, 7)
p.leftClick()

# shut down
p.moveTo(12, 1059)
p.leftClick()
p.moveTo(12, 1020, 0.2)
p.leftClick()
p.moveTo(24, 942, 0.2)
p.leftClick()


