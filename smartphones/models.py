from django.db import models


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
    is_flash_available = models.CharField(max_length=255)
    video_resolution = models.CharField(max_length=255)

    # Battery
    battery_life = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product.name} ({self.product.sku})"
