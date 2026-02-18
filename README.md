# MINI_PROJECT_2

<h1>Iris Species Classification Web Application</h1>

<h2>Project Overview</h2>
<p>
This is a <b>Flask-based web application</b> that classifies Iris flower species
using <b>K-Nearest Neighbors (KNN)</b> and <b>Naive Bayes</b> machine learning algorithms.
The application provides an interactive dashboard where users can input flower
measurements and get real-time predictions along with model performance metrics.
</p>

<h2>Features</h2>

<h3>Interactive Prediction Interface</h3>
<ul>
<li>Sepal Length (cm)</li>
<li>Sepal Width (cm)</li>
<li>Petal Length (cm)</li>
<li>Petal Width (cm)</li>
<li>Toggle between KNN and Naive Bayes models</li>
<li>Real-time species prediction (Setosa, Versicolor, Virginica)</li>
</ul>

<h3>Model Performance Dashboard</h3>
<ul>
<li>Accuracy score</li>
<li>Classification report (Precision, Recall, F1-score)</li>
<li>Confusion matrix</li>
<li>Training & Testing metrics</li>
</ul>

<h2>Architecture</h2>

<h3>Frontend</h3>
<ul>
<li>HTML / CSS / JavaScript</li>
<li>Bootstrap 5</li>
<li>Glass morphism UI</li>
</ul>

<h3>Backend</h3>
<ul>
<li>Python Flask</li>
<li>Pickle model loading</li>
<li>JSON metrics</li>
<li>Jinja2 templating</li>
</ul>

<h2>Machine Learning Models</h2>
<ul>
<li>KNN Classifier (k=3)</li>
<li>Gaussian Naive Bayes</li>
</ul>

<h2>Dataset Information</h2>

<table border="1">
<tr>
<th>Feature</th>
<th>Description</th>
<th>Range</th>
</tr>
<tr>
<td>Sepal Length</td>
<td>Length of sepal in cm</td>
<td>4.3 - 7.9</td>
</tr>
<tr>
<td>Sepal Width</td>
<td>Width of sepal in cm</td>
<td>2.0 - 4.4</td>
</tr>
<tr>
<td>Petal Length</td>
<td>Length of petal in cm</td>
<td>1.0 - 6.9</td>
</tr>
<tr>
<td>Petal Width</td>
<td>Width of petal in cm</td>
<td>0.1 - 2.5</td>
</tr>
</table>

<h2>File Structure</h2>

<pre>
iris-classifier/
├── app.py
├── requirements.txt
├── Procfile
├── templates/index.html
├── KNN.pkl
├── Navis.pkl
</pre>

<h2>Deployment on Render</h2>

<h3>Upload to GitHub</h3>

<pre>
git init
git add .
git commit -m "Initial commit"
git push origin main
</pre>

<h3>Render Settings</h3>
<ul>
<li>Environment: Python 3</li>
<li>Build Command: pip install -r requirements.txt</li>
<li>Start Command: gunicorn app:app</li>
</ul>

<h2>Local Development</h2>

<pre>
python -m venv venv
pip install -r requirements.txt
python app.py
</pre>

<h2>How It Works</h2>

<p>
User Input → Flask Route → Model Loading → Prediction → Template Rendering → Display
</p>

<h2>Future Enhancements</h2>
<ul>
<li>Add more algorithms</li>
<li>Data visualization</li>
<li>Batch prediction</li>
<li>API endpoints</li>
</ul>

<h2>Contact</h2>
<p>Email: sohailmd6661@gmail.com</p>

<p>Created by Mohammed Sohail</p>

