# 0.1.0

- Changes to make module compatible with Django 4 (potentially backwards incompatibility with some older, unsupported 
Django versions).
    - Removed `providing_args` input argument from `Signal` constructor in `signals.py` (removed in Django 4).
    - Renamed `MIDDLEWARE_CLASSES` to `MIDDLEWARE` in `interface/settings.py`.
    - Use `path` instead of `url` in `interface/urls.py`.
- Other small formatting changes.
- Added `.gitignore` file.
