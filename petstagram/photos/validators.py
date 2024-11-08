# from django.core.exceptions import ValidationError
#
#
# def validate_photo_size(value):
#     if value.size > 5 * 1024 * 1024:
#         raise ValidationError('The size of the photo is too big')
#
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PhotoValidator:
    MAX_PHOTO_SIZE = 5

    def __init__(self, photo_size=None):
        self.mb_photo_size = photo_size or self.MAX_PHOTO_SIZE
        self.max_photo_bytes = self.mb_photo_size * 1024 * 1024

    def __call__(self, value):
        if value > self.max_photo_bytes:
            raise ValidationError(f"The file must be below or equal to {self.mb_photo_size} MB.")


