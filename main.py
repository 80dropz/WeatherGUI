import customtkinter
import time
import requests


weather_key = 'key2'
zipcode_key = 'key'

window = customtkinter.CTk()
window.title("Weather GUI")
window.geometry("500x500")
window.iconbitmap('images/sun.ico')
header = customtkinter.CTkLabel(window, text="Weather APP", font=("Roboto", 24), text_color="White")
header.place(relx=.5, rely=.05, anchor="center")

subheader = customtkinter.CTkLabel(window, text="By: @80dropz", font=("roboto", 16))
subheader.place(relx=.5, rely=.13, anchor="center")

city = customtkinter.CTkLabel(window, text=" ",  font=("roboto", 14))
city.place(relx=.5, rely=.5, anchor="center")

zipentry = customtkinter.CTkEntry(window, placeholder_text="Enter Zipcode")
zipentry.place(relx=.5, rely=.6, anchor="center")

submit = customtkinter.CTkButton(window, text="Submit", fg_color="Green", text_color="Black")
submit.place(relx=.5, rely=.7, anchor="center")

window.mainloop()
