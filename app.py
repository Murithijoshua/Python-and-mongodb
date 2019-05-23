from typing import List, Any

from database import Database
from models.post import Post

Database.initialize()
post = Post(
    blog_id="56",
    title="festival",
    content="today was blessing",
    author="joshua",
    date="2345678"

)
p=Database.show()
for i in p:
    print(i)