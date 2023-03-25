# VideoGameMusicPlayer
This code allows you to enjoy your two favorite things, music and video games, without having to tradeoff in game performance. Listen to your favorite songs through Spotify but also be able to hear footsteps and gunshots in your favorite FPS game.

<video src='https://youtu.be/tPXNFMpF_PM'>

# Use steps:
1. First you'll need Spotify premium in order to use their API
2. Log into your API dashboard, make a new app, and gather your credentials. You'll need your client id and client secret.
3. Click on edit settings within your app and add this url under Redirect URIs: http://localhost:8888/callback, then save those changes.
4. Add your client id and client secret to the VideoGameMusicPlayer script.
5. Download a virtual audio cable from this website: https://vb-audio.com/Cable/ (Don't worry if you don't know what this is).
6. Once the audio cable is installed, restart your pc.
7. Once your pc is back on, go into your sound settings on windows and make sure that your input and output settings are set to your usual headset and microphone and not your new CABLE's you just downloaded.
8. Now open up your game of choice and go to your audio settings, in the Output Device setting, choose CABLE Input (VB-Audio Virtual Cable). While your here, make sure your input device is your regular microphone.
9. Now in your windows settings open up Volume Mixer and select your game, then click on the Output device setting and make sure to change it from default to CABLE Input (VB-Audio Virtual Cable).
10. Now pull up your sound control panel, for Windows 11, you'll want to go back to your sound settings, scroll down to advanced and then click more sound settings. 
11. Once your here go to the recording tab and right click the CABLE Output, click properties, click the listen tab, check the Listen to this device box, and change the playback through this device option to your normal headphones. Click apply and OK.
12. Now run the FindAudioDevices script to get an output of all your audio devices and their index, find the index for CABLE Output (VB-Audio Virtual Cable) in the Available input devices: section of the printed results. 
13. Go to the VideoGameMusicPlayer script and change the device_index variable to this index.
14. All there is left to do is start up the spotify application, play a song, and then run the VideoGameMusicPlayer script.
15. Go back to your game and hop into a session testing the threshold and sp.volume() variables, you'll have to stop the  code and rerun after each change.
16. I found what works best is to set the threshold variable as high as possible so your music only gets quiter when your shooting, and to have the highest output of the sp.volume() variables to be loud enough that your able to jam out and get pumped up but quiet enough that its not distracting and your still able to hear footsteps and other important audio queues good enough.
