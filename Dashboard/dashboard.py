import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load data
def load_data():
    day_df = pd.read_csv("https://raw.githubusercontent.com/FahmaZuaf/bike_sharing_analysis/refs/heads/main/Dashboard/main_day.csv")

    # Drop columns
    drop_col = ['instant', 'windspeed']
    day_df.drop(labels=drop_col, axis=1, inplace=True)

    # Rename columns
    day_df.rename(columns={
        'dteday': 'dateday',
        'yr': 'year',
        'mnth': 'month',
        'weathersit': 'weather_cond',
        'cnt': 'count'
    }, inplace=True)

    # Convert date column to datetime
    day_df["dateday"] = pd.to_datetime(day_df.dateday)

    # Map values to descriptive labels
    day_df['season'] = day_df['season'].map({
        1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
    })
    day_df['month'] = day_df['dateday'].dt.month_name()
    day_df['year'] = day_df['dateday'].dt.year
    day_df['weekday'] = day_df['dateday'].dt.day_name()
    day_df['workingday'] = day_df['workingday'].map({
        0: 'Tidak', 1: 'Ya'
    })

    return day_df

# Load data
day_df = load_data()

# Streamlit Dashboard
st.title("Dashboard Bike Sharing")

# Sidebar with Logo, Social Media, and Copyright
st.sidebar.image("https://raw.githubusercontent.com/FahmaZuaf/bike_sharing_analysis/refs/heads/main/Images/logo bike share zuaf.png", use_column_width=True)  # Tambahkan logo dengan path yang sesuai

# Sidebar for filters
st.sidebar.header("Filter")
season_filter = st.sidebar.multiselect("Filter berdasarkan Musim", options=day_df['season'].unique(), default=day_df['season'].unique())
workingday_filter = st.sidebar.multiselect("Filter berdasarkan Hari Kerja", options=day_df['workingday'].unique(), default=day_df['workingday'].unique())
month_filter = st.sidebar.multiselect("Filter berdasarkan Bulan", options=day_df['month'].unique(), default=day_df['month'].unique())

filtered_df = day_df[
    (day_df['season'].isin(season_filter)) &
    (day_df['workingday'].isin(workingday_filter)) &
    (day_df['month'].isin(month_filter))
]

st.write("Data yang ditampilkan:", filtered_df.shape[0], "baris")

# Social media links
st.sidebar.write("**Follow Me on Social Media**")
st.sidebar.markdown("""
[![LinkedIn](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/fahmazuafzarir/)
[![Instagram](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAABRFBMVEVHcEz4D5n9oAf9lAftEKn7lBXhA8VwFf3TPJF3Fv39tgX9egV9GvnpA7b9OFx2GPn7SUH9KXX9UjH////+AWH+Arv+wQPkANL+ygD9BKv+AZP+A27+Mkj/9fP+AYj+XS3+aRj+AXr+cJn+7/ubEvz+YQHUANn+J3Z6FPyIFPv+jQL+Tg/CAd6rAuX/vMT/17P0Asn/ruj+sQD+G3/+Pj3+SjX+dhz/vOD0bt3+ugD+Kmb+dwThGun+PST/y8r+xG3+GpL/rMr9D57+hAKUBuv+LlX+ghX+GGT+Bkb+IVb/s9b+X8P+nwHtAL3+pwH+lgOxEPvGGPXfYeb/xLbzFtHzAKr+N1r/6OH+Kzb7GLf+clD+fIL2uPH+WqP93/f+0O/+Vmb+im/oSOH+LLf+nTT+ylv+qV39Qcj+znvSgfr+mYnWgvrfdhN0AAAAE3RSTlMAx8/PX13K/gnMxsZdzdJhXcrGWouHNAAAAjlJREFUKJFN0utXokAYwOFptzL31u6+mMtVEImC1UxADRYjvGtq5a2Laff28v9/33ewzun3YTiHB2YGzhBCyGY8Fovt7OzWarVsNvsT295eXyW0jXgku6+yTUsmk+sbiPEdSpkaleXtqF7vMyGfIspkT8+wMu1ulM/ne73eeJXEKWX+qPAmtZxPJMbjFYKSOZkBzGf7L83mAPsJlh2H5AT7B+pdMo9Pv/SsQpkNOY6cYircJUfUWErdxfM9qBzHSeQXBvPkKHHBsvfd7j3LLmARziGUJIXiGcx6SGGJbqbEdhddrgTXkqKQ0ShfxjthGKigdjo44GJcB64VnicXF2wXOpKllKAkSRy+U8LVjiDN8wwJgiANR7yug6hYViBJKgSSgsgg6nozDbl2GwdG1y1LiWakyDCkXheuIHdOh7br6jqPyDMvKAjnVzD07RsQhcnEdZsi6Mwr2r5P0fErUBGEehsvTLMVIU9837yFoZlKpUQQczkc6u12K7dE0zQvYU+TZTlVoT+hMhEEAfGG4RVialoRpppXLBbly9vbS8exbaE1BZeihonwUK02Gg10nN5xznF3rSYvEc3zvEMQH4yBYVSrnifLuI4I6VbT4ojsVQ1jD2C6t2w4rEwBP7zetALysWoMjo9/i2+PifjXt+uutULW0PqFQmHr8fEw6umpqJmOLbg6Ht33aAcHW1EHhUJ/YDRwW44w+UYP9bsCpR80yv1BAzft2F82ojO/9mFJS+0f01e/f0X4DzXfhmzQgNUBAAAAAElFTkSuQmCC)](https://www.instagram.com/fahma_zuaf_zarir/)
""")

# Copyright notice
st.sidebar.write("© 2024 Bike Sharing Dashboard by Fahma Zuaf Zarir")

# Plot: Jumlah penyewaan sepeda berdasarkan musim
st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Musim")
season_group = filtered_df.groupby('season')['count'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='count', data=season_group, palette='viridis', ax=ax)
ax.set_title("Jumlah Peminjaman Sepeda Berdasarkan Musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjaman Sepeda")

# Add data labels
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points')

st.pyplot(fig)

# Interpretasi
st.write("Dapat dilihat pada grafik diatas jumlah penyewa sepeda terbanyak berada di musim Fall yang jumlah penyewa sepeda sekitar 1.061.129 dan jumlah penyewa sepeda paling sedikit pada saat musim Spring mencapai angka 471.348.")

# Plot: Rata-rata kelembaban berdasarkan musim
st.subheader("Rata-rata Kelembaban Berdasarkan Musim")
humidity_group = filtered_df.groupby('season')['hum'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='hum', data=humidity_group, palette='plasma', ax=ax)
ax.set_title("Rata-rata Kelembaban Berdasarkan Musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Kelembaban (%)")

# Add data labels
for p in ax.patches:
    ax.annotate(f'{p.get_height():.3f}%', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points')

st.pyplot(fig)

# Interpretasi
st.write("Dapat dilihat barplot diatas, rata-rata kelembaban paling tinggi terjadi pada saat musim winter yang dimana kelembaban mencapai angka 0,669% sedangkan untuk kelembaban paling rendah terjadi pada saat musim Spring yang dimana kelembaban mencapai 0,583%.")

# Plot: Jumlah penyewaan sepeda pada hari kerja vs akhir pekan
st.subheader("Jumlah Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
day_type_group = filtered_df.groupby('workingday')['count'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='workingday', y='count', data=day_type_group, palette='coolwarm', ax=ax)
ax.set_title("Jumlah Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
ax.set_xlabel("Jenis Hari")
ax.set_ylabel("Jumlah Peminjaman Sepeda")

# Add data labels
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points')

st.pyplot(fig)

# Interpretasi
st.write("Dapat dilihat Barplot diatas dapat dijelaskan bahwa peminjaman sepeda paling banyak pada waktu kerja daripada non-hari kerja yang jumlahnya sekitar 2.292.410 dibandingkan dengan hari non-kerja yang berjumlah mencapai 1.000.269.")

# Plot: Distribusi jumlah sepeda yang dipinjam selama setahun
st.subheader("Distribusi Jumlah Sepeda yang Dipinjam Selama Setahun")
monthly_rentals = filtered_df.groupby(filtered_df['dateday'].dt.to_period("M"))['count'].sum()  # Assuming you want monthly data

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x=monthly_rentals.index.astype(str), y=monthly_rentals.values, marker="o", ax=ax)
ax.set_title("Distribusi Jumlah Sepeda yang Dipinjam Selama Setahun")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.tick_params(axis='x', rotation=45)

# Add data labels
for x, y in zip(monthly_rentals.index.astype(str), monthly_rentals.values):
    ax.text(x, y, f'{y}', color='black', ha='center', va='bottom')

st.pyplot(fig)

# Interpretasi 
st.write("Dapat dilihat lineplot tersebut, distribusi jumlah sepeda yang dipinjam selama setahun (2011-2012) paling banyak terjadi pada bulan Agustus yang mencapai angka 351.194 sedangkan distribusi jumlah sepeda yang dipinjam selama setahun (2011-2012) paling sedikit terjadi pada bulan January yang mencapai angka 134.933 selain itu juga pada bulan January sampai June terjadi peningkatan peminjaman sepeda selama 5 bulan dalam satu tahun.")
