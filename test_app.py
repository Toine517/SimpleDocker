import datetime
from flask import Flask # import the Flask class from the flask module
from flask import request # import the request class from the flask module for handling and making HTTP requests
from flask import jsonify # import the jsonify class from the flask module for converting a Python dictionary or list into JSON format
from flask_cors import CORS # import the CORS class from the flask_cors module, this allows cross origin resource sharing which allows for use of your api by other domains
# CORS is a Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible. It is a way to relax the same-origin policy, which is a set of restrictions imposed by browsers to prevent interactions between resources from different origins.
# you can configure CORS options to specify allowed origins, headers, and other settings according to your requirements.


app = Flask(__name__) # creates an instance of the Flask class called "app", this allows Flask to find the location and root path of the application's resources, such as templates and static files.
# __name__ is the name of the current Python module. The app needs to know where it's located to set up some paths, and __name__ is a convenient way to tell it that.
# you can also use the specific name of the file, but using __name__ is better because it's more reliable and just points to whatever module is currently being used as the entry point (so it won't break if you change the file name).
# The app variable is an instance of Flask, so you can use it like any other Python object. The Flask class has a constructor that takes the name of the current module (__name__) as argument.

CORS(app) # use the CORS class to pass in the app variable, this allows cross origin resource sharing which allows for use of your api by other domains

def generate_pi_digits(num_digits):
    """
    Generates pi digits using a pure integer spigot algorithm.
    """
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    digits_found = 0
    pi_string = ""
    
    while digits_found < num_digits:
        if 4 * q + r - t < n * t:
            pi_string += str(n)
            digits_found += 1
            if digits_found == 1:
                pi_string += "."
            
            # Update values for the next extraction
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            # Main algorithm step to generate fractions
            nr = (2 * q + r) * l
            nn = (q * (7 * k + 2) + r * l) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr
            
    return pi_string
    
wrapper = """<html>
<head>
<title>%s output - %s</title>
</head>
<body>
<style>
div {
  width: 95%; 
  border: 0px solid #000000;
}
div.b {
  word-wrap: break-word;
}
</style>
<div class="b">%s</dib>
</body>
</html>"""



@app.route('/', methods=['GET'], strict_slashes=False) # strict_slashes=False allows for both '/products' and '/products/' to return the same thing and methods=['GET'] specifies that this endpoint will only accept GET requests
def get_pi():
    return generate_pi_digits(33)

@app.route('/<int:id>',methods=['GET'], strict_slashes=False)
def get_pi_decimal(id):
    return wrapper % ("Compute-Pi", "10-10-2026", generate_pi_digits(int(id)))

if __name__ == '__main__': # if the script is executed directly, the code block is executed, if the script is imported, the code block is not executed.
    app.run(host='0.0.0.0', port='8080', debug = True) #specify the url and port, and debug = True allows for the server to automatically reload when changes are made to the code
