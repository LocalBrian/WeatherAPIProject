# Will handle all of the GUI related code
# Importing the necessary libraries
import tkinter as tkin

class WeatherGUI:
  def __init__(self, title="No Title Given", width=300, height = 200):
    # Create root window
    self.root = tkin.Tk()
    # root window title and dimension
    self.root.title(title)
    self.root.geometry(f"{wdith}x{height}")

  def start_up_welcome(self):
    

def test_gui():
  # Create  root window
  test_gui = WeatherGUI("Testing GUI",400,300)

  # 

if __name__ == "__main__":
  test_gui()
