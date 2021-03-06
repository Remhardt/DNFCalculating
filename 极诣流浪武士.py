from base import *

class 极诣流浪武士主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '巨剑':
            return round(self.CD / self.恢复 * 1.1, 1)
        if 武器类型 == '太刀':
            return round(self.CD / self.恢复 * 0.95, 1)
        if 武器类型 == '钝器':
            return round(self.CD / self.恢复 * 1.05, 1)
        if 武器类型 == '短剑':
            return round(self.CD / self.恢复 * 1.0, 1)
        if 武器类型 == '光剑':
            return round(self.CD / self.恢复 * 0.81, 1)

class 极诣流浪武士技能0(被动技能):
    名称 = '返本归元'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.04 * self.等级, 5)

class 极诣流浪武士技能1(被动技能):
    名称 = '三花聚顶'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.065 + 0.02 * self.等级, 5)

class 极诣流浪武士技能2(被动技能):
    名称 = '七星耀华'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 极诣流浪武士技能3(被动技能):
    名称 = '剑仙之境'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 极诣流浪武士技能4(极诣流浪武士主动技能):
    名称 = '四象引'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 3336.0
    成长 = 393.0
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7

class 极诣流浪武士技能5(极诣流浪武士主动技能):
    名称 = '一花渡江'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3078.0
    成长 = 366.0
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7

class 极诣流浪武士技能6(极诣流浪武士主动技能):
    名称 = '樱落斩'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3192.0
    成长 = 377.0
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7

class 极诣流浪武士技能7(极诣流浪武士主动技能):
    名称 = '圆舞斩'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4029.0
    成长 = 473.0
    CD = 11.0
    TP成长 = 0.10
    TP上限 = 7

class 极诣流浪武士技能8(极诣流浪武士主动技能):
    名称 = '碎岩裂地掌'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5664.0
    成长 = 648.0
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7


class 极诣流浪武士技能9(极诣流浪武士主动技能):
    名称 = '游龙掌'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7512.3
    成长 = 867.7
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7


class 极诣流浪武士技能10(极诣流浪武士主动技能):
    名称 = '乱花葬'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 24
    基础 = 10720.3
    成长 = 2032.7
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.262

class 极诣流浪武士技能11(极诣流浪武士主动技能):
    名称 = '回天璇鸣剑'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 10388.0
    成长 = 1222.0
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7

class 极诣流浪武士技能12(极诣流浪武士主动技能):
    名称 = '湮烈掌'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 14070.0
    成长 = 1620.0
    CD = 30
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.209

class 极诣流浪武士技能13(极诣流浪武士主动技能):
    名称 = '花舞千魂杀'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 18111.0
    成长 = 2060.0
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.20

class 极诣流浪武士技能14(极诣流浪武士主动技能):
    名称 = '花开寒影'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 48012.6
    成长 = 14488.7
    CD = 145

class 极诣流浪武士技能15(极诣流浪武士主动技能):
    名称 = '啸空十字斩'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 16317.0
    成长 = 1842.0
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.002
        self.CD *= 0.80

class 极诣流浪武士技能16(极诣流浪武士主动技能):
    名称 = '如来神掌'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 29412.0
    成长 = 3323.0
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.184

class 极诣流浪武士技能17(极诣流浪武士主动技能):
    名称 = '莲花剑舞'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 48850.0
    成长 = 5510.0
    CD = 40.0

class 极诣流浪武士技能18(极诣流浪武士主动技能):
    名称 = '樱花劫'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 57984.0
    成长 = 6544.0
    CD = 45.0

class 极诣流浪武士技能19(极诣流浪武士主动技能):
    名称 = '飞花逐月'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 104599.6
    成长 = 31578.8
    CD = 180.0

class 极诣流浪武士技能20(极诣流浪武士主动技能):
    名称 = '落英惊鸿掌'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 94750.3
    成长 = 10698.8
    CD = 60.0

class 极诣流浪武士技能21(极诣流浪武士主动技能):
    名称 = '轻云出月风静夜'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 295573.5
    成长 = 89252.8
    CD = 290.0

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

极诣流浪武士技能列表 = []
i = 0
while i >= 0:
    try:
        exec('极诣流浪武士技能列表.append(极诣流浪武士技能'+str(i)+'())')
        i += 1
    except:
        i = -1

极诣流浪武士技能序号 = dict()
for i in range(len(极诣流浪武士技能列表)):
    极诣流浪武士技能序号[极诣流浪武士技能列表[i].名称] = i

极诣流浪武士一觉序号 = 0
极诣流浪武士二觉序号 = 0
极诣流浪武士三觉序号 = 0
for i in 极诣流浪武士技能列表:
    if i.所在等级 == 50:
        极诣流浪武士一觉序号 = 极诣流浪武士技能序号[i.名称]
    if i.所在等级 == 85:
        极诣流浪武士二觉序号 = 极诣流浪武士技能序号[i.名称]
    if i.所在等级 == 100:
        极诣流浪武士三觉序号 = 极诣流浪武士技能序号[i.名称]

极诣流浪武士护石选项 = ['无']
for i in 极诣流浪武士技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣流浪武士护石选项.append(i.名称)

极诣流浪武士符文选项 = ['无']
for i in 极诣流浪武士技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        极诣流浪武士符文选项.append(i.名称)

class 极诣流浪武士角色属性(角色属性):

    职业名称 = '极诣流浪武士'

    武器选项 = ['光剑','巨剑','钝器','太刀','短剑']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['物理百分比']
    
    #默认
    伤害类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2.25
   
    #基础属性(含唤醒)
    基础力量 = 963.0
    基础智力 = 788.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
  
    def __init__(self):
        self.技能栏= copy.deepcopy(极诣流浪武士技能列表)
        self.技能序号= copy.deepcopy(极诣流浪武士技能序号)

class 极诣流浪武士(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 极诣流浪武士角色属性()
        self.角色属性A = 极诣流浪武士角色属性()
        self.角色属性B = 极诣流浪武士角色属性()
        self.一觉序号 = 极诣流浪武士一觉序号
        self.二觉序号 = 极诣流浪武士二觉序号
        self.三觉序号 = 极诣流浪武士三觉序号
        self.护石选项 = copy.deepcopy(极诣流浪武士护石选项)
        self.符文选项 = copy.deepcopy(极诣流浪武士符文选项)
