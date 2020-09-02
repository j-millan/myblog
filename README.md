### MyBlog

MyBlog is a blogging website. This project is not finished yet. This project was created to test and gain experience with django backend framework, but I'm also learning a lot about frontend and CSS styling. I was somewhat annoyed about some Bootstrap 4 features not working very well, so I decided to choose a simpler CSS library like Bulma and learn it as I built the website.

I got the idea for this blog from [this Pythonista Planet's article](https://www.pythonistaplanet.com/django-project-ideas/) and wanted to make it  little bit more complex. This is not based on any other django project or tutorial/course, however, the *blog.models.BlogPost* model was made following [this tutorial](https://www.youtube.com/watch?v=GcqURKYfv00).

***

#### What are the features?

1. **Authenticaton**. You can  create an account using your email and full name, and also must choose an username. Login only requires your username and password. If you forget your password, you can easily recover it using your email (this feture is not done yet), or if you want to change your password, you can do so by going to the account settings.

2. **Markdown**. *BlogPost* model admits markdown for the article's body so you can format the text and make it look awesome (just like the text you're reading now) by adding titles, lists, links, emphasis and even images.

3. **Comments**. Leave a comment in the article to let the author know your opinions. You can always edit your comment if it has a mistake. (*You must be logged in to add a comment*).

4. **Categories**. To make navigation easier, you can add your posts to different categories or "topics" based on its content. Each category has its own page where all of its articles will appear.

5. **Followers**. You can follow your favourite authors to stay tuned to their posts and also give them more visibility on the site. (As for now, you can only follow and unfollow other users, the rest will be worked on later).

6. **Profile information**. Add a description to your profile and add links to other social accounts so your followers can know more about you. You can also put whatever image you want as a profile picture.

***

#### Installation

If you want to install and test this app on your computer, you must install [Git](https://git-scm.com/downloads) and [Python 3.8.3](https://www.python.org/downloads/release/python-383/) (or greater).

- I recommend installing it on a virtual environment. To install virtualenv, use the next command in the command line:

		pip install virtualenv

- Go to any location in your computer and create a folder for the virtual environment and the project.
	
	- Create the folder for the project

			cd Documents\Development\Django\
			mkdir blog_app
			cd blog_app

	- Create and activate the virtual environment

		virtualenv venv
		venv\Scripts\activate

- Clone this repository.
	
		git clone https://github.com/j-millan/myblog.git
		cd  myblog

- Install all the requirements.

		pip install -r requirements.txt

- Add a new secret key.
	
	- Go to [miniwebtool](https://miniwebtool.com/django-secret-key-generator/) and generate a new key.

	- Create a file called `secrets.py` inside `myblog/project` and add the next line of code:

			SECRET_KEY = 'generated_secret_key_here'

	- Save the file.

- Create the next folder structure inside the project.

	**media / img / profile_pictures** (`media/` folder must be inside `myblog/` folder, next to `blog/`, `accounts/`, `templates/`, etc.)

	Add a png image inside `profile_pictures/` and name it *default.png*, this will be the profile picture every user will have when they create their accounts.

- Run the migration files.

		py manage.py migrate

- (*This step is optional*) Create a default category for all the articles. You can do this by creating a super user and using the [admin panel](http://127.0.0.1:8000/admin/) or by using the python shell as following:

		py manage.py shell

	This will activate ainteractive console where you can execute python commands. Now execute the next commands:

		from blog.models import BlogCategory
		BlogCategory.objects.create(name='Off-topic')
		exit

	This step is jut in case the author doesn't find a specific category that fits the article's content.

***

Now you can execute:

	py manage.py runserver

...and go to [127.0.0.1:800/](http://127.0.0.1:8000/) and start exploring the site.