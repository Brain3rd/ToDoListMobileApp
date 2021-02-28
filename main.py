from kivymd.app import MDApp
# from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, ObjectProperty, StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp


# Window.size = (245, 480)


class ToDoScreen(Screen):
    pass


class DoneScreen(Screen):
    pass


class NewTaskScreen(Screen):
    pass


class SwipeToCompleteItem(MDCardSwipe):
    text = StringProperty()


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()


sm = ScreenManager()
sm.add_widget(ToDoScreen(name='todo'))
sm.add_widget(DoneScreen(name='done'))
sm.add_widget(NewTaskScreen(name='new_task'))


class DoTaskApp(MDApp):
    title = 'DoTask'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu = ObjectProperty()
        self.menu_items = []
        self.todo_list = []
        self.done_list = []
        self.nav_bar_items = {}
        self.dialog = None

    def build(self):

        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Dark"

    def on_start(self):
        # Make self.todo_list and self.done_list draw in screens
        self.read_lists()

        # Set starting screen
        self.root.ids.screen_manager.current = 'new_task'

        # Draw about list
        menu_item = {'text': 'About'}
        self.menu_items.append(menu_item)
        self.menu = MDDropdownMenu(items=self.menu_items, width_mult=2)
        self.menu.bind(on_release=self.menu_callback)

    # Close menu dialog
    def dismiss_btn(self, obj):
        self.dialog.dismiss()

    # Open menu
    def dots_menu(self, button):
        self.menu.caller = button
        self.menu.open()

    # Menu link
    def menu_callback(self, instance_menu, instance_menu_item):
        if not self.dialog:
            self.dialog = MDDialog(
                text='Can add tasks and complete or delete those tasks by swiping.',
                buttons=[MDFlatButton(text='Dismiss', on_release=self.dismiss_btn)]
            )
        self.dialog.open()
        self.menu.dismiss()

    # Bottom bar action
    def bottom_nav(self, screen):
        self.root.ids.screen_manager.current = screen.name

    # To do list swipe
    def on_swipe_complete(self, instance):
        Snackbar(text="Task completed", snackbar_y=dp(50)).open()
        self.done_list.append(instance.text)
        self.root.ids.done_list.add_widget(SwipeToDeleteItem(text=instance.text))
        done_index = self.todo_list.index(instance.text)
        self.todo_list.pop(done_index)
        self.save_list('todo')
        self.save_list('done')
        self.root.ids.todo_list.remove_widget(instance)

    # Done list swipe
    def on_swipe_delete(self, instance):
        Snackbar(text="Task deleted", snackbar_y=dp(50)).open()
        trash_index = self.done_list.index(instance.text)
        self.done_list.pop(trash_index)
        self.root.ids.done_list.remove_widget(instance)
        self.save_list('done')

    # New task input
    def todo_input(self):
        Snackbar(text="Task created", snackbar_y=dp(50)).open()
        text_input = self.root.ids.text_input.text
        self.root.ids.todo_list.add_widget(SwipeToCompleteItem(text=text_input))
        self.todo_list.append(text_input.strip('\n'))
        self.save_list('todo')

    # Read lists from file
    def read_lists(self):
        with open("todo.txt") as data:
            for todo in data.readlines():
                if todo != '\n':
                    self.todo_list.append(todo)
                    self.root.ids.todo_list.add_widget(SwipeToCompleteItem(text=todo))
        with open("done.txt") as data:
            for done in data.readlines():
                if done != '\n':
                    self.done_list.append(done)
                    self.root.ids.done_list.add_widget(SwipeToDeleteItem(text=done))

    # Save list to file
    def save_list(self, list_type):
        if list_type == 'todo':
            with open(f"todo.txt", mode='w') as file:
                for todo in self.todo_list:
                    file.write(f'{todo}\n')
        elif list_type == 'done':
            with open("done.txt", mode='w') as file:
                for done in self.done_list:
                    file.write(f'{done}\n')


if __name__ == '__main__':
    DoTaskApp().run()
