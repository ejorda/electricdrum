'''PyAudio example: Record a few seconds of audio and save to a WAVE file.

import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 15
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
'''
import sounddevice as sd
import soundfile as sf

duration = 15
  # Recording duration in seconds
samplerate = 44100  # Specify the desired samplerate

# Set the default audio input device to the system default (system audio output)
default_input_device = sd.default.device[0]

# Record the system audio
print("recording")
recording = sd.rec(int(duration * samplerate), channels=2, dtype='float32', blocking=True, device=default_input_device)

# Save the recording to a file (example using WAV format)
output_file = 'output.wav'
sf.write(output_file, recording, samplerate)

print(f"System audio recorded and saved to '{output_file}'.")
