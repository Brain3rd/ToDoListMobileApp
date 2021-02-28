KV = """

Screen:         

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            pos_hint: {'top': 1, 'left': 1}
            height: 55
            title: 'DoTask'
            elevation: 8
            left_action_items: [["menu", lambda x: nav_drawer.set_state('open')]]
            right_action_items: [["dots-vertical", lambda x: app.dots_menu(x)]]


        MDBottomNavigation:

            MDBottomNavigationItem:
                name: 'new_task'
                text: 'add'
                icon: 'notebook-edit'
                on_tab_release: app.bottom_nav(self)

            MDBottomNavigationItem:
                name: 'todo'
                text: 'do'
                icon: 'notebook'
                on_tab_release: app.bottom_nav(self)

            MDBottomNavigationItem:
                name: 'done'
                text: 'done'
                icon: 'notebook-check'
                on_tab_release: app.bottom_nav(self) 


    MDNavigationLayout:

        ScreenManager:
            id: screen_manager

            ToDoScreen:
                name: 'todo'        
                ScrollView:
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 0.85
                    size_hint_y: 0.7
                    orientation: "vertical"
                    padding: "8dp"
                    spacing: "8dp"
                    MDList:
                        id: todo_list

            DoneScreen:
                name: 'done'           
                ScrollView:
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: 0.85
                    size_hint_y: 0.7
                    orientation: "vertical"
                    padding: "8dp"
                    spacing: "8dp"  
                    MDList:
                        id: done_list

            NewTaskScreen:
                name: 'new_task'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: 5
                    padding: 40

                MDTextField:
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint_x: None
                    size_hint_y: None
                    width: 200
                    height: 200
                    id: text_input
                    hint_text: 'Enter New Task'
                    helper_text: 'What would you like to do?'
                    helper_text_mode: 'on_focus'
                    multiline: False
                    required: True

                MDRectangleFlatButton:
                    text: 'Add'
                    pos_hint: {"center_x": .5, "center_y": .3}
                    size_hint_x: None
                    width: 50
                    on_release: app.todo_input()


        MDNavigationDrawer:
            id: nav_drawer
            theme_text_color: "Custom"
            on_release: self.parent.set_color_items(self)

            BoxLayout:
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"             
                Image:
                    id: avatar
                    size_hint: None, None
                    size: "120dp", "120dp"
                    source: "logo.png"                
                MDLabel:
                    text: "DoTask" 
                    font_style: "H5"
                    size_hint_y: None
                    height: self.texture_size[1]
                                  
                ScrollView:
                    MDList:
                        padding: "8dp"
                        spacing: "8dp"                    
                        MDLabel:
                            text: "Easy to use:"
                            font_style: "Button"
                            size_hint_y: None
                            height: self.texture_size[1]
                     
                        MDLabel:
                            text: 'Add new task'
                            font_style: "Caption"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: 'Swipe right to complete'
                            font_style: "Caption"
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: 'Swipe right to delete'
                            font_style: "Caption"
                            size_hint_y: None
                            height: self.texture_size[1]


<SwipeToCompleteItem>:
    size_hint_y: None
    height: content.height
    type_swipe: "auto"
    on_swipe_complete: app.on_swipe_complete(root)

    MDCardSwipeLayerBox:

    MDCardSwipeFrontBox:

        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True


<SwipeToDeleteItem>:
    size_hint_y: None
    height: content.height
    type_swipe: "auto"
    on_swipe_complete: app.on_swipe_delete(root)

    MDCardSwipeLayerBox:

    MDCardSwipeFrontBox:

        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True

"""