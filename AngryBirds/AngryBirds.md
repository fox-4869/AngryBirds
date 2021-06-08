# python AngryBirds 

![mainPicture](.\images\mainPicture.jpg)

![游戏截图](.\mdResource\游戏截图.png)

## 游戏简介

简介：

本游戏是基于2D引擎库pymunk的pygame小项目，将github的项目下载下来调通后做了些优化完成的。



图片音乐等资源来源于愤怒小鸟的游戏的资源文件。该游戏可以在论坛https://tieba.baidu.com/p/6492186070下载。

![资源图](.\mdResource\资源图.png)

## Pymunk库简介

官网http://www.pymunk.org/en/latest/

Pymunk官网简介http://www.pymunk.org/en/latest/overview.html

（以下源于谷歌翻译的Pymunk简介）

### 基础

您将在 Pymunk 中使用 4 个基本类。

- **刚体**( [`pymunk.Body`](http://www.pymunk.org/en/latest/pymunk.html#pymunk.Body))

  刚体具有物体的物理特性。（质量、位置、旋转、速度等）它本身没有形状。如果您之前使用过粒子物理学，那么刚体的主要区别在于它们能够旋转。刚体通常与游戏中的精灵具有 1:1 的相关性。您应该构建您的游戏，以便使用刚体的位置和旋转来绘制精灵。

- **碰撞形状**( [`pymunk.Circle`](http://www.pymunk.org/en/latest/pymunk.html#pymunk.Circle),[`pymunk.Segment`](http://www.pymunk.org/en/latest/pymunk.html#pymunk.Segment)和[`pymunk.Poly`](http://www.pymunk.org/en/latest/pymunk.html#pymunk.Poly))

  通过将形状附加到实体，您可以定义实体的形状。您可以将多个形状附加到单个实体以定义复杂的形状，或者如果不需要形状，则不附加任何形状。

- **约束/接头**（`pymunk.constraint.PinJoint`，`pymunk.constraint.SimpleMotor`以及其他许多）

  您可以在两个实体之间附加约束以约束它们的行为，例如保持两个实体之间的固定距离。

- **空间**( [`pymunk.Space`](http://www.pymunk.org/en/latest/pymunk.html#pymunk.Space))

  空间是 Pymunk 中的基本模拟单元。您向空间添加实体、形状和约束，然后整体更新空间。它们控制所有刚体、形状和约束如何相互作用。

实际模拟由空间完成。将应该模拟的对象添加到时空后，该[`pymunk.Space.step()`](http://www.pymunk.org/en/latest/pymunk.html#pymunk.Space.step)功能会以小步向前移动 。

### 为你的物理对象建模

#### 对象形状

您在屏幕上看到的不一定与实际物理对象的形状完全相同。通常用于碰撞检测（和其他物理模拟）的形状是屏幕上绘制内容的简化版本。即使是高端 AAA 游戏也将碰撞形状与屏幕上绘制的形状分开。

有很多原因可以解释为什么将碰撞形状和绘制的内容分开是好的。

- 使用更简单的碰撞形状会更快。因此，如果您有一个非常复杂的对象，例如一棵松树，为了性能，将其碰撞形状简化为三角形可能是有意义的。
- 使用更简单的碰撞形状可以使模拟更好。假设你有一个石头做的地板，中间有一个小裂缝。如果你在这个地板上拖一个盒子，它会卡在裂缝上。但是，如果您将地板简化为平面，您就不必担心东西会卡在裂缝中。
- 使碰撞形状比实际对象更小（或更大）会使游戏玩法更好。假设您在射击类游戏中拥有一艘玩家控制的飞船。很多时候，如果您将碰撞形状与基于它的外观相比应该更小一点，那么玩起来会感觉更有趣。

您可以在[Pymunk 中](http://www.pymunk.org/en/latest/examples.html#using-sprites-py)包含的[using_sprites.py](http://www.pymunk.org/en/latest/examples.html#using-sprites-py)示例中看到这样的示例。那里的物理形状是一个三角形，但绘制的是金字塔中的 3 个盒子，顶部有一条蛇。另一个示例是 [platformer.py](http://www.pymunk.org/en/latest/examples.html#platformer-py)示例，其中玩家被绘制为红灰色女孩。然而，物理形状只是相互叠加的几个圆形。

#### 质量、重量和单位

有时，Pymunk 的用户可能会对所有东西的定义单位感到困惑。例如，物体的质量是克还是千克？Pymunk 是无单位的，不关心您使用哪个单位。如果您将秒传递给期望时间的函数，那么您的时间单位是秒。如果您将像素传递给需要距离的函数，那么您的距离单位就是像素。

那么派生单位只是上述的组合。因此，在秒和像素的情况下，速度单位将是像素/秒。

（这与其他一些物理引擎相反，它们可以具有您应该使用的固定单位）



## 对游戏的分析

接下来步入正题，怎么去调用Pymunk去完成这个小project?

首先要对这个游戏进行简单的分析：

![简单分析](.\mdResource\简单分析.png)

然后对游戏中的流程进行简单分析

![游戏流程](.\mdResource\游戏流程.png)

通过对流程分析后大概可以知道有这么一些模块

![模块](.\mdResource\模块.png)



没有代码空谈这些是耍流氓的！！！





下面进入代码部分hhh

## 游戏内物体类

### Bird

```python
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
```

### Pig

```python
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
```

### Polygon

```python
class Polygon:
    def __init__(self, pos, length, height, space, mass=5.0):
        moment = 1000
        body = pm.Body(mass, moment)
        body.position = Vec2d(pos)
        shape = pm.Poly.create_box(body, (length, height))
        shape.color = (0, 0, 255)
        shape.friction = 0.5
        shape.collision_type = 2
        space.add(body, shape)
        self.body = body
        self.shape = shape
        wood = pygame.image.load("E:/py/AngryBirds/images/wood.png").convert_alpha()
        wood2 = pygame.image.load("E:/py/AngryBirds/images/wood2.png").convert_alpha()
        rect = pygame.Rect(251, 357, 86, 22)
        self.beam_image = wood.subsurface(rect).copy()
        rect = pygame.Rect(16, 252, 22, 84)
        self.column_image = wood2.subsurface(rect).copy()

    def to_pygame(self, p):
        """Convert pymunk to pygame coordinates"""
        # pygame右边x轴，下边y轴
        return int(p.x), int(-p.y+600)

    def draw_poly(self, element, screen):
        """Draw beams and columns"""
        # 梁横 柱竖
        poly = self.shape
        ps = poly.get_vertices()
        ps.append(ps[0])
        ps = map(self.to_pygame, ps)
        ps = list(ps)
        color = (255, 0, 0)
        pygame.draw.lines(screen, color, False, ps)
        if element == 'beams':
            p = poly.body.position
            p = Vec2d(self.to_pygame(p))
            angle_degrees = math.degrees(poly.body.angle) + 180
            rotated_logo_img = pygame.transform.rotate(self.beam_image,
                                                       angle_degrees)
            offset = Vec2d(rotated_logo_img.get_size()) / 2.
            p = p - offset
            np = p
            screen.blit(rotated_logo_img, (np.x, np.y))
        if element == 'columns':
            p = poly.body.position
            p = Vec2d(self.to_pygame(p))
            angle_degrees = math.degrees(poly.body.angle) + 180
            rotated_logo_img = pygame.transform.rotate(self.column_image,
                                                       angle_degrees)
            offset = Vec2d(rotated_logo_img.get_size()) / 2.
            p = p - offset
            np = p
            screen.blit(rotated_logo_img, (np.x, np.y))
```

Tips:

​		注意，pygame和pymunk的坐标系不一样！！！

下图为pygame的坐标图(懒的自己画图了，体谅一下)

![pygame坐标](.\mdResource\pygame坐标.png)

pymunk的y轴是向上的。



## 主要模块介绍

### 猪鸟碰撞

```python
def post_solve_bird_pig(arbiter, space, _):
    """Collision between bird and pig"""
    surface = screen
    a, b = arbiter.shapes
    bird_body = a.body
    pig_body = b.body
    p = to_pygame(bird_body.position)
    p2 = to_pygame(pig_body.position)
    r = 30
    pygame.draw.circle(surface, BLACK, p, r, 4)
    pygame.draw.circle(surface, RED, p2, r, 4)
    pigs_to_remove = []
    for pig in pigs:
        if pig_body == pig.body:
            pig.life -= 20
            pigs_to_remove.append(pig)
            global score
            score += 10000
    for pig in pigs_to_remove:
        space.remove(pig.shape, pig.shape.body)
        pigs.remove(pig)
```



### 发射小鸟

```python
if (event.type == pygame.MOUSEBUTTONUP and
        event.button == 1 and mouse_pressed):
    # Release new bird
    mouse_pressed = False
    if level.number_of_birds > 0:
        song_fly = 'E:/py/AngryBirds/music/bird 01 flying.wav'
        pygame.mixer.music.load(song_fly)
        pygame.mixer.music.play(0)

        level.number_of_birds -= 1
        t1 = time.time() * 1000
        xo = 154
        yo = 156
        if mouse_distance > rope_length:
            mouse_distance = rope_length
        if x_mouse < sling_x + 5:
            bird = Bird(mouse_distance, angle, xo, yo, space)
            birds.append(bird)
        else:
            bird = Bird(-mouse_distance, angle, xo, yo, space)
            birds.append(bird)
        if level.number_of_birds == 0:
            t2 = time.time()
```



其余部分在代码中看（主要还是写的有点乱，粘出来不好看，滑稽）
