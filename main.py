from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

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

@app.get("/", include_in_schema=False)  #include_in_schema=False ---> this will restrict this route not to be shown in swagger docs
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title":"Home"})

@app.get("/api/posts")
def get_posts():
    return posts