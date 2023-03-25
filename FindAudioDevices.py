import pyaudio

audio = pyaudio.PyAudio()

print("Available input devices:")
for i in range(audio.get_device_count()):
    device_info = audio.get_device_info_by_index(i)
    if device_info.get("maxInputChannels") > 0:
        print(f"[{i}] {device_info['name']}")

print("\nAvailable output devices:")
for i in range(audio.get_device_count()):
    device_info = audio.get_device_info_by_index(i)
    if device_info.get("maxOutputChannels") > 0:
        print(f"[{i}] {device_info['name']}")

audio.terminate()