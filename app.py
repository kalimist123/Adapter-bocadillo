from bocadillo import App, configure
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware

app = App()
configure(app)
app.add_middleware

app.add_middleware(CORSMiddleware, allow_origins=['*'])
app.add_middleware(CORSMiddleware, allow_methods=['*'])
app.add_middleware(CORSMiddleware, allow_headers=['*'])

#app = App(
#   enable_cors=True,
#   cors_config={"allow_origins": ["*"], "allow_methods": ["*"]},
#)

CORS = {
    "allow_origins": ["*"],
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}

_COURSES = [
    {
        "id": 1,
        "code": "adv-maths",
        "name": "Advanced Mathematics",
        "created": "2018-08-14T12:09:45",
    },
    {
        "id": 2,
        "code": "cs1",
        "name": "Computer Science I",
        "created": "2018-06-12T18:34:16",
    },
]


@app.route("/courses")
async def courses_list(req, res):
    res.json = _COURSES

