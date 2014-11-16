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

def play_sample(widget, event, data=None):
    s = Sample("samples/debiles.wav")
    key_pressed = keyval_name(event.keyval)
    if key_pressed == 'a':
        s.play_resume()

builder = Gtk.Builder()
builder.add_from_file("gui/main.glade")

window1 = builder.get_object("window1")
window1.connect("delete-event", Gtk.main_quit)
window1.connect("key-press-event", play_sample)

window1.show_all()
Gtk.main()
