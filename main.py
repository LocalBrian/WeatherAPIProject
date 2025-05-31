# Main python file to run from command line

## Needed imports
import tkinter as tk
from gui import WeatherAppGUI

# Jump directly into the UI program
if __name__ == "__main__":
    
    root = tk.Tk()
    # Below you can see the key, it gets fairly frequent free use. This generally isn't best practice, but for this example, it is acceptable.
    app = WeatherAppGUI(root,'edc03d75e4e5d949f7f1ea055454500b')
    root.mainloop()
