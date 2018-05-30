from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
# import ast
import numpy as np

app = Flask(__name__)
app.secret_key = 'test123'
app.config['DEBUG'] = True
TEMPLATES_AUTO_RELOAD = True


# def centeroidnp(arr):
#     length = arr.shape[0]
#     sum_x = np.sum(arr[:, 0])
#     sum_y = np.sum(arr[:, 1])
#     return sum_x/length, sum_y/length


@app.route("/", methods=['GET', 'POST'])
def index():
	print("we here?")
	return render_template('dual_iframes.html')


@app.route('/tab_viz.html')
def tab_viz():
    return render_template('tab_viz.html')


@app.route('/gmaps_placeholder.html')
def gmaps():
    return render_template('gmaps_placeholder.html')



@app.route("/get_marks", methods=['GET', 'POST'])
def get_marks():
	if request.method == "POST":
		lat_lon_list = request.form['Lat_Lon_Array']
		#not sure if this is working properly
		session.clear()
		session['Lat_Lon_Array'] = lat_lon_list
		# session['Center'] = centeroidnp(np.array(lat_lon_list))
		# print(session['Center'])
		#print(lat_lon_list)
		# return render_template("gmaps.html", lat_lon_list=lat_lon_list)
	html_str = render_template("gmaps.html", lat_lon_list=session['Lat_Lon_Array'])
	html_file= open("templates/gmaps_placeholder.html","w")
	html_file.write(html_str)
	html_file.close()
	#return render_template("gmaps.html", lat_lon_list=session['Lat_Lon_Array']) 
	#return render_template("gmaps_placeholder.html")
	# return index()
	return ('', 204)
	# return redirect('/')
	# return tab_viz()




