from django.contrib import admin

from todo_apps.todos.models.models import Todo, Person, Category

admin.site.register(Todo)
admin.site.register(Person)
admin.site.register(Category)

