from PIL import Image, ImageOps 
import pytesseract
import numpy as np

class Captcha(object):
    def __init__(self):
        pass

    def __call__(self, im_path, save_path):
        """
        Algo for inference
        args:
            im_path: .jpg image path to load and to infer
            save_path: output file path to save the one-line outcome
        """
        # Load the image
        image_orgin = Image.open(im_path)
        image = ImageOps.grayscale(image_orgin)
        image_array = np.array(image)
        
         # enhance the contrast between the text and background
        image_array[image_array>40]=255
        
        image_processed = Image.fromarray(image_array)
        
        # Use pytesseract to extract the text
        extracted_text = pytesseract.image_to_string(image_processed, config='--psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        
        # Clean the extracted text (remove any non-uppercase English letters and numbers)
        cleaned_text = ''.join(filter(lambda x: x.isalnum() and (x.isupper() or x.isdigit()), extracted_text))
        
        # Save the result to a file
        with open(save_path, 'w') as f:
            f.write(cleaned_text)

        return cleaned_text

# Instantiate the class
captcha_solver = Captcha()

# Define the paths
im_path = './sampleCaptchas/input/input20.jpg'
save_path = './sampleCaptchas/output/result.txt'

# Call the object to solve the captcha
captcha_result = captcha_solver(im_path, save_path)




















