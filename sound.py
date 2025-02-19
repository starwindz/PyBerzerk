import pyaudio
import wave
import threading
import io
import numpy as np
import keyboard
import time
import random
from utils import *
from debug import *

class WavePlay:
    """Class for preloading and playing a WAV file from memory using PyAudio, with pitch and sampling rate adjustments."""

    def __init__(self, filename):
        """Load the entire WAV file into memory and store original parameters."""
        self.p = pyaudio.PyAudio()
        self.wav_memory = self._load_sound(filename)
        self.original_rate, self.original_audio_data, self.params = self._read_wav_data()

        # Default playback settings
        self.audio_data = self.original_audio_data.copy()  # Keep a working copy
        self.pitch_factor = 1.0
        self.sampling_rate_factor = 1.0

    def _load_sound(self, filename):
        """Read the entire WAV file and store it in memory."""
        with open(filename, 'rb') as f:
            audio_binary = f.read()  # Read the entire file as binary
        return io.BytesIO(audio_binary)  # Store in memory

    def _read_wav_data(self):
        """Extract audio parameters and raw data from the WAV file in memory."""
        self.wav_memory.seek(0)
        with wave.open(self.wav_memory, 'rb') as wf:
            params = wf.getparams()
            audio_data = wf.readframes(wf.getnframes())
            rate = wf.getframerate()
            
        if len(audio_data) % 2 != 0:
            audio_data += b'\x00'
        return rate, np.frombuffer(audio_data, dtype=np.int16), params

    def set_audio_params(self, pitch_factor=1.0, sampling_rate_factor=1.0):
        """Set both pitch and sampling rate, ensuring they stay within 0.1 to 2.0."""
        self.pitch_factor = max(0.1, min(pitch_factor, 2.0))  # Clamp between 0.1 and 2.0
        self.sampling_rate_factor = max(0.1, min(sampling_rate_factor, 2.0))
        self._apply_pitch_shift()

    def _apply_pitch_shift(self):
        """Adjust the pitch by remapping audio sample indices from the original data."""
        num_samples = int(len(self.original_audio_data) / self.pitch_factor)
        new_indices = np.linspace(0, len(self.original_audio_data) - 1, num_samples).astype(int)
        self.audio_data = self.original_audio_data[new_indices]  # Always start from the original data

    def play(self, randomPlay):
        """Play the WAV file from memory with adjusted sampling rate and pitch."""
        def stream_audio():
            if randomPlay:
                _pitch = generate_random_number(1.00, 1.20, 0.01)
                _sample_rate = generate_random_number(1.00, 1.20, 0.01)
                self.set_audio_params(_pitch, _sample_rate)
                _msg = '# pitch = ' + str(round(_pitch, 2)) + ', ' + 'sample_rate = ' + str(round(_sample_rate, 2))
                Debug.printf(_msg)
            
            self.wav_memory.seek(0)
            wf = wave.open(self.wav_memory, 'rb')

            # Apply sampling rate modification
            adjusted_rate = int(self.original_rate * self.sampling_rate_factor)

            # Open an audio stream with the modified sampling rate
            stream = self.p.open(
                format=self.p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=adjusted_rate,  # Use modified sampling rate
                output=True
            )

            # Convert adjusted audio to bytes
            audio_bytes = self.audio_data.astype(np.int16).tobytes()

            # Stream the audio in chunks
            chunk_size = 1024
            for i in range(0, len(audio_bytes), chunk_size):
                stream.write(audio_bytes[i:i+chunk_size])

            stream.stop_stream()
            stream.close()
            wf.close()

        threading.Thread(target=stream_audio, daemon=True).start()

    def close(self):
        """Terminate the PyAudio instance."""
        self.p.terminate()

'''
# Example usage:
if __name__ == "__main__":
    BULLET_SOUND_PATH = "bullet.wav"

    player = WavePlay(BULLET_SOUND_PATH)

    pitch_factor = 1.0
    sampling_rate_factor = 1.0
    running = True

    print("Controls (Real-time, No Enter Required!):")
    print("[U] Increase pitch (up to 2.0)")
    print("[L] Decrease pitch (down to 0.1)")
    print("[S] Increase sampling rate (up to 2.0)")
    print("[D] Decrease sampling rate (down to 0.1)")
    print("[Space] Play sound")
    print("[Q] Quit")

    # Use keyboard hotkeys for real-time control
    def increase_pitch():
        global pitch_factor
        pitch_factor = min(2.0, pitch_factor + 0.1)
        player.set_audio_params(pitch_factor, sampling_rate_factor)
        print(f"\rPitch: {pitch_factor:.2f}, Sampling Rate: {sampling_rate_factor:.2f}", end="")

    def decrease_pitch():
        global pitch_factor
        pitch_factor = max(0.1, pitch_factor - 0.1)
        player.set_audio_params(pitch_factor, sampling_rate_factor)
        print(f"\rPitch: {pitch_factor:.2f}, Sampling Rate: {sampling_rate_factor:.2f}", end="")

    def increase_sampling_rate():
        global sampling_rate_factor
        sampling_rate_factor = min(2.0, sampling_rate_factor + 0.1)
        player.set_audio_params(pitch_factor, sampling_rate_factor)
        print(f"\rPitch: {pitch_factor:.2f}, Sampling Rate: {sampling_rate_factor:.2f}", end="")

    def decrease_sampling_rate():
        global sampling_rate_factor
        sampling_rate_factor = max(0.1, sampling_rate_factor - 0.1)
        player.set_audio_params(pitch_factor, sampling_rate_factor)
        print(f"\rPitch: {pitch_factor:.2f}, Sampling Rate: {sampling_rate_factor:.2f}", end="")

    def play_sound():
        player.play()

    def quit_program():
        global running
        running = False

    # Bind keys to actions
    keyboard.add_hotkey("u", increase_pitch)
    keyboard.add_hotkey("l", decrease_pitch)
    keyboard.add_hotkey("s", increase_sampling_rate)
    keyboard.add_hotkey("d", decrease_sampling_rate)
    keyboard.add_hotkey("space", play_sound)
    keyboard.add_hotkey("q", quit_program)

    # Use keyboard.wait() instead of a busy loop
    keyboard.wait("q")  # Wait for "Q" to exit

    player.close()
'''

class Sound:
    def __init__(self):
        self.soundFolder = 'sound\\';
        
        """
        00: attack it
        01: attack the humanoid
        02: charge it
        03: chicken fight like a robot
        04: destroy it
        05: destroy the intruder
        06: get the chicken
        07: get the intruder
        08: got the humanoid got the intruder
        09: intruder alert intruder alert
        10: kill the intruder
        11: shoot it
        12: the humanoid must not escape
        13: the intruder must not escape
        """
        
        self.voiceFiles = [
            'attack it.wav',
            'attack the humanoid.wav',
            'charge it.wav',
            'chicken fight like a robot.wav',
            'destroy it.wav',
            'destroy the intruder.wav',
            'get the chicken.wav',
            'get the intruder.wav',
            'got the humanoid got the intruder.wav',
            'intruder alert intruder alert.wav',
            'kill the intruder.wav',
            'shoot it.wav',
            'the humanoid must not escape.wav',
            'the intruder must not escape.wav'
        ]
        
        self.playerFiredLaser = WavePlay(self.soundFolder + '_player fired laser_.wav')
        self.robotFiredLaser = WavePlay(self.soundFolder + '_robot fired laser_.wav')       
        self.playerIsDestroyed = WavePlay(self.soundFolder + '_player is destroyed_.wav')
        self.robotIsDestroyed = WavePlay(self.soundFolder + '_robot is destroyed_.wav')
        self.voices = [WavePlay(self.soundFolder + file) for file in self.voiceFiles[:14]]
       
        self.prevTime = time.time()

    def playPlayerFiredLaser(self):
        self.playerFiredLaser.play(False)


    def playRobotFiredLaser(self):
        self.robotFiredLaser.play(False)

        
    def playPlayerIsDestroyed(self):
        self.playerIsDestroyed.play(False)


    def playRobotIsDestroyed(self):
        self.robotIsDestroyed.play(False)
        
    def playRobotVoice(self, index):
        curTime = time.time()
        gapTime = curTime - self.prevTime
        if gapTime > random.randrange(3, 7):  # 3 to 6
            self.prevTime = curTime
            self.voices[index].play(True)
            Debug.printf('# random robot voice played: %f', round(gapTime, 1))
        else:
            pass
            # Debug.printf('# random robot voice skipped: %f', round(gapTime, 1))

sound = Sound()