const express = require('express');
const morgan = require('morgan');
const app = express();
app.set('view engine', 'ejs');

const db = require('./database');
db.sync()
    .then(result => {
        console.log('> Connected to db');
        app.listen(3000, ()=>{
            console.log('> Listening for requests...')
        });
    }).catch(err=>{
        console.log(err);
    });

//Middleware
const livroCtrl = require ('./controllers/livroCtrl.js');

app.use(express.static('assets'));
app.use(morgan('dev'));
app.use(express.urlencoded({extended: true}));

app.get('/', (req, res)=>{
    res.render('index', {title: 'Início'})
});

app.post('/produtos', livroCtrl.livro_post);
app.get('/produtos/:id', livroCtrl.livro_get_id);