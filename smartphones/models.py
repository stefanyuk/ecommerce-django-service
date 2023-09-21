from django.db import models
from django.db.models.query import QuerySet
from products.models import Product


BATTERY_COLUMN_NAMES = {
    "battery_life_in_hours",
    "is_fast_charging_available",
    "is_wireless_charging_available",
}

FRONT_CAMERA_COLUMN_NAMES = {
    "front_camera",
    "front_camera_placement",
    "front_camera_features",
}

MAIN_CAMERA_COLUMN_NAMES = {
    "main_camera",
    "main_camera_features",
    "number_of_main_cameras",
    "is_flash_available"
}

MEMORY_COLUMN_NAMES = {"internal_memory", "ram"}

PROCESSOR_COLUMN_NAMES = {"processor", "number_of_cores"}

OPERATING_SYSTEM_NAMES = {"operating_system",}

SCREEN_COLUMN_NAMES = {
    "screen_size",
    "screen_type",
    "screen_resolution",
    "screen_refresh_rate",
    "screen_material",
}

MAIN_ATTR_COLUMN_NAMES = {"color", "released_on"}

SIM_CARD_COLUMN_NAMES = {
    "sim_card_number",
    "sim_card_size",
    "is_e_sim_supported",
}

MEMORY_ATTR_LABEL = "Memory"
OPERATING_SYSTEM_ATTR_LABEL = "Operating System"
DISPLAY_ATTR_LABEL = "Display"
BATTERY_ATTR_LABEL = "Battery"
FRONT_CAMERA_LABEL = "Front Camera"
MAIN_CAMERA_LABEL = "Main Camera"


class SmartphoneManager(models.Manager):
    def get_color_variations_by_internal_memory(self, smartphone: "Smartphone") -> QuerySet["Smartphone"]:
        return self.filter(name=smartphone.name, internal_memory=smartphone.internal_memory).distinct("color")

    def get_internal_memory_variations_by_color(self, smartphone: "Smartphone") -> QuerySet["Smartphone"]:
        return self.filter(name=smartphone.name, color=smartphone.color).distinct("internal_memory")


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
    communication_standarts = models.ManyToManyField(
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

    # Front Camera
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

    objects = SmartphoneManager()

    class Meta:
        db_table = 'smartphones'
        verbose_name = 'smartphone'
        verbose_name_plural = 'smartphones'

    def __str__(self):
        return f"{self.display_name}"

    @property
    def display_name(self):
        return f"{self.name} {self.color.name} {self.internal_memory} ({self.sku})"

    def get_highlighted_attributes_data(self):
        pass

    def get_attributes_data(self):
        attributes = super().get_attributes_data()
        attributes += [
            self._get_memory_attributes_data(),
            self._get_main_camera_attributes_data(),
            self._get_front_camera_attributes_data(),
        ]
        return attributes

    def _get_front_camera_attributes_data(self) -> dict[str, list[str | list]]:
        front_camera_attributes = {FRONT_CAMERA_LABEL: []}

        for field in self._meta.get_fields():
            if field.column in FRONT_CAMERA_COLUMN_NAMES:
                if field.column == "front_camera_features":
                    value = [feature.name for feature in getattr(self, field.column).all()]
                else:
                    value = getattr(self, field.column)

                front_camera_attributes[FRONT_CAMERA_LABEL].append(
                    {
                        "value": value,
                        "title": self.get_field_title(field)
                    }
                )

        return front_camera_attributes

    def _get_main_camera_attributes_data(self):
        main_camera_attributes = {MAIN_CAMERA_LABEL: []}

        for field in self._meta.get_fields():
            if field.column in MAIN_CAMERA_COLUMN_NAMES:
                if field.column == "main_camera_features":
                    value = [feature.name for feature in getattr(self, field.column).all()]
                else:
                    value = getattr(self, field.column)

                main_camera_attributes[MAIN_CAMERA_LABEL].append(
                    {
                        "value": value,
                        "title": self.get_field_title(field)
                    }
                )

        return main_camera_attributes

    def _get_memory_attributes_data(self):
        memory_attributes = {MEMORY_ATTR_LABEL: []}

        for field in self._meta.get_fields():
            if field.column in MEMORY_COLUMN_NAMES:
                memory_attributes[MEMORY_ATTR_LABEL].append(
                    {
                        "value": getattr(self, field.column),
                        "title": self.get_field_title(field)
                    }
                )

        return memory_attributes


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
