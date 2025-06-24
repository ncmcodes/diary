from django.db import models


class Diary(models.Model):
    entry = models.TextField()
    created = models.DateField(auto_now_add=True, unique=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Diaries"

    def __str__(self):
        return f"{self.created}"


class Tags(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return f"{self.name}"


class DiaryTags(models.Model):
    diary_id = models.ForeignKey(Diary, on_delete=models.PROTECT)
    tag_id = models.ForeignKey(Tags, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Diary Tags"
        unique_together = ("diary_id", "tag_id")

    def __str__(self):
        return f"{self.diary_id} | {self.tag_id}"
