import pyautogui
# pip install PyAutoGUI
def ejemplo_pyautogui():
    pyautogui.PAUSE = 1  # se aplica a todos los comandos

    screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
    print("screen size" ,screenWidth, screenHeight)
    currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
    print("mouse position", currentMouseX, currentMouseY )
    # pyautogui.moveTo(20, 20) #  x, y coordinates
    # pyautogui.click()
    # pyautogui.click(20, 20) # saltar a ordenada y dar click
    # pyautogui.move(0, 20, duration=5)  # Move mouse 10 pixels down,
    # pyautogui.doubleClick()
    # pyautogui.moveTo(500, 500, duration=5)# tween=pyautogui.easeInOutQuad
    # pyautogui.write('Hello world!', interval=0.25)
    # pyautogui.press('esc') # precionar una vez
    # pyautogui.keyDown('shift')# dejar precionado solo caracteres especiales
    # pyautogui.press('left', presses=3)# dejar ptrecionado
    # pyautogui.keyUp('shift')# soltar
    # pyautogui.write([ 'left', 'up', 'right', 'down', 'left'], interval=0.25)   #flechas
    # pyautogui.hotkey('ctrl', 'c')
    # pyautogui.hotkey("ctrl", "v")

    # pyautogui.hotkey('ctrl', 'shift', 'esc')

    # es equivalente a este código:

    # pyautogui.keyDown('ctrl')
    # pyautogui.keyDown('shift')
    # pyautogui.keyDown('esc')
    # pyautogui.keyUp('esc')
    # pyautogui.keyUp('shift')
    # pyautogui.keyUp('ctrl')

    # pyautogui.alert('This is an alert box.')
    # print(pyautogui.confirm('Shall I proceed?'))#OK
    # print(pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C']))
    # print(pyautogui.prompt('What is your name?'))
    # print(pyautogui.password('Enter password (text will be hidden)'))

    # im1 = pyautogui.screenshot()
    # im1.save('my_screenshot.png')
    # im2 = pyautogui.screenshot('my_screenshot2.png')
    # im = pyautogui.screenshot(region=(0,0, 300, 400))
    # im = pyautogui.screenshot()
    # im.getpixel((100, 200))#(130, 135, 144)#saber color de un pixel
    # o simplemente
    # pix = pyautogui.pixel(100, 200)
    # pyautogui.pixelMatchesColor(100, 200, (130, 135, 144), tolerance=10)

    # ubicar una imagen                                       , grayscale=True, confidence=0.9) #Necesita OpenCV instalado
    # button7location = pyautogui.locateOnScreen('button.png') # returns (left, top, width, height) of matching region
    # button7location(1416, 562, 50, 41)
    # buttonx, buttony = pyautogui.center(button7location)
    # buttonx, buttony(1441, 582)
    # pyautogui.click(buttonx, buttony)

    # buscar centro de la imagen
    # buttonx, buttony = pyautogui.locateCenterOnScreen('button.png') # returns (x, y) of matching region
    # buttonx, buttony(1441, 582)
    # pyautogui.click(buttonx, buttony)

    #                                                         region=(0,0, 300, 400), grayscale=True, confidence=0.9) #Necesita OpenCV instalado
    # pyautogui.click('calc7key.png')# buscar centrar y clickar
    # button7location = pyautogui.locateOnScreen('calc7key.png', confidence=0.9) #Necesita OpenCV instalado
    # locateOnScreen(image, grayscale=False)- Devuelve (izquierda, arriba, ancho, alto)
    # locateCenterOnScreen(image, grayscale=False)- Devuelve las coordenadas (x, y)
    # locateAll(needleImage, haystackImage, grayscale=False)- Devuelve un generador que produce (izquierda, arriba, ancho, alto)

    # print(pyautogui.getWindowsWithTitle())

    # pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
    # pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position

    '''
    distance = 50
    while distance > 0:
            pyautogui.drag(distance, 0, duration=0.5)   # move right
            distance -= 5
            pyautogui.drag(0, distance, duration=0.5)   # move down
            pyautogui.drag(-distance, 0, duration=0.5)  # move left
            distance -= 5
            pyautogui.drag(0, -distance, duration=0.5)  # move up
    '''


