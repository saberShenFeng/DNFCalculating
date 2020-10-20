﻿from math import *
from PublicReference.base import *
    

class 元素圣灵主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '法杖':
            return round(self.CD / self.恢复 * 1.1, 1)
        if 武器类型 == '魔杖':
            return round(self.CD / self.恢复 * 1, 1)

class 元素圣灵技能0(元素圣灵主动技能):
    名称 = '烈焰冲击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据 = [0, 2481, 2733, 2986, 3237, 3489, 3741, 3992, 4244, 4495, 4747, 4999, 5252, 5503, 5755, 6007, 6258, 6510, 6762, 7014, 7265, 7516, 7769, 8021, 8273, 8525, 8776, 9028, 9280, 9531, 9782, 10035, 10286, 10540, 10791, 11042, 11295, 11546, 11797, 12050, 12301, 12552, 12805, 13057, 13310, 13561, 13812, 14065, 14316, 14567, 14819, 15071, 15322, 15574, 15827, 16078, 16331, 16582, 16834, 17085, 17337, 17589, 17840, 18092, 18345, 18597, 18848, 19100, 19352, 19603, 19855]
    攻击次数 = 1
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 0.4
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 元素圣灵技能1(被动技能):
    名称 = '属性精通'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5
    圣灵符文倍率 = 1.0
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (0.30 + 0.02 * self.等级) * self.圣灵符文倍率, 5)

class 元素圣灵技能2(元素圣灵主动技能):
    名称 = '虚无之球'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据 = [0, 319, 350, 384, 415, 447, 478, 512, 543, 576, 608, 641, 672, 705, 737, 770, 801, 835, 867, 898, 932, 963, 996, 1027, 1061, 1092, 1125, 1157, 1190, 1221, 1253, 1286, 1318, 1349, 1383, 1414, 1447, 1478, 1512, 1544, 1576, 1609, 1641, 1673, 1704, 1738, 1769, 1802, 1834, 1867, 1898, 1931, 1963, 1996, 2027, 2061, 2092, 2124, 2158, 2189, 2222, 2253, 2287, 2318, 2350, 2383, 2415, 2447, 2479, 2512, 2545]
    攻击次数 = 8
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 4.5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 元素圣灵技能3(元素圣灵主动技能):
    名称 = '冰墙'
    学习间隔 = 2
    sp消耗 = 25
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据 = [0, 4722, 5200, 5677, 6155, 6638, 7114, 7592, 8070, 8552, 9030, 9508, 9986, 10464, 10945, 11423, 11900, 12378, 12861, 13338, 13816, 14294, 14775, 15253, 15731, 16209, 16691, 17169, 17647, 18125, 18606, 19084, 19561, 20039, 20522, 20998, 21476, 21954, 22436, 22914, 23392, 23870, 24351, 24829, 25307, 25784, 26267, 26745, 27222, 27700, 28181, 28659, 29137, 29615, 30097, 30575, 31053, 31531, 32012, 32490, 32968, 33445, 33925, 34404, 34882, 35360, 35841, 36320, 36798, 37278, 37755]
    攻击次数 = 1
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.4
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 元素圣灵技能4(元素圣灵主动技能):
    名称 = '雷旋'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据 = [0, 2350, 2588, 2828, 3069, 3308, 3545, 3784, 4023, 4260, 4499, 4739, 4977, 5215, 5454, 5693, 5932, 6171, 6408, 6647, 6886, 7123, 7363, 7602, 7840, 8079, 8318, 8556, 8795, 9033, 9271, 9510, 9749, 9986, 10226, 10465, 10705, 10943, 11182, 11420, 11659, 11899, 12135, 12375, 12614, 12851, 13090, 13330, 13568, 13806, 14045, 14283, 14522, 14761, 14999, 15238, 15477, 15714, 15955, 16194, 16434, 16670, 16910, 17148, 17387, 17625, 17863, 18102, 18342, 18580, 18818]
    攻击次数 = 1
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 1.0
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 元素圣灵技能5(元素圣灵主动技能):
    名称 = '天雷冲击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据 = [0, 2179, 2401, 2621, 2843, 3064, 3285, 3506, 3727, 3948, 4169, 4390, 4612, 4832, 5054, 5275, 5496, 5717, 5938, 6160, 6380, 6601, 6823, 7044, 7265, 7486, 7707, 7928, 8149, 8371, 8592, 8812, 9034, 9255, 9476, 9697, 9918, 10140, 10360, 10582, 10803, 11024, 11245, 11466, 11688, 11908, 12129, 12351, 12572, 12793, 13014, 13235, 13456, 13677, 13899, 14119, 14340, 14562, 14783, 15004, 15225, 15446, 15667, 15888, 16110, 16331, 16551, 16773, 16994, 17215, 17436]
    攻击次数 = 3
    天雷攻击力增加率 = 1.55
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.2
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.天雷攻击力增加率 * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 1
            self.天雷攻击力增加率 = 5.51
        elif x == 1:
            self.攻击次数 = 1
            self.天雷攻击力增加率 = 5.91

class 元素圣灵技能6(元素圣灵主动技能):
    名称 = '极冰盛宴'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据 = [0, 1150, 1266, 1383, 1500, 1616, 1733, 1849, 1966, 2083, 2199, 2316, 2433, 2549, 2666, 2783, 2899, 3016, 3133, 3249, 3366, 3483, 3599, 3716, 3833, 3949, 4066, 4183, 4299, 4416, 4533, 4649, 4766, 4883, 4999, 5116, 5233, 5349, 5466, 5583, 5699, 5816, 5933, 6049, 6166, 6283, 6399, 6516, 6633, 6749, 6866, 6983, 7099, 7216, 7333, 7449, 7566, 7683, 7799, 7916, 8033, 8149, 8266, 8383, 8499, 8616, 8733, 8849, 8966, 9083, 9199]
    攻击次数 = 8
    CD = 19.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 4.0
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 元素圣灵技能7(元素圣灵主动技能):
    名称 = '湮灭黑洞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据1 = [0, 715, 788, 860, 933, 1005, 1078, 1150, 1224, 1296, 1369, 1441, 1514, 1586, 1659, 1731, 1804, 1876, 1949, 2021, 2095, 2167, 2240, 2312, 2385, 2457, 2530, 2602, 2675, 2747, 2820, 2892, 2966, 3038, 3111, 3183, 3256, 3328, 3401, 3473, 3546, 3618, 3691, 3763, 3837, 3909, 3982, 4054, 4127, 4199, 4272, 4344, 4417, 4489, 4562, 4634, 4708, 4780, 4853, 4925, 4998, 5070, 5143, 5215, 5288, 5360, 5433, 5505, 5579, 5651, 5724]
    攻击次数1 = 15
    数据2 = [0, 3581, 3945, 4307, 4670, 5034, 5397, 5761, 6124, 6488, 6851, 7214, 7577, 7941, 8304, 8667, 9031, 9394, 9758, 10120, 10484, 10847, 11211, 11574, 11938, 12301, 12664, 13027, 13390, 13754, 14117, 14481, 14844, 15208, 15571, 15933, 16297, 16660, 17024, 17387, 17751, 18114, 18478, 18840, 19203, 19567, 19930, 20294, 20657, 21021, 21384, 21747, 22110, 22474, 22837, 23200, 23564, 23927, 24291, 24653, 25017, 25380, 25744, 26107, 26471, 26834, 27197, 27560, 27923, 28287, 28650]
    攻击次数2 = 1
    CD = 35.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 5.0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.28
            self.演出时间 *= 0.6
        elif x == 1:
            self.倍率 *= 1.37
            self.演出时间 *= 0.6

class 元素圣灵技能8(元素圣灵主动技能):
    名称 = '杰克降临'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [0, 3346, 3687, 4026, 4366, 4704, 5044, 5384, 5724, 6064, 6403, 6741, 7082, 7421, 7762, 8101, 8439, 8780, 9119, 9460, 9799, 10139, 10477, 10817, 11157, 11497, 11837, 12176, 12514, 12855, 13194, 13535, 13874, 14212, 14553, 14892, 15232, 15572, 15911, 16252, 16590, 16930, 17269, 17609, 17949, 18287, 18628, 18967, 19308, 19647, 19986, 20326, 20665, 21005, 21345, 21684, 22025, 22363, 22703, 23042, 23382, 23722, 24060, 24401, 24740, 25079, 25420, 25759, 26100, 26438, 26777]
    攻击次数1 = 1
    数据2 = [0, 13389, 14748, 16105, 17463, 18822, 20180, 21538, 22897, 24255, 25614, 26972, 28330, 29689, 31047, 32406, 33763, 35121, 36481, 37838, 39197, 40556, 41913, 43272, 44630, 45989, 47347, 48705, 50064, 51422, 52779, 54139, 55496, 56855, 58214, 59572, 60930, 62290, 63647, 65005, 66365, 67722, 69080, 70438, 71797, 73156, 74513, 75873, 77231, 78588, 79948, 81305, 82663, 84023, 85380, 86739, 88098, 89455, 90814, 92171, 93531, 94889, 96246, 97606, 98964, 100321, 101681, 103038, 104397, 105756, 107114]
    攻击次数2 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.2
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 *= 0.1 * 4
            self.攻击次数2 *= 1.44
        elif x == 1:
            self.攻击次数1 *= 0.1 * 4
            self.攻击次数2 *= 1.54

        
class 元素圣灵技能9(元素圣灵主动技能):
    名称 = '元素之幕'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据1 = [0, 321, 352, 385, 419, 450, 483, 516, 548, 580, 614, 646, 678, 710, 743, 776, 807, 841, 874, 905, 938, 971, 1002, 1036, 1069, 1101, 1133, 1166, 1200, 1231, 1264, 1296, 1329, 1360, 1394, 1427, 1459, 1491, 1524, 1557, 1589, 1622, 1655, 1686, 1719, 1752, 1785, 1817, 1850, 1882, 1914, 1946, 1980, 2013, 2045, 2077, 2110, 2141, 2175, 2208, 2241, 2272, 2305, 2339, 2370, 2403, 2436, 2468, 2500, 2532, 2566]
    攻击次数1 = 20
    数据2 = [0, 9623, 10600, 11576, 12551, 13528, 14504, 15481, 16457, 17433, 18410, 19385, 20361, 21339, 22314, 23292, 24268, 25243, 26220, 27196, 28173, 29149, 30125, 31102, 32077, 33053, 34030, 35006, 35984, 36960, 37936, 38913, 39888, 40865, 41841, 42817, 43794, 44770, 45745, 46722, 47698, 48675, 49651, 50626, 51605, 52580, 53557, 54533, 55509, 56486, 57462, 58437, 59414, 60390, 61367, 62343, 63319, 64296, 65271, 66250, 67225, 68201, 69178, 70154, 71130, 72106, 73082, 74059, 75035, 76011, 76988]
    攻击次数2 = 1
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3.0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.95
            self.攻击次数1 *= 1 + 0.45
            self.攻击次数2 *= 1.17
        if x == 1:
            self.CD *= 0.95
            self.攻击次数1 *= 1 + 0.45
            self.攻击次数2 *= 1.32
        
class 元素圣灵技能10(被动技能):
    名称 = '魔力增幅'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)

class 元素圣灵技能11(元素圣灵主动技能):
    名称 = '陨星幻灭'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [0, 137, 169, 200, 232, 264, 295, 327, 359, 464, 494, 525, 555, 586, 617, 648, 678, 709, 740, 770, 801, 832, 862, 893, 924, 954, 985, 1016, 1046, 1077, 1108, 1138, 1169, 1200, 1231, 1261, 1292, 1322, 1353, 1384, 1414, 1445, 1476, 1507, 1537, 1568, 1599, 1629, 1660, 1691, 1721, 1752, 1783, 1813, 1844, 1875, 1905, 1936, 1967, 1997, 2028, 2059, 2089, 2120, 2151, 2182, 2212, 2243, 2273, 2304, 2335]
    攻击次数1 = 40
    数据2 = [0, 548, 675, 801, 928, 1055, 1182, 1309, 1437, 1858, 1977, 2098, 2221, 2344, 2467, 2590, 2712, 2837, 2959, 3080, 3204, 3327, 3450, 3572, 3696, 3818, 3940, 4063, 4186, 4309, 4431, 4553, 4676, 4799, 4923, 5045, 5166, 5289, 5412, 5534, 5658, 5782, 5904, 6026, 6148, 6272, 6395, 6517, 6641, 6763, 6886, 7008, 7131, 7254, 7375, 7500, 7622, 7745, 7868, 7989, 8112, 8234, 8358, 8481, 8603, 8727, 8848, 8971, 9094, 9217, 9340]
    攻击次数2 = 40
    数据3 = [0, 1096, 1349, 1603, 1856, 2110, 2363, 2618, 2875, 3716, 3953, 4197, 4442, 4687, 4935, 5180, 5424, 5673, 5917, 6160, 6409, 6653, 6899, 7145, 7391, 7635, 7879, 8125, 8372, 8619, 8862, 9105, 9351, 9598, 9846, 10089, 10333, 10578, 10825, 11069, 11315, 11563, 11808, 12052, 12297, 12544, 12789, 13034, 13281, 13526, 13772, 14017, 14262, 14508, 14751, 14999, 15243, 15489, 15735, 15978, 16225, 16469, 16715, 16962, 17206, 17453, 17695, 17943, 18188, 18434, 18681]
    攻击次数3 = 5
    数据4 = [0, 4384, 5396, 6410, 7424, 8441, 9453, 10472, 11498, 14863, 15813, 16787, 17769, 18749, 19739, 20722, 21696, 22692, 23670, 24639, 25635, 26613, 27597, 28578, 29565, 30541, 31517, 32500, 33488, 34475, 35448, 36422, 37405, 38391, 39382, 40357, 41331, 42313, 43299, 44275, 45260, 46252, 47231, 48209, 49187, 50178, 51157, 52135, 53126, 54105, 55087, 56066, 57047, 58031, 59003, 59997, 60973, 61958, 62940, 63912, 64899, 65874, 66861, 67847, 68822, 69814, 70781, 71770, 72752, 73736, 74722]
    攻击次数4 = 5
    CD = 145.0

    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))+(self.数据3[self.等级] * self.攻击次数3 * (1 + self.TP成长 * self.TP等级))+(self.数据4[self.等级] * self.攻击次数4 * (1 + self.TP成长 * self.TP等级))) * self.倍率


class 元素圣灵技能12(元素圣灵主动技能):
    名称 = '元素震荡'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [0, 3911, 4310, 4706, 5103, 5500, 5897, 6293, 6692, 7088, 7485, 7881, 8279, 8675, 9074, 9470, 9867, 10263, 10661, 11057, 11456, 11852, 12249, 12645, 13043, 13439, 13837, 14234, 14631, 15027, 15426, 15821, 16219, 16616, 17013, 17409, 17808, 18203, 18599, 18998, 19394, 19791, 20187, 20586, 20981, 21380, 21776, 22173, 22569, 22968, 23364, 23761, 24158, 24555, 24951, 25350, 25746, 26143, 26540, 26937, 27333, 27732, 28128, 28525, 28922, 29319, 29715, 30114, 30510, 30907, 31303]
    攻击次数1 = 3
    数据2 = [0, 17608, 19394, 21180, 22968, 24754, 26540, 28326, 30114, 31899, 33685, 35472, 37257, 39045, 40831, 42617, 44403, 46191, 47977, 49762, 51550, 53336, 55122, 56908, 58696, 60481, 62268, 64054, 65842, 67627, 69413, 71200, 72985, 74773, 76559, 78345, 80131, 81919, 83704, 85490, 87278, 89064, 90850, 92636, 94424, 96209, 97995, 99782, 101567, 103355, 105141, 106927, 108713, 110501, 112287, 114072, 115860, 117646, 119432, 121218, 123006, 124791, 126578, 128364, 130149, 131937, 133723, 135510, 137295, 139083, 140869]
    攻击次数2 = 1
    数据3 = 0
    攻击次数3 = 0
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 2.6
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 += 0.11 * 16
        elif x == 1:
            self.攻击次数1 += 0.14 * 17
        

class 元素圣灵技能13(元素圣灵主动技能):
    名称 = '圣灵水晶'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据 = [0, 43031, 47396, 51761, 56127, 60493, 64859, 69223, 73588, 77953, 82320, 86685, 91051, 95416, 99783, 104147, 108512, 112878, 117243, 121608, 125975, 130340, 134706, 139071, 143435, 147802, 152167, 156533, 160898, 165265, 169630, 173995, 178359, 182725, 187091, 191457, 195822, 200187, 204554, 208919, 213284, 217649, 222014, 226380, 230746, 235112, 239477, 243842, 248209, 252573, 256938, 261304, 265669, 270036, 274401, 278767, 283132, 287496, 291863, 296228, 300593, 304959, 309325, 313691, 318056, 322420, 326786, 331152, 335517, 339883, 344248]
    攻击次数 = 1
    CD = 40.0
    演出时间 = 1.2
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率 *= 1.25

class 元素圣灵技能14(被动技能):
    名称 = '元素奥义'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 元素圣灵技能15(元素圣灵主动技能):
    名称 = '元素之门'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据 = [0, 4520, 4979, 5437, 5896, 6354, 6817, 7269, 7728, 8186, 8646, 9108, 9562, 10024, 10482, 10942, 11400, 11857, 12315, 12775, 13228, 13689, 14149, 14607, 15068, 15526, 15987, 16442, 16903, 17361, 17820, 18281, 18733, 19194, 19652, 20113, 20571, 21030, 21487, 21946, 22404, 22865, 23326, 23784, 24239, 24696, 25158, 25611, 26074, 26532, 26991, 27451, 27909, 28371, 28825, 29287, 29741, 30200, 30657, 31116, 31574, 32036, 32496, 32954, 33413, 33870, 34329, 34781, 35245, 35702, 36161]
    攻击次数 = 10
    CD = 45.0
    演出时间 = 1.2
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.攻击次数 = 1 * 13.25
        
class 元素圣灵技能17(元素圣灵主动技能):
    名称 = '第六元素'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据1 = [0, 2139, 2637, 3131, 3627, 4121, 4621, 5114, 5611, 6107, 6603, 7098, 7595, 8090, 8586, 9079, 9579, 10071, 10570, 11065, 11561, 12061, 12556, 13052, 13545, 14046, 14539, 15035, 15531, 16027, 16522, 17019, 17514, 18010, 18504, 19003, 19496, 19992, 20489, 20986, 21480, 21980, 22474, 22970, 23466, 23962, 24457, 24956, 25450, 25947, 26440, 26939, 27432, 27928, 28424, 28921, 29417, 29914, 30410, 30905, 31402, 31898, 32395, 32891, 33387, 33881, 34380, 34875, 35371, 35865, 36363]
    攻击次数1 = 20
    数据2 = [0, 99814, 122958, 146105, 169249, 192396, 215542, 238685, 261832, 284978, 308122, 331269, 354413, 377561, 400708, 423853, 446997, 470144, 493289, 516436, 539579, 562724, 585871, 609016, 632163, 655309, 678454, 701601, 724748, 747892, 771037, 794183, 817329, 840477, 863617, 886764, 909912, 933056, 956204, 979348, 1002493, 1025640, 1048785, 1071932, 1095078, 1118224, 1141370, 1164512, 1187659, 1210805, 1233949, 1257097, 1280244, 1303387, 1326533, 1349680, 1372825, 1395972, 1419115, 1442261, 1465409, 1488552, 1511699, 1534845, 1557988, 1581136, 1604280, 1627427, 1650573, 1673719, 1696865]
    攻击次数2 = 1
    CD = 180.0
    def 等效百分比(self, 武器类型):
        return ((self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级))+(self.数据2[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级))) * self.倍率

class 元素圣灵技能16(元素圣灵主动技能):
    名称 = '圣灵符文'
    所在等级 = 75
    等级上限 = 11
    基础等级 = 1
    是否有伤害 = 0
    是否主动 = 1
    data1 = [0, 131, 144, 156, 169, 181, 194, 206, 219, 231, 244, 256, 269, 281, 294, 306, 319, 331, 344, 356, 369]
    data2 = [0, 160, 174, 188, 201, 216, 229, 244, 257, 272, 285, 299, 313, 327, 341, 355, 369, 383, 397, 411, 424]

    自定义描述 = 1
    def 技能描述(self, 武器类型):
        temp = ''
        temp += '属性精通增幅：%.1f%%' % (self.data1[self.等级] / 10) + '<br>'
        temp += '魔法秀增幅：%.1f%%' % (self.data2[self.等级] / 10)
        return temp    

class 元素圣灵技能18(元素圣灵主动技能):
    名称 = '魔法秀'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    魔法秀数值 = [0, 22, 43, 65, 86, 108, 130, 151, 173, 194, 216, 238, 259, 281, 302, 324, 346, 367, 389, 410, 432]
    是否有伤害 = 0
    冷却关联技能 = ['冰墙','元素之门','元素之幕','元素震荡','圣灵水晶','烈焰冲击','天雷冲击','雷旋','杰克降临','湮灭黑洞','极冰盛宴','虚无之球']
    
    圣灵符文倍率 = 1.0
    def CD缩减倍率(self, 武器类型):
        return round(1 - 0.001 * self.魔法秀数值[self.等级] * self.圣灵符文倍率, 3)

class 元素圣灵技能19(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 元素圣灵技能20(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 元素圣灵技能21(被动技能):
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

元素圣灵技能列表 = []
i = 0
while i >= 0:
    try:
        exec('元素圣灵技能列表.append(元素圣灵技能'+str(i)+'())')
        i += 1
    except:
        i = -1

元素圣灵技能序号 = dict()
for i in range(len(元素圣灵技能列表)):
    元素圣灵技能序号[元素圣灵技能列表[i].名称] = i

元素圣灵一觉序号 = 0
元素圣灵二觉序号 = 0
元素圣灵三觉序号 = 0
for i in 元素圣灵技能列表:
    if i.所在等级 == 50:
        元素圣灵一觉序号 = 元素圣灵技能序号[i.名称]
    if i.所在等级 == 85:
        元素圣灵二觉序号 = 元素圣灵技能序号[i.名称]
    if i.所在等级 == 100:
        元素圣灵三觉序号 = 元素圣灵技能序号[i.名称]

元素圣灵护石选项 = ['无']
for i in 元素圣灵技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        元素圣灵护石选项.append(i.名称)

元素圣灵符文选项 = ['无']
for i in 元素圣灵技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        元素圣灵符文选项.append(i.名称)

class 元素圣灵角色属性(角色属性):

    实际名称 = '元素圣灵'
    角色 = '魔法师(女)'
    职业 = '元素师'

    武器选项 = ['魔杖','法杖']
    
    伤害类型选择 = ['魔法百分比']
    
    伤害类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.85
   
    远古记忆 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(元素圣灵技能列表)
        self.技能序号= deepcopy(元素圣灵技能序号)
   
    def CD倍率计算(self):
        圣灵符文 = self.技能栏[self.技能序号['圣灵符文']]
        self.技能栏[self.技能序号['属性精通']].圣灵符文倍率 = 1 + 圣灵符文.data1[圣灵符文.等级] / 1000
        self.技能栏[self.技能序号['魔法秀']].圣灵符文倍率 = 1 + 圣灵符文.data2[圣灵符文.等级] / 1000
        super().CD倍率计算()

class 元素圣灵(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 元素圣灵角色属性()
        self.角色属性A = 元素圣灵角色属性()
        self.角色属性B = 元素圣灵角色属性()
        self.一觉序号 = 元素圣灵一觉序号
        self.二觉序号 = 元素圣灵二觉序号
        self.三觉序号 = 元素圣灵三觉序号
        self.护石选项 = deepcopy(元素圣灵护石选项)
        self.符文选项 = deepcopy(元素圣灵符文选项)
 
