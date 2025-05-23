import google.generativeai as genai
from PIL import Image  #Requires Pillow Library: pip install Pillow

 # Configure the Gemini API key
genai.configure(api_key="YOUR_API_KEY") # Replace with your actual API key

 # Load the Gemini Pro Vision model
model = genai.GenerativeModel('gemini-pro-vision')

 # Load the image
img = Image.open("your_image.jpg")  # Replace with your image path

 # Prepare the prompt
prompt = "Describe what you see in this image."

 # Generate content
response = model.generate_content([prompt, img])

 # Print the response
print(response.text)
from django.shortcuts import render
import sys
import io

def home(request):
    result = "No pgm entered"
    error = "No error"
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        try:
            # Execute the user input code
            exec(user_input)
            result = new_stdout.getvalue()  # Get the output from the executed code
        except Exception as e:
            error = str(e)  # Capture any errors

        # Restore stdout
        sys.stdout = old_stdout

    return render(request, 'index.html', {'result': result, 'error': error})
 