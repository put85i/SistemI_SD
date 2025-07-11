from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Pendaftar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(100))
    jenis_kelamin = db.Column(db.String(20))
    tempat_lahir = db.Column(db.String(50))
    tanggal_lahir = db.Column(db.String(20))
    agama = db.Column(db.String(30))
    tinggi_badan = db.Column(db.String(10))
    berat_badan = db.Column(db.String(10))
    nik_siswa = db.Column(db.String(30))
    no_kk = db.Column(db.String(30))
    alamat_lengkap = db.Column(db.String(200))
    nama_ayah = db.Column(db.String(100))
    pendidikan_ayah = db.Column(db.String(50))
    pekerjaan_ayah = db.Column(db.String(50))
    penghasilan_ayah = db.Column(db.String(50))
    nama_ibu = db.Column(db.String(100))
    pendidikan_ibu = db.Column(db.String(50))
    pekerjaan_ibu = db.Column(db.String(50))
    nomor_hp = db.Column(db.String(30))
    asal_sekolah = db.Column(db.String(100))

class Kontak(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    email = db.Column(db.String(100))
    pesan = db.Column(db.Text)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/formulir")
def formulir():
    return render_template("formulir.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = Pendaftar(
        nama_lengkap = request.form['nama_lengkap'],
        jenis_kelamin = request.form['jenis_kelamin'],
        tempat_lahir = request.form['tempat_lahir'],
        tanggal_lahir = request.form['tanggal_lahir'],
        agama = request.form['agama'],
        tinggi_badan = request.form['tinggi_badan'],
        berat_badan = request.form['berat_badan'],
        nik_siswa = request.form['nik_siswa'],
        no_kk = request.form['no_kk'],
        alamat_lengkap = request.form['alamat_lengkap'],
        nama_ayah = request.form['nama_ayah'],
        pendidikan_ayah = request.form['pendidikan_ayah'],
        pekerjaan_ayah = request.form['pekerjaan_ayah'],
        penghasilan_ayah = request.form['penghasilan_ayah'],
        nama_ibu = request.form['nama_ibu'],
        pendidikan_ibu = request.form['pendidikan_ibu'],
        pekerjaan_ibu = request.form['pekerjaan_ibu'],
        nomor_hp = request.form['nomor_hp'],
        asal_sekolah = request.form['asal_sekolah']
    )
    db.session.add(data)
    db.session.commit()

    return "Terima kasih! Data berhasil dikirim."

@app.route("/contact", methods=["POST"])
def contact():
    nama = request.form["name"]
    email = request.form["email"]
    pesan = request.form["message"]

    data = Kontak(nama=nama, email=email, pesan=pesan)
    db.session.add(data)
    db.session.commit()

    return "Pesan berhasil dikirim! Terima kasih telah menghubungi kami."

import os 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
