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
from samples import Sample

import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((640, 480))


if __name__ == "__main__":
    import sys
    import time
    s1 = Sample(sys.argv[1])
    s2 = Sample(sys.argv[2])
    s3 = Sample(sys.argv[3])
    
    samples = (s1, s2, s3)
    
    running = True

    while running:
        time.sleep(0.01)
        for s in samples:
            if not s.is_active():
                s.rewind()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_KP0:
                    s1.rewind()
                    s1.play_resume()
                elif event.key == K_KP_PERIOD:
                    s2.rewind()
                    s2.play_resume()
                elif event.key == K_KP_ENTER:
                    s3.rewind()
                    s3.play_resume()
                    
            
