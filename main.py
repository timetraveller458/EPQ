import tkinter as tk
import blur_function
import moveblur_function
import brighter_function
#import contrast_function
import negative_function
import sepia_function
import skew_function
import chrom_abr_function
import greyscale_function
import cv2

img = cv2.imread("test.jpg")
img = cv2.resize(img, (0,0), fx=0.5,fy=0.5)
window = tk.Tk()
window.geometry("400x460")


def img_input():
    global img
    img_name = input_txt.get(1.0, "end-1c")
    new = cv2.imread(img_name)
    if new is not None:
        img = new



blur_slider = tk.Scale(window, from_=1, to=4, orient=tk.HORIZONTAL)
blur = tk.Button(window, text="BLUR", command = lambda:blur_function.main(img, blur_slider.get()))

blur_move_slider = tk.Scale(window, from_=1, to=4, orient=tk.HORIZONTAL)
blur_move = tk.Button(window, text="MOVING BLUR", command = lambda:moveblur_function.main(img, blur_move_slider.get()))
#go through code
brighter_slider = tk.Scale(window, from_=1, to=10, orient=tk.HORIZONTAL)
brighter = tk.Button(window, text="BRIGHTER", command= lambda:brighter_function.main(img, brighter_slider.get()))
#go through code
#contrast = tk.Button(window, text="INCREASE CONTRAST", command= lambda:contrast_function.main(img))

negative = tk.Button(window, text="NEGATIVE", command=lambda:negative_function.main(img))

sepia = tk.Button(window, text="SEPIA", command=lambda:sepia_function.main(img))

skew = tk.Button(window, text="SKEW", command=lambda:skew_function.main(img))

chrom_slider = tk.Scale(window, from_=1, to=10, orient=tk.HORIZONTAL)
chrom = tk.Button(window, text="CHROMATIC ABERRATION", command=lambda:chrom_abr_function.main(img, chrom_slider.get()))
grey = tk.Button(window, text="GREYSCALE", command=lambda:greyscale_function.main(img))
input_txt = tk.Text(window, height = 1, width = 20)
imgButton = tk.Button(window, text = "Set image name", command = img_input)

blur.pack()
blur_slider.pack()
blur_move.pack()
blur_move_slider.pack()
brighter.pack()
brighter_slider.pack()
#contrast.pack()
negative.pack()
sepia.pack()
skew.pack()
chrom.pack()
chrom_slider.pack()
grey.pack()
input_txt.pack()
imgButton.pack()

window.mainloop()