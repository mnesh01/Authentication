import os


EMAIL_USE_TLS = True
EMAIL_HOST ='smtp.gmail.com'
EMAIL_HOST_USER = 'mnesh002@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # Fetch from environment variable
EMAIL_PORT = 587