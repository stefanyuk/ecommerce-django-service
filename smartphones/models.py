from django.db import models
from collections import defaultdict


DISPLAY_ATTRIBUTE_LABELS = {
    "screen_size": "Screen Size",
    "screen_type": "Screen Type",
    "screen_resolution": "Screen Resolution",
    "screen_refresh_rate": "Screen Refresh Rate",
    "screen_size": "Screen Size",
}


CONNECTION_ATTRIBUTE_LABELS = {
    "sim_card_number": "Number of Sim Cards",
    "sim_card_size": "Sim-Card Size",
    "is_e_sim_supported": "E-Sim Support",
}


OPERATING_SYSTEM_LABELS = {
    "operating_system": "Operating System",
}


class Smartphone(models.Model):
    product = models.OneToOneField("products.Product", primary_key=True, on_delete=models.CASCADE)
    
    attribute_titles = models.JSONField()
    attribute_labels = models.JSONField()

    # Screen attributes
    screen_size = models.DecimalField(max_digits=5, decimal_places=2)
    screen_type = models.CharField(max_length=255)
    screen_resolution = models.CharField(max_length=255)
    screen_refresh_rate = models.CharField(max_length=255)

    # Connection attributes
    sim_card_number = models.PositiveIntegerField()
    sim_card_size = models.CharField(max_length=255)
    is_e_sim_supported = models.BooleanField()

    # Operating system
    operating_system = models.CharField(max_length=255)

    # Processor
    processor = models.CharField(max_length=255)
    number_of_cores = models.PositiveIntegerField()

    # Memory
    memory = models.CharField(max_length=255)

    # Camera
    main_camera = models.CharField(max_length=255)
    front_camera = models.CharField(max_length=255)
    is_flash_available = models.CharField(max_length=255)
    video_resolution = models.CharField(max_length=255)

    # Battery
    battery_life = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product.name} ({self.product.sku})"

    @property
    def display_name(self):
        return f"{self.product.name} {self.product.color.name} {self.memory} ({self.product.sku})"

    def get_attributes_data(self):
        pass
