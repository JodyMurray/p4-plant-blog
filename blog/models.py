from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from plantblog.validators import validate_text_length, validate_letters


STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        validators=[validate_letters]
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        validators=[validate_letters]
    )
    profile_pic = models.ImageField(
        upload_to='media',
        blank=True
    )
    bio = models.TextField(
        validators=[validate_text_length]
    )

    def __str__(self):
        return self.user.username

    @property
    def get_profile_pic(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/images/default2.jpeg"


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        blank=True
    )
    update_on = models.DateTimeField(
        auto_now=True
    )
    content = models.TextField()
    featured_image = CloudinaryField(
        'image',
        default='placeholder'
    )
    excerpt = models.TextField(
        blank=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    status = models.IntegerField(
        choices=STATUS,
        default=0
    )
    likes = models.ManyToManyField(
        User,
        related_name='blogpost_like',
        blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('add_post')


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    name = models.CharField(
        max_length=80,
    )
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    approved = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
