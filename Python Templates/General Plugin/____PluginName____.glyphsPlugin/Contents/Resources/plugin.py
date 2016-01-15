# encoding: utf-8

###########################################################################################################
#
#
#	General Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/General%20Plugin
#
#
###########################################################################################################


from GlyphsPlugins import *

class ____PluginClassName____(GeneralPlugin):
	def settings(self):
		self.name = Glyphs.localize({'en': 'My General Plugin', 'de': 'Mein allgemeines Plugin'})

	def start(self):
		print 'GeneralPlugin loaded'