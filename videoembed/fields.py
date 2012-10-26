from django.db.models import fields
from django.core.exceptions import ValidationError

from videoembed.registry import wrappers


def validate_video(value):
    for w in wrappers.get_all():
        if w.match_url(value):
            return
    raise ValidationError(u'%s is not valid video url!' % value)


class VideoField(fields.URLField):

    def __init__(self, *args, **kwargs):
        super(VideoField, self).__init__(*args, **kwargs)
        self.validators.append(validate_video)

