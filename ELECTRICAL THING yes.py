import pygame
import pygame_gui
import os
import sys
import re
import random

width = 1100
height = 750
scrn = pygame.display.set_mode((width,height))
pygame.display.set_caption("Electrical Company")
bgc = (0, 0, 0)
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

titlefontpath = os.path.join ("Fonts", "Helvetica.ttf")
titlefont = pygame.font.Font(titlefontpath, 17)

# Button Class
class Button():
    def __init__(self,x,y,image,scale):
        b_width = image.get_width()
        b_height = image.get_height()
        self.image = pygame.transform.scale(image, (int(b_width * scale),int(b_height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.status = False

    def draw(self):
        action = False


        pos = pygame.mouse.get_pos()
    
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.status == False:
                self.status = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.status = False
        scrn.blit(self.image, (self.rect.x, self.rect.y))

        return action

class topbarbuttons(Button):
    def __init__(self, x, y, image, scale):
        Button.__init__(self, x, y, image, scale)

    def draw(self):
        action = Button.draw(self)

        if pygame.mouse.get_pressed()[0] == 0:
            self.status = False

        return action

class timemenubutton(Button):
    def __init__(self, x, y, image, scale):
        Button.__init__(self, x, y, image, scale)

    def draw(self):
        action = Button.draw(self)

        if pygame.mouse.get_pressed()[0] == 0:
            self.status = False

        return action

mng = pygame_gui.UIManager((width,height))
tick = pygame.time.Clock()

# IMAGE LOADING AND PATHS
loginb_path = os.path.join("Assets", "loginb.png")
loginb = pygame.image.load(loginb_path).convert()

logon_path = os.path.join("Assets", "logon.png")
logon = pygame.image.load(logon_path).convert()

register_path = os.path.join("Assets", "Register.png")
register = pygame.image.load(register_path).convert()

welcome_path = os.path.join("Assets", "welcome.png")
welcome = pygame.image.load(welcome_path).convert()

logmenu_path = os.path.join("Assets", "logmenu.png")
logmenu = pygame.image.load(logmenu_path).convert()

registermenu_path = os.path.join("Assets", "registermenu.png")
registermenu = pygame.image.load(registermenu_path).convert()

home_path = os.path.join("Assets", "home.png")
home = pygame.image.load(home_path).convert()

deleteacc_path = os.path.join("Assets", "Deleteaccount.png")
deleteacc = pygame.image.load(deleteacc_path).convert()

abtus_path = os.path.join("Assets", "AboutUs.png")
abtus = pygame.image.load(abtus_path).convert()

abtmenu_path = os.path.join("Assets", "aboutusmenu.png")
abtmenu = pygame.image.load(abtmenu_path).convert()

times_path = os.path.join("Assets", "times.png")
times = pygame.image.load(times_path).convert()

faq_path = os.path.join("Assets", "faq.png")
faq = pygame.image.load(faq_path).convert()

ebill_path = os.path.join("Assets", "ebill.png")
ebill = pygame.image.load(ebill_path).convert()

outage_path = os.path.join("Assets", "outage.png")
outage = pygame.image.load(outage_path).convert()

faqmenu_path = os.path.join("Assets", "faqmenu.png")
faqmenu = pygame.image.load(faqmenu_path).convert()

ebillmenu_path = os.path.join("Assets", "ebillingmenu.png")
ebillmenu = pygame.image.load(ebillmenu_path).convert()

outagemenu_path = os.path.join("Assets", "outagemenu.png")
outagemenu = pygame.image.load(outagemenu_path).convert()

adminbtn_path = os.path.join("Assets", "Admin.png")
adminbtn = pygame.image.load(adminbtn_path).convert()

adminmenu_path = os.path.join("Assets", "Adminmenu.png")
adminmenu = pygame.image.load(adminmenu_path).convert()

infopanel_path = os.path.join("Assets", "Infopanel.png")
infopanel = pygame.image.load(infopanel_path).convert()

getbill_path = os.path.join("Assets", "Getbill.png")
getbill = pygame.image.load(getbill_path).convert()

paymentmenu_path = os.path.join("Assets", "paymentpage.png")
paymentmenu = pygame.image.load(paymentmenu_path).convert()

confirmpayment_path = os.path.join("Assets", "confirmpayment.png")
confirmpayment = pygame.image.load(confirmpayment_path).convert()

paymentsuccess_path = os.path.join("Assets", "paymentsuccess.png")
paymentsuccess = pygame.image.load(paymentsuccess_path).convert()

alreadypaid_path = os.path.join("Assets", "alreadypaid.png")
alreadypaid = pygame.image.load(alreadypaid_path).convert()

hfont_path = os.path.join("Fonts", "Helvetica.ttf")
cfont_path = os.path.join("Fonts", "Courier New Bold.ttf")
helvetica = pygame.font.Font(hfont_path, 20)
courierlarge = pygame.font.Font(cfont_path, 35)
courierreg = pygame.font.Font(cfont_path, 12)

wrongpass = helvetica.render("Incorrect Password or Username.", True, (255,255,255))
alreadytaken = helvetica.render("Username already taken.", True, (255,255,255))

# Usernames and Passwords
# INSERT LIST OF ACCEPTABLE PASSWORDS AND USERS (wip)


# SCREEN DISPLAY FUNCTIONS
def startscreen():
    scrn_1 = pygame.transform.scale(welcome,(1100,750))
    scrn.blit(scrn_1,(0,0))

def logging():
    scrn_2 = pygame.transform.scale(logmenu,(1100,750))
    scrn.blit(scrn_2,(0,0))

def abtmenuscrn():
    scrn_3 = pygame.transform.scale(abtmenu,(1100,750))
    scrn.blit(scrn_3,(0,0))

def timemenu():
    scrn_4 = pygame.transform.scale(times,(1100,750))
    scrn.blit(scrn_4,(0,0))

def faqs():
    scrn_4 = pygame.transform.scale(faqmenu,(1100,750))
    scrn.blit(scrn_4,(0,0))

def ebilling():
    scrn_4 = pygame.transform.scale(ebillmenu, (1100, 750))
    scrn.blit(scrn_4, (0, 0))

def ebillingpayment():
    scrn_4 = pygame.transform.scale(paymentmenu, (1100, 750))
    scrn.blit(scrn_4, (0, 0))

def ebillingsuccess():
    scrn_4 = pygame.transform.scale(paymentsuccess, (1100, 750))
    scrn.blit(scrn_4, (0, 0))
    
def ebillingpaid():
    scrn_4 = pygame.transform.scale(alreadypaid, (1100, 750))
    scrn.blit(scrn_4, (0,0))

def outagemap():
    scrn_4 = pygame.transform.scale(outagemenu,(1100,750))
    scrn.blit(scrn_4,(0,0))

def adminscrn():
    scrn_4 = pygame.transform.scale(adminmenu,(1100,750))
    scrn.blit(scrn_4,(0,0))
    
def registering():
    scrn_5 = pygame.transform.scale(registermenu,(1100,750))
    scrn.blit(scrn_5,(0,0))

# BUTTONS
login_button = Button((width/3)+25,(height/2)-30,loginb,0.27)
logon_button = Button((width/3)-50,(height/2)+130,logon,0.29)
register_button = Button((width/3)+230,(height/2)+130, register, 0.29)
register_button2 = Button((width/3)+77,(height/2)+130, register, 0.29)
home_button = topbarbuttons((width/2)+200,(height/20),home,0.1)
abtus_button = topbarbuttons((width/2)+300,(height/20),abtus,0.06)
deleteacc_button = Button((width/3)+63,(height/2)+250, deleteacc, 0.29)
getbill_button = Button(width / 2 - 450, height / 2 + 100, getbill, 1.25)
confpay_button = Button(width / 2 - 253, 575, confirmpayment, 1)

home_button2 = timemenubutton((width/2)-100,(height/20),home,0.1)
abtus_button2 = timemenubutton((width/2),(height/20),abtus,0.06)
ebill_button = timemenubutton((width/2)+110,(height/20)-3,ebill,0.067)
faq_button = timemenubutton((width/2)+220,(height/20),faq,0.06)
outagemap_button = timemenubutton((width/2)+300,(height/20),outage,0.07)
admin_button = timemenubutton((width/2)-200,(height/20),adminbtn,0.1)



def inp_info():
    username = ""
    password = ""
    username_entered = False
    passowrd_entered = False
    
    user_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 110, height / 2 - 30), (400, 50)), manager=mng, object_id="#usernameentry")
    pass_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 110, height / 2 + 45), (400, 50)), manager=mng, object_id="#passwordentry")
    pass_entry.set_text_hidden(True)
    
    while True:
        fps = tick.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_object_id == "#usernameentry":
                    username = event.text
                    print("username entered")
                    for item in validlist:
                        if username == item[0]:
                            putusername = titlefont.render(username,True,(224, 77, 54))
                            username_entered = True
                            print("Username Correct")
                            
                            usrtype = item[2]
                elif event.ui_object_id == "#passwordentry":
                    password = event.text
                    print("password entered")
                    for item in validlist:
                        if password == item[1]:
                            putpassword = titlefont.render(password,True,(99, 146, 235))
                            passowrd_entered = True
                            print("password correct")


            mng.process_events(event)

        mng.update(fps)
        mng.draw_ui(scrn)
        pygame.display.update()

        if logon_button.draw():
            print("hi")
            if passowrd_entered == True and username_entered == True:
                return username, password, usrtype, None
            else:
                scrn.blit(wrongpass,((width/3)+20,(height/2)+220))
                
        if register_button.draw():
            return None, None, None, True
def newusrinfo():
    a = str(random.randint(1000,10000))
    b = str(random.randint(60,200))
    c = str(random.randint(60,200))
    d = str(random.randint(60,200))
    
    newusrinf = "[#"+a+"#,*"+b+"*,^"+c+"^,("+d+"(]"
    return newusrinf

def reginp_info():
    mng.clear_and_reset()
    username = ""
    password = ""
    username_entered = False
    passowrd_entered = False
    
    user_entry2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 110, height / 2 - 30), (400, 50)), manager=mng, object_id="#usernameentry2")
    pass_entry2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 110, height / 2 + 45), (400, 50)), manager=mng, object_id="#passwordentry2")
    pass_entry2.set_text_hidden(True)

    while True:
        fps = tick.tick(60) / 1000
        usrtype = "Reg"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_object_id == "#usernameentry2":
                    username = event.text
                    username_entered = True
                    print("Username Set")

                elif event.ui_object_id == "#passwordentry2":
                    password = event.text
                    passowrd_entered = True
                    print("Password Set")

            mng.process_events(event)
        
        mng.update(fps)
        mng.draw_ui(scrn)
        pygame.display.update()
        
        for item in validlist:
            if username == item[0]:
                username_entered = False
                passowrd_entered = False
        
        if register_button2.draw():
            print("hello")
            if passowrd_entered == True and username_entered == True:
                    usrinf = newusrinfo()
                    with open("Userinfo.txt", "a") as file:
                        newuser = "usrc[%"+username+"%,&"+password+"&,$"+usrtype+"$]"
                        file.write("\n"+newuser+usrinf)
                    return username, password, usrtype
            else:
                scrn.blit(alreadytaken, ((width/3)+30,(height/2)+220))
def genvalid():
    with open("Userinfo.txt", "r") as file:
        names = []
        passwds = []
        types = []
        
        for line in file:
            items = file.read()
            print(items)

            regexnames = r'%([^%]+)%'
            a = re.findall(regexnames, items)
            for item in a:
                names.append(item)
            
            regexpwd = r'&([^&]+)&'
            b = re.findall(regexpwd, items)
            for item in b:
                passwds.append(item)
            
            regextype = r'\$(.*?)\$'
            c = re.findall(regextype, items)
            for item in c:
                types.append(item)
        
    validlist = []
    for i in range(len(names)):
        cell1 = [names[i],passwds[i],types[i]]
        validlist.append(cell1)
        
    print(validlist)
    return validlist

validlist = genvalid()
def genvalidinfo():
    with open("Userinfo.txt", "r") as file:
        balance = []
        onpeak = []
        midpeak = []
        offpeak = []
        
        for line in file:
            items = file.read()

            regexbalance = r'#([^#]+)#'
            a = re.findall(regexbalance, items)
            for item in a:
                balance.append(item)
            
            regexonp = r'\*([^*]+)\*'
            b = re.findall(regexonp, items)
            for item in b:
                onpeak.append(item)
            
            regexmidp = r'\^([^^]+)\^'
            c = re.findall(regexmidp, items)
            for item in c:
                midpeak.append(item)
                
            regexoffp = r'\(([^(]+)\('
            d = re.findall(regexoffp, items)
            for item in d:
                offpeak.append(item)
        
    validinfolist = []
    for i in range(len(balance)):
        cell2 = [balance[i],onpeak[i],midpeak[i],offpeak[i]]
        validinfolist.append(cell2)

    print(validinfolist)
    return validinfolist
validinfolist = genvalidinfo()

def billlabels():
    mng.clear_and_reset()
    fps = tick.tick(30) / 1000
    usernameent = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 300, height / 2 - 95), (250, 50)), manager=mng, object_id="#usernameent")
    postalent = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((width / 2 - 300, height / 2 - 37), (250, 50)), manager=mng, object_id="#postalent")
    scrn.blit(infopanel, (width / 2 + 40, height / 2 - 115))
    if getbill_button.draw():
        return "a"
    
    mng.update(fps)
    mng.draw_ui(scrn)
    pygame.display.update()
        
def billInfo(units, a, b):
    unit = units
    delivery_fee = b
    
    peak_price = int(int(unit[1]) * 0.182)
    mid_price = int(int(unit[2]) * 0.122)
    off_price = int(int(unit[3]) * 0.087)

    raw_price = peak_price + mid_price + off_price
    if a:
        delivery_fee = random.randint(1000, 10000) / 100
    regulatory_fee = 5.00

    gross_total = int(raw_price + delivery_fee + regulatory_fee)
    total_cost = int(gross_total * 1.13)
    
    infoarray = [peak_price, mid_price, off_price, raw_price, delivery_fee, regulatory_fee, gross_total, total_cost]
    return infoarray
    
    #return f"Customer ID: 1001\nCustomer Name: James\nUnit: {unit}\nAmount: {total_cost:.2f}\nThank You, Come Again!"

def top_bar_buttons(current_scrn):
    if home_button.draw():
        return "home"
    if abtus_button.draw():
        return "about us"

    return current_scrn

def timemenu_buttons(current_scrn, usrtype):
    if home_button2.draw():
        return "times"  
    if abtus_button2.draw():
        return "about us"
    if ebill_button.draw():
        return "ebill"
    if faq_button.draw():
        return "faq"
    if outagemap_button.draw():
        return "om"
    if usrtype == "Admin":
        if admin_button.draw():
            return "admin"
    
    return current_scrn

def adminuserselect():
    fps = tick.tick(60) / 1000
    validlist = genvalid()
    selection = "-"
    mng.clear_and_reset()
    
    regusrlist = ["-"]
    for item in validlist:
        if item[2] == "Reg":
            regusrlist.append(item[0])
    
    dropdown = pygame_gui.elements.UIDropDownMenu(options_list=regusrlist, starting_option="-", relative_rect=pygame.Rect((300, 275), (550, 30)), manager=mng)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED: 
                if event.ui_element == dropdown:
                    selection = event.text
                    return selection
            
            mng.process_events(event)
                    
        mng.update(fps)
        mng.draw_ui(scrn)
        pygame.display.update()

def hide_ui_elements(ui_elements):
    for element in ui_elements:
        element.hide()

def show_ui_elements(ui_elements):
    for element in ui_elements:
        element.show()

def game_loop():
    run = True
    current_scrn = "home"
    previous_scrn = None
    timevisited = False
    ui_elements = []
    temp = True
    devinfo = 0
    alreadypaid = False
    
    while run:
        scrn.fill(bgc)
        if current_scrn == "home":
            startscreen()
            if login_button.draw():
                current_scrn = "logging in"
                print("logging in")

        if current_scrn == "logging in":
            logging()
            validlist = genvalid()
            validinfolist = genvalidinfo()
            username, password, usrtype, reg = inp_info()
            if reg == None:
                current_scrn = "times"
                timevisited = True
            else:
                current_scrn = "register"
            print(f"Username: {username}, Password: {password}")
            
        if current_scrn == "register":
            registering()
            username, password, usrtype = reginp_info()
            timevisited = True
            current_scrn = "times"
            validlist = genvalid()
            validinfolist = genvalidinfo()
            print(f"Username: {username}, Password: {password}")
        
        if current_scrn == "about us":
            abtmenuscrn()
        
        if current_scrn == "times":
            timemenu()

        if current_scrn == "faq":
            faqs()

        if current_scrn == "om":
            outagemap()

        if current_scrn == "ebill":
            ebilling()
            billlabel = billlabels()
            print(validlist)
            for item in validlist:
                print(item[0])
                if username == item[0]:
                    whichusr = validlist.index(item)
            j = validinfolist[whichusr]
            newbillinfo = billInfo(j, temp,devinfo)
            temp = False
            a = 0
            devinfo = newbillinfo[4]
            for item in newbillinfo:
                if item != newbillinfo[3]:
                    text = helvetica.render(str(item), True, (0,0,0))
                    scrn.blit(text,(width/2+290,height/2-90 +a))
                    a += 58
            
            if billlabel == "a":
                current_scrn = "payment"
        
        if current_scrn == "payment":
            ebillingpayment()
            curbal = helvetica.render(str(validinfolist[whichusr][0]), True, (0,0,0))
            totalcost = helvetica.render(str(newbillinfo[7]), True, (0,0,0))
            rembal = helvetica.render(str(int(validinfolist[whichusr][0])-int(newbillinfo[7])), True, (0,0,0))
            scrn.blit(curbal,(width/2+30,height/2-90+30))
            scrn.blit(totalcost,(width/2+30,height/2-32+30))
            scrn.blit(rembal,(width/2+30,height/2+26+30))
            if confpay_button.draw():
                if alreadypaid == False:
                    current_scrn = "paysuccess"
                    alreadypaid = True
                else:
                    current_scrn = "paid"
        
        if current_scrn == "paysuccess":
            ebillingsuccess()
            
        if current_scrn == "paid":
            ebillingpaid()
                

        # Hide UI elements when switching da screen
        if previous_scrn and previous_scrn != current_scrn and ui_elements:
            hide_ui_elements(ui_elements)
            ui_elements = []

        previous_scrn = current_scrn
        # Hide UI elements when switching da screen
        if previous_scrn and previous_scrn != current_scrn and ui_elements:
            hide_ui_elements(ui_elements)
            ui_elements = []

        previous_scrn = current_scrn

        
        if current_scrn == "admin":
            adminscrn()
            a = adminuserselect()
            if a != "-":
                current_scrn = "log"
            
        if current_scrn == "log":
            mng.clear_and_reset()
            adminscrn()
            usertext = "Info about "+ a
            infouser = courierlarge.render(usertext, True, (255,255,255))
            infrect = infouser.get_rect()
            scrn.blit(infouser,((width-infrect.w)//2, 250))
            
            for item in validlist:
                if item[0] == a:
                    b = validlist.index(item)
            usrdet = "Username: "+validlist[b][0]+"\nPassword: "+validlist[b][1]+"\nAccount Type: "+validlist[b][2]+"\nBalance: "+validinfolist[b][0]+"\nOn Peak: "+validinfolist[b][1]+"\nMid Peak: "+validinfolist[b][2]+"\nOff Peak: "+validinfolist[b][3]
            print(usrdet)
            userdetails = courierreg.render(usrdet, True,(255,255,255))
            pygame.draw.rect(scrn, (25, 25, 25), pygame.Rect((width-700)//2, (height-500)//2+185, 700, 300))
            scrn.blit(userdetails, (200, 310))
            
            if deleteacc_button.draw():
                todelete = "%"+a+"%"
                with open("Userinfo.txt", "r") as file:
                    lines = file.readlines()
                with open("Userinfo.txt", "w") as file:
                    for line in lines:
                        if todelete not in line:
                            file.write(line)
                            
                print(validlist)
                for item in validlist:
                    if item[0] == a:
                        validlist.remove(item)
                        
                validlist = genvalid()
                validlistinfo = genvalidinfo()
                current_scrn = "times"
                
            
        if timevisited == True:
            current_scrn = timemenu_buttons(current_scrn,usrtype)
        else:
            current_scrn = top_bar_buttons(current_scrn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            
        pygame.display.update()
        pygame.display.flip()
        mng.update(pygame.time.Clock().tick(60) / 1000)
        mng.draw_ui(scrn)

def draw_text(surface, text, pos, font_size=20, color=(0, 255, 0)):
    font = pygame.font.Font(None, font_size)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (pos[0], pos[1] + i * (font_size + 2)))

game_loop()
print("")
pygame.quit()
sys.exit()