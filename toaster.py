from pathlib import Path
from desktop_notifier import DesktopNotifier, Icon

# make the coroutine object
notification_coroutine = DesktopNotifier(app_name="FileSort", app_icon=Icon(path=Path(__file__).parent / "assets" / "icon.ico")).send(title="FileSort", message="Watchman Live!")