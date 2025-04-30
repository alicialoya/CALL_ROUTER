import pyaudio
import wave

def record_audio(filename, duration=3, sr=16000):
    p = pyaudio.PyAudio()
    
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sr,
                    input=True,
                    frames_per_buffer=1024)
    
    print("Recording...")
    frames = []
    
    for i in range(0, int(sr / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    
    print("Finished recording.")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sr)
    wf.writeframes(b''.join(frames))
    wf.close()
