from django.db import models

# Create your models here.

# class grades(models.Model):
#     classrooms = models.ManyToManyField("Classroom", related_name='students', blank=True)
    
#     class Meta:
#         verbose_name = _("student")
#         verbose_name_plural = _("students")
#         unique_together = ('roll_no', 'current_class')

#     def __str__(self):
#         return self.user.username

#     def get_absolute_url(self):
#         return reverse("Student_detail", kwargs={"pk": self.pk})