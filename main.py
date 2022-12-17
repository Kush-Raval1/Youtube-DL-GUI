#import tkinter
from customtkinter import *
import pytube
import os
import webbrowser
import requests
from tkinter import *
import config

class App(CTk):
	def __init__(self, master=None):
		super().__init__(master)
		self.create_widgets()
		self.title("Youtube Download Tool")
		self.geometry("300x400")
		photo = PhotoImage(file='pytube.png')
		self.wm_iconphoto(False, photo)

	def create_widgets(self):

		#creates the label for the youtube link input box and places it on the GUI window
		self.linkLabel = CTkLabel(self, text="Youtube Link:")
		self.linkLabel.pack(side="top")

		#creates the youtube link input box and places it on the GUI window
		self.linkInput = CTkEntry(self, placeholder_text="Enter Link Here", width=200)
		self.linkInput.pack(side="top")

		#creates the label for the directory input box and places it on the GUI window
		self.directoryLabel = CTkLabel(self, text="Directory:")
		self.directoryLabel.pack(side="top")

		#creates the directory input box and places it on the GUI window
		self.directoryInput = CTkEntry(self, placeholder_text="Leave blank for custom preset", width=200)
		self.directoryInput.pack(side="top", pady=(0, 10))

		#creates the button that will open the directory where the video is located and places it on the GUI window
		self.openDirectoryButton = CTkButton(self, text="Open Directory", command=self.openDirectory)
		self.openDirectoryButton.pack(side="top", pady=(0, 10))

		#creates the button that will open the youtube link in chrome and places it on the GUI window
		self.openLinkButton = CTkButton(self, text="Open Link", command=self.openLink)
		self.openLinkButton.pack(side="top", pady=(0, 10))

		#creates the button that will download the video and places it on the GUI window
		self.downloadButton = CTkButton(self, text="Download", command=self.downloadVideo)
		self.downloadButton.pack(side="top")

		#creates the label that will display the status of the download and places it on the GUI window
		self.statusLabel = CTkLabel(self, text="Status: ")
		self.statusLabel.pack(side="top", pady=(0, 10))

		#creates the button that will quit the program and places it on the GUI window
		self.quit = CTkButton(self, text="QUIT", command=self.destroy)
		self.quit.pack(side="bottom")

	#function that will open the directory where the video is located
	def openDirectory(self):
		if self.directoryInput.get() == "":
			directory = config.ddlDir()
			os.startfile(directory)
		else:
			os.startfile(self.directoryInput.get())


	#function that will open the youtube link in chrome
	def openLink(self):
		if (self.linkInput.get() == ""):
			pass
		else:
			webbrowser.open(self.linkInput.get())

	#function that will download the video
	def downloadVideo(self):
		try:

			yt = pytube.YouTube(self.linkInput.get())
			#gets the highest quality video from the youtube link
			video = yt.streams.get_highest_resolution()
			#gets the directory from the input box
			if self.directoryInput.get() == "":
				directory = config.ddlDir()
			else:
				directory = self.directoryInput.get()
			#downloads the video to the directory specified by the user
			video.download(directory)
			#updates the status label to say that the video is done downloading
			self.statusLabel.configure(text="Status: The video is done downloading")
		except:
			self.statusLabel.configure(text="Status: Please input a valid link")
if __name__ == "__main__":
    app = App()
    app.mainloop()