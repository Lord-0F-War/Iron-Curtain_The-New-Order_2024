


class Sounds_Manager:
    def __init__(self, generic_hover_over_button_sound, generic_click_button_sound) -> None:
        
        self.generic_hover_over_button_sound = generic_hover_over_button_sound
        self.generic_click_button_sound = generic_click_button_sound

        self.sounds = [self.generic_hover_over_button_sound, self.generic_click_button_sound]

    def change_volume(self, volume):
        for sound in self.sounds:
            sound.set_volume(volume)
