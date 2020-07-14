from tkinter import *
from tkinter import ttk
import main
import os

temp = os.path.join(os.path.getcwd(), 'temp', 'scratch.txt')
#TODO: Make basket feature
#def addToBasket(link):


root = Tk()
root.title("Fwibisono87's Video Downloader")

mainframe = ttk.Frame(root, padding="3 3 12 12")
