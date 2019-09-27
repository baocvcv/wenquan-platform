SE Project -- WenQuan Exam Platform

Backend bootstrapped with Django.

Frontend boostrapped with vue@cli3.

## Develop
### Usage

This project requires `npm`. Make sure that it has been installed.

```sh
cd frontend
npm install		# install the packages listed in packages.json
npm run serve # start a server
cd ..
python manage.py runserver [PORT]	# start a server on Django
```

During Development, We want to hot-load the changes made in JavaScript, So we run `npm` commands for the frontend and run a Django Server for backend APIs. But In Production, we would like to integrate them into one server (Not yet implemented). 

### Structure
- frontend Frontend with Vue.js
- backend Backend with Django
- WenQuan_Platform project settings for Django

### Tools

The frontend was bootstrapped with vue@cli. Please install vue@cli.

- `npm run serve`
- `npm run build`
- `npm run test`
- `vue gui`  Modify Vue settings in GUI.