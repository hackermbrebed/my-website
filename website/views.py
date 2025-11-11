from flask import Blueprint, render_template

# Membuat Blueprint. 'views' adalah nama blueprint.
# '__name__' membantu Flask menemukan resource di folder ini.
views = Blueprint('views', __name__)

@views.route('/') # Ini adalah decorator yang mendefinisikan rute untuk URL '/' (halaman utama)
def home():
    # Render file 'index.html' dari folder 'templates'
    # Kita juga bisa mengirimkan data ke template, misalnya title
    return render_template("index.html", title="Direktori Website Kustom")

# Anda bisa menambahkan rute untuk halaman-halaman lain di sini nanti
# @views.route('/about')
# def about():
#     return render_template("about.html")
