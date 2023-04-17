from sound.audio_device import AudioDevice
import sound.synth as synth
import sound.audio_tools as audio_tools
from sound.engine import Engine
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import math

app = Ursina()

Entity.default_shader = lit_with_shadows_shader
#aircraft = Entity(model="Aircraft.blend", colider="mesh", y=1, scale=0.25)
#propeller = Entity(model="propeller.blend", parent=aircraft, y=9.5)
ground = Entity(model='plane', collider='box', texture='grass', scale=100)
player = FirstPersonController(model=Capsule(), color=color.orange, speed=8, collider="mesh")
rpm = 2000
_fire_snd = synth.sine_wave_note(frequency=40, duration=1)
audio_tools.normalize_volume(_fire_snd)
audio_tools.exponential_volume_dropoff(_fire_snd, duration=0.06, base=5)

car_body = Entity(model="car body.blend", collider="mesh", z=15, y=1, scale=0.25, colour=color.orange, texture="brick")
front_wheel1 = Entity(model="wheel.blend", parent=car_body, x=-15, y=0, z=16, collider="mesh", texture="brick")
front_wheel2 = Entity(model="wheel.blend", parent=car_body, x=-15, y=0, z=-16, rotation_x=180, collider="mesh", texture="brick")
rear_wheel2 = Entity(model="wheel.blend", parent=car_body, x=32, y=0, z=16, collider="mesh", texture="brick")
rear_wheel1 = Entity(model="wheel.blend", parent=car_body, x=32, y=0, z=-16, rotation_x=180, collider="mesh", texture="brick")
driver_seat = Entity(model="seat.blend", parent=car_body, x=-3, y=4, z=0, collider="mesh", texture="brick",color =color.gold)
passenger_seat = Entity(model="seat.blend", parent=car_body, x=-3, y=4, z=-10, collider="mesh", texture="brick",color =color.gold)
player_state = "scene"
wheel =  Entity(model="wheel.blend",z = 30, collider="mesh", texture="brick")

# Engine specs
def Rotax_912_iS():
    return Engine(
        idle_rpm=2000,
        limiter_rpm=10000,
        strokes=4,
        cylinders=4,
        timing=[100, 200, 300, 400],
        fire_snd=_fire_snd,
        between_fire_snd=synth.silence(1)
    )


class Capsule(Mesh):
    def __init__(self, height=2, radius=.5, **kwargs):
        # make a capsule by stretching a sphere
        sphere_mesh = load_model('sphere', application.internal_models_compressed_folder, use_deepcopy=True)
        vertices = [Vec3(*v) + (Vec3(0, height, 0) * int(v[1] > 0)) + Vec3(0, .5, 0) for v in sphere_mesh.vertices]

        super().__init__(vertices=vertices, triangles=sphere_mesh.triangles, uvs=sphere_mesh.uvs,
                         normals=sphere_mesh.normals, colors=sphere_mesh.colors, **kwargs)

def Move(obj,amount):
    π = math.pi
    max_rpm = 10000
    environment_conditions = 30
    mass = 1000
    rpm = 0
    diameter = 10
    dist = 1 * (π / 180) * (diameter / 2)
    friction = (mass/1000)+(environment_conditions/100) + ((rpm/max_rpm)*-1)
    total_dist = 0
    while total_dist != amount:
        obj.rotation_z += 1
        if friction > 0.5:
            obj.x += dist





def input(key):
    global throttle, rpm,player_state
    if key == "escape":
        quit()
    if str(key).lower() == "q" or held_keys["q"] == 1:
        rpm += 100
    if str(key).lower() == "e" or held_keys["e"] == 1:
        rpm -= 100
    if str(key).lower() == "w" or held_keys["w"] == 1: #and player_state == "car"
        Move(front_wheel1, 100)
        #rear_wheel2.rotation_z -= 10
        #rear_wheel1.rotation_z += 10
        #front_wheel1.rotation_z -= 10
        #front_wheel2.rotation_z += 10
        #car_body.x -= 10
    if str(key).lower() == "f":
        if player_state != "car" :
            player_state = "car"
            player.parent = driver_seat
        else:
            player.parent = scene
            player_state = "scene"
    if str(key).lower() == "a"  or held_keys["a"] == 1 :
        front_wheel1.rotation_y = 30
        front_wheel2.rotation_y = 30
    elif str(key).lower() == "d"  or held_keys["d"] == 1 :
        front_wheel1.rotation_y =- 30
        front_wheel2.rotation_y = - 30
    else:
        front_wheel1.rotation_y = 0
        front_wheel2.rotation_y = 0



def update():
    # engine.throttle(1.0 if d else 0.0)
    # rear_wheel2.rotation_z -= 10
    # rear_wheel1.rotation_z += 10
    # front_wheel1.rotation_z -= 10
    # front_wheel2.rotation_z += 10
    if player_state == "car":
        player.x = driver_seat.x
        player.y = driver_seat.y
        player.z = driver_seat.z



sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
Sky()
engine = Rotax_912_iS()
audio_device = AudioDevice()
stream = audio_device.play_stream(engine.gen_audio)
thruster = Entity(model="thruster.blend", z=10)

app.run()
stream.close()
audio_device.close()
