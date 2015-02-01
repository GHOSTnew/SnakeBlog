from django.shortcuts import render_to_response
from SnakeBlog.utils.git import GITREVISION
from SnakeBlog.settings import VERSION
from blog.models import Page


def custom_render(template, args=dict()):
    args['git_revision'] = GITREVISION
    args['version'] = VERSION
    args['Pages'] = Page.objects.all()
    return render_to_response(template, args)
