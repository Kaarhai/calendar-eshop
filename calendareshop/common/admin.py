from django.conf import settings


class ImageListAdmin(object):

    def thumb(self, obj):
        image = None
        if hasattr(obj, 'image'):
            image = obj.image
        elif hasattr(obj, 'images'):
            images = list(obj.images.all())
            if images:
                image = images[0].image

        if image:
            return "<img src=\"/resize/200/200%s%s\" />" % (settings.MEDIA_URL, image)
        else:
            return "No image"

    thumb.allow_tags = True

