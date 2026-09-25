from PIL import Image
import pystray

# local imports
import app_context 

# pillow image object
image = Image.open("assets/icon.ico")

# menu methods
def on_exit(icon, item):
    icon.stop()

def toggle_state(icon, item):
    app_context.paused = not app_context.paused
    icon.update_menu()

# Tray Menu UI object
menu = pystray.Menu(
    pystray.MenuItem("FileSort", None, enabled=False),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem(lambda item: "Pause" if not app_context.paused else "Resume", toggle_state),
    pystray.MenuItem("Exit", on_exit)
)

# Tray Object
app = pystray.Icon("filesort", image, "FileSort", menu)