from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3 #3 extra blank spaces for choices (maximum limit that can be set is 1000 blank fields)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        #fieldset(title_string, options_dictionary_inside_the_curly_braces)
        ("Question Title", {"fields": ["question_text"]}), #first argument in the tuple is the name of the field
        ("Date infomation", {"fields": ["pub_date"], "classes":["collapse"]}),] 
        #fields = ["pub_date", "question_text"]#this makes the fileds come in order as they appear here
    inlines = [ChoiceInLine] #Choice objects are edited on the Question adming page, by default , showes existing choices + 3 blank ones
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ['pub_date']
    search_fields = ["question_text"] #this adds a search box at the top of the change list
    list_per_page = 2
admin.site.register(Question, QuestionAdmin)

