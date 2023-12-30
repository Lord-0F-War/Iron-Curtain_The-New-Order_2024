


class Sounds_Manager:
    def __init__(self, generic_hover_over_button_menu_sound, click_main_menu_sound, generic_click_menu_sound) -> None:
        
        self.generic_hover_over_button_menu_sound = generic_hover_over_button_menu_sound
        self.click_main_menu_sound = click_main_menu_sound
        self.generic_click_menu_sound = generic_click_menu_sound

        self.sounds = [self.generic_hover_over_button_menu_sound, self.click_main_menu_sound, self.generic_click_menu_sound]

    def change_volume(self, volume):
        for sound in self.sounds:
            sound.set_volume(volume)
