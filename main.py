from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from schemas import PostCreate, PostResponse

app = FastAPI()

templates = Jinja2Templates(directory='templates')

posts: list[dict] = [
    {
        "id":1,
        "author":"Chorey Schafer",
        "title":"FastAPI is Awesome",
        "content":"This framework is really easy to use and super fast",
        "date_posted":"April 20, 2025"
    },
    {
        "id":2,
        "author":"Jane Doe",
        "title":"Python is great for Web Development",
        "content":"Python and FastAPI together make great applications",
        "date_posted":"April 21, 2025"
    }
]

@app.get("/posts", include_in_schema=False)  #include_in_schema=False ---> this will restrict this route not to be shown in swagger docs
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title":"Home"})


@app.get("/api/posts", response_model=list[PostResponse])
def get_posts():
    return posts


@app.post("/api/post",response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate):
    new_id = max(p["id"] for p in posts)+1 if posts else 1
    new_post = {
        "id": new_id,
        "author":post.author,
        "title":post.title,
        "content":post.content,
        "date_posted": "3rd October 2026"
    }
    posts.append(new_post)
    return new_post


@app.get("/api/posts/{post_id}", response_model=PostResponse)
def get_post(post_id:int):
    for post in posts:
        if post.get("id")==post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post was not found")