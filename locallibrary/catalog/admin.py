from django.contrib import admin  
from .models import Author, Genre, Book, BookInstance  # Retiré Language ici si non utilisé dans l'admin  

# Enregistrement des modèles  
admin.site.register(Genre)  

# Définir la classe admin pour Author  
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Enregistrer la classe admin avec le modèle associé  
admin.site.register(Author, AuthorAdmin)  

# Définir une classe inline pour BookInstance  
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Enregistrer les classes Admin pour Book en utilisant le décorateur  
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Enregistrer les classes Admin pour BookInstance en utilisant le décorateur  
from django.contrib import admin
from .models import BookInstance

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'get_borrower')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

    def get_borrower(self, obj):
        return obj.borrower
    get_borrower.short_description = 'Borrower'