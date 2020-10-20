from PublicReference.base import *

class 绯红玫瑰技能0(主动技能):
    名称 = '致命射击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1281.30
    成长 = 144.70
    CD = 6.2
    TP成长 = 0.1
    TP上限 = 5

class 绯红玫瑰技能1(被动技能):
    名称 = '左轮奥义'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.0 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class 绯红玫瑰技能2(被动技能):
    名称 = '花式枪术'
    所在等级 = 20
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

class 绯红玫瑰技能3(主动技能):
    名称 = '锁链截击'
    所在等级 = 25
    学习间隔 = 3
    SP消耗 = 25
    等级上限 = 60
    学习上限 = 50
    基础等级 = min(int((105 - 所在等级) / 学习间隔 + 1), 学习上限)
    CD = 5.0
    data = [
    #0  第1击多段攻击力 : <data0>%
        [0, 556, 645, 734, 822, 911, 1000, 1089, 1177, 1266, 1355, 1444, 1532, 1621, 1710, 1799, 1887, 1976, 2065, 2154, 2242, 2331, 2420, 2509, 2597, 2686, 2775, 2863, 2952, 3041, 3130, 3218, 3307, 3396, 3485, 3573, 3662, 3751, 3840, 3928, 4017, 4106, 4195, 4283, 4372, 4461, 4550, 4638, 4727, 4816, 4905, 4993, 5082, 5171, 5260, 5348, 5437, 5526, 5615, 5703, 5792],
    #1  第2击攻击力 : <data1>%
        [0, 834, 968, 1101, 1234, 1367, 1500, 1633, 1766, 1899, 2033, 2166, 2299, 2432, 2565, 2698, 2831, 2964, 3097, 3231, 3364, 3497, 3630, 3763, 3896, 4029, 4162, 4295, 4429, 4562, 4695, 4828, 4961, 5094, 5227, 5360, 5494, 5627, 5760, 5893, 6026, 6159, 6292, 6425, 6558, 6692, 6825, 6958, 7091, 7224, 7357, 7490, 7623, 7757, 7890, 8023, 8156, 8289, 8422, 8555, 8688],
    #2  第3击攻击力 : <data2>%
        [0, 834, 968, 1101, 1234, 1367, 1500, 1633, 1766, 1899, 2033, 2166, 2299, 2432, 2565, 2698, 2831, 2964, 3097, 3231, 3364, 3497, 3630, 3763, 3896, 4029, 4162, 4295, 4429, 4562, 4695, 4828, 4961, 5094, 5227, 5360, 5494, 5627, 5760, 5893, 6026, 6159, 6292, 6425, 6558, 6692, 6825, 6958, 7091, 7224, 7357, 7490, 7623, 7757, 7890, 8023, 8156, 8289, 8422, 8555, 8688],
    ]

    #index：   0      1      2      
    rate = [1.000, 1.000, 1.000]
    hits = [1.000, 1.000, 1.000]

    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.hits)):
            sum += self.data[i][self.等级] * self.rate[i] * self.hits[i]
        return self.倍率 * sum

"""
数据描述(已匹配)：
第1击多段攻击力 : <data0>%
第1击多段攻击间隔 : 0.2秒
第2击攻击力 : <data1>%
第3击攻击力 : <data2>%

技能描述：
    使枪刃往垂直方向旋转， 并聚集周围的敌人。 施放技能时， 若再次激活技能键， 则可以将敌人推开； 若此时第二次激活技能键， 则可以将推开的敌人吸附到身边。
"""



class 绯红玫瑰技能4(主动技能):
    名称 = '音速劫击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2789.63
    成长 = 315.38
    CD = 4.4
    TP成长 = 0.1
    TP上限 = 5

class 绯红玫瑰技能5(主动技能):
    名称 = '致命回射'
    所在等级 = 30
    等级上限 = 1
    基础等级 = 1
    CD = 12.5

class 绯红玫瑰技能6(主动技能):
    名称 = '枪舞'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 212.00
    成长 = 24.00
    攻击次数 = 20
    基础2 = 377.30
    成长2 = 42.70
    攻击次数2 = 9
    CD = 17.6
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.9
            self.攻击次数 = 0
            self.攻击次数2 *= (2 * 1.39)
        elif x == 1:
            self.CD *= 0.9
            self.攻击次数 = 0
            self.攻击次数2 *= (2 * 1.49)


class 绯红玫瑰技能7(主动技能):
    名称 = '移动射击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 11618.00
    成长 = 1312.00
    CD = 24.3
    TP成长 = 0.10
    TP上限 = 5

class 绯红玫瑰技能8(主动技能):
    名称 = '多重射击'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 7723.15
    成长 = 871.85
    CD = 19.8
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 = 1.18
        elif x == 1:
            self.倍率 = 1.27

class 绯红玫瑰技能9(主动技能):
    名称 = '双鹰回旋'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 464.17
    成长 = 54.83
    基础2 = 474.00
    成长2 = 56.00
    基础3 = 502.58
    成长3 = 59.42
    攻击次数 = 14
    攻击次数2 = 18
    攻击次数3 = 32
    CD = 44.6
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.倍率 *= 1.15  
            self.倍率 /= 0.8
        elif x == 1:
            self.攻击次数 = 0
            self.攻击次数2 *= 1.1
            self.倍率 *= 1.15
            self.倍率 /= 0.8

class 绯红玫瑰技能10(被动技能):
    名称 = '隐匿切割'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)

class 绯红玫瑰技能11(主动技能):
    名称 = '血腥狂欢'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 38871.42
    成长 = 11779.22
    CD = 145

class 绯红玫瑰技能12(主动技能):
    名称 = '鲜血劫击'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 5698.53
    成长 = 643.47
    基础2 = 6385.12
    成长2 = 720.88
    攻击次数 = 1
    攻击次数2 = 1
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 += 1.47
            self.攻击次数2 = 0
            self.倍率 *= 1.25
        elif x == 1:
            self.攻击次数 += 1.47
            self.攻击次数2 = 0
            self.倍率 *= 1.44

class 绯红玫瑰技能13(主动技能):
    名称 = '压制射击'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 1254.33
    成长 = 141.67
    基础2 = 2789.17
    成长2 = 314.83
    攻击次数 = 20
    攻击次数2 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.185
            self.攻击次数2 *= 1.50
        elif x == 1:
            self.攻击次数 *= 1.185
            self.攻击次数2 *= 2.30

class 绯红玫瑰技能14(被动技能):
    名称 = '枪刃改良'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 绯红玫瑰技能15(主动技能):
    名称 = '死亡锁链'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    基础 = 29878.17
    成长 = 5667.83
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1 + 0.375 * 0.94

class 绯红玫瑰技能16(主动技能):
    名称 = '锁链切割'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 36301.00
    成长 = 4099.00
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.34

class 绯红玫瑰技能17(主动技能):
    名称 = '血舞祭'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 82497.00
    成长 = 24905.00
    CD = 180

class 绯红玫瑰技能18(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 绯红玫瑰技能19(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 绯红玫瑰技能20(被动技能):
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

class 绯红玫瑰技能21(主动技能):
    名称 = '刺踢'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2815.960784
    成长 = 182.0392157
    CD = 4.4
    TP成长 = 0.08
    TP上限 = 5

绯红玫瑰技能列表 = []
i = 0
while i >= 0:
    try:
        exec('绯红玫瑰技能列表.append(绯红玫瑰技能'+str(i)+'())')
        i += 1
    except:
        i = -1

绯红玫瑰技能序号 = dict()
for i in range(len(绯红玫瑰技能列表)):
    绯红玫瑰技能序号[绯红玫瑰技能列表[i].名称] = i

绯红玫瑰一觉序号 = 0
绯红玫瑰二觉序号 = 0
绯红玫瑰三觉序号 = 0
for i in 绯红玫瑰技能列表:
    if i.所在等级 == 50:
        绯红玫瑰一觉序号 = 绯红玫瑰技能序号[i.名称]
    if i.所在等级 == 85:
        绯红玫瑰二觉序号 = 绯红玫瑰技能序号[i.名称]
    if i.所在等级 == 100:
        绯红玫瑰三觉序号 = 绯红玫瑰技能序号[i.名称]

绯红玫瑰护石选项 = ['无']
for i in 绯红玫瑰技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        绯红玫瑰护石选项.append(i.名称)

绯红玫瑰符文选项 = ['无']
for i in 绯红玫瑰技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        绯红玫瑰符文选项.append(i.名称)

class 绯红玫瑰角色属性(角色属性):

    实际名称 = '绯红玫瑰'
    角色 = '神枪手(女)'
    职业 = '漫游枪手'

    武器选项 = ['左轮枪']
    
    伤害类型选择 = ['物理百分比']
    
    伤害类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2.25
   
    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(绯红玫瑰技能列表)
        self.技能序号= deepcopy(绯红玫瑰技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['致命回射']].基础 = self.技能栏[self.技能序号['致命射击']].等效百分比(self.武器类型)*1.25
        self.技能栏[self.技能序号['致命回射']].被动倍率 = self.技能栏[self.技能序号['致命射击']].被动倍率

class 绯红玫瑰(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 绯红玫瑰角色属性()
        self.角色属性A = 绯红玫瑰角色属性()
        self.角色属性B = 绯红玫瑰角色属性()
        self.一觉序号 = 绯红玫瑰一觉序号
        self.二觉序号 = 绯红玫瑰二觉序号
        self.三觉序号 = 绯红玫瑰三觉序号
        self.护石选项 = deepcopy(绯红玫瑰护石选项)
        self.符文选项 = deepcopy(绯红玫瑰符文选项)
