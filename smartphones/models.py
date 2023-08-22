from django.db import models
from collections import defaultdict


DISPLAY_ATTRIBUTE_TITLES = {
    "screen_size": "Screen Size",
    "screen_type": "Screen Type",
    "screen_resolution": "Screen Resolution",
    "screen_refresh_rate": "Screen Refresh Rate",
    "screen_size": "Screen Size",
}


CONNECTION_ATTRIBUTE_TITLES = {
    "sim_card_number": "Number of Sim Cards",
    "sim_card_size": "Sim-Card Size",
    "is_e_sim_supported": "E-Sim Support",
}


OPERATING_SYSTEM_TITLES = {
    "operating_system": "Operating System",
}


class Smartphone(models.Model):
    product = models.OneToOneField("products.Product", primary_key=True, on_delete=models.CASCADE)

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
    is_flash_available = models.BooleanField()
    video_resolution = models.CharField(max_length=255)

    # Battery
    battery_life = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.display_name}"

    @property
    def display_name(self):
        return f"{self.product.name} {self.product.color.name} {self.memory} ({self.product.sku})"

    def get_attributes_data(self):
        attributes = defaultdict(list)

        for attr in self.__dict__.keys():
            if attr in DISPLAY_ATTRIBUTE_TITLES:
                attributes["Display"].append(
                    {
                        "value": getattr(self, attr),
                        "title": DISPLAY_ATTRIBUTE_TITLES[attr]
                    }
                )
            elif attr in CONNECTION_ATTRIBUTE_TITLES:
                attributes["Connection"].append(
                    {
                        "value": getattr(self, attr),
                        "title": CONNECTION_ATTRIBUTE_TITLES[attr]
                    }
                )
            elif attr in OPERATING_SYSTEM_TITLES:
                attributes["Operating System"].append(
                    {
                        "value": getattr(self, attr),
                        "title": OPERATING_SYSTEM_TITLES[attr]
                    }
                )

        return attributes

    def get_highlighted_attributes_data(self):
        pass