
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class AppWindow(Gtk.Window):


	"""docstring for AppWindow"""
	def __init__(self, config):

		Gtk.Window.__init__(self, title=config.getAppName())
		self.connect("delete-event", Gtk.main_quit)
		headerBar = self._buildHeaderBar()
		self.set_titlebar(headerBar)
		mainView = self._buildMainView()
		self.add(mainView)
		self.show_all()
		Gtk.main()

	def _buildHeaderBar(self):
		headerBar = Gtk.HeaderBar()
		headerBar.set_show_close_button(True)
		return headerBar
		
	def _buildMainView(self):
		grid = Gtk.Grid()
		column = Gtk.Grid()
		grid.attach(column, 0, 0, 1, 1)
		button1 = Gtk.Button(label='Echt jetzt')
		button2 = Gtk.Button(label='Wirklich!!')

		column.attach(button1, 0, 0, 1, 1)
		column.attach(button2, 0, 1, 1, 1)
		return grid

