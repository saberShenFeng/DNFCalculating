﻿from math import *
from decimal import *

from PublicReference.base import *

class 刹那永恒主动技能(主动技能):

    def 等效CD(self, 武器类型):
        if 武器类型 == '魔杖':
            return round(self.CD / self.恢复 * 1, 1)
        if 武器类型 == '法杖':
            return round(self.CD / self.恢复 * 1.1, 1)

刹那永恒等级 = 100 + 5

class 刹那永恒技能0(刹那永恒主动技能):
    名称 = '冰魄剑'
    所在等级 = 15
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 627, 689, 755, 821, 885, 946, 1011, 1075, 1143, 1207, 1272, 1333, 1397, 1466, 1528, 1595, 1661, 1728, 1792, 1854, 1920, 1982, 2050, 2115, 2179, 2240, 2306, 2372, 2437, 2502, 2565, 2627, 2694, 2759, 2824, 2887, 2952, 3018, 3081, 3146, 3208, 3275, 3342, 3404, 3473, 3534, 3601, 3666, 3730, 3795, 3859, 3924, 3988, 4052, 4117, 4181, 4246, 4311, 4378, 4440, 4506, 4569, 4635, 4699, 4765, 4827, 4893, 4956, 5022, 5088]
    攻击次数 = 2
    数据2 = [0, 750, 827, 905, 979, 1058, 1136, 1214, 1292, 1372, 1449, 1527, 1602, 1680, 1758, 1835, 1915, 1994, 2070, 2149, 2223, 2301, 2380, 2458, 2537, 2615, 2692, 2771, 2845, 2924, 3002, 3077, 3157, 3231, 3309, 3388, 3464, 3544, 3618, 3696, 3775, 3850, 3931, 4005, 4082, 4167, 4246, 4321, 4399, 4476, 4552, 4629, 4708, 4786, 4865, 4939, 5017, 5096, 5172, 5252, 5329, 5409, 5483, 5560, 5640, 5716, 5795, 5873, 5951, 6026, 6104]
    攻击次数2 = 1
    演出时间 = 1.0
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.攻击次数 + self.数据2[self.等级] * (1 + self.TP成长 * self.TP等级) * self.攻击次数2) * self.倍率

    def 技能形态改变(self):
        self.攻击次数2 = 0

class 刹那永恒技能1(被动技能):
    名称 = '冰武精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.01 * self.等级, 5)

class 刹那永恒技能2(刹那永恒主动技能):
    名称 = '寒冰连枪'
    所在等级 = 20
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 355, 391, 427, 463, 499, 535, 572, 608, 644, 680, 716, 752, 788, 824, 860, 896, 932, 968, 1004, 1041, 1077, 1113, 1149, 1185, 1221, 1257, 1293, 1329, 1365, 1401, 1437, 1473, 1510, 1546, 1582, 1618, 1654, 1690, 1726, 1762, 1798, 1834, 1870, 1906, 1942, 1978, 2015, 2051, 2087, 2123, 2159, 2195, 2231, 2267, 2303, 2339, 2375, 2411, 2447, 2484, 2520, 2556, 2592, 2628, 2664, 2700, 2736, 2772, 2808, 2844]
    攻击次数 = 5
    演出时间 = 1.5
    CD = 3.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.攻击次数) * self.倍率

class 刹那永恒技能3(刹那永恒主动技能):
    名称 = '冰魄旋枪'
    所在等级 = 25
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 253, 278, 304, 330, 355, 381, 407, 432, 458, 484, 509, 535, 561, 587, 612, 638, 664, 689, 715, 741, 766, 792, 818, 843, 869, 895, 920, 946, 972, 997, 1023, 1049, 1075, 1100, 1126, 1152, 1177, 1203, 1229, 1254, 1280, 1306, 1331, 1357, 1383, 1408, 1434, 1460, 1485, 1511, 1537, 1562, 1588, 1614, 1640, 1665, 1691, 1717, 1742, 1768, 1794, 1819, 1845, 1871, 1896, 1922, 1948, 1973, 1999, 2025]
    攻击次数 = 16
    演出时间 = 1.5
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.攻击次数) * self.倍率

class 刹那永恒技能4(刹那永恒主动技能):
    名称 = '冰霜之径'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0

    自定义描述 = 1
    def 技能描述(self, 武器类型):
        return '冰属性强化增加:' + str(self.属强加成())

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (30 + self.等级 * 4)

    def 加成倍率(self, 武器类型):
            return 1.0


class 刹那永恒技能5(被动技能):
    名称 = '冰之领悟'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return (1.02 + self.等级 * 0.01)
        else:
            return (1.12 + (self.等级 - 10) * 0.02)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return (1.02 + self.等级 * 0.01)
        else:
            return (1.12 + (self.等级 - 10) * 0.02)


class 刹那永恒技能6(刹那永恒主动技能):
    名称 = '冰魄之弓'
    所在等级 = 30
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 1365, 1504, 1642, 1781, 1919, 2058, 2196, 2335, 2473, 2612, 2750, 2889, 3027, 3166, 3304, 3443, 3581, 3720, 3858, 3997, 4136, 4274, 4413, 4551, 4690, 4828, 4967, 5105, 5244, 5382, 5521, 5659, 5798, 5936, 6075, 6213, 6352, 6490, 6629, 6768, 6906, 7045, 7183, 7322, 7460, 7599, 7737, 7876, 8014, 8153, 8291, 8430, 8568, 8707, 8845, 8984, 9123, 9261, 9400, 9538, 9677, 9815, 9954, 10092, 10231, 10369, 10508, 10646, 10785, 10923]
    攻击次数 = 3
    数据2 = [0, 2068, 2278, 2488, 2698, 2908, 3118, 3327, 3537, 3747, 3957, 4167, 4377, 4587, 4796, 5006, 5216, 5426, 5636, 5846, 6056, 6266, 6475, 6685, 6895, 7105, 7315, 7525, 7735, 7944, 8154, 8364, 8574, 8784, 8994, 9204, 9414, 9623, 9833, 10043, 10253, 10463, 10673, 10883, 11092, 11302, 11512, 11722, 11932, 12142, 12352, 12562, 12771, 12981, 13191, 13401, 13611, 13821, 14031, 14240, 14450, 14660, 14870, 15080, 15290, 15500, 15710, 15919, 16129, 16339, 16549]
    攻击次数2 = 1
    演出时间 = 1.5
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.攻击次数 + self.数据2[self.等级] * (1 + self.TP成长 * self.TP等级) * self.攻击次数2) * self.倍率

class 刹那永恒技能7(刹那永恒主动技能):
    名称 = '破冰飞刃'
    所在等级 = 30
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 242, 266, 291, 315, 340, 365, 389, 414, 438, 463, 487, 512, 537, 561, 586, 610, 635, 659, 684, 709, 733, 758, 782, 807, 831, 856, 881, 905, 930, 954, 979, 1003, 1028, 1053, 1077, 1102, 1126, 1151, 1175, 1200, 1225, 1249, 1274, 1298, 1323, 1347, 1372, 1397, 1421, 1446, 1470, 1495, 1519, 1544, 1569, 1593, 1618, 1642, 1667, 1691, 1716, 1741, 1765, 1790, 1814, 1839, 1863, 1888, 1913, 1937]
    攻击次数 = 24
    演出时间 = 1.0
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级)* self.攻击次数) * self.倍率

class 刹那永恒技能8(被动技能):
    名称 = '水晶剑'
    所在等级 = 30
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['冰魄剑']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return (2.00 + (self.等级-1) * 0.02)


class 刹那永恒技能9(刹那永恒主动技能):
    名称 = '旋冰穿刺'
    所在等级 = 35
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 818, 901, 984, 1067, 1150, 1233, 1316, 1399, 1482, 1565, 1648, 1731, 1814, 1897, 1980, 2063, 2146, 2229, 2312, 2395, 2478, 2561, 2644, 2727, 2810, 2893, 2976, 3059, 3142, 3225, 3308, 3391, 3474, 3557, 3640, 3723, 3806, 3889, 3972, 4055, 4138, 4221, 4304, 4387, 4470, 4553, 4636, 4719, 4802, 4885, 4968, 5051, 5134, 5217, 5300, 5383, 5466, 5549, 5632, 5715, 5798, 5881, 5964, 6047, 6130, 6213, 6296, 6379, 6462, 6545]
    攻击次数 = 1
    数据2 = [0, 7363, 8110, 8858, 9605, 10352, 11099, 11846, 12593, 13340, 14087, 14834, 15581, 16328, 17075, 17822, 18569, 19316, 20064, 20811, 21558, 22305, 23052, 23799, 24546, 25293, 26040, 26787, 27534, 28281, 29028, 29775, 30522, 31270, 32017, 32764, 33511, 34258, 35005, 35752, 36499, 37246, 37993, 38740, 39487, 40234, 40981, 41728, 42475, 43223, 43970, 44717, 45464, 46211, 46958, 47705, 48452, 49199, 49946, 50693, 51440, 52187, 52934, 53681, 54429, 55176, 55923, 56670, 57417, 58164, 58911]
    攻击次数2 = 1
    演出时间 = 1.5
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.攻击次数 + self.数据2[self.等级] * (1 + self.TP成长 * self.TP等级) * self.攻击次数2) * self.倍率

class 刹那永恒技能10(刹那永恒主动技能):
    名称 = '冰魄锤击'
    所在等级 = 35
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 =[0, 7737, 8522, 9307, 10092, 10877, 11662, 12447, 13232, 14017, 14802, 15587, 16372, 17157, 17942, 18727, 19512, 20296, 21081, 21866, 22651, 23436, 24221, 25006, 25791, 26576, 27361, 28146, 28931, 29716, 30501, 31286, 32071, 32856, 33641, 34426, 35211, 35996, 36781, 37566, 38351, 39136, 39921, 40706, 41491, 42276, 43061, 43846, 44630, 45415, 46200, 46985, 47770, 48555, 49340, 50125, 50910, 51695, 52480, 53265, 54050, 54835, 55620, 56405, 57190, 57975, 58760, 59545, 60330, 61115, 61900]
    攻击次数 = 1
    攻击倍率 = 1.2
    演出时间 = 1.0
    CD = 18.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * self.攻击倍率 * (1 + self.TP成长 * self.TP等级) * self.攻击次数 * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
           self.攻击倍率 *= 1.27
        if x == 1:
           self.攻击倍率 *= 1.36
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>冰魄延伸</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[冰魄锤击]<br>"
            temp += "普通施放时， 发动大范围寒冰冲击波<br>"
            temp += "攻击力 +9%<br>"
            temp += "强制中断其他技能后施放时攻击力 +18%<br>"
            temp += "强制中断其他技能后施放时不产生寒冰冲击波<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "对可抓取的敌人造成和不可抓取的敌人同样的伤害<br>"
            temp += "普通施放时寒冰冲击波范围 +15%<br>"
            temp += "普通施放时攻击力 +6%<br>"
            temp += "强制中断其他技能后施放时攻击力 +9%"
        elif x == 1:
            temp = "<font color='#FF00FF'>冰魄延伸</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[冰魄锤击]<br>"
            temp += "普通施放时， 发动大范围寒冰冲击波<br>"
            temp += "攻击力 +9%<br>"
            temp += "强制中断其他技能后施放时攻击力 +18%<br>"
            temp += "强制中断其他技能后施放时不产生寒冰冲击波<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "对可抓取的敌人造成和不可抓取的敌人同样的伤害<br>"
            temp += "普通施放时寒冰冲击波范围 +15%<br>"
            temp += "普通施放时攻击力 +6%<br>"
            temp += "强制中断其他技能后施放时攻击力 +18%"
        return temp

class 刹那永恒技能11(刹那永恒主动技能):
    名称 = '极冰绽放'
    所在等级 = 40
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 777, 855, 934, 1013, 1092, 1171, 1250, 1328, 1407, 1486, 1565, 1644, 1723, 1801, 1880, 1959, 2038, 2117, 2196, 2274, 2353, 2432, 2511, 2590, 2669, 2747, 2826, 2905, 2984, 3063, 3142, 3221, 3299, 3378, 3457, 3536, 3615, 3694, 3772, 3851, 3930, 4009, 4088, 4167, 4245, 4324, 4403, 4482, 4561, 4640, 4718, 4797, 4876, 4955, 5034, 5113, 5191, 5270, 5349, 5428, 5507, 5586, 5664, 5743, 5822, 5901, 5980, 6059, 6137, 6216]
    攻击倍率 = 1.95
    攻击次数 = 4
    数据2 = [0, 3433, 3782, 4130, 4478, 4827, 5175, 5523, 5872, 6220, 6568, 6917, 7265, 7613, 7962, 8310, 8658, 9007, 9355, 9703, 10052, 10400, 10748, 11097, 11445, 11793, 12142, 12490, 12839, 13187, 13535, 13884, 14232, 14580, 14929, 15277, 15625, 15974, 16322, 16670, 17019, 17367, 17715, 18064, 18412, 18760, 19109, 19457, 19805, 20154, 20502, 20850, 21199, 21547, 21895, 22244, 22592, 22941, 23289, 23637, 23986, 24334, 24682, 25031, 25379, 25727, 26076, 26424, 26772, 27121, 27469]
    攻击倍率2 = 2.35
    攻击次数2 = 1
    演出时间 = 2.0
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级]* (1 + self.TP成长 * self.TP等级) * self.攻击倍率* self.攻击次数 +
                self.数据2[self.等级]* (1 + self.TP成长 * self.TP等级) * self.攻击倍率2* self.攻击次数2) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
           self.攻击倍率 *= 1.11
           self.攻击倍率2 *= 1.23
           self.CD *= 0.90
        if x == 1:
           self.攻击倍率 *= 1.11
           self.攻击倍率2 *= 1.38
           self.CD *= 0.90
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>冰封制动</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[极冰绽放]<br>"
            temp += "删除指定魔法阵位置的功能<br>"
            temp += "缩短魔法阵生成时间<br>"
            temp += "攻击范围 +20%<br>"
            temp += "攻击力 +11%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -10%<br>"
            temp += "最后强击攻击力 +12%<br>"
            temp += "冰柱破碎时的攻击力 +18%<br>"
            temp += "每次攻击时发射[冰之技艺]的冰枪"
        elif x == 1:
            temp = "<font color='#FF00FF'>冰封制动</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[极冰绽放]<br>"
            temp += "删除指定魔法阵位置的功能<br>"
            temp += "缩短魔法阵生成时间<br>"
            temp += "攻击范围 +20%<br>"
            temp += "攻击力 +11%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -10%<br>"
            temp += "最后强击攻击力 +27%<br>"
            temp += "冰柱破碎时的攻击力 +35%<br>"
            temp += "每次攻击时发射[冰之技艺]的冰枪"
        return temp


class 刹那永恒技能12(刹那永恒主动技能):
    名称 = '冰雪风暴'
    所在等级 = 45
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 879, 968, 1058, 1147, 1236, 1325, 1415, 1504, 1593, 1682, 1772, 1861, 1950, 2039, 2129, 2218, 2307, 2396, 2486, 2575, 2664, 2753, 2843, 2932, 3021, 3110, 3200, 3289, 3378, 3467, 3556, 3646, 3735, 3824, 3913, 4003, 4092, 4181, 4270, 4360, 4449, 4538, 4627, 4717, 4806, 4895, 4984, 5074, 5163, 5252, 5341, 5431, 5520, 5609, 5698, 5788, 5877, 5966, 6055, 6145, 6234, 6323, 6412, 6502, 6591, 6680, 6769, 6859, 6948, 7037]
    攻击次数 = 14
    攻击倍率 = 1.0
    数据2 = [0, 8588, 9459, 10330, 11202, 12073, 12944, 13815, 14687, 15558, 16429, 17300, 18172, 19043, 19914, 20786, 21657, 22528, 23399, 24271, 25142, 26013, 26884, 27756, 28627, 29498, 30370, 31241, 32112, 32983, 33855, 34726, 35597, 36468, 37340, 38211, 39082, 39954, 40825, 41696, 42567, 43439, 44310, 45181, 46052, 46924, 47795, 48666, 49538, 50409, 51280, 52151, 53023, 53894, 54765, 55636, 56508, 57379, 58250, 59122, 59993, 60864, 61735, 62607, 63478, 64349, 65220, 66092, 66963, 67834, 68706]
    攻击次数2 = 1
    攻击倍率2 = 1.0
    演出时间 = 2.5
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击倍率 * (1 + self.TP成长 * self.TP等级) * self.攻击次数 +
                self.数据2[self.等级] * self.攻击倍率2 * (1 + self.TP成长 * self.TP等级) * self.攻击次数2) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
           self.攻击次数 = 16
           self.攻击倍率2 *= 1.15
        if x == 1:
           self.攻击次数 = 16
           self.攻击倍率2 *= 1.34
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>冰龙升天破</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[冰雪风暴]<br>"
            temp += "变更为以施放者为中心生成1个巨大的寒气风暴<br>"
            temp += "魔法阵范围 -50%<br>"
            temp += "删除聚集敌人的功能<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "施放技能时直接召唤寒气风暴<br>"
            temp += "多段攻击次数 +2次<br>"
            temp += "爆炸攻击力 +15%"
        elif x == 1:
            temp = "<font color='#FF00FF'>冰龙升天破</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[冰雪风暴]<br>"
            temp += "变更为以施放者为中心生成1个巨大的寒气风暴<br>"
            temp += "魔法阵范围 -50%<br>"
            temp += "删除聚集敌人的功能<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "施放技能时直接召唤寒气风暴<br>"
            temp += "多段攻击次数 +2次<br>"
            temp += "爆炸攻击力 +34%"
        return temp

class 刹那永恒技能13(被动技能):
    名称 = '冰封奥义'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)

class 刹那永恒技能14(刹那永恒主动技能):
    名称 = '千旋冰轮破'
    所在等级 = 50
    等级上限 = 40
    等级精通 = 30
    学习间隔 = 5
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 923, 1137, 1351, 1566, 1780, 1994, 2208, 2422, 2637, 2851, 3065, 3279, 3493, 3707, 3922, 4136, 4350, 4564, 4778, 4993, 5207, 5421, 5635, 5849, 6063, 6278, 6492, 6706, 6920, 7134, 7348, 7563, 7777, 7991, 8205, 8419, 8634, 8848, 9062, 9276, 9490, 9704, 9919, 10133, 10347, 10561, 10775, 10989, 11204, 11418, 11632, 11846, 12060, 12275, 12489, 12703, 12917, 13131, 13345, 13560, 13774, 13988, 14202, 14416, 14630, 14845, 15059, 15273, 15487, 15701]
    攻击次数 = 40
    数据2 = [0, 785, 967, 1149, 1332, 1514, 1696, 1878, 2060, 2242, 2424, 2607, 2789, 2971, 3153, 3335, 3517, 3700, 3882, 4064, 4246, 4428, 4610, 4793, 4975, 5157, 5339, 5521, 5703, 5885, 6068, 6250, 6432, 6614, 6796, 6978, 7161, 7343, 7525, 7707, 7889, 8071, 8254, 8436, 8618, 8800, 8982, 9164, 9346, 9529, 9711, 9893, 10075, 10257, 10439, 10622, 10804, 10986, 11168, 11350, 11532, 11715, 11897, 12079, 12261, 12443, 12625, 12808, 12990, 13172, 13354]
    攻击次数2 = 24
    数据3 = [0, 2751, 3390, 4028, 4666, 5304, 5942, 6580, 7218, 7856, 8494, 9133, 9771, 10409, 11047, 11685, 12323, 12961, 13599, 14238, 14876, 15514, 16152, 16790, 17428, 18066, 18704, 19343, 19981, 20619, 21257, 21895, 22533, 23171, 23809, 24447, 25086, 25724, 26362, 27000, 27638, 28276, 28914, 29552, 30191, 30829, 31467, 32105, 32743, 33381, 34019, 34657, 35295, 35934, 36572, 37210, 37848, 38486, 39124, 39762, 40400, 41039, 41677, 42315, 42953, 43591, 44229, 44867, 45505, 46144, 46782]
    攻击次数3 = 1
    CD = 145.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * self.倍率

class 刹那永恒技能15(刹那永恒主动技能):
    名称 = '冰凌破'
    所在等级 = 60
    等级上限 = 40
    等级精通 = 30
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 678, 746, 815, 884, 953, 1022, 1090, 1159, 1228, 1297, 1366, 1434, 1503, 1572, 1641, 1710, 1778, 1847, 1916, 1985, 2054, 2122, 2191, 2260, 2329, 2397, 2466, 2535, 2604, 2673, 2741, 2810, 2879, 2948, 3017, 3085, 3154, 3223, 3292, 3361, 3429, 3498, 3567, 3636, 3705, 3773, 3842, 3911, 3980, 4049, 4117, 4186, 4255, 4324, 4393, 4461, 4530, 4599, 4668, 4737, 4805, 4874, 4943, 5012, 5080, 5149, 5218, 5287, 5356, 5424]
    攻击次数 = 25
    数据2 = [0, 3229, 3556, 3884, 4211, 4539, 4867, 5194, 5522, 5849, 6177, 6505, 6832, 7160, 7487, 7815, 8143, 8470, 8798, 9125, 9453, 9781, 10108, 10436, 10763, 11091, 11419, 11746, 12074, 12401, 12729, 13056, 13384, 13712, 14039, 14367, 14694, 15022, 15350, 15677, 16005, 16332, 16660, 16988, 17315, 17643, 17970, 18298, 18626, 18953, 19281, 19608, 19936, 20264, 20591, 20919, 21246, 21574, 21902, 22229, 22557, 22884, 23212, 23540, 23867, 24195, 24522, 24850, 25177, 25505, 25833]
    攻击次数2 = 1
    攻击倍率 = 1.0
    演出时间 = 2.0
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.攻击倍率 * self.攻击次数 +
                self.数据2[self.等级] * (1 + self.TP成长 * self.TP等级) * self.攻击倍率 * self.攻击次数2) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
           self.攻击倍率 *= 1.22
        if x == 1:
           self.攻击倍率 *= 1.31
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>苍白之楔</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[冰凌破]<br>"
            temp += "[冰之印]开启后， 追踪并攻击有[冰封奥义]光环的敌人中最强的敌人(攻击开始后不再追踪敌人)<br>"
            temp += "攻击力 +9%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "追击时移动速度 +50%<br>"
            temp += "攻击力 +13%"
        elif x == 1:
            temp = "<font color='#FF00FF'>苍白之楔</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[冰凌破]<br>"
            temp += "[冰之印]开启后， 追踪并攻击有[冰封奥义]光环的敌人中最强的敌人(攻击开始后不再追踪敌人)<br>"
            temp += "攻击力 +9%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "追击时移动速度 +50%<br>"
            temp += "攻击力 +22%"
        return temp


class 刹那永恒技能16(刹那永恒主动技能):
    名称 = '千里冰封'
    所在等级 = 70
    等级上限 = 40
    等级精通 = 30
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 =[0, 9584, 10556, 11528, 12501, 13473, 14445, 15418, 16390, 17362, 18335, 19307, 20279, 21252, 22224, 23196, 24168, 25141, 26113, 27085, 28058, 29030, 30002, 30975, 31947, 32919, 33892, 34864, 35836, 36809, 37781, 38753, 39726, 40698, 41670, 42642, 43615, 44587, 45559, 46532, 47504, 48476, 49449, 50421, 51393, 52366, 53338, 54310, 55283, 56255, 57227, 58200, 59172, 60144, 61116, 62089, 63061, 64033, 65006, 65978, 66950, 67923, 68895, 69867, 70840, 71812, 72784, 73757, 74729, 75701, 76674]
    攻击次数 = 3
    攻击倍率 = 1.0
    演出时间 = 2.0
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * self.攻击倍率 * (1 + self.TP成长 * self.TP等级) * self.攻击次数 * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
           self.攻击次数 = 1
           self.攻击倍率 = 3.56
        if x == 1:
           self.攻击次数 = 1
           self.攻击倍率 = 3.8
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>冰凌花</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[千里冰封]<br>"
            temp += "同时生成所有冰刺<br>"
            temp += "攻击次数变更为1次<br>"
            temp += "发动速度 +50%<br>"
            temp += "攻击力 +230%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "[冰之印]开启时， 冰冻效果变更为强制控制2秒<br>"
            temp += "攻击力 +26%"
        elif x == 1:
            temp = "<font color='#FF00FF'>冰凌花</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[千里冰封]<br>"
            temp += "同时生成所有冰刺<br>"
            temp += "攻击次数变更为1次<br>"
            temp += "发动速度 +50%<br>"
            temp += "攻击力 +230%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "[冰之印]开启时， 冰冻效果变更为强制控制2秒<br>"
            temp += "攻击力 +50%"
        return temp

class 刹那永恒技能17(被动技能):
    名称 = '冰之技艺'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['冰魄之弓','破冰飞刃','冰雪风暴','千旋冰轮破','冰凌破','千里冰封','极冰领域','永罪冰狱']
    关联技能2 = ['冰魄剑', '寒冰连枪', '冰魄旋枪', '旋冰穿刺', '冰魄锤击', '极冰绽放', '碎冰破']
    
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.03 * self.等级, 5)

    def 冰针倍率(self, 武器类型):
        return round(0.24 + 0.03 * self.等级, 5)

#按技能数据无法与游戏中伤害对应，因此从一级起验证，结果按核对伤害手动增加29百分比
class 刹那永恒技能18(刹那永恒主动技能):
    名称 = '碎冰破'
    所在等级 = 75
    等级上限 = 40
    等级精通 = 30
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 30903, 34038, 37173, 40308, 43443, 46578, 49713, 52848, 55984, 59119, 62254, 65389, 68524, 71659, 74794, 77929, 81064, 84200, 87335, 90470, 93605, 96740, 99875, 103010, 106145, 109280, 112416, 115551, 118686, 121821, 124956, 128091, 131226, 134361, 137496, 140632, 143767, 146902, 150037, 153172, 156307, 159442, 162577, 165712, 168848, 171983, 175118, 178253, 181388, 184523, 187658, 190793, 193928, 197063, 200199, 203334, 206469, 209604, 212739, 215874, 219009, 222144, 225279, 228415, 231550, 234685, 237820, 240955, 244090, 247225]
    攻击次数 = 1
    数据2 = [0, 11251, 12393, 13534, 14676, 15817, 16959, 18100, 19242, 20383, 21525, 22666, 23808, 24949, 26091, 27232, 28374, 29515, 30657, 31798, 32940, 34081, 35222, 36364, 37505, 38647, 39788, 40930, 42071, 43213, 44354, 45496, 46637, 47779, 48920, 50062, 51203, 52345, 53486, 54628, 55769, 56911, 58052, 59194, 60335, 61477, 62618, 63760, 64901, 66043, 67184, 68326, 69467, 70609, 71750, 72892, 74033, 75174, 76316, 77457, 78599, 79740, 80882, 82023, 83165, 84306, 85448, 86589, 87731, 88872, 90014]
    攻击次数2 = 1
    攻击倍率 = 1.2
    演出时间 = 1.0
    CD = 40.0

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return (self.数据1[self.等级] * self.攻击倍率 * self.攻击次数 +
                    self.数据2[self.等级] * self.攻击倍率 * self.攻击次数2 + 29) * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.46
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>碎冰破</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[碎冰破]<br>"
            temp += "向前方生成多个冰霜结晶<br>"
            temp += "- 冰霜碎片攻击范围增加<br>"
            temp += "冰霜碎片攻击力 +12%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "碎冰破攻击速度 +50%<br>"
            temp += "冰霜碎片攻击力 +34%<br>"
        return temp[:-4]

class 刹那永恒技能19(刹那永恒主动技能):
    名称 = '极冰领域'
    所在等级 = 80
    等级上限 = 40
    等级精通 = 30
    学习间隔 = 2
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [0, 40711, 44841, 48971, 53101, 57231, 61361, 65491, 69621, 73751, 77882, 82012, 86142, 90272, 94402, 98532, 102662, 106792, 110922, 115053, 119183, 123313, 127443, 131573, 135703, 139833, 143963, 148093, 152224, 156354, 160484, 164614, 168744, 172874, 177004, 181134, 185264, 189395, 193525, 197655, 201785, 205915, 210045, 214175, 218305, 222435, 226566, 230696, 234826, 238956, 243086, 247216, 251346, 255476, 259606, 263737, 267867, 271997, 276127, 280257, 284387, 288517, 292647, 296777, 300908, 305038, 309168, 313298, 317428, 321558, 325688]
    攻击倍率 = 1.0
    演出时间 = 0.65
    CD = 40.0

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击倍率 * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击倍率 *= 1.32
            self.CD *= 0.9
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>极冰领域</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[极冰领域]<br>"
            temp += "部分转职技能命中后可以强制中断并连接施放极冰领域<br>"
            temp += "- 可中断技能列表与冰魄锤击相同<br>"
            temp += "波动攻击力 +14%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "冷却时间 -10%<br>"
            temp += "波动攻击力 +18%<br>"
        return temp[:-4]

class 刹那永恒技能20(刹那永恒主动技能):
    名称 = '永罪冰狱'
    所在等级 = 85
    等级上限 = 40
    等级精通 = 30
    学习间隔 = 5
    基础等级 = min(int((刹那永恒等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 38195, 47052, 55909, 64765, 73622, 82479, 91336, 100193, 109050, 117907, 126764, 135621, 144477, 153334, 162191, 171048, 179905, 188762, 197619, 206476, 215333, 224189, 233046, 241903, 250760, 259617, 268474, 277331, 286188, 295045, 303901, 312758, 321615, 330472, 339329, 348186, 357043, 365900, 374757, 383613, 392470, 401327, 410184, 419041, 427898, 436755, 445612, 454468, 463325, 472182, 481039, 489896, 498753, 507610, 516467, 525324, 534180, 543037, 551894, 560751, 569608, 578465, 587322, 596179, 605036, 613892, 622749, 631606, 640463, 649320]
    攻击次数 = 1
    数据2 = [0, 16970, 20905, 24840, 28775, 32710, 36645, 40581, 44516, 48451, 52386, 56321, 60256, 64191, 68127, 72062, 75997, 79932, 83867, 87802, 91737, 95672, 99608, 103543, 107478, 111413, 115348, 119283, 123218, 127154, 131089, 135024, 138959, 142894, 146829, 150764, 154699, 158635, 162570, 166505, 170440, 174375, 178310, 182245, 186181, 190116, 194051, 197986, 201921, 205856, 209791, 213726, 217662, 221597, 225532, 229467, 233402, 237337, 241272, 245208, 249143, 253078, 257013, 260948, 264883, 268818, 272753, 276689, 280624, 284559, 288494]
    攻击次数2 = 2
    数据3 = [0, 25528, 31448, 37368, 43287, 49207, 55127, 61047, 66966, 72886, 78806, 84725, 90645, 96565, 102485, 108404, 114324, 120244, 126163, 132083, 138003, 143922, 149842, 155762, 161682, 167601, 173521, 179441, 185360, 191280, 197200, 203120, 209039, 214959, 220879, 226798, 232718, 238638, 244558, 250477, 256397, 262317, 268236, 274156, 280076, 285996, 291915, 297835, 303755, 309674, 315594, 321514, 327434, 333353, 339273, 345193, 351112, 357032, 362952, 368872, 374791, 380711, 386631, 392550, 398470, 404390, 410310, 416229, 422149, 428069, 433988]
    攻击次数3 = 1
    CD = 180.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * self.倍率

class 刹那永恒技能21(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 刹那永恒技能22(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 刹那永恒技能23(被动技能):
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

刹那永恒技能列表 = []
i = 0
while i >= 0:
    try:
        exec('刹那永恒技能列表.append(刹那永恒技能'+str(i)+'())')
        i += 1
    except:
        i = -1

刹那永恒技能序号 = dict()
for i in range(len(刹那永恒技能列表)):
    刹那永恒技能序号[刹那永恒技能列表[i].名称] = i

刹那永恒一觉序号 = 0
刹那永恒二觉序号 = 0
刹那永恒三觉序号 = 0
for i in 刹那永恒技能列表:
    if i.所在等级 == 50:
        刹那永恒一觉序号 = 刹那永恒技能序号[i.名称]
    if i.所在等级 == 85:
        刹那永恒二觉序号 = 刹那永恒技能序号[i.名称]
    if i.所在等级 == 100:
        刹那永恒三觉序号 = 刹那永恒技能序号[i.名称]

刹那永恒护石选项 = ['无']
for i in 刹那永恒技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        刹那永恒护石选项.append(i.名称)

刹那永恒符文选项 = ['无']
for i in 刹那永恒技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        刹那永恒符文选项.append(i.名称)


class 刹那永恒角色属性(角色属性):

    实际名称 = '刹那永恒'
    角色 = '魔法师(男)'
    职业 = '冰结师'

    武器选项 = ['魔杖','法杖']
    
    伤害类型选择 = ['魔法百分比']
    
    伤害类型 = '魔法百力比'
    防具类型 = '皮甲'
    防具精通属性 = ['智力']

    主BUFF = 1.800
   
    远古记忆 = 0

    冰针显示开关 = 0
    小冰轮次数 = 0
    大冰轮次数 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(刹那永恒技能列表)
        self.技能序号= deepcopy(刹那永恒技能序号)

    def 被动倍率计算(self):

        if self.远古记忆 > 0:
            self.进图智力 += self.远古记忆 * 15
            
        self.冰属性强化 += self.技能栏[self.技能序号['冰霜之径']].属强加成()
        self.技能栏[self.技能序号['千旋冰轮破']].攻击次数 = self.小冰轮次数 + 36
        self.技能栏[self.技能序号['千旋冰轮破']].攻击次数2 = self.大冰轮次数 + 20

        for i in self.技能栏:
            if i.关联技能 != ['无']:
                if i.关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率(self.武器类型)
                else :
                    for k in i.关联技能:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率(self.武器类型)
            
            if i.关联技能2 != ['无']:
                if i.关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率2(self.武器类型)
                elif i.名称 != '冰之技艺' :
                    for k in i.关联技能2:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率2(self.武器类型)
            
            if i.关联技能3 != ['无']:
                if i.关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率3(self.武器类型)
                else :
                    for k in i.关联技能3:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率3(self.武器类型)


    def 数据计算(self, x = 0, y = -1):
        self.预处理()
        #初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算(y)
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        # 二觉被动冰针
        if self.技能栏[self.技能序号['冰之技艺']].等级 != 0:

            冰之技艺序号 = self.技能序号['冰之技艺']

            技能释放次数[冰之技艺序号] = 1

            if 技能总伤害[self.技能序号['冰魄剑']] != 0:
                temp = 技能总伤害[self.技能序号['冰魄剑']] * self.技能栏[冰之技艺序号].冰针倍率(self.武器类型)
                if self.冰针显示开关 == 1:
                   技能总伤害[冰之技艺序号] += temp
                else:
                   技能总伤害[self.技能序号['冰魄剑']] += temp

            if 技能总伤害[self.技能序号['寒冰连枪']] != 0:
                temp = 技能总伤害[self.技能序号['寒冰连枪']] * self.技能栏[冰之技艺序号].冰针倍率(self.武器类型)
                if self.冰针显示开关 == 1:
                   技能总伤害[冰之技艺序号] += temp
                else:
                   技能总伤害[self.技能序号['寒冰连枪']] += temp

            if 技能总伤害[self.技能序号['冰魄旋枪']] != 0:
                temp = 技能总伤害[self.技能序号['冰魄旋枪']] * self.技能栏[冰之技艺序号].冰针倍率(self.武器类型)
                if self.装备检查('奔流不息之银河'):
                    temp = temp / 0.7
                if self.冰针显示开关 == 1:
                    技能总伤害[冰之技艺序号] += temp
                else:
                    技能总伤害[self.技能序号['冰魄旋枪']] += temp

            if 技能总伤害[self.技能序号['旋冰穿刺']] != 0:
                temp = 技能总伤害[self.技能序号['旋冰穿刺']] * self.技能栏[冰之技艺序号].冰针倍率(self.武器类型)
                if self.装备检查('奔流不息之山川'):
                    temp = temp / 0.7
                if self.冰针显示开关 == 1:
                    技能总伤害[冰之技艺序号] += temp
                else:
                    技能总伤害[self.技能序号['旋冰穿刺']] += temp

            if 技能总伤害[self.技能序号['冰魄锤击']] != 0:
                temp = 技能总伤害[self.技能序号['冰魄锤击']] * self.技能栏[冰之技艺序号].冰针倍率(self.武器类型)
                if self.装备检查('奔流不息之山川'):
                    temp = temp / 0.7
                if self.冰针显示开关 == 1:
                    技能总伤害[冰之技艺序号] += temp
                else:
                    技能总伤害[self.技能序号['冰魄锤击']] += temp

            if 技能总伤害[self.技能序号['极冰绽放']] != 0:
                temp = 技能总伤害[self.技能序号['极冰绽放']] * self.技能栏[冰之技艺序号].冰针倍率(self.武器类型)
                if self.装备检查('奔流不息之伽蓝'):
                    temp = temp / 0.7
                if self.冰针显示开关 == 1:
                    技能总伤害[冰之技艺序号] += temp
                else:
                    技能总伤害[self.技能序号['极冰绽放']] += temp

            if 技能总伤害[self.技能序号['碎冰破']] != 0:
                temp = 技能总伤害[self.技能序号['碎冰破']] * self.技能栏[冰之技艺序号].冰针倍率(self.武器类型)
                if self.冰针显示开关 == 1:
                    技能总伤害[冰之技艺序号] += temp
                else:
                    技能总伤害[self.技能序号['碎冰破']] += temp

            if self.冰针显示开关 == 0:
               for i in self.技能栏[冰之技艺序号].关联技能2:
                   self.技能栏[self.技能序号[i]].被动倍率 *= self.技能栏[冰之技艺序号].加成倍率2(self.武器类型)

        #返回结果
        return self.数据返回(x, 技能释放次数, 技能总伤害)

class 刹那永恒(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 刹那永恒角色属性()
        self.角色属性A = 刹那永恒角色属性()
        self.角色属性B = 刹那永恒角色属性()
        self.一觉序号 = 刹那永恒一觉序号
        self.二觉序号 = 刹那永恒二觉序号
        self.三觉序号 = 刹那永恒三觉序号
        self.护石选项 = deepcopy(刹那永恒护石选项)
        self.符文选项 = deepcopy(刹那永恒符文选项)

    def 界面(self):
        super().界面()
        self.冰针显示开关=QCheckBox('冰针伤害独立显示',self.main_frame2)
        self.冰针显示开关.resize(120,20)
        self.冰针显示开关.move(490,420)
        self.冰针显示开关.setStyleSheet(复选框样式)
        self.冰针显示开关.setChecked(False)

        self.小冰轮次数选择=MyQComboBox(self.main_frame2)
        self.小冰轮次数选择.addItem('小冰轮击中36次')
        self.小冰轮次数选择.addItem('小冰轮击中37次')
        self.小冰轮次数选择.addItem('小冰轮击中38次')
        self.小冰轮次数选择.addItem('小冰轮击中39次')
        self.小冰轮次数选择.addItem('小冰轮击中40次')
        self.小冰轮次数选择.addItem('小冰轮击中41次')
        self.小冰轮次数选择.addItem('小冰轮击中42次')
        self.小冰轮次数选择.setCurrentIndex(6)
        self.小冰轮次数选择.resize(120,20)
        self.小冰轮次数选择.move(325,420)

        self.大冰轮次数选择=MyQComboBox(self.main_frame2)
        self.大冰轮次数选择.addItem('大冰轮击中20次')
        self.大冰轮次数选择.addItem('大冰轮击中21次')
        self.大冰轮次数选择.addItem('大冰轮击中22次')
        self.大冰轮次数选择.addItem('大冰轮击中23次')
        self.大冰轮次数选择.addItem('大冰轮击中24次')
        self.大冰轮次数选择.setCurrentIndex(2)
        self.大冰轮次数选择.resize(120,20)
        self.大冰轮次数选择.move(325,450)

    def 载入配置(self, path='set'):
        super().载入配置(path)
        try:
           setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'r',encoding='utf-8').readlines()
           self.小冰轮次数选择.setCurrentIndex(int(setfile[0].replace('\n', '')));
           self.大冰轮次数选择.setCurrentIndex(int(setfile[1].replace('\n', '')));
           if int(setfile[2].replace('\n', '')) == 1:
              self.冰针显示开关.setChecked(True)
           else:
              self.冰针显示开关.setChecked(False)
        except:
            pass

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'w', encoding='utf-8')
            setfile.write(str(self.小冰轮次数选择.currentIndex())+'\n')
            setfile.write(str(self.大冰轮次数选择.currentIndex())+'\n')
            if self.冰针显示开关.isChecked():
               setfile.write('1\n')
            else:
               setfile.write('0\n')
        except:
            pass
        
    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        if 属性.技能栏[self.角色属性A.技能序号['水晶剑']].等级 != 0:
           属性.技能栏[self.角色属性A.技能序号['冰魄剑']].技能形态改变()

        if self.冰针显示开关.isChecked():
            属性.冰针显示开关 = 1

        属性.小冰轮次数 = self.小冰轮次数选择.currentIndex()
        属性.大冰轮次数 = self.大冰轮次数选择.currentIndex()