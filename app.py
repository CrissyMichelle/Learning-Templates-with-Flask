from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
"""Not the best use of Flask framework"""
# @app.route('/form')
# def show_form():
#     """Show greeting form"""
#     return """
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>FormForWords</title>
# </head>
# <body>
#     <h1>MappedLibs</h1>
#     <form action="/form">
#         <label for="place">place:</label><input type="text" id="place">
#         <br>
#         <label for="noun">noun:</label><input type="text" id="noun">
#         <br>
#         <label for="verb">verb:</label><input type="text" id="verb">
#         <br>
#         <label for="adjective">adjective:</label><input type="text" id="adjective">
#         <br>
#         <label for="plural_noun">plural_noun:</label><input type="text" id="plural_noun">
#         <br>
#         <input type="submit" value="Submit">
#     </form>
#     <h2>Your Creative Masterpiece</h2>
#     <p>Once upon a time,</p>
# </body>
# </html>
# """
"""Much better to use templates!"""
@app.route("/")
def ask_questions():
    """Generates form view to ask for words"""
    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)
# Flask will find my html files in the templates directory automatically!
@app.route("/story")
def show_story():
    """Show resulting MappedLibs story"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)