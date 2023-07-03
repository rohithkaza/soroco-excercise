Exercise:
Create a console application that creates a global Windows OS mouse hook, to collect the following information on every click done across any application running and print the following info on the console: 
•	Mouse coordinates in pixel 
•	Exe of the application running behind the cursor

Solution:
Programming Language used: Python
Description:

1. Import Statements:
•	`win32api`, `win32gui`, `win32process`, `win32con`: These modules provide access to various Windows API functions and constants.
•	`pywintypes`: This module provides Python wrappers for Windows types.
•	`pynput.mouse`: This module from the `pynput` library enables listening to mouse events.

2. `get_foreground_window_exe_name()` Function:
•	This function retrieves the executable name of the foreground window.
•	It uses the `win32gui.GetForegroundWindow()` function to get the handle of the foreground window.
•	Then it retrieves the process ID (`pid`) of the foreground window using `win32process.GetWindowThreadProcessId()`.
•	The `win32api.OpenProcess()` function is used to open a handle to the process with specific access rights.
•	Finally, it calls `win32process.GetModuleFileNameEx()` to get the executable name associated with the process.
•	If any errors occur during this process, it returns "Unknown" as the executable name.

3. `on_click()` Function:
•	This function is the callback for mouse events.
•	It is triggered whenever a mouse button is clicked (pressed or released).
•	It calls `get_foreground_window_exe_name()` to get the executable name of the foreground window.
•	Then it prints the executable name, mouse coordinates (`x` and `y`), and the status of the button (pressed or released).

4. `start_mouse_listener()` Function:
•	This function sets up and starts the mouse listener.
•	It creates a `mouse.Listener` object, passing the `on_click` function as the callback.
•	The listener is started by calling its `start()` method.
•	It uses a `while True` loop to keep the script running until it is interrupted by a keyboard interrupt (`KeyboardInterrupt` exception).
•	When interrupted, it stops the listener by calling its `stop()` method.

5. `__name__ == "__main__"` Block:
•	This block ensures that the code inside it is only executed when the script is run directly, not when it is imported as a module.
•	It calls the `start_mouse_listener()` function to initiate the mouse listener and start capturing mouse events.


Output:
C:\Users\rohit\AppData\Local\Programs\Microsoft VS Code\Code.exe: {X=1375, Y=941}
C:\Users\rohit\AppData\Local\Programs\Microsoft VS Code\Code.exe: {X=751, Y=1040}
C:\Program Files\Google\Chrome\Application\chrome.exe: {X=1519, Y=403}
C:\Program Files\Google\Chrome\Application\chrome.exe: {X=697, Y=1047}
C:\Windows\explorer.exe: {X=1060, Y=791}
C:\Windows\explorer.exe: {X=1073, Y=983}
C:\Program Files\Python311\pythonw.exe: {X=1100, Y=840}
C:\Program Files\Python311\pythonw.exe: {X=1229, Y=1044}
C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE: {X=276, Y=1048}
C:\Windows\System32\cmd.exe: {X=560, Y=666}
C:\Windows\System32\cmd.exe: {X=1516, Y=216}
C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE: {X=1625, Y=1049}
C:\Windows\SystemApps\ShellExperienceHost_cw5n1h2txyewy\ShellExperienceHost.exe: {X=1252, Y=695}
C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE: {X=1023, Y=1048}
C:\Users\rohit\AppData\Local\Programs\Microsoft VS Code\Code.exe: {X=1170, Y=570}
