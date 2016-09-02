from tkinter import *

RGB=["RED","BLUE","GREEN"]
#Colour=""
Hexadecimal=""
#while(RGB[Colour]):
#for Colour, elem in enumerate(RGB):
#while True:

for Colour in RGB:
    #while True:
        try:
            while True:
                print (Colour)
               # print (RGB[Colour])
                Colour = int(input("Please enter a number between 0 and 255 and then press enter."))
                #if (Colour < 0 or Colour > 255):
                    #print("You have entered " + str(Colour))
                #else:
                Colour = (str(hex(Colour)[2:]).upper())
                if (Colour == "0"):
                    Colour = "00"
                Hexadecimal += str(Colour)
                print(str(Hexadecimal))

        except ValueError:
            print("You have not entered a number.")
        except (Colour < 0 or Colour > 255):
            print("You have not entered a number.")
                #else:
                #break
            #Colour = int(input("Please enter a number between 0 and 255 and then press enter."))
            #Hexadecimal = str(Colour)
            #break
            #pass3

           # continue
            #else:265
           # if (Colour < 0 or Colour > 255):
                #print("You have entered " + str(Colour))
                #Colour = int(input("Please enter a number between 0 and 255 and then press enter."))
               # Hexadecimal = str(Colour)
                #break
                #pass
                #continue
            #else:
            #Colour=(str(hex(Colour)[2:]).upper())
            #if (Colour=="0"):
           #     Colour="00"
            #Hexadecimal += str(Colour)
            #print(str(Hexadecimal))
                #continue
        #Colour=Colour+1

root = Tk()
Label(root,
          text="#"+Hexadecimal,
          fg="red",
          bg="#"+Hexadecimal,
          font="Times").pack()
root.mainloop()
#print(RED)
#RollDices(HowManyDicesToBeRolledEntered)
#print(str(hex(Colour)[2:]).upper())
#print(float.hex(float(Red)))
#Redhex=print(str(hex(Red)))
#Reddec=print(Red//16)
#RedRemainder=print(Red%16)
