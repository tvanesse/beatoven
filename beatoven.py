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

from gi.repository import Gtk
from gi.repository.Gdk import keyval_name

class BeatKey:
    """
    A key with a Sample assigned to it.
    """
    def __init__(self, key_name, filename=None):
        self.sample = Sample(filename)
        self.key_name = key_name
        self.key_button_id = "key_butt_" + self.key_name;
        
    def set_sample(filename):
        self.sample = Sample(filename)
        

class Session:
    """
    A Beatoven session.
    """
    def __init__(self, keyboard_layout="belgian"):
        # Create a set of BeatKeys to cover the keyboard
        #TODO
        pass

def key_pressed_handler(widget, event, data=None):
    key_pressed = keyval_name(event.keyval).lower()
    for bk in beatkeys:
        if bk.key_name == key_pressed:
            # Highlight the corresponding button
            # Play the sample
            bk.sample.play_resume()

builder = Gtk.Builder()
builder.add_from_file("gui/main.glade")

window1 = builder.get_object("window1")
window1.connect("delete-event", Gtk.main_quit)
window1.connect("key-press-event", key_pressed_handler)

sample_chooser = builder.get_object("sample_chooser")
loaded = sample_chooser.run()

if loaded == -3:
    print(sample_chooser.get_filename() + " selected")

window1.show_all()
Gtk.main()
