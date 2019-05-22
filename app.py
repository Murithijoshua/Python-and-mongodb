from database import Database
from models.post import Post

Database.initialize()
post = Post(
    blog_id="56",
    title="festival",
    content="today was blessing",
    author="joshua",

)
