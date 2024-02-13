from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    class Meta:
        ordering = ["pub_date"]
        verbose_name_plural = "Questions"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ["-votes"]
        verbose_name_plural = "Choices"

    @property
    def choices(self):
        return f"{self.question} : {self.choice_text} : {self.votes}"

    def save(self, *args, **kwargs):
        """Do something here."""
        super().save(*args, **kwargs)  # Call the "real" save() method.
        """Do something else here."""

# s
# class CommonInfo(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()
#
#     class Meta:
#         ordering = ["-name"]
#         abstract = True
#
#
# class Student(CommonInfo):
#     home_group = models.CharField(max_length=5)
#     customers = models.ManyToManyField(CommonInfo)


class Base(models.Model):
    m2m = models.ManyToManyField(
        Choice,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        abstract = True


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=300)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)


class PersonQuerySet(models.QuerySet):
    def authors(self):
        return self.filter(role="A")

    def editors(self):
        return self.filter(role="E")


class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def authors(self):
        return self.get_queryset().authors()

    def editors(self):
        return self.get_queryset().editors()


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # role = models.CharField(max_length=1, choices={"A": _("Author"), "E": _("Editor")})
    people = PersonManager()
