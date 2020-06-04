from datetime import datetime
from django.conf import settings

from django.shortcuts import render
import os


def file_list(request, date: datetime = None):
    template_name = 'index.html'
    files_list = os.listdir(settings.FILES_PATH)
    files = []
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    for file in files_list:
        stat = os.stat(os.path.join(settings.FILES_PATH, file))

        if date:
            if datetime.fromtimestamp(stat.st_mtime).date() == date:
                files.append({'name': file, 'ctime': datetime.fromtimestamp(stat.st_ctime),
                              'mtime': datetime.fromtimestamp(stat.st_mtime)})
        else:
            files.append({'name': file, 'ctime': datetime.fromtimestamp(stat.st_ctime),
                          'mtime': datetime.fromtimestamp(stat.st_mtime)})

    context = {
        'files': files,
        'date': date  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    with open(os.path.join(settings.FILES_PATH, name), 'r') as file:
        content = file.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )
