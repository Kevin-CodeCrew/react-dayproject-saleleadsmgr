from django.db import models

# A simple User model for organizaing access to Sales Leads
class UserModel(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

    # Provide a verbose name for convenience
    class Meta:
        verbose_name_plural = "App Users"

# Override default toString method
    def __str__(self):
        return self.username

# The data model for the Company a lead belongs to
class CompanyModel(models.Model):
    name = models.CharField(max_length=200)

    # Provide a verbose name for convenience
    class Meta:
        verbose_name_plural = "Companies"

    # Override default toString method
    def __str__(self):
        return self.name

# The data model for a Sales Lead
class SalesLeadModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    userFk = models.ForeignKey(
        UserModel, related_name="leads", on_delete=models.CASCADE, null=True)
    companyFk = models.ForeignKey(
        CompanyModel, related_name="companies", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Provide a verbose name for convenience
    class Meta:
        verbose_name_plural = "Sales Contacts"

    # Override default toString method
    def __str__(self):
        return self.name
