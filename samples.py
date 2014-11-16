"""
Beatoven - The universal sampler
Copyright (C) 2014  Thomas Vanesse - vanessethomas(at)gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import pyaudio
import wave

class Sample():
    """
    A sample to be played in Beatoven.
    """
    def __init__(self, filename):
        self.wf     = wave.open(filename, 'rb')
        self.length = self.wf.getnframes()
        self.p      = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                                  channels=self.wf.getnchannels(),
                                  rate=self.wf.getframerate(),
                                  output=True,
                                  stream_callback=self.callback,
                                  start=False)
                                  
    def callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
#        if self.wf.tell() == self.length:
#            print("About to stop the stream")
#        if not self.is_active():
#            self.stream.stop_stream()
#            print("Stream stopped")
#            self.wf.rewind()
#            print("Stream reloaded")
#            return (data, pyaudio.paComplete)
        return (data, pyaudio.paContinue)
        
    def play_resume(self):
        self.stream.start_stream()
        
    def pause(self):
        self.stream.stop_stream()
        
    def rewind(self):
        self.stream.stop_stream()
        self.wf.rewind()
        
    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.wf.close()
        self.p.terminate()
        
    def is_active(self):
        return self.stream.is_active()
        
        
        
if __name__ == "__main__":
    import sys
    import time
    
    s1 = Sample(sys.argv[1])
    s2 = Sample(sys.argv[1])
    
    s1.play_resume()
    time.sleep(2)
    print(s1.is_active())
    s1.rewind()
    s1.play_resume()
    time.sleep(2)
    
    while s1.is_active():
        time.sleep(0.1)
