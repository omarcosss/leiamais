const Livro = require('../models/livroModel.js')

const livro_post = (req, res)=>{
    const novoLivro = Livro.create({
        titulo: 'A Biblioteca da Meia Noite',
        autor: 'Matt Haig',
        ano: 2021,
        editora: 'Editora Bertrand Brasil',
        categoria: 'Romance',
        estoque: 100,
        valor: 39.90
    })
}

const livro_get_id = (req, res)=>{
    const livroId = req.params.id;
    Livro.findByPk(livroId)
        .then(result=>{
            console.log(result);
            res.render('produto', {result, title: result.titulo})
        }).catch(err=>{
            console.log(err);
        })
};

module.exports = {
    livro_post,
    livro_get_id
}