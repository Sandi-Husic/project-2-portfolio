from flask import Flask, render_template

app = Flask(__name__)
app2 = Flask(__name__)

projects = {} 


@app.get('/')
def home():
  return render_template("home.html")


@app.get('/projects')
def display_projects():
  return render_template("projects.html")

@app.post('/projects/<string:project_slug>')
def show_projects(project_slug):
    project = projects.get(project_slug)

    if project is None: 
         return "Project not found!", 404

  
    return render_template("view_project.html", project = project())


@app.get('/contact')
def display_contact():
  return render_template("contact.html")
  
@app.get('/cms')
def display_cms():
  return render_template("cms.html")


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=81, debug=True)

     from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81)