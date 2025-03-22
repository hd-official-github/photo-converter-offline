import ctypes
import sys
import os

def run_as_admin():
    """ Restart the script with administrator privileges if not already running as admin. """
    if ctypes.windll.shell32.IsUserAnAdmin():
        return  # Already running as admin
    
    # Re-run the script with admin rights
    script = os.path.abspath(sys.argv[0])
    params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
    
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
    sys.exit()  #