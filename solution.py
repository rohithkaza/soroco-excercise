# These modules provide access to various Windows API functions and constants.
import win32api
import win32gui
import win32process
import win32con

# This module provides Python wrappers for Windows types.
import pywintypes

# This module from the pynput library enables listening to mouse events.
from pynput import mouse


# This function retrieves the executable name of the foreground window.
def get_foreground_window_exe_name():
    hwnd = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    try:
        process_handle = win32api.OpenProcess(
            win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid
        )
        exe_name = win32process.GetModuleFileNameEx(process_handle, 0)
    
    # If any errors occur during this process, it returns "Unknown" as the executable name.
    except (win32api.error, pywintypes.error):
        exe_name = "Unknown"

    return exe_name


# This function is the callback for mouse events.
def on_click(x, y, button, pressed):
    if pressed:
        exe_name = get_foreground_window_exe_name()
        print(f"{exe_name}: {{X={x}, Y={y}}}")

# This function sets up and starts the mouse listener.
def start_mouse_listener():
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        listener.stop()


if __name__ == "__main__":
    start_mouse_listener()
