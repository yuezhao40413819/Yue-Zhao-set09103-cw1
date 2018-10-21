from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home ():
    return render_template('home.html')
@app.route('/Characters/')
def Characterrs():
    return render_template('Characters.html')
@app.route('/log_in/',methods=['GET','POST'])
def log_in():
    if request.method == 'POST':
      return redirect(url_for('home'))
    else:
      return render_template('log_in.html')
@app.route('/Development/')
def  Development():
	return render_template('Development.html')
@app.errorhandler(404)
def page_not_found(error):
  return "Sorry, we couldn't find the page you requested.", 404



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

