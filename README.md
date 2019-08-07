# ng-courses

This repo is the supporting material for the following blog posts:

- [Consuming APIs In Angular: The Model-Adapter Pattern](https://blog.florimondmanca.com/consuming-apis-in-angular-the-model-adapter-pattern)
- [Consuming APIs In Angular: Displaying Data In Components](https://blog.florimondmanca.com/consuming-apis-in-angular-displaying-data-in-components)

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 6.0.5.

## Install

For the Angular app, install dependencies with:

```bash
npm install
```

The backend server requires Python 3.6+. Its only dependency is [Bocadillo], which can be installed using:

```bash
pip install bocadillo
```

Alternatively, if you're using [pipenv](https://github.com/pypa/pipenv), you can run `pipenv install`.

## Quick start

First, fire up the backend server:

```bash
python app.py
```

It will be running at `http://localhost:8000`.

You can then start the Angular dev server using:

```bash
ng serve
```

Navigate to `http://localhost:4200` to see the result. 🎊

## License

MIT
