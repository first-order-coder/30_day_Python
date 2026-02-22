from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class QustionAdmin(admin.ModelAdmin):
    fieldsets = [
        #fieldset(title_string, options_dictionary_inside_the_curly_braces)
        ("Question Title", {"fields": ["question_text"]}), #first argument in the tuple is the name of the field
        ("Date infomation", {"fields": ["pub_date"], "classes":["collapse"]}),] 
        #fields = ["pub_date", "question_text"]#this makes the fileds come in order as they appear here
    inlines = [ChoiceInLine]
    
admin.site.register(Question, QustionAdmin)

