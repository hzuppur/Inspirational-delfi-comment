# Inspirational-delfi-comment ✨

### A application to display a random delfi comment in the style of a inspirational quote

This application is made with django and the database to store the comments uses PostgreSQL.

It is deployed over at heroku. [Link to the app](https://delfi-comment-inspirational.herokuapp.com/)

### How it works
The application automatically scrapes the delfi front page articles for their comments and adds them to the database every hour. It also adds a timestamp to the articles. After each scrape, it automatically deletes over day old articles and their comments.

Every time someone requests the page, the application returns a random comment from the database.

