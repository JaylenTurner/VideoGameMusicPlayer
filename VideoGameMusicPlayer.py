import pyaudio
import audioop
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your-client-id",
                                               client_secret="your-client-secret",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-modify-playback-state"))

# Audio capture setup
threshold = 1400  # Change this so that the only thing that turns down your sound is gunshots
capture_duration = 0.5  # Change to make more or less responsive
device_index = 2  # Change this to the index of CABLE Output (VB-Audio Virtual Cable)

# Get device info
audio = pyaudio.PyAudio()
device_info = audio.get_device_info_by_index(device_index)
print("Using device:", device_info['name'])

# Capture in-game audio
audio_format = pyaudio.paInt16
channels = 1
rate = 44100
chunk = int(rate * capture_duration)
stream = audio.open(format=audio_format, channels=channels, rate=rate, input=True, input_device_index=device_index, frames_per_buffer=chunk)

# Main loop
while True:
    # Capture audio
    audio_data = stream.read(chunk, exception_on_overflow=False)
    audio_level = audioop.rms(audio_data, 2)

    # Adjust music volume if audio_level is above the threshold
    if audio_level > threshold:
        sp.volume(0)  # Adjust volume to desired lower output
    else:
        sp.volume(45)  # Restore volume to desired higher output, so you can stil hear footsteps or other important sound queues

    time.sleep(capture_duration)