import random
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.app import App
from kivy.graphics import Rectangle, Color
from kivy.core.audio import SoundLoader



class Manager(ScreenManager):
        pass

class DX(Screen):
        rect = None

        def __init__(self, **kwargs):
             super(DX, self).__init__(**kwargs)
             self.init_shapes()

        def init_shapes(self):
             with self.canvas:
                  self.rect = Rectangle(bg_color=Color(1, 1, 1))
                  self.rect.source = 'Pictures/DX.png'

        def on_size(self, *args):
             self.rect.pos = (0, 0)
             self.rect.size = (int(self.width), int(self.height))


        def on_touch_move(self, touch):
          if touch.x < touch.ox :
               sound = SoundLoader.load('Sounds/D4.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='left')
               self.manager.current = 'D4'
          elif touch.x > touch.ox :
               sound = SoundLoader.load('Sounds/D20.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='right')
               self.manager.current = 'D20'

        def on_touch_up(self, touch):
          print("DX")
                
                
                
class D4(Screen):
        rect = None

             
        def __init__(self, **kwargs):
             super(D4, self).__init__(**kwargs)
             self.init_shapes()

        def init_shapes(self):
             with self.canvas:
                  self.rect = Rectangle(bg_color=Color(0.9, 0.9, 0.9))
                  self.rect.source = 'Pictures/D4.png'

        def on_size(self, *args):
             self.rect.pos = (0, 0)
             self.rect.size = (int(self.width), int(self.height))

        def on_touch_move(self, touch):
          if touch.x < touch.ox :
               sound = SoundLoader.load('Sounds/D6.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='left')
               self.manager.current = 'D6'
          elif touch.x > touch.ox :
               self.manager.transition = SlideTransition(direction='right')
               self.manager.current = 'DX'

        def on_touch_up(self, touch):
          self.LD4 = random.randint(1, 4)
          print(self.LD4)
          if self.LD4 == 1: 
               sound = SoundLoader.load('Sounds/1.m4a')
               sound.play()
          if self.LD4 == 2: 
               sound = SoundLoader.load('Sounds/2.m4a')
               sound.play()
          if self.LD4 == 3: 
               sound = SoundLoader.load('Sounds/3.m4a')
               sound.play()
          if self.LD4 == 4: 
               sound = SoundLoader.load('Sounds/4.m4a')
               sound.play()
               

class D6(Screen):
        rect = None
             
        def __init__(self, **kwargs):
             super(D6, self).__init__(**kwargs)
             self.init_shapes()

        def init_shapes(self):
             with self.canvas:
                  self.rect = Rectangle(bg_color=Color(0.8, 0.8, 0.8))
                  self.rect.source = 'Pictures/D6.png'

        def on_size(self, *args):
             self.rect.pos = (0, 0)
             self.rect.size = (int(self.width), int(self.height))
          
        def on_touch_move(self, touch):
          if touch.x < touch.ox :
               sound = SoundLoader.load('Sounds/D8.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='left')
               self.manager.current = 'D8'
          elif touch.x > touch.ox :
               sound = SoundLoader.load('Sounds/D4.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='right')
               self.manager.current = 'D4'

        def on_touch_up(self, touch):
          self.LD6 = random.randint(1, 6)
          print(self.LD6)
          if self.LD6 == 1: 
               sound = SoundLoader.load('Sounds/1.m4a')
               sound.play()
          if self.LD6 == 2: 
               sound = SoundLoader.load('Sounds/2.m4a')
               sound.play()
          if self.LD6 == 3: 
               sound = SoundLoader.load('Sounds/3.m4a')
               sound.play()
          if self.LD6 == 4: 
               sound = SoundLoader.load('Sounds/4.m4a')
               sound.play()
          if self.LD6 == 5: 
               sound = SoundLoader.load('Sounds/5.m4a')
               sound.play()
          if self.LD6 == 6: 
               sound = SoundLoader.load('Sounds/6.m4a')
               sound.play()

class D8(Screen):
        rect = None
             
        def __init__(self, **kwargs):
             super(D8, self).__init__(**kwargs)
             self.init_shapes()

        def init_shapes(self):
             with self.canvas:
                  self.rect = Rectangle(bg_color=Color(0.7, 0.7, 0.7))
                  self.rect.source = 'Pictures/D8.png'

        def on_size(self, *args):
             self.rect.pos = (0, 0)
             self.rect.size = (int(self.width), int(self.height))
          
        def on_touch_move(self, touch):
          if touch.x < touch.ox :
               sound = SoundLoader.load('Sounds/D10.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='left')
               self.manager.current = 'D10'
          elif touch.x > touch.ox :
               sound = SoundLoader.load('Sounds/D6.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='right')
               self.manager.current = 'D6'

        def on_touch_up(self, touch):
          self.LD8 = random.randint(1, 8)
          print(self.LD8)
          if self.LD8 == 1: 
               sound = SoundLoader.load('Sounds/1.m4a')
               sound.play()
          if self.LD8 == 2: 
               sound = SoundLoader.load('Sounds/2.m4a')
               sound.play()
          if self.LD8 == 3: 
               sound = SoundLoader.load('Sounds/3.m4a')
               sound.play()
          if self.LD8 == 4: 
               sound = SoundLoader.load('Sounds/4.m4a')
               sound.play()
          if self.LD8 == 5: 
               sound = SoundLoader.load('Sounds/5.m4a')
               sound.play()
          if self.LD8 == 6: 
               sound = SoundLoader.load('Sounds/6.m4a')
               sound.play()
          if self.LD8 == 7: 
               sound = SoundLoader.load('Sounds/7.m4a')
               sound.play()
          if self.LD8 == 8: 
               sound = SoundLoader.load('Sounds/8.m4a')
               sound.play()

class D10(Screen):
        rect = None
             
        def __init__(self, **kwargs):
             super(D10, self).__init__(**kwargs)
             self.init_shapes()

        def init_shapes(self):
             with self.canvas:
                  self.rect = Rectangle(bg_color=Color(0.6, 0.6, 0.6))
                  self.rect.source = 'Pictures/D10.png'

        def on_size(self, *args):
             self.rect.pos = (0, 0)
             self.rect.size = (int(self.width), int(self.height))
          
        def on_touch_move(self, touch):
          if touch.x < touch.ox :
               sound = SoundLoader.load('Sounds/D12.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='left')
               self.manager.current = 'D12'
          elif touch.x > touch.ox :
               sound = SoundLoader.load('Sounds/D8.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='right')
               self.manager.current = 'D8'

        def on_touch_up(self, touch):
          self.LD10 = random.randint(1, 10)
          print(self.LD10)
          if self.LD10 == 1: 
               sound = SoundLoader.load('Sounds/1.m4a')
               sound.play()
          if self.LD10 == 2: 
               sound = SoundLoader.load('Sounds/2.m4a')
               sound.play()
          if self.LD10 == 3: 
               sound = SoundLoader.load('Sounds/3.m4a')
               sound.play()
          if self.LD10 == 4: 
               sound = SoundLoader.load('Sounds/4.m4a')
               sound.play()
          if self.LD10 == 5: 
               sound = SoundLoader.load('Sounds/5.m4a')
               sound.play()
          if self.LD10 == 6: 
               sound = SoundLoader.load('Sounds/6.m4a')
               sound.play()
          if self.LD10 == 7: 
               sound = SoundLoader.load('Sounds/7.m4a')
               sound.play()
          if self.LD10 == 8: 
               sound = SoundLoader.load('Sounds/8.m4a')
               sound.play()
          if self.LD10 == 9: 
               sound = SoundLoader.load('Sounds/9.m4a')
               sound.play()
          if self.LD10 == 10: 
               sound = SoundLoader.load('Sounds/10.m4a')
               sound.play()

class D12(Screen):
        rect = None
             
        def __init__(self, **kwargs):
             super(D12, self).__init__(**kwargs)
             self.init_shapes()

        def init_shapes(self):
             with self.canvas:
                  self.rect = Rectangle(bg_color=Color(0.5, 0.5, 0.5))
                  self.rect.source = 'Pictures/D12.png'

        def on_size(self, *args):
             self.rect.pos = (0, 0)
             self.rect.size = (int(self.width), int(self.height))
          
        def on_touch_move(self, touch):
          if touch.x < touch.ox :
               sound = SoundLoader.load('Sounds/D20.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='left')
               self.manager.current = 'D20'
          elif touch.x > touch.ox :
               sound = SoundLoader.load('Sounds/D10.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='right')
               self.manager.current = 'D10'

        def on_touch_up(self, touch):
          self.LD12 = random.randint(1, 12)
          print(self.LD12)
          if self.LD12 == 1: 
               sound = SoundLoader.load('Sounds/1.m4a')
               sound.play()
          if self.LD12 == 2: 
               sound = SoundLoader.load('Sounds/2.m4a')
               sound.play()
          if self.LD12 == 3: 
               sound = SoundLoader.load('Sounds/3.m4a')
               sound.play()
          if self.LD12 == 4: 
               sound = SoundLoader.load('Sounds/4.m4a')
               sound.play()
          if self.LD12 == 5: 
               sound = SoundLoader.load('Sounds/5.m4a')
               sound.play()
          if self.LD12 == 6: 
               sound = SoundLoader.load('Sounds/6.m4a')
               sound.play()
          if self.LD12 == 7: 
               sound = SoundLoader.load('Sounds/7.m4a')
               sound.play()
          if self.LD12 == 8: 
               sound = SoundLoader.load('Sounds/8.m4a')
               sound.play()
          if self.LD12 == 9: 
               sound = SoundLoader.load('Sounds/9.m4a')
               sound.play()
          if self.LD12 == 10: 
               sound = SoundLoader.load('Sounds/10.m4a')
               sound.play()
          if self.LD12 == 11: 
               sound = SoundLoader.load('Sounds/11.m4a')
               sound.play()
          if self.LD12 == 12: 
               sound = SoundLoader.load('Sounds/12.m4a')
               sound.play()
          
class D20(Screen):
        rect = None
             
        def __init__(self, **kwargs):
             super(D20, self).__init__(**kwargs)
             self.init_shapes()

        def init_shapes(self):
             with self.canvas:
                  self.rect = Rectangle(bg_color=Color(0.4, 0.4, 0.4))
                  self.rect.source = 'Pictures/D20.png'

        def on_size(self, *args):
             self.rect.pos = (0, 0)
             self.rect.size = (int(self.width), int(self.height))
          
        def on_touch_move(self, touch):
          if touch.x < touch.ox :
               self.manager.transition = SlideTransition(direction='left')
               self.manager.current = 'DX'
          elif touch.x > touch.ox :
               sound = SoundLoader.load('Sounds/D12.m4a')
               sound.play()
               self.manager.transition = SlideTransition(direction='right')
               self.manager.current = 'D12'

        def on_touch_up(self, touch):
          self.LD20 = random.randint(1, 20)
          print(self.LD20)
          if self.LD20 == 1: 
               sound = SoundLoader.load('Sounds/NAT1.m4a')
               sound.play()
          if self.LD20 == 2: 
               sound = SoundLoader.load('Sounds/2.m4a')
               sound.play()
          if self.LD20 == 3: 
               sound = SoundLoader.load('Sounds/3.m4a')
               sound.play()
          if self.LD20 == 4: 
               sound = SoundLoader.load('Sounds/4.m4a')
               sound.play()
          if self.LD20 == 5: 
               sound = SoundLoader.load('Sounds/5.m4a')
               sound.play()
          if self.LD20 == 6: 
               sound = SoundLoader.load('Sounds/6.m4a')
               sound.play()
          if self.LD20 == 7: 
               sound = SoundLoader.load('Sounds/7.m4a')
               sound.play()
          if self.LD20 == 8: 
               sound = SoundLoader.load('Sounds/8.m4a')
               sound.play()
          if self.LD20 == 9: 
               sound = SoundLoader.load('Sounds/9.m4a')
               sound.play()
          if self.LD20 == 10: 
               sound = SoundLoader.load('Sounds/10.m4a')
               sound.play()
          if self.LD20 == 11: 
               sound = SoundLoader.load('Sounds/11.m4a')
               sound.play()
          if self.LD20 == 12: 
               sound = SoundLoader.load('Sounds/12.m4a')
               sound.play()
          if self.LD20 == 13: 
               sound = SoundLoader.load('Sounds/13.m4a')
               sound.play()
          if self.LD20 == 14: 
               sound = SoundLoader.load('Sounds/14.m4a')
               sound.play()
          if self.LD20 == 15: 
               sound = SoundLoader.load('Sounds/15.m4a')
               sound.play()
          if self.LD20 == 16: 
               sound = SoundLoader.load('Sounds/16.m4a')
               sound.play()
          if self.LD20 == 17: 
               sound = SoundLoader.load('Sounds/17.m4a')
               sound.play()
          if self.LD20 == 18: 
               sound = SoundLoader.load('Sounds/18.m4a')
               sound.play()
          if self.LD20 == 19: 
               sound = SoundLoader.load('Sounds/19.m4a')
               sound.play()
          if self.LD20 == 20: 
               sound = SoundLoader.load('Sounds/NAT20.m4a')
               sound.play()
          

     
    


class MyApp(App):
    def build(self):
        return Manager()


if __name__ == '__main__':
    MyApp().run()