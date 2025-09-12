# ----------------------------------
# LOTFR1 menu.py
# Version: 1.0.0
# Last Updated: 2025/07/24
# ----------------------------------

### Project Settings

#Add Formats
nuke.addFormat("3840 1600 LOTFR_Full")
nuke.addFormat("1920 800 LOTFR_Half")
nuke.addFormat("960 400 LOTFR_Quarter")

#Set Default Format
nuke.knobDefault("Root.format", "LOTFR_Full")
