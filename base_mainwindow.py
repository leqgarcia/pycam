# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 15 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class BaseMainWindow
###########################################################################

class BaseMainWindow(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"XaaS Automation © MMXIX", pos=wx.DefaultPosition,
                          size=wx.Size(1000, 749), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(
            wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        self.app_menu = wx.MenuBar(0)
        self.script = wx.Menu()
        self.app_menu.Append(self.script, u"Script")

        self.SetMenuBar(self.app_menu)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer15.SetMinSize(wx.Size(-1, 0))
        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"res/logo apct heigh 50.png", wx.BITMAP_TYPE_ANY),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_bitmap1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_bitmap1.SetMinSize(wx.Size(230, 54))

        bSizer15.Add(self.m_bitmap1, 0, wx.ALL, 1)

        self.m_toolBar1 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL)
        self.m_toolBar1.SetToolBitmapSize(wx.Size(-1, 43))
        self.m_toolBar1.AddSeparator()

        self.tool_home = self.m_toolBar1.AddTool(wx.ID_ANY, u"tool",
                                                 wx.Bitmap(u"res/xaas_logo_32.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                 wx.ITEM_NORMAL, wx.EmptyString, u"Job Home Page", None)

        self.tool_input = self.m_toolBar1.AddTool(wx.ID_ANY, u"tool", wx.Bitmap(u"res/input.png", wx.BITMAP_TYPE_ANY),
                                                  wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Input Scripts", None)

        self.tool_cleanup = self.m_toolBar1.AddTool(wx.ID_ANY, u"tool",
                                                    wx.Bitmap(u"res/cleanup.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, wx.EmptyString, u"Clean Up / Netlist", None)

        self.tool_analysis = self.m_toolBar1.AddTool(wx.ID_ANY, u"tool",
                                                     wx.Bitmap(u"res/analyze.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                     wx.ITEM_NORMAL, wx.EmptyString, u"DFM Analysis", None)

        self.tool_edit = self.m_toolBar1.AddTool(wx.ID_ANY, u"tool", wx.Bitmap(u"res/pcb.png", wx.BITMAP_TYPE_ANY),
                                                 wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Prod Edit", None)

        self.m_tool11 = self.m_toolBar1.AddTool(wx.ID_ANY, u"tool", wx.Bitmap(u"res/panel.png", wx.BITMAP_TYPE_ANY),
                                                wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Coupons & Panel", None)

        self.tool_targets = self.m_toolBar1.AddTool(wx.ID_ANY, u"tool",
                                                    wx.Bitmap(u"res/targets.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap,
                                                    wx.ITEM_NORMAL, wx.EmptyString, u"Overlay & Targets", None)

        self.m_tool12 = self.m_toolBar1.AddTool(wx.ID_ANY, u"tool", wx.Bitmap(u"res/output.png", wx.BITMAP_TYPE_ANY),
                                                wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Output System", None)

        self.m_toolBar1.AddSeparator()

        self.m_toolBar1.AddSeparator()

        self.t_head_home = wx.StaticText(self.m_toolBar1, wx.ID_ANY, u"PyCAM Scripting System v 0.1",
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.t_head_home.Wrap(-1)

        self.t_head_home.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow"))

        self.m_toolBar1.AddControl(self.t_head_home)
        self.m_toolBar1.Realize()

        bSizer15.Add(self.m_toolBar1, 1, wx.EXPAND, 0)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer15.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer15, 0, wx.EXPAND, 0)

        self.app_book = wx.Simplebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.page_0 = wx.Panel(self.app_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.bSizer18 = wx.BoxSizer(wx.VERTICAL)

        self.lb_home = wx.Listbook(self.page_0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT)
        self.m_panel11 = wx.Panel(self.lb_home, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.lb_home.AddPage(self.m_panel11, u"Summary", True)
        self.m_panel9 = wx.Panel(self.lb_home, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl4 = wx.TextCtrl(self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer20.Add(self.m_textCtrl4, 1, wx.ALL | wx.EXPAND, 1)

        bSizer22 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer22.SetMinSize(wx.Size(-1, 50))
        self.m_button3 = wx.Button(self.m_panel9, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer22.Add(self.m_button3, 0, wx.ALL | wx.EXPAND, 0)

        self.m_button4 = wx.Button(self.m_panel9, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer22.Add(self.m_button4, 0, wx.ALL | wx.EXPAND, 0)

        bSizer20.Add(bSizer22, 0, wx.EXPAND, 0)

        self.m_panel9.SetSizer(bSizer20)
        self.m_panel9.Layout()
        bSizer20.Fit(self.m_panel9)
        self.lb_home.AddPage(self.m_panel9, u"Job Log", False)
        self.m_panel10 = wx.Panel(self.lb_home, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer21 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel10.SetSizer(bSizer21)
        self.m_panel10.Layout()
        bSizer21.Fit(self.m_panel10)
        self.lb_home.AddPage(self.m_panel10, u"Job Notes", False)

        self.bSizer18.Add(self.lb_home, 1, wx.EXPAND | wx.ALL, 3)

        self.page_0.SetSizer(self.bSizer18)
        self.page_0.Layout()
        self.bSizer18.Fit(self.page_0)
        self.app_book.AddPage(self.page_0, u"a page", False)
        self.page_1 = wx.Panel(self.app_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self.page_1, wx.ID_ANY, u"TBD INPUT", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText6.Wrap(-1)

        self.m_staticText6.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow"))
        self.m_staticText6.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        bSizer12.Add(self.m_staticText6, 0, wx.ALL | wx.EXPAND, 0)

        self.page_1.SetSizer(bSizer12)
        self.page_1.Layout()
        bSizer12.Fit(self.page_1)
        self.app_book.AddPage(self.page_1, u"a page", False)
        self.page_2 = wx.Panel(self.app_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer123 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText63 = wx.StaticText(self.page_2, wx.ID_ANY, u"TBD CLEAN UP", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText63.Wrap(-1)

        self.m_staticText63.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow"))
        self.m_staticText63.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        bSizer123.Add(self.m_staticText63, 0, wx.ALL | wx.EXPAND, 0)

        self.page_2.SetSizer(bSizer123)
        self.page_2.Layout()
        bSizer123.Fit(self.page_2)
        self.app_book.AddPage(self.page_2, u"a page", False)
        self.page_3 = wx.Panel(self.app_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer1231 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText631 = wx.StaticText(self.page_3, wx.ID_ANY, u"TBD ANALYSIS", wx.DefaultPosition,
                                             wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText631.Wrap(-1)

        self.m_staticText631.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow"))
        self.m_staticText631.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        bSizer1231.Add(self.m_staticText631, 0, wx.ALL | wx.EXPAND, 0)

        self.page_3.SetSizer(bSizer1231)
        self.page_3.Layout()
        bSizer1231.Fit(self.page_3)
        self.app_book.AddPage(self.page_3, u"a page", False)
        self.page_4 = wx.Panel(self.app_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer121 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText61 = wx.StaticText(self.page_4, wx.ID_ANY, u"TBD PROD", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText61.Wrap(-1)

        self.m_staticText61.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow"))
        self.m_staticText61.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        bSizer121.Add(self.m_staticText61, 0, wx.ALL | wx.EXPAND, 0)

        self.page_4.SetSizer(bSizer121)
        self.page_4.Layout()
        bSizer121.Fit(self.page_4)
        self.app_book.AddPage(self.page_4, u"a page", False)
        self.page_5 = wx.Panel(self.app_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer122 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText62 = wx.StaticText(self.page_5, wx.ID_ANY, u"TBD CPNs PANEL", wx.DefaultPosition,
                                            wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText62.Wrap(-1)

        self.m_staticText62.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow"))
        self.m_staticText62.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        bSizer122.Add(self.m_staticText62, 0, wx.ALL | wx.EXPAND, 0)

        self.page_5.SetSizer(bSizer122)
        self.page_5.Layout()
        bSizer122.Fit(self.page_5)
        self.app_book.AddPage(self.page_5, u"a page", False)
        self.page_6 = wx.Panel(self.app_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bx_targets = wx.BoxSizer(wx.VERTICAL)

        self.m_listbook121 = wx.Listbook(self.page_6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT)
        self.pn_di_app = wx.Panel(self.m_listbook121, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bx_tgt_app = wx.BoxSizer(wx.HORIZONTAL)

        bSizer211 = wx.BoxSizer(wx.VERTICAL)

        self.g_di_layers = wx.grid.Grid(self.pn_di_app, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.g_di_layers.CreateGrid(0, 5)
        self.g_di_layers.EnableEditing(True)
        self.g_di_layers.EnableGridLines(True)
        self.g_di_layers.EnableDragGridSize(False)
        self.g_di_layers.SetMargins(0, 0)

        # Columns
        self.g_di_layers.EnableDragColMove(False)
        self.g_di_layers.EnableDragColSize(True)
        self.g_di_layers.SetColLabelSize(30)
        self.g_di_layers.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.g_di_layers.EnableDragRowSize(True)
        self.g_di_layers.SetRowLabelSize(80)
        self.g_di_layers.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.g_di_layers.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer211.Add(self.g_di_layers, 1, wx.ALL | wx.EXPAND, 5)

        bSizer221 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer221.SetMinSize(wx.Size(-1, 50))
        self.bt_di_save = wx.Button(self.pn_di_app, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bt_di_save.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bSizer221.Add(self.bt_di_save, 1, wx.ALL | wx.EXPAND, 2)

        self.bt_di_undo = wx.Button(self.pn_di_app, wx.ID_ANY, u"Reload", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bt_di_undo.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bSizer221.Add(self.bt_di_undo, 1, wx.ALL | wx.EXPAND, 2)

        self.bt_di_undo1 = wx.Button(self.pn_di_app, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bt_di_undo1.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bSizer221.Add(self.bt_di_undo1, 1, wx.ALL | wx.EXPAND, 2)

        bSizer211.Add(bSizer221, 0, wx.EXPAND, 1)

        bx_tgt_app.Add(bSizer211, 1, wx.EXPAND, 1)

        bSizer23 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText22 = wx.StaticText(self.pn_di_app, wx.ID_ANY, u"Select Target Set", wx.DefaultPosition,
                                            wx.Size(-1, 27), wx.ALIGN_CENTER_HORIZONTAL | wx.BORDER_THEME)
        self.m_staticText22.Wrap(-1)

        self.m_staticText22.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bSizer23.Add(self.m_staticText22, 0, wx.ALL | wx.EXPAND, 5)

        bSizer23.Add((0, 5), 0, 0, 5)

        self.tx_di_set1 = wx.StaticText(self.pn_di_app, wx.ID_ANY, u"Target Set    A", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.tx_di_set1.Wrap(-1)

        self.tx_di_set1.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bSizer23.Add(self.tx_di_set1, 0, wx.ALL, 5)

        ch_di_set1Choices = []
        self.ch_di_set1 = wx.Choice(self.pn_di_app, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_di_set1Choices, 0)
        self.ch_di_set1.SetSelection(0)
        self.ch_di_set1.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

        bSizer23.Add(self.ch_di_set1, 0, wx.ALL | wx.EXPAND, 5)

        self.tx_di_set2 = wx.StaticText(self.pn_di_app, wx.ID_ANY, u"Target Set    B", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.tx_di_set2.Wrap(-1)

        self.tx_di_set2.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bSizer23.Add(self.tx_di_set2, 0, wx.ALL, 5)

        ch_di_set2Choices = []
        self.ch_di_set2 = wx.Choice(self.pn_di_app, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_di_set2Choices, 0)
        self.ch_di_set2.SetSelection(0)
        self.ch_di_set2.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

        bSizer23.Add(self.ch_di_set2, 0, wx.ALL | wx.EXPAND, 5)

        self.tx_di_set3 = wx.StaticText(self.pn_di_app, wx.ID_ANY, u"Target Set    C", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.tx_di_set3.Wrap(-1)

        self.tx_di_set3.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bSizer23.Add(self.tx_di_set3, 0, wx.ALL, 5)

        ch_di_set3Choices = []
        self.ch_di_set3 = wx.Choice(self.pn_di_app, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_di_set3Choices, 0)
        self.ch_di_set3.SetSelection(0)
        self.ch_di_set3.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

        bSizer23.Add(self.ch_di_set3, 0, wx.ALL | wx.EXPAND, 5)

        self.tx_di_set4 = wx.StaticText(self.pn_di_app, wx.ID_ANY, u"Target Set    D", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.tx_di_set4.Wrap(-1)

        self.tx_di_set4.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bSizer23.Add(self.tx_di_set4, 0, wx.ALL, 5)

        ch_di_set4Choices = []
        self.ch_di_set4 = wx.Choice(self.pn_di_app, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_di_set4Choices, 0)
        self.ch_di_set4.SetSelection(0)
        self.ch_di_set4.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

        bSizer23.Add(self.ch_di_set4, 0, wx.ALL | wx.EXPAND, 5)

        bSizer23.Add((0, 30), 0, 0, 5)

        bx_di_cmds = wx.BoxSizer(wx.HORIZONTAL)

        bx_di_cmds.SetMinSize(wx.Size(-1, 50))
        self.m_button10 = wx.Button(self.pn_di_app, wx.ID_ANY, u"Apply Target Sets", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.m_button10.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bx_di_cmds.Add(self.m_button10, 1, wx.ALL | wx.EXPAND, 2)

        self.m_button11 = wx.Button(self.pn_di_app, wx.ID_ANY, u"Remove All DI Tg", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        self.m_button11.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))

        bx_di_cmds.Add(self.m_button11, 1, wx.ALL | wx.EXPAND, 2)

        bSizer23.Add(bx_di_cmds, 0, wx.EXPAND, 5)

        bx_tgt_app.Add(bSizer23, 1, wx.EXPAND, 5)

        self.pn_di_app.SetSizer(bx_tgt_app)
        self.pn_di_app.Layout()
        bx_tgt_app.Fit(self.pn_di_app)
        self.m_listbook121.AddPage(self.pn_di_app, u"DI Targets", False)

        bx_targets.Add(self.m_listbook121, 1, wx.EXPAND | wx.ALL, 2)

        self.page_6.SetSizer(bx_targets)
        self.page_6.Layout()
        bx_targets.Fit(self.page_6)
        self.app_book.AddPage(self.page_6, u"a page", False)
        self.page_7 = wx.Panel(self.app_book, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer12311 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6311 = wx.StaticText(self.page_7, wx.ID_ANY, u"TBD OUTPUT", wx.DefaultPosition, wx.DefaultSize,
                                              wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText6311.Wrap(-1)

        self.m_staticText6311.SetFont(
            wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow"))
        self.m_staticText6311.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        bSizer12311.Add(self.m_staticText6311, 0, wx.ALL | wx.EXPAND, 0)

        self.page_7.SetSizer(bSizer12311)
        self.page_7.Layout()
        bSizer12311.Fit(self.page_7)
        self.app_book.AddPage(self.page_7, u"a page", False)

        bSizer7.Add(self.app_book, 1, wx.ALL | wx.EXPAND, 1)

        self.SetSizer(bSizer7)
        self.Layout()
        self.sb_status = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.sb_status.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_bitmap1.Bind(wx.EVT_LEFT_UP, self.exit_script)
        self.Bind(wx.EVT_TOOL, self.activate_home, id=self.tool_home.GetId())
        self.Bind(wx.EVT_TOOL_ENTER, self.exec_tool_enter, id=self.tool_home.GetId())
        self.Bind(wx.EVT_TOOL, self.activate_input, id=self.tool_input.GetId())
        self.Bind(wx.EVT_TOOL, self.activate_cleanup, id=self.tool_cleanup.GetId())
        self.Bind(wx.EVT_TOOL, self.activate_analysis, id=self.tool_analysis.GetId())
        self.Bind(wx.EVT_TOOL, self.activate_edit, id=self.tool_edit.GetId())
        self.Bind(wx.EVT_TOOL, self.activate_panel, id=self.m_tool11.GetId())
        self.Bind(wx.EVT_TOOL, self.activate_targets, id=self.tool_targets.GetId())
        self.Bind(wx.EVT_TOOL, self.activate_output, id=self.m_tool12.GetId())
        self.bt_di_save.Bind(wx.EVT_LEFT_UP, self.cmd_save)
        self.bt_di_undo1.Bind(wx.EVT_LEFT_UP, self.exit_script)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def exit_script(self, event):
        event.Skip()

    def activate_home(self, event):
        event.Skip()

    def exec_tool_enter(self, event):
        event.Skip()

    def activate_input(self, event):
        event.Skip()

    def activate_cleanup(self, event):
        event.Skip()

    def activate_analysis(self, event):
        event.Skip()

    def activate_edit(self, event):
        event.Skip()

    def activate_panel(self, event):
        event.Skip()

    def activate_targets(self, event):
        event.Skip()

    def activate_output(self, event):
        event.Skip()

    def cmd_save(self, event):
        event.Skip()
