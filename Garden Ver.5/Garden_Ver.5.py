import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox
from PIL import ImageTk
import random

# 預設的名字、大卡上下限、最低份數
name = "使用者"
height = 160
weight = 55
BMI = weight/((height/100)*(height/100))
kalupperlimit = 35*weight + 100
kalunderlimit = 35*weight - 100
CurSta = "體重正常"
fruitlimit = (weight/20) - 1
milklimit = 1
vegetablelimit = ((weight/20)-1)+1
proteinlimit = weight/10 - 1
grainlimit = (weight/20) - 1

# 把檔案讀進來
with open('list.txt', mode="r", encoding="utf-8") as f:
    for line in f:
        garden1 = line.split(',')
garden = garden1[0:30]
for i in range(len(garden)):
    garden[i] = int(garden[i])
f.close()

with open('used.txt', mode="r", encoding="utf-8") as f2:
    for line in f2:
        used_list = line.split()
used = used_list[0]
f2.close()

print(used)

# 把profile讀進來
name = 0
height = 0
weight = 0
with open(file="profile.txt", mode='r', encoding='utf-8') as p:
    for line in p:
        profile = line.split(',')

name = profile[0]
height = float(profile[1])
weight = float(profile[2])
p.close()


class Garden(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("My Healthy Garden")
        self.master.geometry("400x480")
        self.master.resizable(False, False)
        self.pack(fill="both")
        # 規則的圖片
        self.imagerule = ImageTk.PhotoImage(file="rule.png")
        # 食物的圖片
        self.imagemilk = ImageTk.PhotoImage(file="milk.png")
        self.imagefruit = ImageTk.PhotoImage(file="apple.png")
        self.imagevegetable = ImageTk.PhotoImage(file="lettuce.png")
        self.imageprotein = ImageTk.PhotoImage(file="fried-egg.png")
        self.imagegrain = ImageTk.PhotoImage(file="rice.png")
        # 花的圖片(預設)
        self.imagegrass = ImageTk.PhotoImage(file = "grass.png")
        self.imageflower = ImageTk.PhotoImage(file = "tulip.png")  # 花
        self.imageflower1 = ImageTk.PhotoImage(file = "sunflower.png")
        self.imageflower2 = ImageTk.PhotoImage(file="floral.png")
        self.imagebug = ImageTk.PhotoImage(file = "tulip_bug.png")  # 一隻蟲
        self.imagebug1 = ImageTk.PhotoImage(file="sunflower_bug.png")
        self.imagebug2 = ImageTk.PhotoImage(file="floral_bug.png")
        self.imagetwobug = ImageTk.PhotoImage(file="tulip_bug2.png")  # 兩隻蟲
        self.imagetwobug1 = ImageTk.PhotoImage(file="sunflower_bug2.png")
        self.imagetwobug2 = ImageTk.PhotoImage(file="floral_bug2.png")
        self.createWidgets()
        self.f1 = tkFont.Font(size = 24, family = "Courier New")
        self.f2 = tkFont.Font(size = 18, family = "Courier New")
        self.f3 = tkFont.Font(size = 15, family = "Courier New")
        self.varSex = tk.IntVar()
        self.varSex.set(1)       # 預設值1=男
        self.flower = garden

# 主框架
    def createWidgets(self):

        f1 = tkFont.Font(size = 20, family = "Courier New")
        f2 = tkFont.Font(size = 18, family = "Courier New")
        f3 = tkFont.Font(size = 15, family = "Courier New")
        
        self.frmMain = tk.Frame(self, bg=self.cget("background"), height=480, width=400)
        self.frmMain.pack(side = "top")
        
        self.lblGarden = tk.Label(self, text="歡迎來到健康花園!",
                                  bg='LightSteelBlue3', font=f1)
        self.lblRule = tk.Label(self, image=self.imagerule)

        self.btnStart = tk.Button(self, text="開始", bg='LightSteelBlue3',
                                  command=self.createset if used == "1000" else self.creategarden, font=f3)

        self.btnGarden = tk.Button(self, text = "花園", bg = 'LightSteelBlue2',
                                   command = self.creategarden, font = f2)
        self.btnProfile = tk.Button(self, text = "檔案", bg = 'LightSteelBlue2',
                                   command = self.createprofile, font = f2)
        self.btnFood = tk.Button(self, text = "食物", bg = 'LightSteelBlue3',
                                 command = self.createfood, font = f2) 
        self.btnSet = tk.Button(self, text = "設定", bg = 'LightSteelBlue3',
                                 command = self.createset, font = f2) 

        self.lblGarden.place(x=0, y=0, height = 60, width = 400)
        self.btnProfile.place(x=0, y=440, height = 40, width = 100)
        self.btnFood.place(x=100, y=440, height = 40, width = 100)
        self.btnGarden.place(x=200, y=440, height = 40, width = 100)
        self.btnSet.place(x=300, y=440, height = 40, width = 100)
        self.lblRule.place(x=20, y=80, height=300, width=360)
        self.btnStart.place(x=20, y=370, height=50, width=360)

# 資訊介面
    def createprofile(self):

        self.frmMain2 = tk.Frame(self, bg=self.cget("background"))
        self.frmMain2.place(x=0, y=0, height=440, width=400)
        
        self.lblProfile = tk.Label(self, text = name +  "的檔案", bg = 'LightSteelBlue3', font = self.f1)
        self.lblProfile.place(x=0, y=0, height = 60, width = 400)

        self.frmHeight = tk.Frame(self, bg='thistle2')
        self.frmHeight.place(x=20, y=80, height=100, width=120)

        self.frmWeight = tk.Frame(self, bg='bisque')
        self.frmWeight.place(x=140, y=80, height=100, width=120)

        self.frmBMI = tk.Frame(self, bg='linen')
        self.frmBMI.place(x=260, y=80, height=100, width=120)

        self.frmSugkal = tk.Frame(self, bg='LightPink2')
        self.frmSugkal.place(x=20, y=200, height=100, width=360)

        self.frmCurSta = tk.Frame(self, bg='light gray')
        self.frmCurSta.place(x=20, y=320, height=100, width=360)

        self.lblHeight = tk.Label(self, text = "身高\n\n" + str(height) + " CM", bg = 'thistle2', font = self.f3)
        self.lblHeight.place(x=20, y=80, height = 100, width = 120)

        self.lblWeight = tk.Label(self, text = "體重\n\n" + str(weight) + " KG", bg = 'bisque', font = self.f3)
        self.lblWeight.place(x=140, y=80, height = 100, width = 120)

        self.lblBMI = tk.Label(self, text = "BMI\n\n" + ('%.1f' % BMI), bg = 'linen', font = self.f3)
        self.lblBMI.place(x=260, y=80, height = 100, width = 120)

        self.lblSugkal = tk.Label(self, text = "建議每日攝取總熱量\n\n" + str(kalunderlimit) + " kcal ~ " + str(kalupperlimit) + " kcal", bg = 'LightPink2', font = self.f2)
        self.lblSugkal.place(x=20, y=200, height = 100, width = 360)

        self.lblCurSta = tk.Label(self, text = "現在身體狀態\n\n" + str(CurSta), bg = 'light gray', font = self.f2)
        self.lblCurSta.place(x=20, y=320, height = 100, width = 360)

# 食物介面
    def createfood(self):

        self.frmMain3 = tk.Frame(self, bg=self.cget("background"))
        self.frmMain3.place(x=0, y=0, height=440, width=400)
        
        self.lblFood = tk.Label(self, text = name + "的健康餐盤", bg = 'LightSteelBlue3', font = self.f1)
        self.lblFood.place(x=0, y=0, height = 60, width = 400)

        self.btnfoodNote = tk.Button(self, text="註", bg="LightSteelBlue3", 
                                       command=self.foodNote, font=self.f2)
        self.btnfoodNote.place(x=340, y=10, height=40, width=40)

        self.btnFruit = tk.Button(self, image=self.imagefruit,
                                  command=self.enterFruit)
        self.btnFruit.place(x=20, y=80, height=120, width=180)

        self.btnMilk = tk.Button(self, image=self.imagemilk,
                                 comman=self.enterMilk)
        self.btnMilk.place(x=200, y=80, height=120, width=180)

        self.btnVegetable = tk.Button(self, image=self.imagevegetable,
                                      command=self.enterVegetable)
        self.btnVegetable.place(x=20, y=200, height=120, width=180)

        self.btnProtein = tk.Button(self, image=self.imageprotein,
                                    command=self.enterProtein)
        self.btnProtein.place(x=200, y=200, height=120, width=180)

        self.btnGrain = tk.Button(self, image=self.imagegrain,
                                  command=self.enterGrain)
        self.btnGrain.place(x=20, y=320, height=100, width=280)

        self.btnConfirm = tk.Button(self, text="OK",
                                    bg='LightSteelBlue3',
                                    command=self.confirmfood, font=self.f2)
        self.btnConfirm.place(x=300, y=320, height=100, width=80)

    def foodNote(self):  # 食物份數註解
        tkinter.messagebox.showinfo('一天所需份數說明', '1.水果類：體重÷20(份)，1份=2/3碗\r'
                                    + '2.奶類：2份，1份=240c.c.\r'
                                    + '3.蔬菜類：比水果多1份，1份=煮熟後2/3碗\r'
                                    + '4.蛋豆魚肉類：體重÷10(份) - 2，魚肉、瘦肉1份=半個手掌大、雞蛋1份=1顆\r'
                                    + '5.五穀根莖類：體重÷20(碗)，1碗=1平碗')

    def enterFruit(self):
        self.frmFruit = tk.Frame(self, bg='thistle2')
        self.frmFruit.place(x=20, y=80, height=120, width=180)

        self.lblFruit = tk.Label(self, text="水果類",
                                 bg='thistle2', font=self.f2)
        self.lblFruit.place(x=40, y=100, height=50, width=140)

        self.spinboxFruit = tk.Spinbox(self, from_=0, to=9.5, format='%.1f',
                                       increment=0.5, bg='thistle2',
                                       font=self.f2)
        self.spinboxFruit.place(x=60, y=150, height=25, width=70)
        self.lbl2Fruit = tk.Label(self, text="份", bg='thistle2', font=self.f2)
        self.lbl2Fruit.place(x=130, y=150, height=25, width=70)

    def enterMilk(self):
        self.frmMilk = tk.Frame(self, bg='bisque', height=120, width=180)
        self.frmMilk.place(x=200, y=80)

        self.lblMilk = tk.Label(self, text="奶類", bg='bisque', font=self.f2)
        self.lblMilk.place(x=220, y=100, height=50, width=140)

        self.spinboxMilk = tk.Spinbox(self, from_=0, to=9.5, format='%.1f',
                                      increment=0.5, bg='bisque', font=self.f2)
        self.spinboxMilk.place(x=240, y=150, height=25, width=70)
        self.lbl2Milk = tk.Label(self, text="份", bg='bisque', font=self.f2)
        self.lbl2Milk.place(x=310, y=150, height=25, width=70)

    def enterVegetable(self):
        self.frmVegetable = tk.Frame(self, bg='linen')
        self.frmVegetable.place(x=20, y=200, height=120, width=180)

        self.lblVegetable = tk.Label(self, text="蔬菜類",
                                     bg='linen', font=self.f2)
        self.lblVegetable.place(x=40, y=220, height=50, width=140)

        self.spinboxVegetable = tk.Spinbox(self, from_=0, to=9.5,
                                           format='%.1f', increment=0.5,
                                           bg='linen', font=self.f2)
        self.spinboxVegetable.place(x=60, y=270, height=25, width=70)
        self.lbl2Vegetable = tk.Label(self, text="份", bg='linen', font=self.f2)
        self.lbl2Vegetable.place(x=130, y=270, height=25, width=70)

    def enterProtein(self):
        self.frmProtein = tk.Frame(self, bg='LightPink2')
        self.frmProtein.place(x=200, y=200, height=120, width=180)

        self.lblProtein = tk.Label(self, text="蛋豆魚肉類",
                                   bg='LightPink2', font=self.f2)
        self.lblProtein.place(x=220, y=220, height=50, width=140)

        self.spinboxProtein = tk.Spinbox(self, from_=0, to=9.5,
                                         format='%.1f', increment=0.5,
                                         bg='LightPink2', font=self.f2)
        self.spinboxProtein.place(x=240, y=270, height=25, width=70)
        self.lbl2Protein = tk.Label(self, text="份",
                                    bg='LightPink2', font=self.f2)
        self.lbl2Protein.place(x=310, y=270, height=25, width=70)

    def enterGrain(self):
        self.frmGrain = tk.Frame(self, bg='light gray')
        self.frmGrain.place(x=20, y=320, height=100, width=280)

        self.lblGrain = tk.Label(self, text="五穀根莖類",
                                 bg='light gray', font=self.f2)
        self.lblGrain.place(x=85, y=325, height=50, width=140)

        self.spinboxGrain = tk.Spinbox(self, from_=0, to=9.5,
                                       format='%.1f', increment=0.5,
                                       bg='light gray', font=self.f2)
        self.spinboxGrain.place(x=120, y=370, height=25, width=70)
        self.lbl2Grain = tk.Label(self, text="份",
                                  bg='light gray', font=self.f2)
        self.lbl2Grain.place(x=190, y=370, height=25, width=70) 

# 花園介面
    def creategarden(self):
        
        self.frmMain4 = tk.Frame(self, bg=self.cget("background"))
        self.frmMain4.place(x=0, y=0, height=440, width=400)
        
        self.lblGarden2 = tk.Label(self, text = name +  "的健康花園", bg = 'LightSteelBlue3', font = self.f1)
        self.lblGarden2.place(x=0, y=0, height = 60, width = 400)
        
        for i in range(30):

            for n in range(31):
                if self.flower[i] == n:
                    grass = tk.Label(self, image = self.imagegrass,
                                    height = 60, width = 60)
                    grass.place(x = 20 + (i%6)*60, y = 100 + (i//6)*60)


            if self.flower[i] == 100:
                flower = tk.Label(self, image = self.imageflower,
                                height = 60, width = 60)
                flower.place(x = 20 + (i%6)*60, y = 100 + (i//6)*60)

                
            if self.flower[i] == 101:
                flower = tk.Label(self, image = self.imageflower1,
                                height = 60, width = 60)
                flower.place(x = 20 + (i%6)*60, y = 100 + (i//6)*60)

                
            if self.flower[i] == 102:
                flower = tk.Label(self, image = self.imageflower2,
                                height = 60, width = 60)
                flower.place(x = 20 + (i%6)*60, y = 100 + (i//6)*60)

                
            if self.flower[i] == -100:
                bug = tk.Label(self, image = self.imagebug,
                                             height = 60, width = 60)
                bug.place(x = 20 + (i%6)*60, y = 100 + (i//6)*60)


            if self.flower[i] == -101:
                bug = tk.Label(self, image = self.imagebug1,
                                             height = 60, width = 60)
                bug.place(x = 20 + (i%6)*60, y = 100 + (i//6)*60)

                
            if self.flower[i] == -102:
                bug = tk.Label(self, image = self.imagebug2,
                                             height = 60, width = 60)
                bug.place(x = 20 + (i%6)*60, y = 100 + (i//6)*60)


            if self.flower[i] == -200:
                bug = tk.Label(self, image = self.imagetwobug,
                                             height = 60, width = 60)
                bug.place(x = 20 + (i%6)*60, y = 100 + (i//6)*60)

                
            if self.flower[i] == -201:
                bug = tk.Label(self, image = self.imagetwobug1,
                                             height = 60, width = 60)
                bug.place(x = 20 + (i%6)*60, y = 100 + (i//6)*60)

                
            if self.flower[i] == -202:
                bug = tk.Label(self, image = self.imagetwobug2,
                                             height = 60, width = 60)
                bug.place(x = 20 + (i%6)*60, y = 100 + (i//6)*60)



# 設定介面
    def createset(self):

        self.frmMain5 = tk.Frame(self, bg=self.cget("background"))
        self.frmMain5.place(x=0, y=0, height=440, width=400)
        
        self.lblSet = tk.Label(self, text = "設定", bg = 'LightSteelBlue3', font = self.f1)
        self.lblSet.place(x=0, y=0, height = 60, width = 400)

        self.lblUser = tk.Label(self, text = "姓名", bg='thistle2', font = self.f3)
        self.lblUser.place(x=40, y=80, height=40, width=110)

        self.lblCM = tk.Label(self, text = "身高", bg='bisque', font = self.f3)
        self.lblCM.place(x=40, y=140, height=40, width=110)

        self.lblKG = tk.Label(self, text = "體重", bg='linen', font = self.f3)
        self.lblKG.place(x=40, y=200, height=40, width=110)

        self.lblGender = tk.Label(self, text = "性別", bg='LightPink2', font = self.f3)
        self.lblGender.place(x=40, y=260, height=40, width=110)

        self.lblActivity = tk.Label(self, text = "活動量", bg='light gray', font = self.f3)
        self.lblActivity.place(x=40, y=320, height=40, width=110)

        self.entUser = tk.Entry(self, bg=self.cget("background"), font = self.f3)
        self.entUser.place(x=160, y=80, height = 40, width = 200)

        self.entCM = tk.Entry(self, bg=self.cget("background"), font = self.f3)
        self.entCM.place(x=160, y=140, height = 40, width = 200)
        
        self.entKG = tk.Entry(self, bg=self.cget("background"), font = self.f3)
        self.entKG.place(x=160, y=200, height = 40, width = 200)
        

        self.genderMale = tk.Radiobutton(self, variable=self.varSex, value=1,text='生理男', font = self.f3)
        self.genderMale.place(x=160, y=260, height = 40, width = 100)
        self.genderFemale = tk.Radiobutton(self, variable=self.varSex, value=0,text='生理女', font = self.f3)
        self.genderFemale.place(x=260, y=260, height = 40, width = 100)
        
        self.activityinput = ttk.Combobox(self,value=["輕度工作","中度工作","重度工作"], font = self.f3)
        self.activityinput.place(x=160, y=320, height = 40, width = 150) # 下拉式選單
        self.activityinput.current(1)
        self.btnactiveNote = tk.Button(self, text="註", bg="light gray", 
                                       command=self.activitynote, font=self.f3)
        self.btnactiveNote.place(x=320, y=320, height=40, width=40)
        
        self.btnEnter = tk.Button(self, text = "完成", bg = 'LightSteelBlue3', command = self.enter, font = self.f3)
        self.btnEnter.place(x=150, y=380, height = 40, width = 100)

        self.btnreset = tk.Button(self, text = "重製", bg="light gray", command = self.reset, font = self.f3)
        self.btnreset.place(x=320, y=380, height = 40, width = 60)

    def activitynote(self):  # 工作量說明
        tkinter.messagebox.showinfo('說明', '1.輕度工作：大部分從事靜態或坐著的工作，如家庭主婦、坐辦公室的上班族、售貨員等\r'
                                    + '2.中度工作：從事機械操作、接待或家事等站立活動較多的工作，如褓母、護士、服務生等\r'
                                    +  '3.重度工作：從事農耕、漁業、建築等重度使用體力之工作，如運動員、搬家工人等')

    def enter(self):
        lst_garden = open('list.txt', mode='w')
        lst_used = open('used.txt', mode='w')
        flowerstr = []
        for i in range(len(self.flower)):
            flowerstr.append(str(self.flower[i]))
        to_txt = ','.join(flowerstr)
        lst_garden.write(to_txt)
        lst_used.write('1001')
        lst_garden.close()
        lst_used.close()

        global name, height, weight, BMI, kalupperlimit, kalunderlimit, ActiveSta, CurSta, fruitlimit, milklimit, proteinlimit, grainlimit
        name = str(self.entUser.get())
        height = float(self.entCM.get())
        weight = float(self.entKG.get())

        with open(file="profile.txt", mode='w', encoding='utf-8') as p:
            p.write(name + str(',') + str(height) + str(',') + str(weight))
            # p.write(str(height))
            # p.write(str(weight))
            p.close()

        gender = self.varSex.get()  # 1代表男生 0代表女生 
        BMI = weight/((height/100)*(height/100))
        ActiveSta = str(self.activityinput.get())
        if ActiveSta == '輕度工作':
            if BMI < 18.5:  # 需要增重
                CurSta = "體重過輕"
                kalupperlimit = 35*weight + 100
                kalunderlimit = 35 * weight - 100
            elif 18.5 <= BMI < 24:  # 體重正常
                CurSta = "體重正常"
                kalupperlimit = 30 * weight + 100
                kalunderlimit = 30 * weight - 100
            elif BMI >= 24:  # 需要減重
                CurSta = "體重過重"
                kalupperlimit = 25 * weight + 100
                kalunderlimit = 25 * weight - 100
        elif ActiveSta == '中度工作':
            if BMI < 18.5:  # 需要增重
                CurSta = "體重過輕"
                kalupperlimit = 40 * weight + 100
                kalunderlimit = 40 * weight - 100
            elif 18.5 <= BMI < 24:  # 體重正常
                CurSta = "體重正常"
                kalupperlimit = 35 * weight + 100
                kalunderlimit = 35 * weight - 100
            elif BMI >= 24:  # 需要減重
                CurSta = "體重過重"
                kalupperlimit = 30 * weight + 100
                kalunderlimit = 30 * weight - 100
        elif ActiveSta == '重度工作':
            if BMI < 18.5:  # 需要增重
                CurSta = "體重過輕"
                kalupperlimit = 45 * weight + 100
                kalunderlimit = 45 * weight - 100
            elif 18.5 <= BMI < 24:  # 體重正常
                CurSta = "體重正常"
                kalupperlimit = 40 * weight + 100
                kalunderlimit = 40 * weight - 100
            elif BMI >= 24:  # 需要減重
                CurSta = "體重過重"
                kalupperlimit = 35 * weight + 100
                kalunderlimit = 35 * weight - 100

        # 稍微放低標準(原本的全部-1)
        fruitlimit = (weight/20) - 1
        milklimit = 1
        vegetablelimit = ((weight/20)-1)+1
        proteinlimit = weight/10 - 1
        grainlimit = (weight/20) - 1

        self.createWidgets()
        self.createprofile()

    def confirmfood(self):
        lst_garden = open('list.txt', mode='w')
        self.flower_kind = [100, 101, 102]  # 三種不同花
        self.one_bug = [-100, -101, -102]  # 三種不同花長一隻蟲
        self.two_bug = [-200, -201, -202]  # 三種不同花長兩隻蟲


        # 達到30朵花就破關
        time2end = self.ending()
        if time2end is True:
            self.creategarden()
            tkinter.messagebox.showinfo('END', "CONGRATS\n" + "You Are Healthy!")
        else:
            check = 0
    
            totalkal = (float(self.spinboxFruit.get())*60 + float(self.spinboxMilk.get())*150
            + float(self.spinboxVegetable.get())*25 + float(self.spinboxProtein.get())*75
            + float(self.spinboxGrain.get())*70)  # 計算總大卡
    
            # 看食物份數是否達標
            if float(self.spinboxFruit.get()) > fruitlimit and float(self.spinboxMilk.get()) > milklimit and float(self.spinboxVegetable.get()) > vegetablelimit and float(self.spinboxProtein.get()) > proteinlimit and float(self.spinboxGrain.get()) > grainlimit:
                if kalunderlimit < totalkal < kalupperlimit:  # 看總大卡是否達標
                    check = 1
    
            if check != 1:
                check = -1
                for n in range(len(self.flower)):
                    if self.flower[n] > 30 or self.flower[n] < 0:  # 場上有花或有一隻蟲的花
                        check = 0
                        break
    
            if check == 1:  # 達成兩個條件-->長花/除蟲
    
                flag = 1  # 先預設花園裡沒有蟲
                for i in range(len(self.flower)):
                    if self.flower[i] == -100 or self.flower[i] == -101 or self.flower[i] == -102 or self.flower[i] == -200 or self.flower[i] == -201 or self.flower[i] == -202:  # 花園裡有蟲->flag = 0
                        flag = 0
    
                if flag == 1:  # 完全沒有蟲-->長花
                    while True:
                        grow_flower = random.randint(1, 30)  # 隨機選一個格子長花
                        flower_kind = random.randint(100, 102)  # 隨機選一種花長
                        if grow_flower in self.flower:  # 如果該格子還沒有長花，就長一朵花
                            self.flower[grow_flower-1] = self.flower_kind[flower_kind-100]    
                            self.creategarden()                        
                            tkinter.messagebox.showinfo('成功長花', '成功長出新的花花囉！\n' + '總大卡：' + str(totalkal) + "卡")
                            flowerstr = []
                            for i in range(len(self.flower)):
                                flowerstr.append(str(self.flower[i]))
                            to_txt = ','.join(flowerstr)
                            lst_garden.write(to_txt)
                            lst_garden.close()
                            break
    
                else:  # 有長蟲-->除蟲
                    for n in range(len(self.flower)):
                        if self.flower[n] == -200 or self.flower[n] == -201 or self.flower[n] == -202:
                            two_bugs = []
                            for i in range(30):
                                if self.flower[i] == -200 or self.flower[i] == -201 or self.flower[i] == -202:
                                    two_bugs.append(i)
                            kill_bug = random.sample(two_bugs, 1)  # 隨機抽出一個長了2隻蟲的花的index
                            if self.flower[kill_bug[0]] == -200:
                                self.flower[kill_bug[0]] = -100  # 把那朵花的蟲殺死一隻
                                self.creategarden()
                                tkinter.messagebox.showinfo('成功驅蟲', '成功驅蟲\n' + '總大卡：' + str(totalkal) + "卡")
                                flowerstr = []
                                for i in range(len(self.flower)):
                                    flowerstr.append(str(self.flower[i]))
                                    to_txt = ','.join(flowerstr)
                                lst_garden.write(to_txt)
                                lst_garden.close()
                                break
                            elif self.flower[kill_bug[0]] == -201:
                                self.flower[kill_bug[0]] = -101
                                self.creategarden()
                                tkinter.messagebox.showinfo('成功驅蟲', '成功驅蟲\n' + '總大卡：' + str(totalkal) + "卡")
                                flowerstr = []
                                for i in range(len(self.flower)):
                                    flowerstr.append(str(self.flower[i]))
                                to_txt = ','.join(flowerstr)
                                lst_garden.write(to_txt)
                                lst_garden.close()
                                # used = 1001
                                break
                            elif self.flower[kill_bug[0]] == -202:
                                self.flower[kill_bug[0]] = -102
                                self.creategarden()
                                tkinter.messagebox.showinfo('成功驅蟲', '成功驅蟲\n' + '總大卡：' + str(totalkal) + "卡")
                                flowerstr = []
                                for i in range(len(self.flower)):
                                    flowerstr.append(str(self.flower[i]))
                                to_txt = ','.join(flowerstr)
                                lst_garden.write(to_txt)
                                lst_garden.close()
                                break
                            
    
                    else:  # 場上的花都只長一隻蟲的情況->隨便找一朵除蟲
                        one_bug = []
                        for i in range(len(self.flower)):
                            if self.flower[i] == -100 or self.flower[i] == -101 or self.flower[i] == -102:
                                one_bug.append(i)
                        kill_bug = random.sample(one_bug, 1)
                        if self.flower[kill_bug[0]] == -100:
                            self.flower[kill_bug[0]] = 100  # 把那朵花的蟲殺死
                        elif self.flower[kill_bug[0]] == -101:
                            self.flower[kill_bug[0]] = 101
                        elif self.flower[kill_bug[0]] == -102:
                            self.flower[kill_bug[0]] = 102  # 把那一隻蟲除掉
                        self.creategarden()
                        tkinter.messagebox.showinfo('成功驅蟲', '成功驅蟲\n' + '總大卡：' + str(totalkal) + "卡")
                        flowerstr = []
                        for i in range(len(self.flower)):
                            flowerstr.append(str(self.flower[i]))
                        to_txt = ','.join(flowerstr)
                        lst_garden.write(to_txt)
                        lst_garden.close()
    
            if check == 0:  # 未達標(check == 0)->長蟲/吃花
                check1 = 0
                for n in range(len(self.flower)):
                    if self.flower[n] == -200 or self.flower[n] == -201 or self.flower[n] == -202: # 若花園裡有-2的花->那些花會死掉(因為蟲長了2天)，變回它所在位置的數字(空地)
                        two_bugs = []
                        for i in range(len(self.flower)):
                            if self.flower[i] == -200 or self.flower[i] == -201 or self.flower[i] == -202:
                                two_bugs.append(i)
                        for k in range(len(two_bugs)):
                            self.flower[two_bugs[k]] = two_bugs[k] + 1  # 該格子變回原本的編號(空地)
                            check1 = 1
                    if check1 == 1:
                        break

                if check1 == 1:
                    self.creategarden()
                    tkinter.messagebox.showinfo('花被蟲吃掉了', '啊啊啊...花被蟲吃掉了啦！！\n' + '總大卡：' + str(totalkal) + "卡")
                    flowerstr = []
                    for i in range(len(self.flower)):
                        flowerstr.append(str(self.flower[i]))
                    to_txt = ','.join(flowerstr)
                    lst_garden.write(to_txt)
                    lst_garden.close()
    
                else:  # 花園裡沒有-2的花->原本-1的花變-2或長出一隻新蟲
    
                    flower_bug = []
                    
                    for i in range(len(self.flower)):
                        if self.flower[i] == -100 or self.flower[i] == -101 or self.flower[i] == -102 or self.flower[i] == 100 or self.flower[i] == 101 or self.flower[i] == 102:
                            flower_bug.append(i)
                
                    grow_bug = random.sample(flower_bug, 1)
                    if self.flower[grow_bug[0]] == 100:  # 讓有一隻蟲的花再長一隻蟲
                        self.flower[grow_bug[0]] = -100
                    elif self.flower[grow_bug[0]] == 101:
                        self.flower[grow_bug[0]] = -101
                    elif self.flower[grow_bug[0]] == 102:
                        self.flower[grow_bug[0]] = -102
    
                    elif self.flower[grow_bug[0]] == -100:  # 讓沒長蟲的花長一隻蟲
                        self.flower[grow_bug[0]] = -200
                    elif self.flower[grow_bug[0]] == -101:
                        self.flower[grow_bug[0]] = -201
                    elif self.flower[grow_bug[0]] == -102:
                        self.flower[grow_bug[0]] = -202
                    self.creategarden()
                    tkinter.messagebox.showinfo('長蟲了', '啊 長蟲了\n' + '總大卡：' + str(totalkal) + "卡")
                    flowerstr = []
                    for i in range(len(self.flower)):
                        flowerstr.append(str(self.flower[i]))
                    to_txt = ','.join(flowerstr)
                    lst_garden.write(to_txt)
                    lst_garden.close()

            if check == -1:
                self.creategarden()
                tkinter.messagebox.showinfo('沒花可以長蟲', '沒花可以長蟲 你好可憐\n' + '總大卡：' + str(totalkal) + "卡")
                flowerstr = []
                for i in range(len(self.flower)):
                    flowerstr.append(str(self.flower[i]))
                to_txt = ','.join(flowerstr)
                lst_garden.write(to_txt)
                lst_garden.close()


    def reset(self):
        lst_used = open('used.txt', mode='w')
        lst_used.write('1000')
        lst_used.close()
        
        lst_garden = open('list.txt', mode='w')
        global name, height, weight
        name = "使用者"
        height = 160
        weight = 55
        self.flower = [1, 2, 3, 4, 5, 6,
                       7, 8, 9, 10, 11, 12,
                       13, 14, 101, 16, 17, 18,
                       19, 20, 21, 22, 23, 24,
                       25, 26, 27, 28, 29, 30]
        flowerstr = []
        for i in range(len(self.flower)):
            flowerstr.append(str(self.flower[i]))
        to_txt = ','.join(flowerstr)
        lst_garden.write(to_txt)
        lst_garden.close()
        with open(file="profile.txt", mode='w', encoding='utf-8') as p:
            p.write(name + str(',') + str(height) + str(',') + str(weight))
            p.close()
# ENDING
    def ending(self):
        count = 0
        possibility = {100, 101, 102}
        for flower in self.flower:
            if flower in possibility:
                count += 1
        if count == 30:
            return True
        else:
            return False

food = Garden()
food.mainloop()

# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,101,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
