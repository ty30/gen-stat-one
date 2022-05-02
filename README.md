# gen-stat-one

Python 3 static-site generator

These generators are everywhere, this is my version.

It uses Flask, Flask-FlatPages, and Flask Frozen for the basic build.

I've added Minify to squeeze another ounce of weight from the build.

There's some instructions to get it working. Use them, don't use them, what am I your mother, do whatever you like.

# WorkFlow:

## How-To install for Ubuntu Linux 20.04 (adjust for your OS):

```
git clone https://github.com/ty30/gen-stat-one
python3 -m venv venv
source venv/bin/activate
pip install -r requirement.txt
```

## Run App:

- Modify app.py, templates, styles to taste (Yes this is a recipe, Go Nuts)
- Run app in development mode `python app.py`
- Run app to build static pages `python app.py build`, a directory(build) is created.

The build directory can be uploaded to hosting, etc

Cheers...Ty

Thanks to https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/ for the genesis of this code.
