# جنگو الستیک سرچ

این پروژه یک برنامه Django است که با Elasticsearch یکپارچه شده است. شما می‌توانید با استفاده از این پروژه داده‌ها را در Elasticsearch ذخیره کرده و جستجو کنید.

## نحوه اجرا

برای راه‌اندازی پروژه و اجرای آن در محیط Docker، مراحل زیر را دنبال کنید:

### پیش‌نیازها

- Docker
- Docker Compose

### مراحل اجرا

1. ابتدا Docker و Docker Compose را نصب کنید (اگر قبلاً نصب نکرده‌اید).
2. در دایرکتوری پروژه، دستور زیر را اجرا کنید تا Docker Compose کانتینرها را بسازد و اجرا کند:

    ```bash
    docker compose up --build
    ```

3. پس از اجرای موفق دستور بالا، پروژه به طور خودکار در محیط Docker شروع به کار خواهد کرد.

### دسترسی به پروژه

پس از راه‌اندازی موفق پروژه، می‌توانید به آن از طریق آدرس زیر دسترسی پیدا کنید:

- **Django Admin**: `http://localhost:8000/admin/`
- **API**: `http://localhost:8000/swagger/`

### نحوه استفاده

- برای استفاده از Elasticsearch، می‌توانید از APIهای مختلف برای جستجو و مدیریت داده‌ها استفاده کنید.
- برای وارد کردن داده‌ها به Elasticsearch، می‌توانید از فایل‌های CSV استفاده کرده و آن‌ها را از طریق API ارسال کنید.

### نکات

- تمامی پیکربندی‌ها در فایل‌های مربوط به Docker و Django قرار دارد.
- این پروژه با استفاده از Elasticsearch به منظور جستجو در داده‌ها طراحی شده است.

## تکنولوژی‌ها

- Django
- Elasticsearch
- Docker
- Docker Compose

## نویسندگان

- [Amir Hossein](https://github.com/AMIRJA2002)

