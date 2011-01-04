"""
Custom configuration for qtile

One of the idea is to get as close as possible to
Wmii's behavior.

"""
from libqtile.manager import Key, Screen, Group, Drag
from libqtile.command import lazy
from libqtile import layout, bar, widget
import libqtile


mod = 'mod4'
xterm = 'sakura'


# Groups
groups = [
  Group("main"),
  Group("music"),
  Group("www"),
]

# Keys
keys = [
  Key([mod], "Return", lazy.spawn("sakura")),
  Key([mod], "p", lazy.spawncmd()),
  Key([mod, "shift"], "r", lazy.restart()),
  Key([mod, "shift"], "q", lazy.shutdown()),

  Key([mod, "shift"], "c", lazy.window.kill()),
  Key([mod], "space", lazy.window.toggle_floating()),
  Key([mod], "m",     lazy.window.toggle_maximize()),
  Key([mod], "f",     lazy.window.toggle_fullscreen()),

  Key([mod], "k", lazy.layout.down()),
  Key([mod], "j", lazy.layout.up()),
  Key([mod], "h", lazy.layout.previous()),
  Key([mod], "l", lazy.layout.next()),

  # Those are specific to the Stack layout:
  Key([mod], "s", lazy.layout.toggle_split()),
  Key([mod], "d", lazy.layout.toggle_split()),
  Key([mod], "a", lazy.layout.add()),
  Key([mod], "d", lazy.layout.delete()),
  Key([mod, "shift"], "h", lazy.layout.client_to_previous()),
  Key([mod, "shift"], "l", lazy.layout.client_to_next()),

  # Dealing with groups:
  Key([mod], "b", lazy.group.prevgroup()),
  Key([mod], "n", lazy.group.nextgroup()),
  Key([mod], "t", lazy.addgroupcmd()),
  Key([mod, "shift"], "t", lazy.window.togroupcmd()),
  Key([mod, "shift"], "d", lazy.group.delgroup())
]

for i in range(0, 9):
  keys.append(
	Key([mod], str(i+1), lazy.group.switch_to_group_number(i))
  )

# Mouse:
mouse = [
  Drag([mod], "Button1", lazy.window.set_position_floating(),
	start=lazy.window.get_position()),
  Drag([mod], "Button3", lazy.window.set_size_floating(),
	start=lazy.window.get_size()),
]

# Layouts:
layouts = [
  layout.Stack(stacks=1, wmii_style=True),
]

# Screens:
screens = [
  Screen(
	bottom = bar.Bar(
	  [
		widget.GroupBox(borderwidth=2, fontsize=14, padding=1, margin_x=1, margin_y=1),
		widget.Sep(),
		widget.Prompt(),
		widget.Spacer(),
		widget.Sep(),
		widget.CPUGraph(width=50, graph_color='0066FF', fill_color='001188'),
		widget.MemoryGraph(width=50, graph_color='22FF44', fill_color='11AA11'),
		widget.Sep(),
		widget.Systray(),
		widget.Clock('%d/%m/%y %H:%M', fontsize=14, padding=6),
	  ],
	  24
    ),
  ),
]



def on_new_client(client):
  """Called when a new client appears.

  """
  client_class = client.window.get_wm_class()[0]
  if client_class == "Navigator":
	client.togroup("www")

libqtile.hook.subscribe.client_new(on_new_client)

# vim: sw=2 noet
