#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os

class Wizard:

    def __init__(self):
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL) # Create a new window
        self.window.set_title("System Information Wizard") # Set the window title
        self.window.set_border_width(20)# Sets the border width of the window.
        self.window.resize (350,100)
        self.window.connect("delete_event", self.delete_event) # Click on the X -> close window
        
        # Create vertical box
        self.vbox = gtk.VBox ()
        
        # EACH OPTION GETS ITS OWN HORIZONTAL BOX (wizard_option)
        
        # OPTION 1: General System Information
        self.box_image = '/usr/share/icons/gTangish-2.0a1/32x32/devices/computer.png'
        self.box_label = 'General System Information'
        self.box = self.wizard_option (self.box_image, self.box_label, self.hardinfo)
        self.vbox.add (self.box)
        
        # Option 2: GSmartControl
        self.box_image = '/usr/share/icons/hicolor/32x32/apps/gsmartcontrol.png'
        self.box_label = 'Hard Drive Health'
        self.box = self.wizard_option (self.box_image, self.box_label, self.gsmartcontrol)
        self.vbox.add (self.box)
        
        # Show everything
        #self.table.show()
        self.window.add (self.vbox)
        self.window.show ()
        self.window.show_all ()
        
        
        
    # This callback quits the program
    def delete_event (self, widget, event, data=None):
        gtk.main_quit()
        return False
        
    def hardinfo (self, widget, callback_data=None):
        os.system ('hardinfo &')
        
    def gsmartcontrol (self, widget, callback_data=None):
        os.system ('su-to-root -X -c gsmartcontrol')
    
    def wizard_option (self, filename_image, string_label, fctn_action):
        # Horizontal box
        self.hbox = gtk.HBox ()
        
        # Button icon
        self.image = gtk.Image ()
        self.image.set_from_file (filename_image)
        self.image.show ()
        
        # Button
        self.button = gtk.Button()
        self.button.set_size_request(64, 64)
        self.button.connect('clicked', fctn_action)
        self.button.add(self.image) # Add image to button
        self.button.show()
        self.hbox.pack_start(self.button, False, False, 0)
        
        # Label
        self.label = gtk.Label (' ' + string_label)
        self.label.set_alignment (0, .5)
        self.label.show ()
        
        self.hbox.pack_start(self.label, False, False, 0)
        self.hbox.show ()
        
        return self.hbox
    
def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    Wizard()
    main()
