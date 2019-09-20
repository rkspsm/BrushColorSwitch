from krita import *

switch_brush_action_name = "previous_preset"
switch_color_action_name = "toggle_fg_bg"
erase_action_name = "erase_action"

class BrushColSwitchExtension(Extension):
  def __init__(self,parent):
    super().__init__(parent)

  def createActions(self,window):
    self.bc_switch = window.createAction("bc_switch", "Brush Color Switch")
    self.bc_switch_keep_eraser = \
        window.createAction("bc_switch_keep_eraser", "Brush Color Switch(Keep Eraser)")

    krita = Krita.instance()
    switch_brush_action = krita.action(switch_brush_action_name)
    switch_color_action = krita.action(switch_color_action_name)
    erase_action = krita.action(erase_action_name)

    @self.bc_switch.triggered.connect
    def on_bc_switch_trigger():
      doc = krita.activeDocument()
      is_eraser = erase_action.isChecked()

      if is_eraser:
        switch_brush_action.trigger()
        switch_color_action.trigger()
      else:
        switch_color_action.trigger()
        switch_brush_action.trigger()

    @self.bc_switch_keep_eraser.triggered.connect
    def on_bc_switch_keep_eraser_trigger():
      doc = krita.activeDocument()
      erase_action_state = erase_action.isChecked()
      switch_brush_action.trigger()
      switch_color_action.trigger()
      if erase_action_state != erase_action.isChecked():
        erase_action.trigger()

  def setup(self):
    pass

Krita.instance().addExtension(BrushColSwitchExtension(Krita.instance()))

