from PIL import Image
from colored import fg, bg, attr
import os, sys
import glob

def startup():
    files = glob.glob("img/*.jpg")

    print
    print ('Welcome to: %sO U T L I N E R %s' % (fg(13), attr(0)))
    print
    print "A simple image processor that outlines sections of photos based on their R, G, and B values."
    print
    print "To begin, please make sure this python file is running from a directory containing a folder labled img, which should contain all of the images that you would like to edit."
    print "To check which directory you are in/see what files and folders exist in this directory, please enter \'yes\' or \'y\'. If you would like to skip this step, please enter \'no\' or \'n\'."
    print
    checkContinue = raw_input(("%sWould you like to check which directory you are in? : %s") % (fg(13), attr(0)))
    print

    if checkContinue in ["yes", "y", "Yes"]:
        dirPath = os.path.dirname(os.path.realpath(__file__))
        print "you are currently in " + dirPath
        print "these are the files/folders it countains :"
        print os.listdir(dirPath)
        if os.path.exists(dirPath + "/img"):
            print
            print ("%sCool%s, it looks like you have an image folder in this directory! Lets keep going:" % (fg(10), attr(0)))
            return color_val(files)
        else:
            print ("%sHmmm%s, it doesn't seem like you have and img folder in this directory, try adding one before running the program again" % (fg(1), attr(0)))
            return (False,)

    else:
        dirPath = os.path.dirname(os.path.realpath(__file__))
        if os.path.exists(dirPath + "/img"):
            print ("%sCool%s, it looks like you have an image folder in this directory! Lets keep going:" % (fg(10), attr(0)))
            return color_val(files)
        else:
            print ("%sHmmm%s, it doesn't seem like you have and img folder in this directory, try adding one before running the program again" % (fg(1), attr(0)))
            return (False,)

def color_val(files):
    print "Alright, so now we are going to choose R,G, and B values to check for."
    print
    print "The program will go through the image pixel by pixel and check whether the R,G,or B values are greater than the number you provided."
    print
    print "This operation will return TRUE or FALSE and change the pixels color to black or white respectively."
    print "(telling you whether that pixel has matched the parameters you have selected or not)"
    print
    print "After you have completed this step, we will select two colors to outline the sections that match and fill the space around them."
    print

    while True:
        try:
            rl = int(raw_input(("Enter an %sR%s value to check for (between 0-255): ") % (fg(1), attr(0))))
            if 0 <= rl <= 255:
                break
            else:
                print ("%sSorry%s that's not in range. Let's try again" % (fg(1), attr(0)))
        except ValueError:
            print ("%sOops!%s  That was not a valid number. Let's try again..." % (fg(1), attr(0)))

    while True:
        try:
            gl = int(raw_input(("Enter an %sG%s value to check for (between 0-255): ") % (fg(10), attr(0))))
            if 0 <= gl <= 255:
                break
            else:
                print ("%sSorry%s that's not in range. Let's try again" % (fg(1), attr(0)))
        except ValueError:
            print ("%sOops!%s  That was not a valid number. Let's try again..." % (fg(1), attr(0)))

    while True:
        try:
            bl = int(raw_input(("Enter an %sB%s value to check for (between 0-255): ") % (fg(21), attr(0))))
            if 0 <= bl <= 255:
                break
            else:
               print ("%sSorry%s that's not in range. Let's try again" % (fg(1), attr(0)))
        except ValueError:
            print ("%sOops!%s  That was not a valid number. Let's try again..." % (fg(1), attr(0)))

    print
    print ("%sCool%s, now that the images have been processed, we have to choose a fill and outline color" % (fg(10), attr(0)))
    print
    print ("%sLet's start with the outline,%s " % (fg(13), attr(0)))

    while True:
        try:
            outline_r = int(raw_input(("Enter an %sR%s value for the outline (between 0-255): ") % (fg(1), attr(0))))
            if 0 <= outline_r <= 255:
                break
            else:
                print ("%sSorry%s that's not in range. Let's try again" % (fg(1), attr(0)))
        except ValueError:
            print ("%sOops!%s  That was not a valid number. Let's try again..." % (fg(1), attr(0)))

    while True:
        try:
            outline_g = int(raw_input("Enter an G value for the outline (between 0-255): "))
            if 0 <= outline_g <= 255:
                break
            else:
                print ("%sSorry%s that's not in range. Let's try again" % (fg(1), attr(0)))
        except ValueError:
            print ("%sOops!%s  That was not a valid number. Let's try again..." % (fg(1), attr(0)))

    while True:
        try:
            outline_b = int(raw_input("Enter an B value for the outline (between 0-255): "))
            if 0 <= outline_b <= 255:
                break
            else:
                print ("%sSorry%s that's not in range. Let's try again" % (fg(1), attr(0)))
        except ValueError:
            print ("%sOops!%s  That was not a valid number. Let's try again..." % (fg(1), attr(0)))

    outline = (outline_r, outline_g, outline_b)
    print "Your outline color is : RGB( " + str(outline[0]) + ", " + str(outline[1]) + ", " + str(outline[2]) +" )"
    print ""
    print "Now lets do the fill,"

    while True:
        try:
            fill_r = int(raw_input("Enter an R value for the fill (between 0-255): "))
            if 0 <= fill_r <= 255:
                break
            else:
                print ("%sSorry%s that's not in range. Let's try again" % (fg(1), attr(0)))
        except ValueError:
            print ("%sOops!%s  That was not a valid number. Let's try again..." % (fg(1), attr(0)))

    while True:
        try:
            fill_g = int(raw_input("Enter an G value for the fill (between 0-255): "))
            if 0 <= fill_g <= 255:
                break
            else:
                print ("%sSorry%s that's not in range. Let's try again" % (fg(1), attr(0)))
        except ValueError:
            print ("%sOops!%s  That was not a valid number. Let's try again..." % (fg(1), attr(0)))

    while True:
        try:
            fill_b = int(raw_input("Enter an B value for the fill (between 0-255): "))
            if 0 <= fill_b <= 255:
                break
            else:
                print ("%sSorry%s that's not in range. Let's try again" % (fg(1), attr(0)))
        except ValueError:
            print ("%sOops!%s  That was not a valid number. Let's try again..." % (fg(1), attr(0)))

    fill = (fill_r, fill_g, fill_b)
    print "Your fill color is : RGB( " + str(fill[0]) + ", " + str(fill[1]) + ", " + str(fill[2]) +" )"

    return (True, (files, rl, gl, bl, outline, fill))


def img_processing(args): #files, rl, bl, gl, outline, fill):
    files, rl, gl, bl, outline, fill = args
    count = 0;

    for i in files:
        im = Image.open(i)
        pixdata = im.load()

        width = im.size[0]
        height = im.size[1]

        newIm = Image.new("RGB", (width, height))
        newData = newIm.load()

        count += 1
        strCount = str(count)

        for y in xrange(im.size[1]):
            for x in xrange(im.size[0]):
                if rl < pixdata[x, y][0] or gl < pixdata[x, y][1] or bl < pixdata[x, y][2]:
                    pixdata[x, y] = (0, 0, 0)
                else:
                    pixdata[x, y] = (255, 255, 255)

        for y in xrange(1, im.size[1]-1):
            for x in xrange(1, im.size[0]-1):
                if pixdata[x, y] == (0,0,0) and (pixdata[x + 1, y] == (255, 255, 255) or pixdata[x + 1, y + 1] == (255, 255, 255) or pixdata[x, y + 1] == (255, 255, 255) or pixdata[x - 1, y] == (255, 255, 255) or pixdata[x - 1, y - 1] == (255, 255, 255) or pixdata[x, y + 1] == (255, 255, 255) or pixdata[x - 1, y + 1] == (255, 255, 255) or pixdata[x + 1, y - 1] == (255, 255, 255)):
                    newData[x, y] = outline
                else:
                    newData[x, y] = fill

        newIm.convert('RGB')
        newIm.save('out/outliner-input/' + strCount + '.jpg', "JPEG")

success, args = startup()
if success:
    img_processing(args)