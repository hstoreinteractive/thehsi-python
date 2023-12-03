@echo off
cls
cd %~dp0
echo Last Version:
type version
echo.
set /p "ver=This Version (x.x.x)> "
echo %ver%>version
git init
git remote add origin https://github.com/hstoreinteractive/thehsi-python.git
git add .
git commit -m "Updated to v%ver%"
git push -u origin main
pause
python setup.py sdist
echo.
echo Username: __token__
echo Password: pypi-AgEIcHlwaS5vcmcCJDNiMmZjMTZiLTYxYTctNGJjMS05MjU5LWVhNTI0MWRlOTBhNgACDlsxLFsidGhlaHNpIl1dAAIsWzIsWyIzZDc5MjU0OS0xMjQ0LTQ5MjUtOTc0Yi1kYmQ5NDYxNGFjN2QiXV0AAAYg6R2JOfcAJuA2ACuWS4WgCttfWxyXPZ6Vr0Yeb2O9zR4
echo pypi-AgEIcHlwaS5vcmcCJDNiMmZjMTZiLTYxYTctNGJjMS05MjU5LWVhNTI0MWRlOTBhNgACDlsxLFsidGhlaHNpIl1dAAIsWzIsWyIzZDc5MjU0OS0xMjQ0LTQ5MjUtOTc0Yi1kYmQ5NDYxNGFjN2QiXV0AAAYg6R2JOfcAJuA2ACuWS4WgCttfWxyXPZ6Vr0Yeb2O9zR4 | clip
echo.
twine upload dist/*
rmdir /S /Q thehsi.egg-info
rmdir /S /Q dist