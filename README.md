# File structure

Every frontend/react file is in src folder  
Every backend/python file is in python folder

# React

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

### React command

In the project directory, you can run:

#### `npm start`

#### `npm test`

#### `npm run build`

#### `npm run eject`

### Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Deploy To Firebase (https://socialeye-seniorproject.web.app/)

`firebase deploy`

###

## Command

### Activate Virtual Env

`.\backend\python\social-eye-env\Scripts\Activate`

### Go to directory activate

`cd .\backend\python\social_eye_scrapy\social_eye_scrapy`

### Crawl

##### Amphur search

`scrapy crawl teedin108 -O .\result\teedin108_amphur_23.json -a amphur=23`

##### Province search

`scrapy crawl teedin108 -O .\result\teedin108_province_1.json -a province=1`

##### Crawl inside

`scrapy crawl teedin108inside -O .\result\teedin108_23_inside.json`
