https://tugas-tiga-pbp-balqis.herokuapp.com/todolist/
https://tugas-tiga-pbp-balqis.herokuapp.com/todolist/login

Link

Balqis Asy-Syifa Lumbun , 2106751184 , PBP - E

A. {% csrf_token %} 
Fungsinya adalah melindungi data dari Cross Site Request Forgery.  Bila tokennya tidak sama, sesi user akan diterminasi dan eventnya dianggap sebagai potensi serangan.
B. Elemen <form> manual
Secara manual form dapat dibuat dengan cara membuat forms.py, dan di line paling atas tuliskan "from django import forms", lalu buat kelas dan import kelasnya di views.py.
C.Alur data
User menulis data dan klik submit. User mengirimkan request "POST", lalu dicek methodnya oleh fungsi yang ada di views.py. Datanya masuk ke database, lalu untuk ditampilkan dapat menggunakan class.objects.all() dan masuk ke context sebagai parameter fungsi di views.py. Setelah itu bisa ditampilkan.
D.Implementasi:
1. Membuat todolist dengan command python manage.py startapp todolist
2. Mendaftarkan app todolist di settings.py dan menambahkan path todolist di urls.py project django
3. Ke models.py dan bikin model task beserta atribut-atributnya
4. Membuat registrasi, login, logout dengan html masing-masing, redirect, path di urls.py, fungsi di views.py
5. Memboat todolist.html beserta username, tombol task baru yang meredirect ke form, logout, tabel task
6. Membuat routing di folder todolist, urls.py
7. Deploy
