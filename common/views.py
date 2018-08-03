from django.http import JsonResponse
import os
from django.conf import settings
import uuid


def upload(request):
    file = request.FILES.get('file')
    file_suffix = os.path.splitext(file.name)[1]
    tmp_file = '%s%s' % (uuid.uuid1(), file_suffix)

    f = open(os.path.join(settings.TEMP_PATH, tmp_file), 'wb')
    for chunk in file.chunks():
        f.write(chunk)
    f.close()

    return JsonResponse({'fileName': tmp_file, 'status': 'success'})