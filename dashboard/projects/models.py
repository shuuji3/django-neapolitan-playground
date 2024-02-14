from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    has_tests = models.BooleanField()
    has_docs = models.BooleanField()

    NA = 'na'
    PLANNED = 'PL'
    STARTED = 'ST'
    FIRST_RESULTS = 'FR'
    MATURE_RESULTS = 'MR'
    DONE = 'DO'
    DEFERRED = 'DE'
    BLOCKED = 'BL'
    INACTIVE = 'IN'

    STATUS_CHOICES = [
        (PLANNED, 'Planned'),
        (STARTED, 'Started'),
        (FIRST_RESULTS, 'First Results'),
        (MATURE_RESULTS, 'Mature Results'),
        (DONE, 'Done'),
        (DEFERRED, 'Deferred'),
        (BLOCKED, 'Blocked'),
        (INACTIVE, 'Inactive'),
    ]

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
    )

    last_review = models.DateField(null=True, blank=True)

    def is_at_risk(self):
        return self.status in (self.BLOCKED, self.INACTIVE)

    def __str__(self):
        return self.name
