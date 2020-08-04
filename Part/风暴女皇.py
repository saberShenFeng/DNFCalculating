from math import *
from PublicReference.base import *

class 风暴女皇技能0(主动技能):
    名称 = '背摔'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 1386.43
    成长 = 156.57
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5

class 风暴女皇技能1(主动技能):
    名称 = '抛投'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 3164.50
    成长 = 357.47
    CD = 8.5
    TP成长 = 0.1
    TP上限 = 5

class 风暴女皇技能2(被动技能):
    名称 = '摔技强化'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1 + 0.01 * self.等级, 5)
            else:
                return round(1.1 + 0.02 * (self.等级 - 10), 5)

class 风暴女皇技能3(主动技能):
    名称 = '折颈'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 41
    基础 = 3430.65
    成长 = 387.38
    CD = 7.7
    TP成长 = 0.1
    TP上限 = 5

class 风暴女皇技能4(主动技能):
    名称 = '野蛮冲撞'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 4091.91
    成长 = 462.08
    CD = 8.0
    TP成长 = 0.1
    TP上限 = 5

class 风暴女皇技能5(被动技能):
    名称 = '强力抱摔'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 风暴女皇技能6(主动技能):
    名称 = '霹雳肘击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5348.07
    成长 = 603.95
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5

class 风暴女皇技能7(主动技能):
    名称 = '空绞锤'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 3787.39
    成长 = 436.65
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5

class 风暴女皇技能8(主动技能):
    名称 = '霹雳冲击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 2559.92
    成长 = 289.04
    基础2 = 5835.91
    成长2 = 659.11
    攻击次数2 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

class 风暴女皇技能9(主动技能):
    名称 = '螺旋彗星落'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8630.10
    成长 = 974.93
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.23 

class 风暴女皇技能10(主动技能):
    名称 = '地狱摇篮（抓轰炮）'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 13623.29
    成长 = 1539.26
    CD = 30.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.23 
        
class 风暴女皇技能11(主动技能):
    名称 = '裂石破天'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 15889.25
    成长 = 1794.98
    CD = 45
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.23 

class 风暴女皇技能12(被动技能):
    名称 = '抓取奥义'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.09 + 0.015 * self.等级, 5)

class 风暴女皇技能13(主动技能):
    名称 = '末日风暴'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 1340.79
    成长 = 406.02
    基础2 = 20945.11
    成长2 = 6317.08
    攻击次数2 = 1
    CD = 140.0

class 风暴女皇技能14(主动技能):
    名称 = '空绞连锤（抓轰炮）'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 1170.88
    成长 = 132.08
    基础2 = 14058.93
    成长2 = 1588.06
    攻击次数2 = 1
    CD = 30.0
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.12

class 风暴女皇技能15(被动技能):
    名称 = '极手奥义'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 风暴女皇技能16(主动技能):
    名称 = '死亡摇篮'
    所在等级 = 70
    等级上限 = 60
    基础等级 = 18
    基础 = 25524.88
    成长 = 2883.51
    CD = 45
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.23

class 风暴女皇技能17(主动技能):
    名称 = '末日摇篮'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 7654.70
    成长 = 864.27
    基础2 = 30620.97
    成长2 = 3457.06
    攻击次数2 = 1
    CD = 40.0

class 风暴女皇技能18(主动技能):
    名称 = '风暴之舞'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 5308.98
    成长 = 600.99
    攻击次数 = 6
    基础2 = 14760.91
    成长2 = 1665.05
    攻击次数2 = 1
    CD = 45.0   
class 风暴女皇技能19(主动技能):
    名称 = '苍宇彗星落'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 8601.87
    成长 = 2598.03
    基础2 = 77442.63
    成长2 = 23385.07
    攻击次数2 = 1
    CD = 180

class 风暴女皇技能20(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 风暴女皇技能21(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 风暴女皇技能22(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


风暴女皇技能列表 = []
i = 0
while i >= 0:
    try:
        exec('风暴女皇技能列表.append(风暴女皇技能'+str(i)+'())')
        i += 1
    except:
        i = -1

风暴女皇技能序号 = dict()
for i in range(len(风暴女皇技能列表)):
    风暴女皇技能序号[风暴女皇技能列表[i].名称] = i

风暴女皇一觉序号 = 0
风暴女皇二觉序号 = 0
风暴女皇三觉序号 = 0
for i in 风暴女皇技能列表:
    if i.所在等级 == 50:
        风暴女皇一觉序号 = 风暴女皇技能序号[i.名称]
    if i.所在等级 == 85:
        风暴女皇二觉序号 = 风暴女皇技能序号[i.名称]
    if i.所在等级 == 100:
        风暴女皇三觉序号 = 风暴女皇技能序号[i.名称]

风暴女皇护石选项 = ['无']
for i in 风暴女皇技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        风暴女皇护石选项.append(i.名称)

风暴女皇符文选项 = ['无']
for i in 风暴女皇技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        风暴女皇符文选项.append(i.名称)

class 风暴女皇角色属性(角色属性):

    实际名称 = '风暴女皇'
    角色 = '格斗家(女)'
    职业 = '柔道家'

    武器选项 = ['手套','臂铠','东方棍','爪']
    
    伤害类型选择 = ['物理固伤']
    
    伤害类型 = '物理固伤'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 2.07

    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(风暴女皇技能列表)
        self.技能序号= deepcopy(风暴女皇技能序号)

class 风暴女皇(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 风暴女皇角色属性()
        self.角色属性A = 风暴女皇角色属性()
        self.角色属性B = 风暴女皇角色属性()
        self.一觉序号 = 风暴女皇一觉序号
        self.二觉序号 = 风暴女皇二觉序号
        self.三觉序号 = 风暴女皇三觉序号
        self.护石选项 = deepcopy(风暴女皇护石选项)
        self.符文选项 = deepcopy(风暴女皇符文选项)

    def 界面(self):
        super().界面()

        self.死亡风暴次数选择=MyQComboBox(self.main_frame2)
        for i in range(1, 14):
            self.死亡风暴次数选择.addItem('末日风暴：' + str(i) + '段')
        self.死亡风暴次数选择.setCurrentIndex(12)
        self.死亡风暴次数选择.resize(120,20)
        self.死亡风暴次数选择.move(325,390)   

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        属性.技能栏[属性.技能序号['末日风暴']].攻击次数 *= self.死亡风暴次数选择.currentIndex() + 1