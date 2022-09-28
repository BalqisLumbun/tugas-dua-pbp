Link Heroku: https://tugas-tiga-pbp-balqis.herokuapp.com/katalog/

-Karena berupa file tertulis maka saya akan berikan penjelasan bukan bagan:
Request dari klien muncul ke internet, lalu diterima django sebagai webserver environment.
manage.py menjalankan program. 
Argumen dari request diterima oleh views.py yang memiliki function.
Function ini juga memiliki hubungan dengan database berparameter Models. 
models.py memiliki class sebuah item sehingga models.py dan file .json dapat bekerja bersama
untuk membentuk data. Data yang sudah rapi, dapat digunakan views.py, dan 
ditampilkan di index.html . Tetapi sebelum dapat ditampilkan, dari views.py,urls.py mengambil
informasi dan membuat path di urlpatterns supaya file dapat diakses sebelum ditampilkan. Web page
yang sudah jadi, dapat diakses di internet.

-Virtual env bermanfaat untuk memisahkan pengaturan dan package Django sehingga tidak ada
file yang tercampur dan mempersulit development. Selain itu adanya virtual env menyebabkan
adanya preview website dan debugging yang baik.
Virtual environment bukan syarat mutlak untuk membuat aplikasi Django, tetapi sangat membantu.

- 1. import CatalogItem dari katalog.models, buat fungsi yang mereturn render dengan paramnya 
- katalog.html
- Memenuhi kebutuhan katalog.html, variabelnya ada list_katalog dari data item katalog, ada 
- nama, npm.
- 2. Routing dibuat di katalog/urls.py dengan mengimpor show_katalog dari katalog.views. Membuat app name,
- Lalu memberi path di urlpatterns dengan show_katalog. Di project django/urls.py, urlpatterns juga 
- ditambahkan path('katalog/', include('katalog.urls')),
- 3. Mapping dilakukan dengan mengganti fillme menjadi {{nama}} dan {{npm}} lalu iterasi dengan
- {% for items in list_katalog %}, buat baris dengan <tr>, setiap 1 bagian dibuat dengan <th>, impor
  dari variabel list katalog, seperti {{items.item_name}} untuk menulis nama secara otomatis. Akan
  looping hingga akhir.
- 4. Deploy setelah push dengan buat app di heroku, ambil API Key, masukkan api key dan nama app
  heroku di github secret, dpl.yml sudah ada, lalu jalankan. (Di github katanya deploy berhasil 
  centang hijau tetapi di website tulisannya error)
