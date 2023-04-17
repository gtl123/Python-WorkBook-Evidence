from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

Entity.default_shader = lit_with_shadows_shader

ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(model=Capsule(), color=color.orange, speed=8)
MeshCollider(player)
gun = Entity(model="gun.blend", parent=player, position=(0.2, 1, 1), scale=(0.01, 0.01, 0.01), color=color.red, on_cooldown=False)
gun.muzzle_flash = Entity(parent=gun, position = Vec3(0, -1, 5), world_scale=.5, model='circle', color=color.yellow, enabled=False)

shootables_parent = Entity()
mouse.traverse_target = shootables_parent

class Capsule(Mesh):
    def __init__(self, height=2, radius=.5, **kwargs):
        # make a capsule by stretching a sphere
        sphere_mesh = load_model('sphere', application.internal_models_compressed_folder, use_deepcopy=True)
        vertices = [Vec3(*v) + (Vec3(0,height,0) * int(v[1] > 0)) + Vec3(0,.5,0) for v in sphere_mesh.vertices]

        super().__init__(vertices=vertices, triangles=sphere_mesh.triangles, uvs=sphere_mesh.uvs, normals=sphere_mesh.normals, colors=sphere_mesh.colors, **kwargs)




for i in range(100):
    Entity(model='cube', scale=1, texture='brick',
           x=random.uniform(-100, 100),
           z=random.uniform(-100, 100) + 8,
           collider='box',
           )


def update():
    if held_keys['left mouse']:
        shoot()


def shoot():
    if not gun.on_cooldown:
        gun.on_cooldown = True
        gun.muzzle_flash.enabled = True
        from ursina.prefabs.ursfx import ursfx
        ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=10, wave='noise',
              pitch=random.uniform(-13, -12), pitch_change=-12, speed=3.0)
        invoke(gun.muzzle_flash.disable, delay=.05)
        invoke(setattr, gun, 'on_cooldown', False, delay=.15)
        if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
            mouse.hovered_entity.hp -= 10
            mouse.hovered_entity.blink(color.green)



class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=shootables_parent, model='cube', scale_y=2, origin_y=-.5, color=color.light_gray, collider='box', **kwargs)
        self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
        self.max_hp = 100
        self.hp = self.max_hp

    def update(self):
        dist = distance_xz(player.position, self.position)
        if dist > 40:
            return

        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)


        self.look_at_2d(player.position, 'y')
        hit_info = raycast(self.world_position + Vec3(0,1,0), self.forward, 30, ignore=(self,))
        if hit_info.entity == player:
            if dist > 2:
                self.position += self.forward * time.dt * 5

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if value <= 0:
            destroy(self)
            return

        self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
        self.health_bar.alpha = 1

# Enemy()
enemies = [Enemy(x=x*4) for x in range(4)]


def pause_input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        editor_camera.enabled = not editor_camera.enabled

        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position

        application.paused = editor_camera.enabled

pause_handler = Entity(ignore_paused=True, input=pause_input)


sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
Sky()

app.run()




