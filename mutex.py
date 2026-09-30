from ctypes import windll

# create a named file within windows, if the name already exists, modify the last error to 183
windll.kernel32.CreateMutexW(None, False, "FileSort_instance")

# if last error is 183, the last error was MUTEX_ALREADY_EXISTS error
if windll.kernel32.GetLastError() == 183:
    raise SystemExit