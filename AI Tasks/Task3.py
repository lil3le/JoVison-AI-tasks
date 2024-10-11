import pandas as pd
from PIL import Image
from Functions.GetFile import get_image_file
import os

def NumberOF_FingersTouched_Count(image_path):
    image = Image.open(image_path)
    width, height = image.size
    
    for i in range(width):
        r, g, b = image.getpixel((i, height - 1))
        if r >= 150 and g == 0 and b == 0:
            return [0] * 5 

    image = image.crop((width // 2, 0, width, height))
    image.show()

    Fingers = [
        image.crop((0, 0, width // 2, height // 10)),
        image.crop((0, height // 5, width // 2, height // 3)),
        image.crop((0, height // 3, width // 2, height // 2)),
        image.crop((0, height // 2, width // 2, height // 1.5)),
        image.crop((0, height // 1.5, width // 2, height))
    ]
    
    Pressure = []
    
    for finger in Fingers:
        pixels = finger.load()
        finger_width, finger_height = finger.size
        pressure_detected = False
        
        for x in range(finger_width):
            for y in range(finger_height):
                r, g, b = pixels[x, y]
                if r >= 10 and g >= 150 and b >= 240:
                    pressure_detected = True
                    break
            if pressure_detected:
                break
        
        Pressure.append(1 if pressure_detected else 0)
    
    return Pressure

def save_to_excel(result, file_name='Results/results.xlsx'):
    file_path = os.path.join('AI Tasks', file_name)
    
    if os.path.exists(file_path):
        df_existing = pd.read_excel(file_path, engine='openpyxl')
    else:
        df_existing = pd.DataFrame(columns=['Finger', 'PressureDetected'])
    
    new_data = pd.DataFrame({'Finger': ['Finger1', 'Finger2', 'Finger3', 'Finger4', 'Finger5'], 
                             'PressureDetected': result})
    
    df_combined = pd.concat([df_existing, new_data], ignore_index=True)
    df_combined.to_excel(file_path, index=False, engine='openpyxl')
    print("Saved to excel, appended new results.")




result = NumberOF_FingersTouched_Count(get_image_file())
print(result)
save_to_excel(result)
