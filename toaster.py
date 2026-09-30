from pathlib import Path
from desktop_notifier import DesktopNotifier, Icon
import asyncio

# apps notification object
notification_object = DesktopNotifier(app_name="FileSort", app_icon=Icon(path=Path(__file__).parent / "assets" / "icon.ico"))

# notification sender function
def send_notification(message, title="FileSort"):
    asyncio.run(notification_object.send(title=title, message=message))