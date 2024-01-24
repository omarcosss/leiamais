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

app.get('/', livroCtrl.livro_get_home);
app.post('/produtos', livroCtrl.livro_post);
app.get('/produtos', livroCtrl.livro_get_shop);
app.get('/produto!:id', livroCtrl.livro_get_id);

app.use((req,res)=>{
    res.status(404).render('404', {title: '404'});
})