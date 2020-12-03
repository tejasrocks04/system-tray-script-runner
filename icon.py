from PIL import Image, ImageDraw
from pystray import Icon as icon, Menu , MenuItem as item
import sys
import main as main
def create_image():
    # Generate an image and draw a pattern
    image = Image.new('RGB', (100,100))
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (100 // 2, 0, 100, 100 // 2),
        fill='green')
    dc.rectangle(
        (0, 100 // 2, 100 // 2, 100),
        fill='green')

    return image

state = False
icon.icon = create_image()
def on_clicked(icon, item):
    global state
    state = not item.checked
    main.main()
    state=False
def on_quit(icon):
    icon.visible = False  # Need it to stop the main while loop. I think any global var also will do the thing
    icon.stop()  

icon("test",create_image(),menu=Menu(
        item(
            'start',
                    on_clicked,
                checked=lambda item: state),
        item(
            'quit',on_quit))).run()
