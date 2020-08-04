from PublicReference.base import *

class 极诣·阿修罗技能0(主动技能):
    名称 = '波动刻印'
    备注 = '(一轮,TP为基础精通)'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20
    基础 = 372
    CD = 1.0
    TP上限 = 3
    TP成长 = 0.1
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1.00 + 0.005 * self.等级, 5)
        else:
            return round(1.10 + 0.015 * (self.等级 - 20), 5)

class 极诣·阿修罗技能1(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['波动刻印']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class 极诣·阿修罗技能2(主动技能):
    名称 = '地裂·波动剑'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1669.54
    成长 = 188.48
    CD = 3.0
    TP成长 = 0.08
    TP上限 = 5

class 极诣·阿修罗技能3(主动技能):
    名称 = '鬼印珠'
    备注 = '(5印)'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 4485.24 * 1.003
    成长 = 505.78 * 1.003
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5

class 极诣·阿修罗技能4(主动技能):
    名称 = '邪光斩'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 5445.00
    成长 = 615.10
    CD = 10.0
    TP成长 = 0.10
    TP上限 = 5

class 极诣·阿修罗技能5(被动技能):
    名称 = '修罗邪光斩'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['邪光斩']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.45 + 0.05 * self.等级, 5)

class 极诣·阿修罗技能6(主动技能):
    名称 = '波动爆发'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 27
    基础 = 4505.52
    成长 = 854.50
    CD = 7.5
    TP成长 = 0.10
    TP上限 = 5

class 极诣·阿修罗技能7(被动技能):
    名称 = '挫折意志'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.13 + 0.02 * self.等级, 5)        

class 极诣·阿修罗技能8(主动技能):
    名称 = '冰刃·波动剑'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4576.38 * 1.003
    成长 = 517.63 * 1.003
    CD = 7
    TP成长 = 0.10
    TP上限 = 5

class 极诣·阿修罗技能9(主动技能):
    名称 = '杀意波动'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    基础 = 570.95
    成长 = 19.05
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 5

class 极诣·阿修罗技能10(主动技能):
    名称 = '爆炎·波动剑'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 12157.50 * 0.993
    成长 = 1371.18 * 0.993
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5

class 极诣·阿修罗技能11(主动技能):
    名称 = '无双波'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 11427.86
    成长 = 1290.17
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.20

class 极诣·阿修罗技能12(主动技能):
    名称 = '邪光波动阵'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 13024.19
    成长 = 1470.99
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.15
        self.CD *= 0.85

class 极诣·阿修罗技能13(主动技能):
    名称 = '不动明王阵'
    备注 = '(5印)'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 26424.63 * 0.98
    成长 = 2989.34 * 0.98
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.2381

class 极诣·阿修罗技能14(被动技能):
    名称 = '心眼'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['所有']
    关联技能2 = ['地裂·波动剑']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 16:
            return round(0.99 + 0.015 * self.等级, 5)  
        else:
            return round(1.23 + 0.02 * (self.等级 - 16), 5)  

    def 加成倍率2(self, 武器类型):
        return self.地波加成() / self.加成倍率(武器类型)

    def 地波加成(self):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 16:
            return round(1.105 + 0.015 * self.等级, 5)  
        else:
            return round(1.345 + 0.02 * (self.等级 - 16), 5)  

class 极诣·阿修罗技能15(主动技能):
    名称 = '暗天波动眼'
    备注 = '(终结)'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 35457.01
    成长 = 10704.25
    CD = 140.0

class 极诣·阿修罗技能16(主动技能):
    名称 = '波动剑·光翼'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    基础 = 1907.14
    成长 = 575.82
    TP成长 = 0.08
    CD = 1.2

class 极诣·阿修罗技能17(主动技能):
    名称 = '波动眼·天照'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    基础 = 2301.63
    成长 = 694.45
    TP成长 = 0.1
    CD = 2.5

class 极诣·阿修罗技能18(主动技能):
    名称 = '波动剑·闪枪'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    基础 = 3975.32
    成长 = 1199.99
    TP成长 = 0.1
    CD = 4.9

class 极诣·阿修罗技能19(主动技能):
    名称 = '波动剑·刺轮'
    备注 = '(含一轮平X)'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    基础 = 4496.63
    成长 = 1363.80
    CD = 1.0

class 极诣·阿修罗技能20(主动技能):
    名称 = '极冰·裂波剑'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 17180.21
    成长 = 1939.91
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.2309

class 极诣·阿修罗技能21(主动技能):
    名称 = '极炎·裂波剑'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 23087.13 * 1.009
    成长 = 2606.72 * 1.009
    CD = 35.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.2088

class 极诣·阿修罗技能22(主动技能):
    名称 = '天雷·波动剑'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 65775.64
    成长 = 7428.35
    CD = 40.0

class 极诣·阿修罗技能23(主动技能):
    名称 = '雷神之息'
    备注 = '(1次)'
    是否主动 = 0
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    基础 = 3302.59
    成长 = 624.43
    CD = 2.5
    关联技能 = ['所有']
    def 等效CD(self, 武器类型):
        return 2.5
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.06 + 0.02 * self.等级, 5)  

class 极诣·阿修罗技能24(主动技能):
    名称 = '天雷·降魔杵'
    备注 = '(终结)'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 51915.63 * 0.999
    成长 = 5865.91 * 0.999
    CD = 45.0

class 极诣·阿修罗技能25(主动技能):
    名称 = '天雷·降魔杵(雷针)'
    备注 = '(1轮)'
    所在等级 = 80
    等级上限 = 1
    基础等级 = 1
    基础 = 4952.01
    成长 = 560.13
    CD = 2.0

class 极诣·阿修罗技能26(主动技能):
    名称 = '雷神降世：裁决'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 115355.09 * 0.996
    成长 = 34839.29 * 0.996
    CD = 180

class 极诣·阿修罗技能27(被动技能):
    名称 = '波动视界：慧眼'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 极诣·阿修罗技能28(主动技能):
    名称 = '波动慧眼：无为法'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 121042.84
    成长 = 13667.14
    CD = 60.0

class 极诣·阿修罗技能29(主动技能):
    名称 = '波动神诀：万空'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 359630.24
    成长 = 108568.10
    CD = 290
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

极诣·阿修罗技能列表 = []
i = 0
while i >= 0:
    try:
        exec('极诣·阿修罗技能列表.append(极诣·阿修罗技能'+str(i)+'())')
        i += 1
    except:
        i = -1

极诣·阿修罗技能序号 = dict()
for i in range(len(极诣·阿修罗技能列表)):
    极诣·阿修罗技能序号[极诣·阿修罗技能列表[i].名称] = i

极诣·阿修罗一觉序号 = 15
极诣·阿修罗二觉序号 = 26
极诣·阿修罗三觉序号 = 29


极诣·阿修罗护石选项 = ['无']
for i in 极诣·阿修罗技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣·阿修罗护石选项.append(i.名称)

极诣·阿修罗符文选项 = ['无', '邪光斩', '波动爆发', '冰刃·波动剑', '鬼印珠', '爆炎·波动剑', '无双波', '邪光波动阵', '不动明王阵', '极冰·裂波剑', '极炎·裂波剑', '天雷·波动剑', '天雷·降魔杵']

class 极诣·阿修罗角色属性(角色属性):

    实际名称 = '极诣·阿修罗'
    角色 = '鬼剑士(男)'
    职业 = '阿修罗'

    武器选项 = ['太刀','钝器','巨剑','短剑']
    
    伤害类型选择 = ['魔法固伤']
    
    伤害类型 = '魔法固伤'
    防具类型 = '板甲'
    防具精通属性 = ['智力']

    主BUFF = 1.59
   
    远古记忆 = 0
    刀魂之卡赞 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(极诣·阿修罗技能列表)
        self.技能序号= deepcopy(极诣·阿修罗技能序号)

    def 伤害指数计算(self):

        self.技能栏[self.技能序号['波动剑·光翼']].等级 = self.技能栏[self.技能序号['暗天波动眼']].等级
        self.技能栏[self.技能序号['波动眼·天照']].等级 = self.技能栏[self.技能序号['暗天波动眼']].等级
        self.技能栏[self.技能序号['波动剑·闪枪']].等级 = self.技能栏[self.技能序号['暗天波动眼']].等级
        self.技能栏[self.技能序号['波动剑·刺轮']].等级 = self.技能栏[self.技能序号['暗天波动眼']].等级

        self.技能栏[self.技能序号['波动剑·光翼']].TP等级 = self.技能栏[self.技能序号['地裂·波动剑']].TP等级
        self.技能栏[self.技能序号['波动眼·天照']].TP等级 = self.技能栏[self.技能序号['冰刃·波动剑']].TP等级
        self.技能栏[self.技能序号['波动剑·闪枪']].TP等级 = self.技能栏[self.技能序号['爆炎·波动剑']].TP等级

        self.技能栏[self.技能序号['天雷·降魔杵(雷针)']].等级 = self.技能栏[self.技能序号['天雷·降魔杵']].等级
        self.技能栏[self.技能序号['天雷·降魔杵(雷针)']].倍率 = self.技能栏[self.技能序号['天雷·降魔杵']].倍率

        super().伤害指数计算()

class 极诣·阿修罗(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 极诣·阿修罗角色属性()
        self.角色属性A = 极诣·阿修罗角色属性()
        self.角色属性B = 极诣·阿修罗角色属性()
        self.一觉序号 = 极诣·阿修罗一觉序号
        self.二觉序号 = 极诣·阿修罗二觉序号
        self.三觉序号 = 极诣·阿修罗三觉序号
        self.护石选项 = deepcopy(极诣·阿修罗护石选项)
        self.符文选项 = deepcopy(极诣·阿修罗符文选项)
