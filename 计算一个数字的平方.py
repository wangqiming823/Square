# -*- coding: utf-8 -*-
import wx 
  
# 导入gui工具生成的python文件 mysquare.py
import mysquare
class CalcFrame(mysquare.MyFrame1): 
   def __init__(self,parent): 
      mysquare.MyFrame1.__init__(self,parent)  
		
   def mySquare(self,event):   # 定义事件处理函数
      num = int(self.m_textCtrl1.GetValue()) 
      self.m_textCtrl2.SetValue (str(num*num)) 
        
app = wx.App(False) 
frame = CalcFrame(None) 
frame.Show(True) 
# 主循环
app.MainLoop()
