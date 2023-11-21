import express from "express";
import { PORT, mongodbURL } from "./config.js";
import mongoose from 'mongoose';

const app = express();

app.get('/', (request, response) => {
    console.log(request);
    return response.status(234).send('Olá mundo!');
});

mongoose
    .connect(mongodbURL)
    .then(() => {
        console.log('> Conectado ao MongoDB');
        app.listen(PORT, () => {
            console.log('> App ouvindo à porta: ' + PORT)
        });
    })
    .catch((error) => {
        console.log(error);
    });