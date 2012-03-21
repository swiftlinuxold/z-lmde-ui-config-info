#!/bin/bash 
# This is the script for the Network Wizard
# Command for executing this script: config-network.sh (NOT "sh config-network.sh")

export InfoWizard=$(cat <<End_of_Text

<window title="`gettext $"System Information Wizard"`" window-position="1">

<vbox>
  <frame>
  <hbox>
	<vbox>
	  <frame>
	  <hbox>
		<button>
		<input file>"/usr/share/icons/gTangish-2.0a1/32x32/devices/computer.png"</input>
		<action>hardinfo &</action>
		</button>
		<text use-markup="true" width-chars="15"><label>"`gettext $"General System Information"`"</label></text>
      </hbox>
      </frame>
	</vbox>

	<vbox>
	  <frame>
	  <hbox>
		<button>
		<input file>"/usr/share/icons/hicolor/32x32/apps/gsmartcontrol.png"</input>
		<action>su-to-root -X -c gsmartcontrol</action>
		</button>
		<text use-markup="true" width-chars="15"><label>"`gettext $"Hard Drive Health"`"</label></text>
      </hbox>
      </frame>
	</vbox>
  </hbox>
  </frame>
		
  <hbox>
	<button>
	  <label>"`gettext $"Close"`"</label>
	  <input file>"/usr/share/icons/gTangish-2.0a1/16x16/actions/dialog-cancel.png"</input>
	  <action>EXIT:close</action>
	</button>
  </hbox>
</vbox>
  
</window>
End_of_Text
)

gtkdialog -c --program=InfoWizard
unset InfoWizard
