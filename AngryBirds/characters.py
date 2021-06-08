import pymunk as pm
from pymunk import Vec2d


class Bird:
    def __init__(self, distance, angle, x, y, space):
        self.life = 20  # 生命值20
        mass = 5        # 质量  5
        radius = 12     # 刚力小圆圈的半径 12
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))  # 转动惯量
        body = pm.Body(mass, inertia)   # 初始化刚体
        body.position = x, y            # 鸟的位置
        power = distance * 53           # 放大距离，优化参数增强游戏体验
        impulse = power * Vec2d(1, 0)   # 冲力
        angle = -angle
        body.apply_impulse_at_local_point(impulse.rotated(angle))   # rotated 旋转向量 apply_impulse_at_local_point 在局部点施加脉冲
        shape = pm.Circle(body, radius, (0, 0))  # 碰撞类型圆形好计算
        shape.elasticity = 0.95         # 弹性
        shape.friction = 0.9            # 摩擦力
        shape.collision_type = 0        # 碰撞类型
        space.add(body, shape)          # 加到2维平面

        self.body = body
        self.shape = shape


class Pig:
    def __init__(self, x, y, space):
        self.life = 20
        mass = 5
        radius = 14
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = x, y
        shape = pm.Circle(body, radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 0.9
        shape.collision_type = 1
        space.add(body, shape)
        self.body = body
        self.shape = shape
