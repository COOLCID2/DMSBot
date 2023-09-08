
import os
from PIL import ImageGrab
from pyzbar.pyzbar import decode
import time
import pyautogui
import time
import pytesseract
from PIL import Image
print(pytesseract.__file__)

def GettoDoctype():
    pyautogui.press('f5')
    time.sleep(2)
    click_image(image_path='./data/reset.png', click_offset=(0, 0))
    # Delay for a few seconds to give you time to focus on the target window
    # Click the 'tasks.png' image with an offset of (-10, 20) from the center
    click_image(image_path='./data/tasks.png', click_offset=(-10, 0))
    # Click the 'selecttask.png' image with an offset of (0, 0) from the center
    click_image(image_path='./data/selecttask.png', click_offset=(0, 50), confidence=.8,timeout=7)
    click_image(image_path='./data/preview.png', click_offset=(0, 0), confidence=.7)
    time.sleep(2)
    pyautogui.scroll(8000)
    time.sleep(2)
    click_image(image_path='./data/automaticzoom.png', click_offset=(0, 0),timeout=2)
    time.sleep(2)
    click_image(image_path='./data/200.png', click_offset=(0, 0), confidence=.95,timeout=1)

def capture_screenshot(region, save_path):
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(save_path)
    return pytesseract.image_to_string(save_path, lang='eng')
def click_image(image_path, click_offset=(0, 0), confidence=0.7, timeout=4):
    start_time = time.time()

    while True:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location[0] + click_offset[0], location[1] + click_offset[1])
            break  # Exit the loop once the image is found and clicked

        # Check for timeout
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            print(f"Timeout reached. Couldn't find the image {image_path}.")
            break

        # Small sleep to prevent high CPU usage
        time.sleep(0.1)

def GetAccountingInfo():
    try:
        time.sleep(2)
        pyautogui.scroll(-1580)
        time.sleep(1)
        # Find the location of the specified image on the screen
        image_location = pyautogui.locateCenterOnScreen('./data/dollar.png', confidence=0.8)
        print(image_location)
        x, y = image_location
        x -= -100
        y -= 150
        width, height = 160, 50  # Set the width and height for the region 160, 70

        # Capture the specified area of the screen as an image
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save('Ronum.png')  # Save the screenshot for reference (optional)

        # Perform OCR on the captured image
        Ronum = pytesseract.image_to_string('Ronum.png', lang='eng')
        #
        #
        #

        # Capture the specified area of the screen as an image
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save('Amount.png')  # Save the screenshot for reference (optional)

        # Perform OCR on the captured image
        Amount = pytesseract.image_to_string('Amount.png', lang='eng')
        print("Amount is "+ Amount + "Accounting number is "+ Ronum)
        print(Ronum)
        time.sleep(1)
        # Find the location of the specified image on the screen
        image_location = pyautogui.locateCenterOnScreen('./data/dollar.png', confidence=0.8)
        print(image_location)
        x, y = image_location
        x -= -12
        y -= 25
        width, height = 160, 70  # Set the width and height for the region

        # Capture the specified area of the screen as an image
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save('Amount.png')  # Save the screenshot for reference (optional)

        # Perform OCR on the captured image
        Amount = pytesseract.image_to_string('Amount.png', lang='eng')
        print("Amount is "+ Amount + "Accounting number is "+ Ronum)

        import re

        # Replace commas that are followed by exactly two digits with a period
        Amount = re.sub(r',(?=\d{2}\b)', '.', Amount)

        # If there's no period in the amount, insert one two places from the end
        if '.' not in Amount:
            Amount = Amount[:-2] + '.' + Amount[-2:]

        # Remove any existing commas
        Amount = Amount.replace(',', '')

        # Convert the string to a float
        amount_float = float(Amount)

        # Format the float to include commas as needed
        Amount = "{:,.2f}".format(amount_float)

        print(Amount)
        print("test")
    except:
        TypeError
    try:
        return Ronum,Amount
    except:
        UnboundLocalError
        pass
def Accountingafter():
    try:
        Ronum, Amount = GetAccountingInfo()
    except Exception as e:
        print(f"An error occurred: {e}")
        Ronum, Amount = None, None  #
    click_sequence = [
        {'action': 'click', 'path': './data/exit.png', 'offset': (0, 0)},
        {'action': 'click', 'path': './data/documenttype.png', 'offset': (0, 0)},
        {'action': 'delay', 'duration': 1},
        {'action': 'press', 'content': 'enter'},
        {'action': 'delay', 'duration': 2},
        {'action': 'click','path': './data/document.png', 'offset': (0, 30), 'confidence': 0.85},
        {'action': 'delay', 'duration': 1},
        {'action': 'write', 'content': str(Ronum)},
        {'action': 'delay', 'duration': 2},
        {'action': 'click', 'path': './data/autofill.png', 'offset': (0, 0)},
        {'action': 'delay', 'duration': 2},
        {'action': 'check_image', 'path': './data/success.png', 'confidence': 0.8},
        {'action': 'delay', 'duration': 5},
        {'action': 'click', 'path': './data/amountspot.png', 'offset': (0, 30)},
        {'action': 'press', 'content': ['ctrl', 'a']},
        {'action': 'delay', 'duration': 2},
        {'action': 'write', 'content': str(Amount)},
        {'action': 'delay', 'duration': 1},
        {'action': 'click', 'path': './data/classify.png', 'offset': (0, 0)}

    ]

    for action_item in click_sequence:
        if action_item['action'] == 'click':
            confidence = action_item.get('confidence', 0.7)
            click_image(action_item['path'], action_item['offset'], confidence)
        elif action_item['action'] == 'write':
            pyautogui.write(action_item['content'])
        elif action_item['action'] == 'press':
            if isinstance(action_item['content'], list):
                pyautogui.hotkey(*action_item['content'])
            else:
                pyautogui.press(action_item['content'])
        elif action_item['action'] == 'delay':
            time.sleep(action_item['duration'])
        elif action_item['action'] == 'check_image':
            timeout = 9  # You can adjust the timeout value as needed
            start_time = time.time()
            while True:
                location = pyautogui.locateOnScreen(action_item['path'], confidence=action_item.get('confidence', 0.7))
                if location:
                    break  # Image found, exit the loop
                # Check for timeout
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    print(f"Confirmation image {action_item['path']} not found within timeout. Exiting...")
                    return  # Exiting if the image was not found within the timeout period



def capture_near_reference(reference_image_path, offset_x, offset_y, capture_width, capture_height, output_image_path,
                           output_padded_image_path, padding=50, confidence_level=0.70):
    # Load the reference image
    reference_image = pyautogui.locateOnScreen(reference_image_path, confidence=confidence_level)
    Documentnumber = None
    if reference_image is not None:
        print("Found Reference Image")
        reference_x, reference_y, reference_width, reference_height = reference_image

        # Calculate the coordinates of the region you want to capture
        capture_x = reference_x + offset_x
        capture_y = reference_y + offset_y

        # Capture the screenshot of the specified region
        screenshot = pyautogui.screenshot(region=(capture_x, capture_y, capture_width, capture_height))
        screenshot.save(output_image_path)

        img_with_border = Image.new('RGB', (screenshot.width + 2 * padding, screenshot.height + 2 * padding), 'white')
        img_with_border.paste(screenshot, (padding, padding))

        # Save the padded image
        img_with_border.save('Document.png')
        Documentnumber = pytesseract.image_to_string('Document.png', lang='eng').replace('\n', '')

        print(Documentnumber)
    return Documentnumber


def process_parts():
    print("This is a parts document")

    try:
        Documentnumber = capture_near_reference('./data/Purchaseorder.png', 15, 35, 185, 24,
                                                'captured_purchaseorder.png', 'captured_pURCHASEORDER1.png')

        # Find all the digits in the string
        digits = "".join(filter(lambda x: x.isdigit(), str(Documentnumber)))

        if len(digits) >= 8:
            # Keep only the first 8 digits
            valid_document_number = digits[:8]
            print("Valid Document Number:", valid_document_number)
            Documentnumber = valid_document_number
        else:
            print("Invalid Document Number:", Documentnumber)
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(2)
    # Sequence of actions
    click_sequence = [
        {'action': 'click', 'path': './data/exit.png', 'offset': (0, 0)},
        {'action': 'click', 'path': './data/documenttype.png', 'offset': (0, 0)},
        {'action': 'click', 'path': './data/parts.png', 'offset': (0, 0)},
        {'action': 'delay', 'duration': 2},
        {'action': 'click','path': './data/invoicenumber.png', 'offset': (0, 10), 'confidence': 0.9},
        {'action': 'delay', 'duration': 1},
        {'action': 'write', 'content': str(Documentnumber)},
        {'action': 'delay', 'duration': 2},
        {'action': 'click', 'path': './data/autofill.png', 'offset': (0, 0)},
        {'action': 'check_image', 'path': './data/success.png', 'confidence': 0.7},
        {'action': 'delay', 'duration': 5},
        {'action': 'click', 'path': './data/generalparts.png', 'offset': (0, 0)},
        {'action': 'click', 'path': './data/partsinvoice.png', 'offset': (0, 0)},
        {'action': 'delay', 'duration': 2},
        {'action': 'click', 'path': './data/classify.png', 'offset': (0, 0)}

    ]

    for action_item in click_sequence:
        if action_item['action'] == 'click':
            confidence = action_item.get('confidence', 0.7)
            click_image(action_item['path'], action_item['offset'], confidence)
        elif action_item['action'] == 'write':
            pyautogui.write(action_item['content'])
        elif action_item['action'] == 'delay':
            time.sleep(action_item['duration'])
        elif action_item['action'] == 'check_image':
            timeout = 9  # You can adjust the timeout value as needed
            start_time = time.time()

            while True:
                location = pyautogui.locateOnScreen(action_item['path'], confidence=action_item.get('confidence', 0.7))
                if location:
                    break  # Image found, exit the loop

                # Check for timeout
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    print(f"Confirmation image {action_item['path']} not found within timeout. Exiting...")
                    return  # Exiting if the image was not found within the timeout period

                # Small sleep to prevent high CPU usage
                time.sleep(0.1)


print("need to redo loop from here")

def process_Accounting():
    # ... (your code for processing invoice document goes here)
    time.sleep(1)
    print('This is aan accounting document.')
    Accountingafter()



def process_Service():
    # ... (your code for processing order document goes here)
    time.sleep(1)
def main():
    GettoDoctype()
    print("test")
    pyautogui.scroll(-100)
    time.sleep(2)
    found = False
    for confidence in [0.8, 0.7, 0.55,0.5]:
        if pyautogui.locateCenterOnScreen('./data/invoicenumber1.png', confidence=confidence):
            process_parts()
            found = True
            break
        elif pyautogui.locateCenterOnScreen('./data/Accountingexample.png', confidence=confidence):
            process_Accounting()
            found = True
            break
        elif pyautogui.locateCenterOnScreen('./data/servicedocument.png',confidence=confidence):  # Change the path to the correct image
            process_Service()
            found = True
            break
    if not found:
        print("Couldn't identify Document type")

if __name__ == "__main__":
    while 1==1:
        time.sleep(1)
        main()
        time.sleep(3)
