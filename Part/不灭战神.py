from math import *
from PublicReference.base import *

#加站街物理攻击力 10级30%？ 算的28.4%
class 不灭战神技能0(被动技能):
    名称 = '战戟精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        return 1.0

    def 武器倍率(self):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.02 * self.等级, 5)

# 霸王戟=猛攻  有TP0.1
class 不灭战神技能1(被动技能):
    名称 = '战戟猛攻'
    所在等级 = 25
    等级上限 = 30
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1 + 0.005 * self.等级, 5)
        else:
            return round(1.1 + 0.02 * (self.等级 - 20), 5)

    def 物理攻击力倍率进图(self, 武器类型):
        return self.加成倍率(武器类型)

class 不灭战神技能2(被动技能):
    名称 = '战戟之魂'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class 不灭战神技能3(被动技能):
    名称 = '战神之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)


class 不灭战神技能4(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 不灭战神技能5(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class 不灭战神技能6(被动技能):
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


# 霸王机吃精通吗？
class 不灭战神技能7(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class 不灭战神技能8(主动技能):
    名称 = '霸王戟'
    所在等级 = 25
    等级上限 = 1
    基础等级 = 1
    是否主动 = 0
    基础 = 2281
    成长 = 311
    CD = 0.5
    TP成长 = 0.10
    TP上限 = 5


# 果体测试就2段+1段
class 不灭战神技能9(主动技能):
    名称 = '破军突击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2476   #2585 3次  #测试只有2段+1
    成长 = 291   #307
    CD = 5.5
    # TP成长 = 0.10
    # TP上限 = 5


class 不灭战神技能10(主动技能):
    名称 = '追魂斩'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3172
    成长 = 360
    CD = 6.6
    TP成长 = 0.10
    TP上限 = 5


class 不灭战神技能11(主动技能):
    名称 = '落月斩'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4292
    成长 = 483
    CD = 7.7
    TP成长 = 0.10
    TP上限 = 5


class 不灭战神技能12(主动技能):
    名称 = '冷血突刺'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8672
    成长 = 963
    CD = 17.6
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.2


class 不灭战神技能13(主动技能):
    名称 = '破灭斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7081
    成长 = 799
    CD = 15.4
    TP成长 = 0.10
    TP上限 = 5


class 不灭战神技能14(主动技能):
    名称 = '夺命乱舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 10134
    成长 = 1133
    CD = 19.8
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.27


class 不灭战神技能15(主动技能):
    名称 = '横扫八荒'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 18970
    成长 = 2130
    CD = 44
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.2587


class 不灭战神技能16(主动技能):
    名称 = '长虹贯日'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 17551
    成长 = 1979
    CD = 27.5
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.2320

#下劈中了，就不中冲击波。下劈。冲击波不计算伤害
class 不灭战神技能17(主动技能):
    名称 = '穿云裂地斩-下劈'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 33760    #125368
    成长 =  3813  #3813
    #冲击波
    基础2 = 30210
    成长2 = 3411
    攻击次数2 = 0
    CD = 55
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.22

class 不灭战神技能18(主动技能):
    名称 = '破灭轮回刺'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 43816
    成长 = 4948
    CD = 44


class 不灭战神技能19(主动技能):
    名称 = '断魂裂岩斩'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 48000
    成长 = 5433
    CD = 49.5


class 不灭战神技能20(主动技能):
    名称 = '千魂弑'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 44019
    成长 = 13283
    CD = 159.5


class 不灭战神技能21(主动技能):
    名称 = '血战天狱'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 109081
    成长 = 32931
    CD = 198


不灭战神技能列表 = []
i = 0
while i >= 0:
    try:
        exec('不灭战神技能列表.append(不灭战神技能' + str(i) + '())')
        i += 1
    except:
        i = -1

不灭战神技能序号 = dict()
for i in range(len(不灭战神技能列表)):
    不灭战神技能序号[不灭战神技能列表[i].名称] = i

不灭战神一觉序号 = 0
不灭战神二觉序号 = 0
不灭战神三觉序号 = 0
for i in 不灭战神技能列表:
    if i.所在等级 == 50:
        不灭战神一觉序号 = 不灭战神技能序号[i.名称]
    if i.所在等级 == 85:
        不灭战神二觉序号 = 不灭战神技能序号[i.名称]
    if i.所在等级 == 100:
        不灭战神三觉序号 = 不灭战神技能序号[i.名称]

不灭战神护石选项 = ['无']
for i in 不灭战神技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        不灭战神护石选项.append(i.名称)

不灭战神符文选项 = ['无']
for i in 不灭战神技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        不灭战神符文选项.append(i.名称)


class 不灭战神角色属性(角色属性):
    实际名称 = '不灭战神'
    角色 = '魔枪士'
    职业 = '征战者'

    武器选项 = ['战戟']

    伤害类型选择 = ['物理百分比']

    伤害类型 = '物理百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量']

    主BUFF = 1.80

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(不灭战神技能列表)
        self.技能序号 = deepcopy(不灭战神技能序号)

    def 被动倍率计算(self):
        self.技能栏[8].等级 = self.技能栏[1].等级
        self.物理攻击力 = int((self.物理攻击力 - 65) * self.技能栏[0].武器倍率() + 65)
        super().被动倍率计算()

    def 伤害指数计算(self):
        self.进图物理攻击力 = int((self.进图物理攻击力 - 40) * self.技能栏[0].武器倍率() + 40)
        super().伤害指数计算()

class 不灭战神(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 不灭战神角色属性()
        self.角色属性A = 不灭战神角色属性()
        self.角色属性B = 不灭战神角色属性()
        self.一觉序号 = 不灭战神一觉序号
        self.二觉序号 = 不灭战神二觉序号
        self.三觉序号 = 不灭战神三觉序号
        self.护石选项 = deepcopy(不灭战神护石选项)
        self.符文选项 = deepcopy(不灭战神符文选项)
