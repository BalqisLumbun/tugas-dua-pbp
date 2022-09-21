 https://tugas-tiga-pbp-balqis.herokuapp.com/mywatchlist/
 https://tugas-tiga-pbp-balqis.herokuapp.com/mywatchlist/html/
 https://tugas-tiga-pbp-balqis.herokuapp.com/mywatchlist/xml/
 https://tugas-tiga-pbp-balqis.herokuapp.com/mywatchlist/json

 
 Jelaskan perbedaan antara JSON, XML, dan HTML! (+ Postman)
 ![html]((https://github.com/BalqisLumbun/tugas-dua-pbp/blob/main/mywatchlist/pics/html.jpg)
 HTML adalah bahasa (lebih tepatnya aturan) pemformatan web, jadi digunakan untuk 
 dasar tampilan web dan bukan sebagai tempat simpanan data.
 ![xml]((https://github.com/BalqisLumbun/tugas-dua-pbp/blob/main/mywatchlist/pics/xml.jpg)
 XML fungsinya untuk menyimpan dan mengirimkan data, dan sifatnya dinamis, tidak seperti HTML. Secara tampilan
 terlihat seperti tag HTML, tetapi tidak menampilkan data selain object-object.
 ![json]((https://github.com/BalqisLumbun/tugas-dua-pbp/blob/main/mywatchlist/pics/json.jpg)
 Seperti XML, JSON sifatnya juga menyimpan data. JSON adalah notasi Javascript dalam menyimpan object,
 sehigga kata-kata tampilan (heading) yang seperti di HTML tidak ada, tetapi hanya data-data seperti XML.
 Notasinya berbeda dengan XML, JSON cenderung menyimpan object di array.
 
 Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 Sebuah platform website memiliki informasi yang dibutuhkan oleh user, sehingga untuk mempermudah
 seorang user atau komputer lain mendapatkan data-data penting (seperti bentuk json atau xml, yang ada
 hanya objek dan variabelnya), digunakan data delivery.
 
 Jelaskan bagaimana cara kamu mengimplementasikan tugas 3.
 - Membuat app baru dengan "python manage.py startapp mywatchlist" di cmd
 - Memasukkan mywatchlist ke settings.py
 - Menambahkan model dengan variabel watched, title, rating, release_date, review di models.py
 - Membuat json isi film-film dengan variabel yang ada di models.py, lalu
 - python manage.py loaddata initial_watchist_data.json agar datanya bisa masuk
 - Membuat fungsi fungsi show watchlist yang mereturn request, wishlist.html, context,
 - dan untuk JSON dan XML membuat seperti 
 - return HttpResponse(serializers.serialize("json/xml", data), content_type="application/json atau xml")
 - Untuk urlnya memasukkan from mywatchlist.views import fungsi yang sudah dibuat,
 - di urlpatterns, masukkan path('html/', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),path('json/', show_json, name='show_json')
 - Lalu deploy ke heroku, menggunakan procfile yang seperti template.
 - Unit test dilakukan dengan membuat object serupa lalu dicek kesamaannya.
 - Setelah jadi webnya, cek di postman.
