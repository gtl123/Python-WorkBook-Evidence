from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
App = Ursina()
Entity.default_shader = lit_with_shadows_shader





class Voxel(Button,Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            color=color.gold,
            texture="brick",
            highlight_color=color.blue
        )

def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)


def Chunk(pos):
    for z in range(4):
        for x in range(4):
            for y in range(4):
                 Voxel(position=(pos[0]+x, pos[1]+y, pos[2]+z))





class Capsule(Mesh):
    def __init__(self, height=2, radius=.5, **kwargs):
        # make a capsule by stretching a sphere
        sphere_mesh = load_model('sphere', application.internal_models_compressed_folder, use_deepcopy=True)
        vertices = [Vec3(*v) + (Vec3(0,height,0) * int(v[1] > 0)) + Vec3(0,.5,0) for v in sphere_mesh.vertices]

        super().__init__(vertices=vertices, triangles=sphere_mesh.triangles, uvs=sphere_mesh.uvs, normals=sphere_mesh.normals, colors=sphere_mesh.colors, **kwargs)


class Player(Entity):
    def __init__(self,**kwargs):
        super().__init__(model=Capsule(), color=color.light_gray, collider=None,eternal = True, **kwargs)
        MeshCollider(self)
        self.cam = FirstPersonController()


    def update(self):

        self.position = Vec3(self.cam.position[0], self.cam.position[1]+2, self.cam.position[2])
        if self.position[0] >= self.px + 4 or self.position[0] <= self.px - 4:

            self.px = self.position[0]
            self.py = self.position[1]
            self.pz = self.position[2]
            Chunk(self.position)
        elif self.position[1] >= self.py + 4 or self.position[1] <= self.py - 4:

            self.px = self.position[0]
            self.py = self.position[1]
            self.pz = self.position[2]
            Chunk(self.position)
        elif self.position[2] >= self.pz + 4 or self.position[2] <= self.pz - 4:

            self.px = self.position[0]
            self.py = self.position[1]
            self.pz = self.position[2]
            Chunk(self.position)



litsource = DirectionalLight()
litsource.look_at(Vec3(10, -10, 10))
p = Player()
Chunk(p.position)
p.px = p.position[0]
p.py = p.position[1]
p.pz = p.position[2]
sky = Sky()
App.run()