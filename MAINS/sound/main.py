import controls
from audio_device import AudioDevice
import synth
import audio_tools
from engine import Engine

_fire_snd = synth.sine_wave_note(frequency=40, duration=1)
audio_tools.normalize_volume(_fire_snd)
audio_tools.exponential_volume_dropoff(_fire_snd, duration=0.06, base=5)


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


engine = Rotax_912_iS()
audio_device = AudioDevice()
stream = audio_device.play_stream(engine.gen_audio)

try:
    controls.capture_input(engine)  # blocks until user exits
except KeyboardInterrupt:
    pass
stream.close()
audio_device.close()
