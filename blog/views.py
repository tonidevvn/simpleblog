
import random
import datetime
from django.shortcuts import render

# Sample data
authors = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
titles = ['Exploring the Universe', 'The Art of Cooking', 'Tech Innovations', 'Travel Diaries', 'Fitness Journey', 'Gardening Tips', 'Music and Life', 'History Unveiled', 'Science Wonders', 'Literature Love']
contents = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'Curabitur pretium tincidunt lacus. Nulla gravida orci a odio.', 'Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris.', 'Integer in mauris eu nibh euismod gravida.', 'Duis ac tellus et risus vulputate vehicula.', 'Donec lobortis risus a elit.']

# Function to generate random posts
def generate_random_posts(num_posts):
    posts = []
    for i in range(num_posts):
        post = {
            'author': random.choice(authors),
            'title': random.choice(titles),
            'content': random.choice(contents),
            'date_posted': (datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 365))).strftime('%B %d, %Y')
        }
        posts.append(post)
    return posts

# Generate 10 random posts
random_posts = generate_random_posts(10)

def index(request):
    context = {
        'posts': random_posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {'title': 'About'})