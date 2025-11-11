from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kunci-rahasia-anda-yang-sangat-rahasia-dan-kuat' # Ganti dengan kunci rahasia yang lebih kuat!
    
    # Import Blueprint dari modul 'website' kita
    from .website.views import views as website_views
    # Daftarkan Blueprint agar aplikasi tahu rute-rute di dalamnya
    app.register_blueprint(website_views, url_prefix='/') # url_prefix='/' berarti rute dasar

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) # debug=True akan me-reload server secara otomatis saat ada perubahan
