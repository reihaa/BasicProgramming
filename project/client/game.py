import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import requests
from network import Network


class Game2:
    pos1 = [8, 4]
    pos2 = [0, 4]
    v_list = [[0 for _ in range(8)] for _ in range(9)]
    h_list = [[0 for _ in range(8)] for _ in range(9)]
    hey = [[0 for _ in range(8)] for _ in range(8)]

    def move(self, pos_, turn):
        i = False
        if turn == 1:
            pos_a = self.pos1
            pos_b = self.pos2
        else:
            pos_a = self.pos2
            pos_b = self.pos1
        print(turn, pos_a, pos_)
        if pos_a[0] == pos_[0] + 1 and pos_[1] == pos_a[1] and not (
                        pos_b[0] == pos_a[0] - 1 and pos_b[1] == pos_a[1]) and self.h_list[pos_a[1]][pos_a[0] - 1] == 0:
            pos_a = pos_  # down
            i = True
        elif pos_a[0] == pos_[0] - 1 and pos_[1] == pos_a[1] and not (
                        pos_b[0] == pos_a[0] + 1 and pos_b[1] == pos_a[1]) and self.h_list[pos_a[1]][pos_a[0]] == 0:
            pos_a = pos_  # up
            i = True
        elif pos_a[0] == pos_[0] and pos_[1] == pos_a[1] + 1 and not (
                        pos_b[0] == pos_a[0] and pos_b[1] == pos_a[1] + 1) and self.v_list[pos_a[0]][pos_a[1]] == 0:
            pos_a = pos_  # right
            i = True
        elif pos_a[0] == pos_[0] and pos_[1] == pos_a[1] - 1 and not (
                        pos_b[0] == pos_a[0] and pos_b[1] == pos_a[1] - 1) and self.v_list[pos_a[0]][pos_a[1] - 1] == 0:
            pos_a = pos_  # left
            i = True
        if pos_a[0] == pos_[0] + 2 and pos_[1] == pos_a[1] and (
                        pos_b[0] == pos_a[0] - 1 and pos_b[1] == pos_a[1]) and self.h_list[pos_a[1]][
                    pos_a[0] - 1] == 0 and self.h_list[pos_a[1]][pos_a[0] - 1]:
            pos_a = pos_  # jump down
            i = True
        elif not (not (pos_a[0] == pos_[0] - 2) or not (pos_[1] == pos_a[1]) or not (
                        pos_b[0] == pos_a[0] + 1 and pos_b[1] == pos_a[1]) or not (
                    self.h_list[pos_a[1]][pos_a[0]] == 0) or not (self.h_list[pos_a[1]][pos_a[0] + 1] == 0)):
            pos_a = pos_  # jump up
            i = True
        elif pos_a[0] == pos_[0] and pos_[1] == pos_a[1] + 2 and (
                        pos_b[0] == pos_a[0] and pos_b[1] == pos_a[1] + 1) and self.v_list[pos_a[0]][pos_a[1]] == 0 and \
                        self.v_list[pos_a[0]][pos_a[1] + 1] == 0:
            pos_a = pos_  # jump right
            i = True
        elif pos_a[0] == pos_[0] and pos_[1] == pos_a[1] - 2 and (
                        pos_b[0] == pos_a[0] and pos_b[1] == pos_a[1] - 1) and self.v_list[pos_a[0]][
                    pos_a[1] - 1] == 0 and self.v_list[pos_a[0]][pos_a[1] - 2] == 0:
            pos_a = pos_  # jump left
            i = True
        if i:
            if turn == 1:
                self.pos1 = pos_a
            elif turn == 2:
                self.pos2 = pos_a
        return i, pos_a

    def v_wall(self, pos_):
        i = False
        print(pos_)
        if self.v_list[pos_[0]][pos_[1]] == 0 and pos_[0] != 8 and self.v_list[pos_[0] + 1][pos_[1]] == 0:
            if (self.hey[pos_[0]][pos_[1]] == 0):
                i = True
                self.v_list[pos_[0]][pos_[1]] = 1
                self.v_list[pos_[0] + 1][pos_[1]] = 1
                self.hey[pos_[0]][pos_[1]] = 1
        return i, self.v_list

    def h_wall(self, pos_):
        i = False
        if self.h_list[pos_[0]][pos_[1]] == 0 and pos_[0] != 8 and self.h_list[pos_[0] + 1][pos_[1]] == 0:
            if self.hey[pos_[1]][pos_[0]] == 0:
                i = True
                self.h_list[pos_[0]][pos_[1]] = 1
                self.h_list[pos_[0] + 1][pos_[1]] = 1
                self.hey[pos_[1]][pos_[0]] = 1
        print(i)
        return i, self.h_list


class Board2(App):
    turn = 1
    pos = pos1 = [8, 4]
    pos2 = [0, 4]
    game = Game2()
    i = False
    v_list = [[0 for _ in range(8)] for _ in range(9)]
    h_list = [[0 for _ in range(8)] for _ in range(9)]

    def build(self):
        Window.system_size = (900, 900)
        layout = FloatLayout()
        with layout.canvas:
            Rectangle(size=(900, 900), source='/home/rey/Desktop/1.png', pos=(0, 0))
        with layout.canvas:
            Color(201 / 250, 251 / 250, 255 / 250, 1)
            Rectangle(pos=(100, 100), size=(700, 700))

        self.h = []
        for i in range(9):  # horizontal walls
            q = []
            for j in range(8):
                g = Button(size=(60, 20), pos=(i * 80 + 100, j * 80 + 160),
                           size_hint=(None, None),
                           background_color=(80 / 255, 6 / 255, 114 / 255, 1))
                g.bind(on_press=self.h_wall)
                layout.add_widget(g)
                q.append(g)
            self.h.append(q)

        self.v = []
        for i in range(9):  # vertical walls
            q = []
            for j in range(8):
                g = Button(size=(20, 60), pos=(j * 80 + 160, i * 80 + 100),
                           size_hint=(None, None),
                           background_color=(
                               80 / 255, 6 / 255, 114 / 255, 1))
                g.bind(on_press=self.v_wall)
                layout.add_widget(g)
                q.append(g)
            self.v.append(q)

        self.w = []
        for x in range(9):
            q = []
            for y in range(9):  # board
                g = Button(text='%d %d' % (x, y), size=(60, 60), pos=(80 * y + 100, 80 * x + 100),
                           size_hint=(None, None), background_color=(229 / 255, 1, 74 / 22, 27 / 255))
                g.bind(on_press=self.move)
                if x == 8 and y == 4:
                    g.background_color = (104 / 255, 27 / 255, 229 / 255, 1)
                if x == 0 and y == 4:
                    g.background_color = (99 / 255, 4 / 255, 28 / 255, 1)
                layout.add_widget(g)
                q.append(g)
            self.w.append(q)
            back = Button(text="Back", size=(150, 50), background_color=(0, 5 / 250, 25 / 250, 1), pos=(10, 10),
                          size_hint=(None, None))
            back.bind(on_press=self.back)
            layout.add_widget(back)
        return layout

    def move(self, instance):
        pos_ = [0, 0]
        for i in range(9):
            if instance in self.w[i]:
                pos_[0] = i
                pos_[1] = self.w[i].index(instance)
                break
        pos_p = self.pos
        self.i, self.pos = self.game.move(pos_, self.turn)
        print('i:', self.i, 'pos:', self.pos)
        if self.i:
            self.w[pos_p[0]][pos_p[1]].background_color = (229 / 255, 1, 74 / 22, 27 / 255)
            print('pre color changed', pos_p)
            if self.turn == 1 and self.pos[0] == 0:
                self.win()
            if self.turn == 2 and self.pos[0] == 8:
                self.win()
            self._turn(a=1)

    def v_wall(self, instance):
        pos_ = [0, 0]
        for i in range(9):
            if instance in self.v[i]:
                pos_[0] = i
                pos_[1] = self.v[i].index(instance)
                break

        self.i, self.v_list = self.game.v_wall(pos_)
        if self.i:
            self.v[pos_[0]][pos_[1]].background_color = (1, 0, 0, 1)
            self.v[pos_[0] + 1][pos_[1]].background_color = (1, 0, 0, 1)
            self._turn(a=0)

    def h_wall(self, instance):
        pos_ = [0, 0]
        for i in range(9):
            if instance in self.h[i]:
                pos_[0] = i
                pos_[1] = self.h[i].index(instance)
                break

        self.i, self.h_list = self.game.h_wall(pos_)
        if self.i:
            self.h[pos_[0]][pos_[1]].background_color = (1, 0, 0, 1)
            self.h[pos_[0] + 1][pos_[1]].background_color = (1, 0, 0, 1)
            self._turn(a=0)

    def _turn(self, a):
        if self.turn == 1:
            if a:
                self.w[self.pos[0]][self.pos[1]].background_color = (104 / 255, 27 / 255, 229 / 255, 1)
                print('turn 1, changed')
            self.turn = 2
            self.pos1 = self.pos
            self.pos = self.pos2
        elif self.turn == 2:
            if a:
                self.w[self.pos[0]][self.pos[1]].background_color = (99 / 255, 4 / 255, 28 / 255, 1)
                print('2, changed', self.pos)
            self.turn = 1
            self.pos2 = self.pos
            self.pos = self.pos1

    def win(self):
        Win.turn = self.turn
        self.stop()
        Win().run()

    def back(self, instance):
        self.stop()
        SecMenu.session = self.session
        SecMenu().run()


class Game4:
    pos1 = [8, 4]
    pos2 = [0, 4]
    pos3 = [4, 0]
    pos4 = [4, 8]
    v_list = [[0 for _ in range(8)] for _ in range(9)]
    h_list = [[0 for _ in range(8)] for _ in range(9)]
    hey = [[0 for _ in range(8)] for _ in range(8)]

    def move(self, pos_, turn):
        i = False
        if turn == 1:
            pos_a = self.pos1
            c = [self.pos4, self.pos3, self.pos2]
        elif turn == 2:
            pos_a = self.pos2
            c = [self.pos1, self.pos4, self.pos3]
        elif turn == 3:
            c = [self.pos1, self.pos2, self.pos4]
            pos_a = self.pos3
        elif turn == 4:
            c = [self.pos1, self.pos2, self.pos3]
            pos_a = self.pos4
        # board = [[0 for _ in range(9)] for _ in range(9)]
        # board[self.pos1[0]][self.pos1[1]] = 1
        # board[self.pos2[0]][self.pos2[1]] = 1
        # board[self.pos3[0]][self.pos3[1]] = 1
        # board[self.pos4[0]][self.pos4[1]] = 1
        for pos_b in c:
            print('pos_a:',pos_a, 'pos_b', pos_b)
            if pos_a[0] == pos_[0] + 1 and pos_[1] == pos_a[1] and not (
                            pos_b[0] == pos_a[0] - 1 and pos_b[1] == pos_a[1]) and self.h_list[pos_a[1]][
                        pos_a[0] - 1] == 0:
                pos_a = pos_  # down
                i = True
            elif pos_a[0] == pos_[0] - 1 and pos_[1] == pos_a[1] and not (
                            pos_b[0] == pos_a[0] + 1 and pos_b[1] == pos_a[1]) and self.h_list[pos_a[1]][pos_a[0]] == 0:
                pos_a = pos_  # up
                i = True
            elif pos_a[0] == pos_[0] and pos_[1] == pos_a[1] + 1 and not (
                            pos_b[0] == pos_a[0] and pos_b[1] == pos_a[1] + 1) and self.v_list[pos_a[0]][pos_a[1]] == 0:
                pos_a = pos_  # right
                i = True
            elif pos_a[0] == pos_[0] and pos_[1] == pos_a[1] - 1 and not (
                            pos_b[0] == pos_a[0] and pos_b[1] == pos_a[1] - 1) and self.v_list[pos_a[0]][
                        pos_a[1] - 1] == 0:
                pos_a = pos_  # left
                i = True
            if pos_a[0] == pos_[0] + 2 and pos_[1] == pos_a[1] and (
                            pos_b[0] == pos_a[0] - 1 and pos_b[1] == pos_a[1]) and self.h_list[pos_a[1]][
                        pos_a[0] - 1] == 0 and self.h_list[pos_a[1]][pos_a[0] - 1]:
                pos_a = pos_  # jump down
                i = True
            elif not (not (pos_a[0] == pos_[0] - 2) or not (pos_[1] == pos_a[1]) or not (
                            pos_b[0] == pos_a[0] + 1 and pos_b[1] == pos_a[1]) or not (
                        self.h_list[pos_a[1]][pos_a[0]] == 0) or not (self.h_list[pos_a[1]][pos_a[0] + 1] == 0)):
                pos_a = pos_  # jump up
                i = True
            elif pos_a[0] == pos_[0] and pos_[1] == pos_a[1] + 2 and (
                            pos_b[0] == pos_a[0] and pos_b[1] == pos_a[1] + 1) and self.v_list[pos_a[0]][
                pos_a[1]] == 0 and \
                            self.v_list[pos_a[0]][pos_a[1] + 1] == 0:
                pos_a = pos_  # jump right
                i = True
            elif pos_a[0] == pos_[0] and pos_[1] == pos_a[1] - 2 and (
                            pos_b[0] == pos_a[0] and pos_b[1] == pos_a[1] - 1) and self.v_list[pos_a[0]][
                        pos_a[1] - 1] == 0 and self.v_list[pos_a[0]][pos_a[1] - 2] == 0:
                pos_a = pos_  # jump left
                i = True
            if i:
                if turn == 1:
                    self.pos1 = pos_a
                elif turn == 2:
                    self.pos2 = pos_a
                elif turn == 3:
                    self.pos3 = pos_a
                elif turn == 4:
                    self.pos4 = pos_a
        return i, pos_a

    def v_wall(self, pos_):
        i = False
        print(pos_)
        if self.v_list[pos_[0]][pos_[1]] == 0 and pos_[0] != 8 and self.v_list[pos_[0] + 1][pos_[1]] == 0:
            if (self.hey[pos_[0]][pos_[1]] == 0):
                i = True
                self.v_list[pos_[0]][pos_[1]] = 1
                self.v_list[pos_[0] + 1][pos_[1]] = 1
                self.hey[pos_[0]][pos_[1]] = 1
        return i, self.v_list

    def h_wall(self, pos_):
        i = False
        if self.h_list[pos_[0]][pos_[1]] == 0 and pos_[0] != 8 and self.h_list[pos_[0] + 1][pos_[1]] == 0:
            if self.hey[pos_[1]][pos_[0]] == 0:
                i = True
                self.h_list[pos_[0]][pos_[1]] = 1
                self.h_list[pos_[0] + 1][pos_[1]] = 1
                self.hey[pos_[1]][pos_[0]] = 1
        print(i)
        return i, self.h_list


class Board4(App):
    turn = 1
    pos = pos1 = [8, 4]
    pos2 = [0, 4]
    pos3 = [4, 0]
    pos4 = [4, 8]
    game = Game4()
    i = False
    v_list = [[0 for _ in range(8)] for _ in range(9)]
    h_list = [[0 for _ in range(8)] for _ in range(9)]

    def build(self):
        Window.system_size = (900, 900)
        layout = FloatLayout()
        with layout.canvas:
            Rectangle(size=(900, 900), source='/home/rey/Desktop/1.png', pos=(0, 0))
        with layout.canvas:
            Color(201 / 250, 251 / 250, 255 / 250, 1)
            Rectangle(pos=(100, 100), size=(700, 700))

        self.h = []
        for i in range(9):  # horizontal walls
            q = []
            for j in range(8):
                g = Button(size=(60, 20), pos=(i * 80 + 100, j * 80 + 160),
                           size_hint=(None, None),
                           background_color=(80 / 255, 6 / 255, 114 / 255, 1))
                g.bind(on_press=self.h_wall)
                layout.add_widget(g)
                q.append(g)
            self.h.append(q)

        self.v = []
        for i in range(9):  # vertical walls
            q = []
            for j in range(8):
                g = Button(size=(20, 60), pos=(j * 80 + 160, i * 80 + 100),
                           size_hint=(None, None),
                           background_color=(
                               80 / 255, 6 / 255, 114 / 255, 1))
                g.bind(on_press=self.v_wall)
                layout.add_widget(g)
                q.append(g)
            self.v.append(q)

        self.w = []
        for x in range(9):
            q = []
            for y in range(9):  # board
                g = Button(text='%d %d' % (x, y), size=(60, 60), pos=(80 * y + 100, 80 * x + 100),
                           size_hint=(None, None), background_color=(229 / 255, 1, 74 / 22, 27 / 255))
                g.bind(on_press=self.move)
                if x == 8 and y == 4:
                    g.background_color = (104 / 255, 27 / 255, 229 / 255, 1)
                if x == 0 and y == 4:
                    g.background_color = (99 / 255, 4 / 255, 28 / 255, 1)
                if x == 4 and y == 0:
                    g.background_color = (18 / 255, 142 / 255, 78 / 255, 1)
                if x == 4 and y == 8:
                    g.background_color = (147 / 255, 16 / 255, 55 / 255, 1)
                q.append(g)
                layout.add_widget(g)
            self.w.append(q)
            back = Button(text="Back", size=(150, 50), background_color=(0, 5 / 250, 25 / 250, 1), pos=(10, 10),
                          size_hint=(None, None))
            back.bind(on_press=self.back)
            layout.add_widget(back)
        return layout

    def move(self, instance):
        pos_ = [0, 0]
        for i in range(9):
            if instance in self.w[i]:
                pos_[0] = i
                pos_[1] = self.w[i].index(instance)
                break
        pos_p = self.pos
        self.i, self.pos = self.game.move(pos_, self.turn)
        print('i:', self.i, 'pos:', self.pos)
        if self.i:
            self.w[pos_p[0]][pos_p[1]].background_color = (229 / 255, 1, 74 / 22, 27 / 255)
            print('pre color changed', pos_p)
            if (self.turn == 1 and self.pos[0] == 0) or (self.turn == 2 and self.pos[0] == 8) or (
                            self.turn == 3 and self.pos[1] == 0) or (self.turn == 4 and self.pos[1] == 8):
                self.win()
            self._turn(a=1)

    def v_wall(self, instance):
        pos_ = [0, 0]
        for i in range(9):
            if instance in self.v[i]:
                pos_[0] = i
                pos_[1] = self.v[i].index(instance)
                break

        self.i, self.v_list = self.game.v_wall(pos_)
        if self.i:
            self.v[pos_[0]][pos_[1]].background_color = (1, 0, 0, 1)
            self.v[pos_[0] + 1][pos_[1]].background_color = (1, 0, 0, 1)
            self._turn(a=0)

    def h_wall(self, instance):
        pos_ = [0, 0]
        for i in range(9):
            if instance in self.h[i]:
                pos_[0] = i
                pos_[1] = self.h[i].index(instance)
                break

        self.i, self.h_list = self.game.h_wall(pos_)
        if self.i:
            self.h[pos_[0]][pos_[1]].background_color = (1, 0, 0, 1)
            self.h[pos_[0] + 1][pos_[1]].background_color = (1, 0, 0, 1)
            self._turn(a=0)

    def _turn(self, a):
        print(self.turn)
        if self.turn == 1:
            if a:
                self.w[self.pos[0]][self.pos[1]].background_color = (104 / 255, 27 / 255, 229 / 255, 1)
                print('turn 1, changed')
            self.turn = 2
            self.pos1 = self.pos
            self.pos = self.pos2
        elif self.turn == 2:
            if a:
                self.w[self.pos[0]][self.pos[1]].background_color = (99 / 255, 4 / 255, 28 / 255, 1)
                print('2, changed', self.pos)
            self.turn = 3
            self.pos2 = self.pos
            self.pos = self.pos3
        elif self.turn == 3:
            if a:
                self.w[self.pos[0]][self.pos[1]].background_color = (18 / 255, 142 / 255, 78 / 255, 1)
            self.turn = 4
            self.pos3 = self.pos
            self.pos = self.pos4
        elif self.turn == 4:
            if a:
                self.w[self.pos[0]][self.pos[1]].background_color = (147 / 255, 16 / 255, 55 / 255, 1)
            self.turn = 1
            self.pos4 = self.pos
            self.pos = self.pos1

    def win(self):
        Win.turn = self.turn
        self.stop()
        Win().run()

    def back(self, instance):
        self.stop()
        SecMenu.session = self.session
        SecMenu().run()


class Win(App):
    def build(self):
        Window.system_size = (900, 900)
        layout = FloatLayout()
        with layout.canvas:
            Rectangle(size=(900, 900), source='/home/rey/Desktop/1.png', pos=(0, 0))
        Window.system_size = (900, 900)
        with layout.canvas:
            Color(84 / 250, 179 / 250, 196 / 250, 1)
            Rectangle(size=(700, 400), pos=(100, 400))
        hey = Label(text='player %s won' % (self.turn), font_size=50, pos=(50, 400), size=(800, 400),
                    size_hint=(None, None))
        layout.add_widget(hey)
        btn1 = Button(text='Menu', font_size=30, size_hint=(None, None), size=(300, 100), pos=(300, 200),
                      color=(201 / 250, 203 / 250, 224 / 250, 1), background_color=(0, 5 / 250, 25 / 250, 1))
        btn1.bind(on_press=self.menu)
        layout.add_widget(btn1)
        return layout

    def menu(self, instance):
        self.stop()
        SecMenu().run()


class SecMenu(App):
    def build(self):
        layout = FloatLayout()
        Window.clearcolor = (0, 5 / 250, 25 / 250, 1)
        Window.system_size = (900, 900)
        btn1 = Button(text='two player', font_size=30, size_hint=(None, None), size=(300, 100), pos=(300, 300),
                      color=(201 / 250, 203 / 250, 224 / 250, 1), background_color=(0, 5 / 250, 25 / 250, 1))
        btn1.bind(on_press=self.two_player)
        btn2 = Button(text='four player', font_size=30, size_hint=(None, None), size=(300, 100), pos=(300, 410),
                      color=(201 / 250, 203 / 250, 224 / 250, 1), background_color=(0, 5 / 250, 25 / 250, 1))
        btn2.bind(on_press=self.four_player)
        btn3 = Button(text='log out', font_size=30, size_hint=(None, None), size=(300, 100), pos=(300, 520),
                      color=(201 / 250, 203 / 250, 224 / 250, 1), background_color=(0, 5 / 250, 25 / 250, 1))
        btn3.bind(on_press=self.logout)
        btn4 = Button(text='Exit', font_size=20, size_hint=(None, None), size=(200, 50), pos=(10, 10),
                      color=(201 / 250, 203 / 250, 224 / 250, 1), background_color=(0, 5 / 250, 25 / 250, 1))
        btn4.bind(on_press=lambda instance: exit())
        layout.add_widget(btn1)
        layout.add_widget(btn4)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        back = Button(text="Back", size=(150, 50), background_color=(0, 5 / 250, 25 / 250, 1), pos=(10, 10),
                      size_hint=(None, None))
        back.bind(on_press=self.back)
        layout.add_widget(back)
        return layout

    def four_player(self, instance):
        Board4.session = self.session
        self.stop()
        Board4().run()

    def two_player(self, instance):
        Board2.session = self.session
        # Qrdtwo.session['game'] = self.session
        self.stop()
        Board2().run()

    def back(self, instance):
        self.stop()
        FirstMenu().run()

    def logout(self, instance):
        Network.session = self.session
        network = Network()
        network.logout()
        self.stop()
        FirstMenu().run()


class LogIn(App):
    k = 0

    def build(self):
        self.layout = FloatLayout()
        with self.layout.canvas:
            Rectangle(size=(900, 900), source='/home/rey/Desktop/1.png', pos=(0, 0))
        Window.system_size = (900, 900)
        txt = Label(text="log in", font_size=30, pos=(5, 600), size=(200, 50), size_hint=(None, None))
        with self.layout.canvas:
            Color(84 / 250, 179 / 250, 196 / 250, 1)
            RoundedRectangle(size=(400, 200), pos=(50, 400))
        self.layout.add_widget(txt)
        userinput = TextInput(size_hint=(None, None), size=(200, 30), pos=(60, 510))
        self.layout.add_widget(userinput)
        name = Label(text='username', font_size=20, pos=(15, 530), size=(200, 50), size_hint=(None, None), )
        self.layout.add_widget(name)
        passinput = TextInput(size_hint=(None, None), size=(200, 30), pos=(60, 430))
        self.layout.add_widget(passinput)
        password = Label(text='password', font_size=20, pos=(15, 450), size=(200, 50), size_hint=(None, None), )
        self.layout.add_widget(password)
        contbtn = Button(text="continue", size=(70, 30), background_color=(0, 5 / 250, 25 / 250, 1), pos=(360, 410),
                         size_hint=(None, None))
        self.layout.add_widget(contbtn)
        contbtn.bind(on_press=lambda x: self.log_in(self, inf={'username': userinput.text, 'password': passinput.text}))
        back = Button(text="Back", size=(150, 50), background_color=(0, 5 / 250, 25 / 250, 1), pos=(10, 10),
                      size_hint=(None, None))
        back.bind(on_press=self.back)
        self.layout.add_widget(back)
        return self.layout

    def log_in(self, instance, inf):
        network = Network()
        network.session = self.session
        i, text = network.login(inf)
        if i:
            self.stop()
            SecMenu.session = self.session
            SecMenu().run()
        else:
            if self.k == 1:
                self.layout.remove_widget(self.p)
            self.p = Label(text=text, font_size=20, pos=(200, 200), size=(300, 100))
            self.layout.add_widget(self.p)
            self.k = 1

    def back(self, instance):
        self.stop()
        FirstMenu().run()


class Register(App):
    k = 0

    def build(self):
        self.layout = FloatLayout()
        Window.background_image = '1.png'
        Window.system_size = (900, 900)
        with self.layout.canvas:
            Rectangle(size=(900, 900), source='/home/rey/Desktop/1.png', pos=(0, 0))
        txt = Label(text="Register", font_size=30, pos=(5, 600), size=(200, 50), size_hint=(None, None))
        with self.layout.canvas:
            Color(84 / 250, 179 / 250, 196 / 250, 1)
            RoundedRectangle(size=(400, 300), pos=(50, 300))
        self.layout.add_widget(txt)
        self.userinput = TextInput(size_hint=(None, None), size=(200, 30), pos=(60, 510))
        self.layout.add_widget(self.userinput)
        name = Label(text='username', font_size=20, pos=(15, 530), size=(200, 50), size_hint=(None, None), )
        self.layout.add_widget(name)
        self.passinput = TextInput(size_hint=(None, None), size=(200, 30), pos=(60, 430))
        self.layout.add_widget(self.passinput)
        password = Label(text='password', font_size=20, pos=(15, 450), size=(200, 50), size_hint=(None, None), )
        self.layout.add_widget(password)
        self.confinput = TextInput(size_hint=(None, None), size=(200, 30), pos=(60, 350))
        self.layout.add_widget(self.confinput)
        cpassword = Label(text='confirm password', font_size=20, pos=(45, 370), size=(200, 50),
                          size_hint=(None, None), )
        self.layout.add_widget(cpassword)
        contbtn = Button(text="continue", size=(70, 30), background_color=(0, 5 / 250, 25 / 250, 1), pos=(360, 310),
                         size_hint=(None, None))
        back = Button(text="Back", size=(150, 50), background_color=(0, 5 / 250, 25 / 250, 1), pos=(10, 10),
                      size_hint=(None, None))
        back.bind(on_press=self.back)
        self.layout.add_widget(back)
        self.layout.add_widget(contbtn)
        contbtn.bind(on_press=lambda x: self.register(self,
                                                      inf={'username': self.userinput.text,
                                                           'password': self.passinput.text,
                                                           'confpass': self.confinput.text}))

        return self.layout

    def register(self, instance, inf):
        Network.session = self.session
        network = Network()
        i, text = network.register(inf)
        if i:
            self.stop()
            SecMenu.session = self.session
            SecMenu().run()
        else:
            if self.k == 1:
                self.layout.remove_widget(self.p)
            self.p = Label(text=text, font_size=20, pos=(200, 200), size=(300, 100))
            self.layout.add_widget(self.p)
            self.k = 1

    def back(self, instance):
        self.stop()
        FirstMenu().run()


class FirstMenu(App):
    session = requests.Session()

    def build(self):
        layout = FloatLayout()
        Window.clearcolor = (0, 5 / 250, 25 / 250, 1)
        Window.system_size = (900, 900)
        btn2 = Button(text='register', font_size=30, size_hint=(None, None), size=(300, 100), pos=(300, 410),
                      color=(201 / 250, 203 / 250, 224 / 250, 1), background_color=(0, 5 / 250, 25 / 250, 1))
        btn2.bind(on_press=self.register)
        btn3 = Button(text='log in', font_size=30, size_hint=(None, None), size=(300, 100), pos=(300, 520),
                      color=(201 / 250, 203 / 250, 224 / 250, 1), background_color=(0, 5 / 250, 25 / 250, 1))
        btn3.bind(on_press=self.logIn)
        btn4 = Button(text='Exit', font_size=20, size_hint=(None, None), size=(200, 50), pos=(10, 10),
                      color=(201 / 250, 203 / 250, 224 / 250, 1), background_color=(0, 5 / 250, 25 / 250, 1))
        btn4.bind(on_press=lambda instance: exit())
        layout.add_widget(btn4)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return (layout)

    def register(self, instance):
        Register.session = self.session
        self.stop()
        Register().run()

    def logIn(self, instance):
        LogIn.session = self.session
        self.stop()
        LogIn().run()
