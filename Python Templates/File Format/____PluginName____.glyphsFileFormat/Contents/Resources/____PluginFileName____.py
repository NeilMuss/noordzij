#!/usr/bin/env python
# encoding: utf-8

import objc
from Foundation import *
from AppKit import *
import sys, os, re, commands
from types import *


GlyphsFileFormatProtocol = objc.protocolNamed( "GlyphsFileFormat" )

class ____PluginClassName____ ( NSObject, GlyphsFileFormatProtocol ):
	settings_view = objc.IBOutlet()
	
	def init( self ):
		"""
		Do all initializing here.
		"""
		try:
			#Bundle = NSBundle.bundleForClass_( NSClassFromString( self.className() ));
			NSBundle.loadNibNamed_owner_( "____PluginFileName____Dialog", self )
			thisBundle = NSBundle.bundleForClass_( NSClassFromString( self.className() ) )
			self.toolbarIcon = NSImage.alloc().initWithContentsOfFile_( thisBundle.pathForImageResource_( "ExportIcon" ) )
			self.toolbarIcon.setName_( "ExportIcon" )
			return self
		except Exception as e:
			self.logToConsole( "init: %s" % str(e) )
		
	def title( self ):
		"""
		This is the human-readable name as it appears in the export dialog.
		"""
		try:
			return "____PluginMenuName____"
		except Exception as e:
			self.logToConsole( "title: %s" % str(e) )
	
	def toolbarTitle( self ):
		"""
		Name below the icon in the Export dialog toolbar.
		"""
		try:
			return "____PluginToolbarTitle____"
		except Exception as e:
			self.logToConsole( "toolbarTitle: %s" % str(e) )
			
	def toolbarIconName( self ):
		"""
		The filename suffix without the dot.
		"""
		try:
			return "xxx"
		except Exception as e:
			self.logToConsole( "toolbarIconName: %s" % str(e) )
	
	def groupID( self ):
		"""
		Determines the position in the Export dialog toolbar.
		Lower values are further to the left.
		"""
		try:
			return 100
		except Exception as e:
			self.logToConsole( "groupID: %s" % str(e) )
	
	def interfaceVersion( self ):
		"""
		Distinguishes the API version the plugin was built for. 
		Return 1.
		"""
		try:
			return 1
		except Exception as e:
			self.logToConsole( "interfaceVersion: %s" % str(e) )
	
	def progressWindow( self ):
		try:
			return None
		except Exception as e:
			self.logToConsole( "progressWindow: %s" % str(e) )
	
	def exportSettingsView( self ):
		"""
		Returns the view to be displayed in the export dialog.
		Don't touch this.
		"""
		try:
			return self.settings_view
		except Exception as e:
			self.logToConsole( "exportSettingsView: %s" % str(e) )
	
	def font( self ):
		try:
			return self._font
		except Exception as e:
			self.logToConsole( "font: %s" % str(e) )
	
	def setFont_( self, GSFontObj ):
		"""
		The GSFont object is assigned to the plugin prior to the export.
		This is used to publish the export dialog.
		"""
		try:
			self._font = GSFontObj
		except Exception as e:
			self.logToConsole( "setFont_: %s" % str(e) )
	
	def writeFont_error_( self, font, error ):
		"""
		Outputs a Font object. 
		This method is called when the Next button is pressed in the Export dialog,
		and should ask the user for the place to store the font.
		font: The font to export.
		error: On return, If the document contents could not be read, a pointer to an error object that encapsulates the reason they could not be read.
		return True if the operation was successful;
		"""
		try:
			# Build up an export string that will later be written to the file:
			# Don't forget \n at the end
			exportString = "Font: %s.\n" % font
			exportString += "....\n"
			
			# Ask for export destination and write the file:
			dialogMessage = "Choose export destination"
			dialogProposedFileName = font.familyName
			dialogFiletypes = [ self.toolbarIconName() ]
			filepath = self.saveFileDialog( message = dialogMessage, ProposedFileName = dialogProposedFileName, filetypes = dialogFiletypes )
			file = open( filepath, "w" )
			file.write( exportString )
			file.close()
			
			# return True if successful:
			return True
		except Exception as e:
			self.logToConsole( "writeFont_error_: %s" % str(e) )
			return False
	
	def writeFont_toURL_error_( self, font, URL, error ):
		"""
		Outputs a Font object to the specified URL.
		
		font: the font to export.
		URL: the URL to save the font to.
		error: on return, if the document contents could not be read, a pointer to an error object that encapsulates the reason they could not be read.
		
		return (True, None) if the operation was successful;
		otherwise return a tuple with False and an NSError object that contains info about the problem (False, NSError).
		
		NSError:
		https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSError_Class/Reference/Reference.html
		"""
		try:
			print "__writeFont_toURL_error_", font
			return ( True, None )
		except Exception as e:
			self.logToConsole( "writeFont_toURL_error_: %s" % str(e) )
			return ( False, error )
	
	def fontFromURL_ofType_error_( self, URL, fonttype, error ):
		"""
		Reads a Font object from the specified URL.
		
		URL: the URL to read the font from.
		error: on return, if the document contents could not be read, a pointer to an error object that encapsulates the reason they could not be read.
		Return the font object, or None if an error occurred.
		"""
		try:
			# Create a new font object:
			font = GSFont()
			# Add glyphs and other info here...
			pass
			# Return the font object to be opened in Glyphs:
			return font
		except Exception as e:
			self.logToConsole( "fontFromURL_ofType_error_: %s" % str(e) )
			return None
	
	def saveFileDialog( self, message=None, ProposedFileName=None, filetypes=None ):
		if filetypes is None:
			filetypes = []
		Panel = NSSavePanel.savePanel().retain()
		if message is not None:
			Panel.setTitle_( message )
		Panel.setCanChooseFiles_( True )
		Panel.setCanChooseDirectories_( False )
		Panel.setAllowedFileTypes_( filetypes )
		if ProposedFileName is not None:
			Panel.setNameFieldStringValue_( ProposedFileName )
		pressedButton = Panel.runModalForTypes_(filetypes)
		if pressedButton == 1: # 1=OK, 0=Cancel
			return Panel.filename()
		return None
		
	def logToConsole( self, message ):
		"""
		The variable 'message' will be passed to Console.app.
		Use self.logToConsole( "bla bla" ) for debugging.
		"""
		myLog = "Font format %s:\n%s" % ( self.title(), message )
		NSLog( myLog )
