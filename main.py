import wx

from pprint import pprint as pp

from colorsys import rgb_to_hls, hls_to_rgb

from base_mainwindow import BaseMainWindow

from app6_1 import DI_Script


class MainWindow(BaseMainWindow):

    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.app_book_status = {}

        # self.cmd_exit.Bind(wx.EVT_LEFT_DOWN, cmd_exit)
        # self.cmd_save.Bind(wx.EVT_LEFT_DOWN, self.cmd_save)
        self.SetPosition((0, 0))
        page6_1_init(self)
        self.app_book.SetSelection(6)

    def exec_ok(self, event):
        print "Ok"
        event.Skip()

    def exec_close(self, event):
        exit(0)
        event.Skip()

    def exec_tool_enter(self, event):
        print "Ok", event.GetSelection()
        event.Skip()

    def update_head_home(self, text):
        self.t_head_home.SetLabelText(text)
        self.bSizer18.Layout()

    def activate_home(self, event):
        self.update_head_home("    HOME")
        self.app_book.SetSelection(0)
        event.Skip()

    def activate_input(self, event):
        self.update_head_home("    INPUT")
        self.app_book.SetSelection(1)
        event.Skip()

    def activate_cleanup(self, event):
        self.update_head_home("    CLEAN UP")
        self.app_book.SetSelection(2)
        event.Skip()

    def activate_analysis(self, event):
        self.update_head_home("    ANALYSIS")
        self.app_book.SetSelection(3)
        event.Skip()

    def activate_edit(self, event):
        self.update_head_home("    PROD EDIT")
        self.app_book.SetSelection(4)
        event.Skip()

    def activate_panel(self, event):
        self.update_head_home("    COUPONS & PANEL")
        self.app_book.SetSelection(5)
        event.Skip()

    def activate_targets(self, event):
        self.update_head_home("    OVLAY & TARGETS")
        self.app_book.SetSelection(6)
        event.Skip()

    def activate_output(self, event):
        self.update_head_home("    OUTPUT")
        self.app_book.SetSelection(7)
        event.Skip()

    def init_module_page(self, event):
        selected_page = self.app_book.GetSelection() + 1

        if selected_page not in self.app_book_status.keys():
            if selected_page == 6:
                print "to do: Page 6 Initialized"
                self.app_book_status[selected_page] = {"initialized": True}
        event.Skip()

    def init_6subpage(self, event):
        selected_subpage = self.app_book.GetSelection() + 1

        if selected_subpage not in self.app_book_status.keys():
            if selected_subpage == 6:
                print "to do: Page 6 Initialized"
                self.app_book_status[selected_subpage] = {"initialized": True}
        event.Skip()

    def exit_script(self, event):
        exit(0)

    def cmd_save(self, event):
        app_data = {}
        row_data = []
        g = self.g_di_layers
        for i in xrange(g.NumberRows):
            j = i % 4
            g.SetCellValue(i, j+1, "1")

        for i in xrange(g.NumberRows):
            single_row = []
            for j in xrange(g.NumberCols):
                single_row.append(g.GetCellValue(i, j).encode('ascii', 'ignore'))
            row_data.append(single_row)

        app_data ={
            'layer_data': row_data,
            'target_set_data': [
                w.c_set_a.GetSelection(),
                w.c_set_b.GetSelection(),
                w.c_set_c.GetSelection(),
                w.c_set_d.GetSelection(),
            ]
        }

        print w.c_set_a.GetSelection()

        event.Skip()


def adjust_color_lightness(r, g, b, factor):
    h, l, s = rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    l = max(min(l * factor, 1.0), 0.0)
    r, g, b = hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)


def lighten_color(r, g, b, factor=0.1):
    return adjust_color_lightness(r, g, b, 1 + factor)


def darken_color(r, g, b, factor=0.1):
    return adjust_color_lightness(r, g, b, 1 - factor)


def page6_1_init(window):
    w = MainWindow
    if True:
        w = window
    g = w.g_di_layers

    di = DI_Script()

    # Virtual event handlers, override them in your derived class
    def on_mouse(event):
        e = wx.grid.GridEvent
        if True:
            e = event
        e_row = e.GetRow()
        e_col = e.GetCol()
        if e_row > 0 and e_col > 0:
            wx.CallLater(100, toggle_check_box)
        e.Skip()

    def toggle_check_box():
        g.cb.Value = not g.cb.Value
        after_check_box(g.cb.Value)

    def on_cell_selected(evt):
        if evt.Col in xrange(1, 5):
            wx.CallAfter(g.EnableCellEditControl)
        evt.Skip()

    def on_editor_created(evt):
        if evt.Col in xrange(1, 5):
            g.cb = evt.Control
            g.cb.WindowStyle |= wx.WANTS_CHARS
            g.cb.Bind(wx.EVT_KEY_DOWN, on_key_down)
            g.cb.Bind(wx.EVT_CHECKBOX, on_check_box)
        evt.Skip()

    def on_key_down(evt):
        if evt.KeyCode == wx.WXK_UP:
            if g.GridCursorRow > 0:
                g.DisableCellEditControl()
                g.MoveCursorUp(False)
        elif evt.KeyCode == wx.WXK_DOWN:
            if g.GridCursorRow < (g.NumberRows - 1):
                g.DisableCellEditControl()
                g.MoveCursorDown(False)
        elif evt.KeyCode == wx.WXK_LEFT:
            if g.GridCursorCol > 0:
                g.DisableCellEditControl()
                g.MoveCursorLeft(False)
        elif evt.KeyCode == wx.WXK_RIGHT:
            if g.GridCursorCol < (g.NumberCols - 1):
                g.DisableCellEditControl()
                g.MoveCursorRight(False)
        else:
            evt.Skip()

    def on_check_box(evt):
        after_check_box(evt.IsChecked())

    def after_check_box(is_checked):
        print 'after CheckBox', g.GridCursorRow, is_checked

    g.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, on_mouse)
    g.Bind(wx.grid.EVT_GRID_SELECT_CELL, on_cell_selected)
    g.Bind(wx.grid.EVT_GRID_EDITOR_CREATED, on_editor_created)

    g.SetDefaultCellFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))
    g.SetDefaultRowSize(22, True)

    rows = di.get_rows

    g.SetRowLabelSize(0)

    labels = ['LAYER','Set A', 'Set B', 'Set C', 'Set D']

    for i in range(len(labels)):
        g.SetColLabelValue(i, labels[i])

    attr = wx.grid.GridCellAttr()
    attr.SetEditor(wx.grid.GridCellBoolEditor())
    attr.SetRenderer(wx.grid.GridCellBoolRenderer())

    g.SetColSize(0, 150)

    g.SetColAttr(1, attr)
    g.SetColSize(1, 50)
    for i in range(2, 5):
        g.SetColAttr(i, attr.Clone())
        g.SetColSize(i, 50)

    for row in rows:
        g.AppendRows(1)

        rgb = tuple(int(row[2][i:i+2], 16) for i in (0, 2, 4))
        light_rgb = lighten_color(rgb[0], rgb[1], rgb[2], 0.2)
        rown = g.NumberRows-1
        g.SetCellBackgroundColour(rown, 0, light_rgb)
        g.SetCellValue(g.NumberRows-1, 0, row[0])

        for col in xrange(1,5):
            g.SetCellBackgroundColour(rown, col, rgb)
            g.SetCellAlignment(rown, col, wx.ALIGN_LEFT, wx.ALIGN_TOP)

    for itm in [w.ch_di_set1,
                w.ch_di_set2,
                w.ch_di_set3,
                w.ch_di_set4
                ]:
        itm.SetItems(di.cases)
        itm.SetSelection(0)




if __name__ == "__main__":
    app = wx.App()
    w = MainWindow(None)

    w.Show()
    app.MainLoop()
