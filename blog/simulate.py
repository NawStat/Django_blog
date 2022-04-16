from random import choice
from string import ascii_letters
import datetime
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Post 

for i in range(10):
    title = ''.join(choice(ascii_letters) for i in range(12))
    tilte = 'title_' + title
    slug = 'slug-simulated' + ''.join(choice(ascii_letters) for i in range(12))
    body = 'Body ' + ''.join(choice(ascii_letters) for i in range(12))
    # author ='publish' + ''.join(choice(ascii_letters) for i in range(12))
    # user = User.objects.create_user(author, 'lennon@thebeatles.com', 'johnpassword')
    # user.last_name = 'Lennon'
    # user.save()
    author = User.objects.get(username='Nawres')
    # status =  choice(['published', 'draft'])
    status = 'published'
    publish = timezone.now()
    created = timezone.now()
    updated = timezone.now()
    p = Post(body=body, title=title, slug=slug, author=author, status=status, publish=publish, created=created, updated=updated)
    p.save()


