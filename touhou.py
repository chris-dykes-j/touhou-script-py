import pyautogui
import keyboard

print("Let's play Touhou! Press 'c' to hold fire")
print("Press 'q' to exit")


def toggle_action(tap_key, hold_key, key_down):
    if keyboard.is_pressed(tap_key):
        print("Holding " + hold_key)
        if key_down:
            pyautogui.keyUp(hold_key)
            key_down = False
        else:
            pyautogui.keyDown(hold_key)
            key_down = True

    if keyboard.is_pressed(hold_key) and key_down:
        print("Quit holding " + hold_key)
        pyautogui.keyUp(hold_key)
        key_down = False

    return key_down


fire_key_down = False
slow_key_down = False

while True:
    # Exit program
    if keyboard.is_pressed('q'):
        break

    # Auto-fire
    fire_key_down = toggle_action('c', 'z', fire_key_down)

print("Touhou time over, GG")
