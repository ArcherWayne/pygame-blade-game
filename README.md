# pygame-blade-game

 *pygame repo for blade game*
 
 *这是个垃圾游戏*
 
 *250sbxm*

***写nm的寻路系统, 滚***

# 中文文档

## 想要实现的游戏效果

### 英雄

- 存在一个英雄, 是玩家操作的角色. 
- 英雄具备血量, 伤害, 移速, 攻击距离, 攻击前摇和攻击后摇等属性. 
- 英雄有一个攻击距离, 右键点击小兵后首先会移动到攻击距离以内, 然后释放一个弹道. 
- 弹道具备弹道速度属性. 
- 弹道会一直以被点击小兵为目标匀速移动, 直到弹道和被点击小兵碰撞, 对被点击小兵造成伤害. 
  > 存在近战英雄, 攻击范围非常小, 但不等于0. 其弹道速度为最大值. 即弹道所消耗的时间为0. 

### 小兵
- 存在多个小兵, 是游戏事件按时间生成的角色.
- 小兵存在血量, 伤害, 移速, 攻击距离, 攻击前摇和攻击后摇等属性. 
  > 小兵的属性可能随游戏设计变化而修改. 
- 小兵存在非仇恨状态和仇恨状态两个不同的状态. 
- 当小兵与英雄或防御塔的距离大于一定值时, 小兵处于非仇恨状态, 时刻匀速向屏幕左边移动. 
- 当小兵与英雄或防御塔的距离小于一定值时, 小兵处于仇恨状态, 向英雄或防御塔进行移动. 
- 当小兵与英雄或防御塔的距离小于小兵攻击范围时, 小兵将对英雄或防御塔进行攻击. 攻击的对象由仇恨的目标决定. 
  >小兵对英雄的仇恨优先级高于小兵对防御塔的仇恨, 但是若???? 若什么若, 仇恨系统还没想好, 嘿几把

### 防御塔
- 存在两座防御塔, 自动对最近的小兵单位进行弹道攻击. 
- 防御塔存在血量, 伤害, 攻击间隔, 弹道速度等属性. 
- 防御塔可以使用金钱进行升级. 每次升级恢复一定的血量. 

### 补刀系统
- 补刀系统是游戏的核心玩法.
- 当小兵的血量是由英雄的攻击置为0或小于0时, 英雄获得一定金额的金钱奖励. 

# English Documentation
*i cAnNoT sPeAk eNgliSh, fuCk yOu*