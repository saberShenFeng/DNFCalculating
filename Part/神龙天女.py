﻿from math import *
from PublicReference.base import *

class 神龙天女主动技能(主动技能):
    def 等效CD(self, 武器类型):
        return round(self.CD  / self.恢复 * 1.05, 1)
        #念珠1.05

class 神龙天女技能0(神龙天女主动技能):
    名称 = '罪业加身'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 2014 - 204.4468
    成长 = 204.4468
    CD = 6.0
    TP成长 = 0.08
    TP上限 = 5

class 神龙天女技能1(神龙天女主动技能):
    名称 = '唤雷符'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1721 - 174.644
    成长 = 174.644
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5

class 神龙天女技能2(神龙天女主动技能):
    名称 = '念珠连射'
    备注 = '(TP为基础精通)'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    基础 = 9195.58 / 9.362
    成长 = 0
    CD = 1.0
    TP成长 = 0.1
    TP上限 = 3

class 神龙天女技能3(神龙天女主动技能):
    名称 = '木槵子经'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1602 - 163.6
    成长 = 163.6
    CD = 4.0
    TP成长 = 0.1
    TP上限 = 5

class 神龙天女技能4(神龙天女主动技能):
    名称 = '束灵符'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2052 - 208.214
    成长 = 208.214
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 5

class 神龙天女技能5(神龙天女主动技能):
    名称 = '驱邪咒'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 5100 - 519
    成长 = 519
    CD = 12.0
    TP上限 = 5
    TP倍率 = [1, 1.125, 1.228, 1.330, 1.433, 1.535]

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.基础 + self.成长 * self.等级)* self.TP倍率[self.TP等级] * self.倍率)

class 神龙天女技能6(被动技能):
    名称 = '祈雨祭'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)

class 神龙天女技能7(被动技能):
    名称 = '神术强化'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.05 + 0.015 * self.等级, 5)
        else:
            return round(1.00 + 0.02 * self.等级, 5)

class 神龙天女技能8(神龙天女主动技能):
    名称 = '和合之玉'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5233 - 531.108
    成长 = 531.108
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 5

class 神龙天女技能9(神龙天女主动技能):
    名称 = '聚魂吸星符'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6004 - 609.629
    成长 = 609.629
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
                self.倍率 *= 1.2964
                self.CD *= 0.95
        elif x == 1:
                self.倍率 *= 1.3779
                self.CD *= 0.95



class 神龙天女技能10(神龙天女主动技能):
    名称 = '龙魂之怒'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 8116 - 823.406
    成长 = 823.406
    CD = 20.0
    TP成长 = 0.1
    TP上限 = 5

class 神龙天女技能11(神龙天女主动技能):
    名称 = '百八念珠'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 13060 - 1326.25
    成长 = 1326.25
    CD = 25.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
                self.倍率 *= 1.18
                self.CD *= 0.83
        elif x == 1:
                self.倍率 *= 1.27
                self.CD *= 0.83

class 神龙天女技能12(神龙天女主动技能):
    名称 = '不动珠箔阵'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 16138 - 1635.567
    成长 = 1635.567
    CD = 45.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
                self.倍率 *= 1.09
                self.CD *= 0.9
        elif x == 1:
                self.倍率 *= 1.17
                self.CD *= 0.9

class 神龙天女技能13(神龙天女主动技能):
    名称 = '神龙如意珠'
    备注 = '(1次)'
    是否主动 = 0
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    基础 = 526 - 83.947
    成长 = 83.947
    CD = 0.5
    关联技能 = ['所有']
    def 等效CD(self, 武器类型):
        return 0.5
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.115 + 0.015 * self.等级, 5)  

class 神龙天女技能14(神龙天女主动技能):
    名称 = '神谕：神龙雷雨祭'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 45113 - 10407
    成长 = 10407
    CD = 140

class 神龙天女技能15(神龙天女主动技能):
    名称 = '因果业火符'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 13346 - 1354.864
    成长 = 1354.864
    CD = 30.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
                self.倍率 *= 1.24
        elif x == 1:
                self.倍率 *= 1.33

class 神龙天女技能16(神龙天女主动技能):
    名称 = '夺命大念阵'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 24291 - 2464.235
    成长 = 2464.235
    CD = 50.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
                self.倍率 *= 1.24
        elif x == 1:
                self.倍率 *= 1.32

class 神龙天女技能17(被动技能):
    名称 = '龙神之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)

class 神龙天女技能18(神龙天女主动技能):
    名称 = '退魔阴阳符'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 42399 - 4303.067
    成长 = 4303.067
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.32

class 神龙天女技能19(神龙天女主动技能):
    名称 = '天坠阴阳玉'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 40585 - 4117.917
    成长 = 4117.917
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.288
            self.CD *= 0.86

class 神龙天女技能20(神龙天女主动技能):
    名称 = '龙威如狱·龙恩如海'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 92783 - 21518
    成长 = 21518
    CD = 180.0

class 神龙天女技能21(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 神龙天女技能22(被动技能):
     名称 = '超卓之心'
     所在等级 = 95
     等级上限 = 11
     基础等级 = 1
     def 加成倍率(self, 武器类型):
         if self.等级 == 0:
             return 1.0
         else:
             return round(1.045 + 0.005 * self.等级, 5)

class 神龙天女技能23(被动技能):
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

class 神龙天女技能24(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['念珠连射']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

神龙天女技能列表 = []
i = 0
while i >= 0:
    try:
        exec('神龙天女技能列表.append(神龙天女技能'+str(i)+'())')
        i += 1
    except:
        i = -1

神龙天女技能序号 = dict()
for i in range(len(神龙天女技能列表)):
    神龙天女技能序号[神龙天女技能列表[i].名称] = i

神龙天女一觉序号 = 0
神龙天女二觉序号 = 0
神龙天女三觉序号 = 0
for i in 神龙天女技能列表:
    if i.所在等级 == 50:
        神龙天女一觉序号 = 神龙天女技能序号[i.名称]
    if i.所在等级 == 85:
        神龙天女二觉序号 = 神龙天女技能序号[i.名称]
    if i.所在等级 == 100:
        神龙天女三觉序号 = 神龙天女技能序号[i.名称]

神龙天女护石选项 = ['无']
for i in 神龙天女技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        神龙天女护石选项.append(i.名称)

神龙天女符文选项 = ['无']
for i in 神龙天女技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        神龙天女符文选项.append(i.名称)

class 神龙天女角色属性(角色属性):

    实际名称 = '神龙天女'
    角色 = '圣职者(女)'
    职业 = '巫女'

    武器选项 = ['念珠']
    
    伤害类型选择 = ['魔法百分比']
    
    伤害类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 2.08
   
    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(神龙天女技能列表)
        self.技能序号= deepcopy(神龙天女技能序号)

class 神龙天女(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 神龙天女角色属性()
        self.角色属性A = 神龙天女角色属性()
        self.角色属性B = 神龙天女角色属性()
        self.一觉序号 = 神龙天女一觉序号
        self.二觉序号 = 神龙天女二觉序号
        self.三觉序号 = 神龙天女三觉序号
        self.护石选项 = deepcopy(神龙天女护石选项)
        self.符文选项 = deepcopy(神龙天女符文选项)