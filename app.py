from flask import Flask

# Fungsi untuk membuat dan mengkonfigurasi aplikasi
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kunci-rahasia-anda' 
    
    # Import dan registrasi Blueprint (akan kita tambahkan nanti)
    # from .website import views
    # app.register_blueprint(views.bp)

    return app

if __name__ == '__main__':
    # Jalankan aplikasi (mode debug=True selama pengembangan)
    app = create_app()
    # Pastikan Anda menginstal Flask: pip install Flask
    app.run(debug=True)
