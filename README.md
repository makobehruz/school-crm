# Maktab CRM

Bu loyiha maktablarni boshqarish tizimi uchun yaratilgan. Tizim maktabdagi o'quvchilar, o'qituvchilar, guruhlar va fanlarni boshqarishni osonlashtirish uchun ishlab chiqilgan.

## Loyihaning imkoniyatlari

1. **Asosiy boshqaruv paneli**:
   - O'quvchilar sonini ko'rish.
   - O'qituvchilar sonini ko'rish.
   - Guruhlar va fanlar statistikasi.

2. **O'quvchilarni boshqarish**:
   - Yangi o'quvchi qo'shish.
   - O'quvchi ma'lumotlarini yangilash yoki o'chirish.
   
3. **O'qituvchilarni boshqarish**:
   - O'qituvchilar ro'yxati bilan ishlash.
   - Yangi o'qituvchi qo'shish.
   
4. **Guruhlar va fanlar**:
   - Guruhlarni yaratish va boshqarish.
   - Fanlar ro'yxatini yaratish va boshqarish.

---

## O'rnatish

Loyihani ishga tushirish uchun quyidagi amallarni bajaring:

1. **Kodni yuklab oling:**
   ```bash
   git clone https://github.com/your-repository/maktab-crm.git
   ```

2. **Talab qilinadigan kutubxonalarni o'rnating:**
   Loyihaning asosiy kutubxonalarini o'rnatish uchun quyidagi buyruqni bajaring:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ma'lumotlar bazasini sozlang:**
   Ma'lumotlar bazasi uchun kerakli migratsiyalarni bajaring:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Ishga tushirish:**
   Dastur localhostda ishga tushishi uchun quyidagi buyruqni bajaring:
   ```bash
   python manage.py runserver
   ```

5. **Tizimga kirish:**
   Brauzerda `http://127.0.0.1:8000` manziliga o'ting.

---

## Foydalanish

1. **Admin panel:**
   - Dasturga kirgandan so'ng asosiy boshqaruv panelidan kerakli ma'lumotlarni ko'rish va boshqarish mumkin.
   
2. **O'quvchilarni yaratish:**
   - "O'quvchilar" bo'limiga o'ting va "Yangi o'quvchi yaratish" tugmasini bosing.
   - Forma orqali o'quvchi haqida ma'lumotlarni kiriting.

3. **Ma'lumotlarni yangilash yoki o'chirish:**
   - Har bir bo'limda tegishli yozuvlarni tahrirlash yoki o'chirish imkoniyati mavjud.

---

## Texnologiyalar

- Backend: Python (Django)
- Frontend: HTML, CSS, Bootstrap
- Ma'lumotlar bazasi: SQLite (yoki boshqa DBMS)

---

## Hissa qo'shish

Biz har qanday hissa qo'shishni mamnuniyat bilan qabul qilamiz! Quyida qanday hissa qo'shishingiz mumkinligi haqida ma'lumot berilgan:

1. **Xatoliklarni xabar qiling:**
   Agar siz tizimda xatolik topsangiz, [Issues bo'limida](https://github.com/your-repository/maktab-crm/issues) xabar qoldiring.

2. **Fikr-mulohazalar bering:**
   Yangi funksiyalar taklif qiling yoki mavjud imkoniyatlarni yaxshilash bo'yicha o'z fikrlaringizni bildiring.

3. **Kodga hissa qo'shing:**
   1. Loyihani fork qiling.
   2. Yangi branch yarating:
      ```bash
      git checkout -b yangi-branch-nomi
      ```
   3. O'zgartirishlarni kiriting va commit qiling:
      ```bash
      git commit -m "O'zgartirish tavsifi"
      ```
   4. Branchni push qiling:
      ```bash
      git push origin yangi-branch-nomi
      ```
   5. Pull request yarating.

4. **Hujjatlarni yangilang:**
   Agar README yoki boshqa hujjatlar uchun yaxshilash takliflaringiz bo'lsa, ularni ham qo'shing.

---


