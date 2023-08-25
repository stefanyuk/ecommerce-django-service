from django.db import models
from collections import defaultdict
from products.models import Product


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


class Smartphone(Product):
    product = models.OneToOneField(
        "products.Product",
        on_delete=models.CASCADE,
        parent_link=True,
        related_name="smartphone"
    )

    # Screen attributes
    screen_size = models.DecimalField(verbose_name="screen size", max_digits=5, decimal_places=2)
    screen_type = models.CharField(verbose_name="screen type", max_length=255)
    screen_resolution = models.CharField(verbose_name="screen resolution", max_length=255)
    screen_refresh_rate = models.CharField(verbose_name="screen refresh rate", max_length=255)
    screen_material = models.CharField(verbose_name="screen material", max_length=255)

    # Sim Card attributes
    sim_card_number = models.PositiveIntegerField(verbose_name="number of sim cards")
    sim_card_size = models.CharField(verbose_name="size of sim card", max_length=255)
    is_e_sim_supported = models.BooleanField(verbose_name="E-Sim support")

    # Operating system
    operating_system = models.CharField(verbose_name="operating system", max_length=255)

    # Processor
    processor = models.CharField(max_length=255)
    number_of_cores = models.PositiveIntegerField()

    # Communication standarts
    communication_standart = models.ManyToManyField(
        "CommunicationStandarts",
        related_name="smartphones",
        verbose_name="communication standarts"
    )

    # Memory
    internal_memory = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)

    # Main Camera
    main_camera = models.CharField(verbose_name="main camera", max_length=255)
    main_camera_features = models.ManyToManyField(
        "CameraFeatures",
        verbose_name="main camera features",
        related_name="smartphones_with_main_camera_feature"
    )
    number_of_main_cameras = models.PositiveIntegerField(verbose_name="number of main cameras")

    front_camera_features = models.ManyToManyField(
        "CameraFeatures",
        verbose_name="front camera features",
        related_name="smartphones_with_front_camera_feature"
    )
    front_camera = models.CharField(verbose_name="front camera", max_length=255)
    front_camera_placement = models.CharField(verbose_name="front camera placement", max_length=255)
    is_flash_available = models.BooleanField()

    # Battery
    battery_life_in_hours = models.PositiveIntegerField(verbose_name="battery life in hours")
    is_fast_charging_available = models.BooleanField(verbose_name="fast charging")
    is_wireless_charging_available = models.BooleanField(verbose_name="wireless charging")
    
    class Meta:
        db_table = 'smartphones'
        verbose_name = 'smartphone'
        verbose_name_plural = 'smartphones'

    def __str__(self):
        return f"{self.display_name}"

    @property
    def display_name(self):
        return f"{self.name} {self.color.name} {self.internal_memory} ({self.sku})"

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


class CommunicationStandarts(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        db_table = 'communication_standarts'
        verbose_name = 'communication standart'
        verbose_name_plural = 'communication standarts'
    
    def __str__(self):
        return f"{self.name}"


class CameraFeatures(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'camera_features'
        verbose_name = 'camera feature'
        verbose_name_plural = 'camera features'

    def __str__(self):
        return f"{self.name}"
