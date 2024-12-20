import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from imblearn.over_sampling import SMOTE


# Read the CSV file
df = pd.read_csv('Prediksi motivasi belajar mahasiswa (Responses) - Form responses 1 (2).csv')

# Clean column names
df.columns = df.columns.str.strip()

# Data preprocessing
def categorize_motivation(row):
    # Categorize motivation based on the last column
    motivation_status = row['Apakah anda merasa termotivasi untuk melakukan yang terbaik di bidang akademik?']
    if motivation_status == 'Ya':
        return 'Termotivasi'
    else:
        return 'Tidak Termotivasi'

df['Motivation_Category'] = df.apply(categorize_motivation, axis=1)

# Convert study hours to numeric
study_hours_map = {
    '< 1 jam': 0.5,
    '1-2 jam': 1.5,
    '3-4 jam': 3.5,
    '> 4 jam': 5
}
df['Study_Hours_Numeric'] = df['Berapa jam per hari Anda alokasikan untuk belajar di luar jam kuliah?'].map(study_hours_map)

# Convert categorical columns to numeric
df['Time_Management_Numeric'] = pd.to_numeric(df['Seberapa teratur Anda dalam membuat jadwal harian atau mingguan untuk kegiatan akademik dan non-akademik?'])
df['Procrastination_Numeric'] = df['Apakah Anda sering menunda-nunda tugas kuliah?'].map({
    'Tidak pernah': 1, 
    'Kadang-kadang': 2, 
    'Ya, sangat sering': 3
})

# Data dan label (X = fitur, y = target)
X = df[['Time_Management_Numeric', 'Procrastination_Numeric', 'Study_Hours_Numeric']]
y = df['Motivation_Category']

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)
# Model Decision Tree untuk klasifikasi
clf = DecisionTreeClassifier(max_depth=5, min_samples_split=4, min_samples_leaf=2, random_state=42)
clf.fit(X, y)

# Visualisasi Decision Tree
plt.figure(figsize=(12, 8))
tree.plot_tree(clf, feature_names=X.columns, class_names=clf.classes_, filled=True)
plt.title('Decision Tree untuk Klasifikasi Motivasi')
plt.show()
plt.savefig('Decision tree hasil.png')
plt.close()

# 1. Decision Tree-like Visualization
plt.figure(figsize=(12, 6))
sns.violinplot(x='Motivation_Category', y='Study_Hours_Numeric', 
               hue='Apakah Anda sering menunda-nunda tugas kuliah?', 
               split=True, data=df)
plt.title('Hubungan Jam Belajar, Prokrastinasi, dan Motivasi')
plt.xlabel('Kategori Motivasi')
plt.ylabel('Jam Belajar')
plt.tight_layout()
plt.savefig('motivation_decision_tree.png')
plt.close()

# 2. Countplot of Part-time Job
plt.figure(figsize=(10, 6))
sns.countplot(x='Motivation_Category', hue='Apakah Anda bekerja paruh waktu?', data=df)
plt.title('Keterlibatan Kerja Paruh Waktu berdasarkan Kategori Motivasi')
plt.xlabel('Kategori Motivasi')
plt.ylabel('Jumlah')
plt.tight_layout()
plt.savefig('part_time_job_count.png')
plt.close()

# 3. Stacked Barplot of Motivation by Age and Program
motivation_by_age_program = df.groupby(['Usia', 'Program Studi'])['Motivation_Category'].value_counts(normalize=True).unstack()
plt.figure(figsize=(12, 6))
motivation_by_age_program.plot(kind='bar', stacked=True)
plt.title('Proporsi Motivasi berdasa    rkan Usia dan Program Studi')
plt.xlabel('Usia dan Program Studi')
plt.ylabel('Proporsi')
plt.legend(title='Motivasi', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('motivation_age_program_stacked.png')
plt.close()

# 4. Bar Plot of Study Hours by Motivation
plt.figure(figsize=(10, 6))
sns.barplot(x='Berapa jam per hari Anda alokasikan untuk belajar di luar jam kuliah?', 
            y='Motivation_Category', 
            data=df, 
            order=['> 4 jam', '3-4 jam', '1-2 jam', '< 1 jam'])
plt.title('Jam Belajar berdasarkan Status Motivasi')
plt.xlabel('Jam Belajar per Hari')
plt.ylabel('Status Motivasi')
plt.tight_layout()
plt.savefig('study_hours_by_motivation.png')
plt.close()

# 5. Count Plot of Motivation by Program Studi
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Program Studi', hue='Motivation_Category')
plt.title('Status Motivasi berdasarkan Program Studi')
plt.xlabel('Program Studi')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('motivation_by_program.png')
plt.close()

# 6. Line Plot of Motivation by Program Studi
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, 
             x='Time_Management_Numeric',
             y='Study_Hours_Numeric',
             hue='Motivation_Category')
plt.title('Hubungan Manajemen Waktu dan Jam Belajar')
plt.xlabel('Keteraturan Manajemen Waktu')
plt.ylabel('Jam Belajar per Hari')
plt.tight_layout()
plt.savefig('time_management_study_hours_line.png')
plt.close()


print("Semua visualisasi telah disimpan dalam direktori saat ini.")