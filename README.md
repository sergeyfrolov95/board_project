# Imageboard on Django framework.

This imageboard approach to discuss news or other different things. In threads (themes to discuss) you can post comments and share pictures in messages.

## Prerequisites

You will need Python 2.7 interpreter and latest version of Django framework to be installed. Also, you need to download and unpack this project.

## Running

In board_project directory do next steps:

First of all you need to migrate models and generate db.sqlite3 file. To do it run this command:

	python manage.py migrate

To start server run this command:

	python manage.py runserver

To stop server interrupt previous 'runserver' command (for example using ctrl-c in command line).

## How to use it

Once server is running go to next page in browser:

	http://127.0.0.1:8000/board/

On that page you can add new theme using form or choose one of existing.
On thread page you can find messages of different users and post your own message attaching picture if you want. To do it use form on the top of the page.
You can offer one of threads on the top of thread list by using keyword "bump" (or "Bump", "Bump!" etc) in a post message. It will work until there are more than 100 messages in a thread. Threads that older than 14 days will be removed.

## TODO

- [X] Better UI
- [ ] File type validation
- [ ] File size validation
- [X] Deleting old threads
- [X] Bump system
- [ ] More powerful DB
