import telebot

# Masukkan TOKEN API dari BotFather
TOKEN = "..............."
bot = telebot.TeleBot(TOKEN)

# Dictionary untuk daftar pertanyaan berdasarkan topik
qa_data = {
    "Data":
    [("Apa itu Data Analytics?",
      "Data Analytics adalah proses menganalisis data mentah untuk mendapatkan wawasan yang berguna dalam pengambilan keputusan."
      ),
     ("Apa tujuan Data Analytics?",
      "Tujuan utama Data Analytics adalah mengidentifikasi pola, tren, dan hubungan dalam data untuk mendukung pengambilan keputusan bisnis."
      ),
     ("Apa itu ETL dalam Data Analytics?",
      "ETL (Extract, Transform, Load) adalah proses mengambil data dari berbagai sumber, mengubahnya menjadi format yang sesuai, dan menyimpannya dalam data warehouse."
      ),
     ("Apa itu SQL dalam Data Analytics?",
      "SQL (Structured Query Language) adalah bahasa yang digunakan untuk mengakses, mengelola, dan memanipulasi database dalam proses analisis data."
      ),
     ("Apa itu Dashboard dalam Data Analytics?",
      "Dashboard adalah tampilan visual yang menyajikan data dalam bentuk grafik atau tabel untuk membantu analisis dan pengambilan keputusan."
      ),
     ("Apa itu Data Science?",
      "Data Science adalah bidang ilmu yang menggabungkan statistik, machine learning, dan pemrograman untuk mengekstrak wawasan dari data."
      ),
     ("Apa perbedaan Data Science dan Data Analytics?",
      "Data Analytics berfokus pada analisis data historis untuk pengambilan keputusan, sedangkan Data Science mencakup analisis prediktif dan machine learning untuk menghasilkan model yang dapat memprediksi kejadian di masa depan."
      ),
     ("Apa itu Machine Learning dalam Data Science?",
      "Machine Learning adalah cabang dari Data Science yang menggunakan algoritma untuk membuat sistem yang dapat belajar dari data tanpa perlu diprogram secara eksplisit."
      ),
     ("Apa itu Python dan R dalam Data Science?",
      "Python dan R adalah bahasa pemrograman yang sering digunakan dalam Data Science untuk analisis data, machine learning, dan visualisasi."
      ),
     ("Apa itu Model Training dalam Data Science?",
      "Model Training adalah proses melatih algoritma machine learning menggunakan data latih untuk menghasilkan model yang dapat membuat prediksi."
      ),
     ("Apa itu AI dalam Data Science?",
      "AI (Artificial Intelligence) adalah teknologi yang memungkinkan mesin untuk meniru kecerdasan manusia, termasuk dalam proses analisis data dan machine learning."
      ),
     ("Apa itu Big Data dalam Data Science?",
      "Big Data adalah kumpulan data yang sangat besar dan kompleks sehingga membutuhkan teknologi khusus untuk penyimpanan dan analisisnya."
      ),
     ("Apa itu Data Engineering?",
      "Data Engineering adalah disiplin ilmu yang berfokus pada pembangunan, pemeliharaan, dan pengelolaan infrastruktur data untuk keperluan analisis."
      ),
     ("Apa tugas utama Data Engineer?",
      "Data Engineer bertugas membangun pipeline data, mengelola database, dan memastikan data tersedia dalam format yang siap untuk dianalisis."
      ),
     ("Apa itu Data Pipeline?",
      "Data Pipeline adalah serangkaian proses otomatis untuk mengumpulkan, mentransformasikan, dan mengirimkan data ke sistem tujuan."
      ),
     ("Apa itu Data Warehouse dan Data Lake?",
      "Data Warehouse adalah tempat penyimpanan data terstruktur yang dioptimalkan untuk analisis, sedangkan Data Lake menyimpan data dalam format mentah dan tidak terstruktur."
      ),
     ("Apa itu Apache Spark dan Hadoop?",
      "Apache Spark dan Hadoop adalah framework open-source yang digunakan untuk pemrosesan data dalam skala besar."
      ),
     ("Apa roadmap untuk menjadi Data Analyst?",
      "Roadmap Data Analyst mencakup belajar SQL, Excel, statistik, visualisasi data, dan tools BI seperti Tableau atau Power BI."
      ),
     ("Apa roadmap untuk menjadi Data Scientist?",
      "Roadmap Data Scientist mencakup belajar statistik, machine learning, Python/R, big data, dan deep learning."
      ),
     ("Apa roadmap untuk menjadi Data Engineer?",
      "Roadmap Data Engineer mencakup belajar SQL, database, pipeline data, cloud computing, dan framework big data seperti Hadoop dan Spark."
      )],
    "Cloud":
    [("Apa itu Cloud Computing?",
      "Cloud Computing adalah model komputasi yang memungkinkan akses ke sumber daya IT melalui internet tanpa memerlukan infrastruktur fisik sendiri."
      ),
     ("Apa manfaat Cloud Computing?",
      "Manfaat Cloud Computing meliputi skalabilitas, efisiensi biaya, fleksibilitas, serta kemudahan akses dan pengelolaan sumber daya IT."
      ),
     ("Apa perbedaan Cloud Computing dan On-Premise?",
      "Cloud Computing menggunakan layanan berbasis internet, sedangkan On-Premise mengharuskan perusahaan memiliki dan mengelola infrastruktur sendiri."
      ),
     ("Apa itu Virtual Machine (VM) dalam Cloud?",
      "VM adalah mesin virtual yang berjalan di atas infrastruktur cloud dan memungkinkan pengguna menjalankan sistem operasi dan aplikasi secara fleksibel."
      ),
     ("Apa itu Container dalam Cloud Computing?",
      "Container adalah teknologi yang memungkinkan aplikasi berjalan dalam lingkungan yang terisolasi dan ringan dibandingkan VM."
      ),
     ("Apa itu Serverless Computing?",
      "Serverless Computing adalah model komputasi cloud di mana pengembang dapat menjalankan kode tanpa harus mengelola server secara langsung."
      ),
     ("Apa itu IaaS (Infrastructure as a Service)?",
      "IaaS adalah model layanan cloud yang menyediakan infrastruktur IT seperti server, storage, dan jaringan secara on-demand."
      ),
     ("Apa itu PaaS (Platform as a Service)?",
      "PaaS adalah model layanan cloud yang menyediakan platform pengembangan aplikasi tanpa perlu mengelola infrastruktur."
      ),
     ("Apa itu SaaS (Software as a Service)?",
      "SaaS adalah layanan cloud yang menyediakan perangkat lunak siap pakai yang dapat diakses melalui internet."
      ),
     ("Apa roadmap untuk menjadi Cloud Engineer?",
      "Roadmap Cloud Engineer mencakup belajar dasar networking, sistem operasi, cloud platforms (AWS, Azure, GCP), automation, dan security."
      )],
    "DevOps":
    [("Apa itu DevOps?",
      "DevOps adalah praktik yang mengintegrasikan pengembangan perangkat lunak (Development) dan operasional (Operations) untuk meningkatkan efisiensi dan kecepatan dalam siklus pengembangan perangkat lunak."
      ),
     ("Apa tujuan utama dari DevOps?",
      "Tujuan utama DevOps adalah mempercepat pengiriman perangkat lunak dengan kualitas tinggi melalui otomatisasi, kolaborasi, dan integrasi yang lebih baik."
      ),
     ("Apa manfaat DevOps bagi perusahaan?",
      "DevOps membantu perusahaan meningkatkan efisiensi, mengurangi kesalahan dalam deployment, dan mempercepat inovasi dengan siklus pengembangan yang lebih cepat."
      ),
     ("Apa perbedaan DevOps dan SysAdmin?",
      "SysAdmin berfokus pada pengelolaan infrastruktur dan server, sedangkan DevOps mencakup pengembangan, otomatisasi, dan operasional untuk mempercepat delivery aplikasi."
      ),
     ("Apa itu CI/CD dalam DevOps?",
      "CI/CD (Continuous Integration/Continuous Deployment) adalah praktik DevOps untuk mengotomatisasi build, testing, dan deployment aplikasi."
      ),
     ("Apa itu Containerization dalam DevOps?",
      "Containerization adalah metode untuk menjalankan aplikasi dalam lingkungan terisolasi menggunakan teknologi seperti Docker."
      ),
     ("Apa roadmap untuk menjadi DevOps Engineer?",
      "Roadmap DevOps Engineer mencakup belajar Linux, scripting, cloud computing, CI/CD, Infrastructure as Code, dan security."
      ),
     ("Apa itu Kubernetes?",
      "Kubernetes adalah sistem orkestrasi container untuk mengelola aplikasi berbasis container dalam skala besar."
      ),
     ("Apa itu Terraform?",
      "Terraform adalah alat Infrastructure as Code (IaC) yang memungkinkan otomatisasi pembuatan dan pengelolaan infrastruktur cloud."
      )]
}

# Dictionary untuk menyimpan status pengguna
user_state = {}

# ✅ Debugging: Print daftar topik untuk memastikan semuanya benar
print("🔹 Available topics:", list(qa_data.keys()))


# 🔥 Handle command /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Halo! Saya TechMateBot. Pilih topik yang ingin kamu pelajari:\n\n"
        "👉 *Data*\n👉 *Cloud*\n👉 *DevOps*\n\n"
        "Ketik nama topiknya untuk melihat daftar pertanyaan.",
        parse_mode="Markdown")


# 🔥 Handle pemilihan topik
@bot.message_handler(func=lambda message: message.text.strip().lower() in
                     [t.lower() for t in qa_data])
def choose_topic(message):
    topic_input = message.text.strip().lower()

    # Mencari topik yang cocok dari dictionary
    matched_topic = next((t for t in qa_data if t.lower() == topic_input),
                         None)

    if matched_topic:
        user_state[message.chat.id] = {
            "topic": matched_topic
        }  # Simpan topik yang dipilih user

        # Menampilkan daftar pertanyaan
        questions = "\n".join(f"{i+1}. {q[0]}"
                              for i, q in enumerate(qa_data[matched_topic]))
        bot.reply_to(
            message,
            f"Kamu memilih topik *{matched_topic}*. Pilih pertanyaan yang ingin kamu tanyakan dengan mengetik angkanya:\n\n{questions}",
            parse_mode="Markdown")
    else:
        bot.reply_to(
            message,
            "Maaf, topik tidak ditemukan. Coba ketik 'Data', 'Cloud', atau 'DevOps'."
        )


# 🔥 Handle pemilihan pertanyaan dengan angka
@bot.message_handler(func=lambda message: message.chat.id in user_state)
def answer_question(message):
    user_id = message.chat.id
    state = user_state[user_id]  # Ambil status user
    topic = state["topic"]

    if message.text.isdigit():  # Cek apakah input adalah angka
        question_index = int(message.text) - 1  # Konversi input ke index
        if 0 <= question_index < len(qa_data[topic]):
            question, answer = qa_data[topic][question_index]
            bot.reply_to(message,
                         f"*{question}*\n\n{answer}",
                         parse_mode="Markdown")
        else:
            bot.reply_to(
                message,
                "Nomor yang kamu pilih tidak valid. Pilih angka yang tersedia di daftar."
            )
    else:
        bot.reply_to(
            message,
            "Ketik angka yang sesuai dengan pertanyaan yang ingin kamu tanyakan."
        )


# ✅ Debugging: Print pesan untuk memastikan bot berjalan
print("🤖 Bot sedang berjalan...")

# 🔥 Menjalankan bot
bot.polling(none_stop=True)
