import pyautogui
import keyboard

print("Let's play Touhou! Press 'c' to hold fire")
print("Press 'q' to exit")

key_down = False

while True:
    # Exit program
    if keyboard.is_pressed('q'):
        break

    # Start auto-fire
    if keyboard.is_pressed('c'):
        while keyboard.is_pressed('c'):
            pass
        # Release
        if key_down:
            pyautogui.keyUp('z')
            key_down = False
        # Activate
        else:
            pyautogui.keyDown('z')
            key_down = True

print("Touhou time over, GG")
