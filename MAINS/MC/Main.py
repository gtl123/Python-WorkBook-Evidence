from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor, abs
from perlin_noise import PerlinNoise
from random import *
import time

app = Ursina()
window.color = color.rgb(0, 200, 211)
window.exit_button.visible = False
window.fullscreen = True
window.show_ursina_splash = True
scene.fog_density = .01
scene.fog_color = color.rgb(255, 255, 255)
prevTime = time.time()

noise = PerlinNoise(octaves=2, seed=randint(2000, 5000))
amp = 34
freq = 100
terrain = Entity(model=None, collider=None)
terrain_width = 100
subWidth = terrain_width
subsets = []
subCubes = []
sci = 0  # SubCube index
currentSubset = 0
terrainFinished = False
tex = "blank"

for i in range(subWidth):
    bud = Entity(model="cube")
    subCubes.append(bud)

for i in range(int((terrain_width * terrain_width) / subWidth)):
    bud = Entity(model=None)
    bud.parent = terrain
    subsets.append(bud)

shellies = []
shellWidth = 3
for i in range(shellWidth * shellWidth):
    bud = Entity(model="cube", collider="box")
    bud.visible = False
    shellies.append(bud)


def input(key):
    if key == "q" or key == "escape":
        quit()
    if key == "g":
        generateSubset()


def update():
    global prevZ, prevX, prevTime
    if abs(player.z - prevZ) > 1 or abs(player.x - prevX > 1):
        generateShell()
    if time.time() - prevTime > 0.05:
        generateSubset()
        prevTime = time.time()
    # Safety net in case of glitching through terrain
    if player.y < -amp + 1:
        player.y = player.height + floor(noise([player.x / freq, player.z / freq]) * amp)
        player.land()
    mob.look_at(player, axis="forward")
    #  mob.rotation_x = 0


def nMap(n, min1, max1, min2, max2):
    return ((n - min1) / (max1 - min1)) * (max2 - min2) + min2


def generateSubset():
    global sci, currentSubset, subWidth, freq, amp
    if currentSubset >= len(subsets):
        FinishTerrian()
        return
    for i in range(subWidth):
        x = subCubes[i].x = floor((i + sci) / terrain_width)
        z = subCubes[i].z = floor((i + sci) % terrain_width)
        y = subCubes[i].y = floor(noise([x / freq, z / freq]) * amp)
        subCubes[i].parent = subsets[currentSubset]
        r = nMap(x, -amp, amp, 0, 255)
        b = nMap(z, -amp, amp, 0, 255)
        g = nMap(y, -amp, amp, 0, 255)
        subCubes[i].color = color.rgb(r, g, b)
        subCubes[i].visible = False
    subsets[currentSubset].combine(auto_destroy=False)
    subsets[currentSubset].texture = tex
    sci += subWidth
    currentSubset += 1


def FinishTerrian():
    global terrainFinished
    if terrainFinished == True: return
    terrain.combine()
    terrain.texture = tex
    terrainFinished = True


def generateShell():
    global shellWidth, amp, freq
    for i in range(len(shellies)):
        x = shellies[i].x = floor((i / shellWidth) + player.x - 0.5 * shellWidth)
        z = shellies[i].z = floor((i % shellWidth) + player.z - 0.5 * shellWidth)
        shellies[i].y = floor(noise([x / freq, z / freq]) * amp)


mob = Entity(model="cube", scale=2, texture="brick", collider="mesh", y=2)

player = FirstPersonController()
player.cursor.visible = False
player.gravity = 0.5
player.x = player.z = 5
player.y = 12
prevZ = player.z
prevX = player.x
generateShell()
app.run()
