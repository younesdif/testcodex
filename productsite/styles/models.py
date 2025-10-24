"""Database models for the styles application."""

from django.db import models


class SupStyle(models.Model):
    """Represents a higher-level style grouping."""

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Supstyle"
        verbose_name_plural = "Supstyles"

    def __str__(self) -> str:
        return self.name


class Style(models.Model):
    """Represents a product style."""

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    supstyles = models.ManyToManyField(
        SupStyle, related_name="styles", blank=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Style"
        verbose_name_plural = "Styles"

    def __str__(self) -> str:
        return self.name
