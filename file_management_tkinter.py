from tkinter import filedialog as fd
# import tkinter as tk
from tkinter import *

path: str = fd.askopenfilename(title="Select a file")
print(path)
print(tkinter._test())