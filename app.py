import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Menampilkan judul di halaman web
st.title("Analisis Data Film IMDB")

# Membaca file CSV
file_path = 'top_picks_film.csv'
df = pd.read_csv(file_path, encoding='latin1')

# Menampilkan DataFrame sebagai tabel
st.dataframe(df)

# Sidebar untuk navigasi
st.sidebar.title("Dashboard Options")
option = st.sidebar.selectbox("Choose Aspect", 
                              ["Comparisson", 
                               "Relationship", 
                               "Composition", 
                               "Distribution"])

# Perbandingan: Anggaran vs Pendapatan Kotor
if option == "Comparisson":
    st.header("Dashboard - Comparisson")
    
    st.subheader("Graph 1: Top 10 Film berdasarkan Anggaran")
    top_10_anggaran = df.nlargest(10, 'Budget')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(top_10_anggaran['Title'], top_10_anggaran['Budget'], color='skyblue')
    ax.set_xlabel('Judul Film')
    ax.set_ylabel('Anggaran (dalam jutaan)')
    ax.set_title('Top 10 Film berdasarkan Anggaran')
    ax.set_xticklabels(top_10_anggaran['Title'], rotation=90)
    st.pyplot(fig)
    
    st.write("""
    **Analisa Grafik**

    Grafik ini membandingkan anggaran dari 10 film teratas dalam dataset. Film dengan anggaran tertinggi adalah judul film, dengan anggaran sekitar jumlah anggaran. Terlihat bahwa variasi anggaran antar film cukup signifikan, yang mengindikasikan bahwa beberapa film memiliki anggaran produksi yang jauh lebih besar dibandingkan yang lain. Hubungan antara anggaran produksi dengan pendapatan kotor film bisa dilihat lebih jelas dalam analisis ini.
    """)

    st.subheader("Graph 2: Top 10 Film berdasarkan Pendapatan Kotor")
    top_10_gross = df.nlargest(10, 'Gross_us')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(top_10_gross['Title'], top_10_gross['Gross_us'], color='orange')
    ax.set_xlabel('Judul Film')
    ax.set_ylabel('Pendapatan Kotor (dalam jutaan)')
    ax.set_title('Top 10 Film berdasarkan Pendapatan Kotor')
    ax.set_xticklabels(top_10_gross['Title'], rotation=90)
    st.pyplot(fig)
    
    st.write("""
    **Analisa Grafik**

    Grafik ini menampilkan 10 film teratas berdasarkan pendapatan kotor di AS. Dari grafik, kita dapat melihat film mana yang paling sukses dari segi pendapatan kotor. Film dengan pendapatan tertinggi adalah [judul film], yang berhasil meraup sekitar [jumlah pendapatan] juta dolar. Analisis ini penting untuk memahami daya tarik komersial dari film-film tertentu dan bagaimana strategi pemasaran dan distribusi mempengaruhi pendapatan mereka. Pendapatan kotor yang tinggi biasanya menunjukkan bahwa film tersebut memiliki penerimaan yang baik dari penonton dan mungkin juga didukung oleh kampanye pemasaran yang efektif serta rilis di waktu yang strategis.
    """)

# Hubungan: Anggaran vs Pendapatan Kotor
elif option == "Relationship":
    st.header("Dashboard - Relationship")
    
    st.subheader("Graph 1: Hubungan antara Anggaran dan Pendapatan Kotor (di AS)")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Budget'], df['Gross_us'], color='green')
    ax.set_xlabel('Anggaran (dalam jutaan)')
    ax.set_ylabel('Pendapatan Kotor (di AS) (dalam jutaan)')
    ax.set_title('Hubungan antara Anggaran dan Pendapatan Kotor (di AS)')
    st.pyplot(fig)
    
    st.write("""
    **Analisa Grafik**

    Scatter plot ini mengilustrasikan hubungan antara anggaran produksi film dengan pendapatan kotor yang dihasilkan. Terlihat dari grafik bahwa tidak selalu film dengan anggaran tinggi menghasilkan pendapatan kotor yang besar. Namun demikian, ada kecenderungan bahwa film dengan anggaran lebih tinggi cenderung memiliki pendapatan kotor yang lebih besar, meskipun terdapat beberapa outlier yang menunjukkan film dengan anggaran rendah namun memperoleh pendapatan kotor tinggi.
    """)

    st.subheader("Graph 2: Hubungan antara Pendapatan Minggu Pertama dan Pendapatan Kotor (di AS)")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Opening_week_rev'], df['Gross_us'], color='blue')
    ax.set_xlabel('Pendapatan Minggu Pertama (dalam jutaan)')
    ax.set_ylabel('Pendapatan Kotor (di AS) (dalam jutaan)')
    ax.set_title('Hubungan antara Pendapatan Minggu Pertama dan Pendapatan Kotor (di AS)')
    st.pyplot(fig)
    
    st.write("""
    **Analisa Grafik**

    Scatter plot ini menunjukkan hubungan antara pendapatan pada minggu pertama dengan pendapatan kotor total. Dari grafik ini, kita bisa mengamati bahwa film yang memiliki pendapatan tinggi pada minggu pertama cenderung memiliki pendapatan kotor yang tinggi juga. Hal ini menunjukkan pentingnya minggu pertama rilis film sebagai indikator kesuksesan jangka panjang. Film dengan pendapatan tinggi pada minggu pertama biasanya didukung oleh kampanye pemasaran yang besar dan perilisan di bioskop yang luas, yang menarik banyak penonton awal. Sebaliknya, film dengan pendapatan minggu pertama yang rendah mungkin menghadapi tantangan dalam mendapatkan perhatian penonton, yang dapat berdampak negatif pada pendapatan kotor total
    """)

# Komposisi: Pendapatan Minggu Pertama
elif option == "Composition":
    st.header("Dasboard - Composition")
    
    st.subheader("Graph 1: Komposisi Pendapatan Minggu Pertama untuk 5 Film Teratas")
    top_5_pendapatan_awal = df.nlargest(5, 'Opening_week_rev')
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(top_5_pendapatan_awal['Opening_week_rev'], labels=top_5_pendapatan_awal['Title'], autopct='%1.1f%%', startangle=140)
    ax.set_title('Komposisi Pendapatan Minggu Pertama untuk 5 Film Teratas')
    st.pyplot(fig)
    
    st.write("""
    **Analisa Grafik**

    Pie chart ini menunjukkan komposisi pendapatan dari minggu pertama untuk 5 film teratas dalam dataset. Film dengan pendapatan minggu pertama tertinggi adalah judul film, yang menyumbang sekitar [persentase] dari total pendapatan minggu pertama. Analisis ini menyoroti pentingnya performa film pada minggu pertama perilisannya dalam mendukung kesuksesan akhir film tersebut.
    """)

    st.subheader("Graph 2: Komposisi Genre Film")
    genre_counts = df['Genre'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title('Komposisi Genre Film')
    st.pyplot(fig)
    
    st.write("""
    **Analisa Grafik**

    Pie chart ini menggambarkan distribusi genre dari film-film dalam dataset. Dari grafik ini, kita dapat melihat genre film yang paling umum dan bagaimana distribusinya. Genre yang dominan mungkin mencerminkan tren industri film dan preferensi penonton pada periode tertentu. Misalnya, jika genre aksi dan petualangan mendominasi, ini bisa menunjukkan minat penonton yang tinggi terhadap film dengan elemen aksi dan petualangan. Sebaliknya, jika genre drama atau dokumenter memiliki persentase yang lebih kecil, ini bisa menunjukkan bahwa film dengan genre tersebut kurang populer atau diproduksi lebih sedikit. Memahami distribusi genre ini membantu produser dan pembuat film dalam membuat keputusan tentang genre apa yang akan diproduksi untuk menarik penonton.
    """)

# Distribusi: Pendapatan Kotor
elif option == "Distribution":
    st.header("Dashboard - Distribution")
    
    st.subheader("Graph 1: Distribusi Pendapatan Kotor")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['Gross_us'], bins=15, color='purple', edgecolor='black')
    ax.set_xlabel('Pendapatan Kotor (di AS) (dalam jutaan)')
    ax.set_ylabel('Jumlah Film')
    ax.set_title('Distribusi Pendapatan Kotor')
    st.pyplot(fig)
    
    st.write("""
    **Analisa Grafik**

    Histogram ini menggambarkan distribusi pendapatan kotor dari semua film dalam dataset. Distribusi tampaknya condong ke kanan, yang menunjukkan bahwa sebagian besar film dalam dataset memiliki pendapatan kotor yang relatif rendah, sedangkan hanya sedikit film yang mencatatkan pendapatan kotor yang sangat tinggi. Ini mencerminkan sifat industri film di mana sebagian besar film menghasilkan pendapatan moderat, sementara hanya sedikit film blockbuster yang mencatatkan pendapatan kotor yang signifikan.
    """)

    st.subheader("Graph 2: Distribusi Durasi Film")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['Runtime'], bins=15, color='red', edgecolor='black')
    ax.set_xlabel('Durasi Film (menit)')
    ax.set_ylabel('Jumlah Film')
    ax.set_title('Distribusi Durasi Film')
    st.pyplot(fig)
    
    st.write("""
    **Analisa Grafik**

    Histogram ini menunjukkan distribusi durasi film dalam dataset. Dari grafik ini, kita bisa melihat rentang durasi film yang paling umum. Kebanyakan film memiliki durasi antara rentang waktu menit, dengan hanya beberapa film yang berdurasi lebih pendek atau lebih panjang. Distribusi durasi ini memberikan wawasan tentang standar industri untuk panjang film. Film dengan durasi yang lebih umum mungkin lebih mudah diterima oleh penonton, sementara film dengan durasi yang sangat panjang atau sangat pendek mungkin menargetkan audiens yang lebih spesifik. Informasi ini berguna bagi produser film dalam menentukan durasi ideal untuk film mereka agar sesuai dengan ekspektasi dan kenyamanan penonton.
    """)
