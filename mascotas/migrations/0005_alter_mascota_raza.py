# Generated by Django 5.1.3 on 2024-12-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0004_mascota_castrado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(choices=[('Airedale Terrier', 'Airedale Terrier'), ('Akita Inu', 'Akita Inu'), ('Alaskan Malamute', 'Alaskan Malamute'), ('American Bully', 'American Bully'), ('American Pit Bull Terrier', 'American Pit Bull Terrier'), ('American Staffordshire Terrier', 'American Staffordshire Terrier'), ('Australian Cattle Dog', 'Australian Cattle Dog'), ('Australian Shepherd', 'Australian Shepherd'), ('Basset Hound', 'Basset Hound'), ('Beagle', 'Beagle'), ('Belgian Malinois', 'Belgian Malinois'), ('Bernese Mountain Dog', 'Bernese Mountain Dog'), ('Bichón Frisé', 'Bichón Frisé'), ('Bloodhound', 'Bloodhound'), ('Border Collie', 'Border Collie'), ('Boston Terrier', 'Boston Terrier'), ('Boxer', 'Boxer'), ('Bulldog Francés', 'Bulldog Francés'), ('Bulldog Inglés', 'Bulldog Inglés'), ('Bullmastiff', 'Bullmastiff'), ('Cane Corso', 'Cane Corso'), ('Caniche (Poodle)', 'Caniche (Poodle)'), ('Cavalier King Charles Spaniel', 'Cavalier King Charles Spaniel'), ('Chihuahua', 'Chihuahua'), ('Chow Chow', 'Chow Chow'), ('Cocker Spaniel', 'Cocker Spaniel'), ('Collie', 'Collie'), ('Dálmata', 'Dálmata'), ('Dóberman', 'Dóberman'), ('Dogo Argentino', 'Dogo Argentino'), ('Dogo de Burdeos', 'Dogo de Burdeos'), ('Galgo Español', 'Galgo Español'), ('Golden Retriever', 'Golden Retriever'), ('Gran Danés', 'Gran Danés'), ('Husky Siberiano', 'Husky Siberiano'), ('Jack Russell Terrier', 'Jack Russell Terrier'), ('Labrador Retriever', 'Labrador Retriever'), ('Maltés', 'Maltés'), ('Mastín Español', 'Mastín Español'), ('Mastín Napolitano', 'Mastín Napolitano'), ('Pastor Alemán', 'Pastor Alemán'), ('Pastor Australiano', 'Pastor Australiano'), ('Pekinés', 'Pekinés'), ('Pembroke Welsh Corgi', 'Pembroke Welsh Corgi'), ('Pinscher Miniatura', 'Pinscher Miniatura'), ('Pit Bull Terrier', 'Pit Bull Terrier'), ('Pomerania', 'Pomerania'), ('Pug', 'Pug'), ('Rottweiler', 'Rottweiler'), ('Samoyedo', 'Samoyedo'), ('San Bernardo', 'San Bernardo'), ('Scottish Terrier', 'Scottish Terrier'), ('Setter Irlandés', 'Setter Irlandés'), ('Shiba Inu', 'Shiba Inu'), ('Shih Tzu', 'Shih Tzu'), ('Schnauzer', 'Schnauzer'), ('Staffordshire Bull Terrier', 'Staffordshire Bull Terrier'), ('Teckel (Dachshund)', 'Teckel (Dachshund)'), ('Terranova', 'Terranova'), ('Weimaraner', 'Weimaraner'), ('West Highland White Terrier', 'West Highland White Terrier'), ('Whippet', 'Whippet'), ('Yorkshire Terrier', 'Yorkshire Terrier'), ('Mestizo', 'Mestizo')], default='Otra', max_length=50),
        ),
    ]
