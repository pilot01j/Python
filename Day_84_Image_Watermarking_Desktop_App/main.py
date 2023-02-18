from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont


FONT_NAME = "Courier"
TEXT_COLLOR = "#1F8A70"
WATERMARK_RGB_COLLOR = (255, 48, 48)
WATERMARK_FONT_SIZE = 50
WATERMARK_POSITION = (680, 550)
BUTTON_FONT = ('Arial', 14)
ENTRY_FONT = ('Arial', 20)


# Creating Windows and Labels with Tkinter
root = Tk()
root.title('WATERMARK_IMG')
root.config(padx=25, pady=25)
img_file = ''


# Saving Data to File
def watermark(img_input, img_output, text_watermark, xy_pos):
    image = Image.open(img_input)

    edit_image = ImageDraw.Draw(image)

    font_watermark = ImageFont.truetype("arial.ttf", WATERMARK_FONT_SIZE)
    edit_image.text(xy_pos, text_watermark, font=font_watermark, fill=WATERMARK_RGB_COLLOR)
    image.show()
    image.save(img_output)


# Selecting Files to Watermark
def select_file():
    global img_file
    img_file = askopenfilename()


def watermark_img():
    if img_file == '':
        messagebox.showerror("No image found", "Please select an image first.")
    else:
        img_output = f'watermarked.jpg'
        text_watermark = text_entry.get()
        watermark(img_file, img_output, text_watermark=text_watermark, xy_pos=WATERMARK_POSITION)
        messagebox.showinfo("Complete", "Successfully!")


# Use grid() and columnspan to Complete the User Interface

title_label = Label(text="IMG Watermark", font=(FONT_NAME, 50, "bold"), fg=TEXT_COLLOR, )

b1 = Button(root, text="Select IMG", font=BUTTON_FONT, bg="blue", width=15, command=select_file)
b2 = Button(root, text="Save", font=BUTTON_FONT, bg="green", width=15, command=watermark_img)

# Dialog Boxes and Pop-Ups in Tkinter
text_label = Label(text="Write Text", font=ENTRY_FONT)
text_entry = Entry(width=30, font=ENTRY_FONT)

title_label.grid(column=1, row=1, columnspan=4, padx=25, pady=25)
b1.grid(column=1, row=2, padx=25, pady=25)
text_label.grid(column=2, row=2, padx=35, pady=35)
text_entry.grid(column=3, row=2)
b2.grid(column=4, row=2, padx=25, pady=25)

root.mainloop()
