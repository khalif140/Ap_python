def dryCleaner():
    ClothesDry = False
    while ClothesDry == False:
        print('keep drying clothes')
        dryClothing = input('are the clothes dry?: ') 
        if dryClothing == 'y':
            print(' stop the dryer. Clothes are dry') 
            break

dryCleaner()


# Create while loops for the following conditions


# 1. Create a security camera program that uses a while loop to detect if there is an
# object in site. 
def securityCamera():
    camera = False
    while camera is True:
        
        securityCamera = input(': ')
        if securityCamera == 'movement':
            print('Movement detected')
            
        if securityCamera == 'nothing':
            print('Nothing is there')
        else:
            print('Leave the Security Cam alone')
            


securityCamera()
# 2. Create a Printer Loop program that will continue to print copies of a document based on the number
# that the user inputs. 
printer = 0
Amount = float(input('How many?: '))
while printer < Amount:
    print('Document.563.exe printed')
    printer += 1
# 3. Create a Stop Light Loop that will change the light color based on different time intervals. 
# every 30 seconds the light should change between green and red. 
def trafficLight():
    i = 0
    red = "Stop"
    green = "go"

    while i < 120:
        print('count down: ' + str(i))
        i-=1
        ifi/2=0
        print(red)

trafficLight()
# 3. BONUS: add an additional condition that will change the light to yellow for 5 seconds before the
# next light change. 