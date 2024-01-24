const Livro = require('../models/livroModel.js')

var livros_todos = [];

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

const livro_get_home = (req, res)=>{
    Livro.findAll()
    .then(result=>{
        livros_todos = result;
        res.render('index', {title: 'Início', table: livros_todos});
    }).catch(err=>{
        console.log(err);
    });
}

const livro_get_shop = (req, res)=>{
    Livro.findAll()
    .then(result=>{
        livros_todos = result;
        res.render('shop', {title: 'Produtos', table: livros_todos});
    }).catch(err=>{
        console.log(err);
    });
}

const livro_get_id = (req, res)=>{
    const livroId = req.params.id;
    Livro.findByPk(livroId)
        .then(result=>{
            console.log(result);
            res.render('produto', {result, title: result.titulo, table: livros_todos})
        }).catch(err=>{
            console.log(err);
            res.status(404).render('404', {title: '404'});
        })
};

const test_db = (req, res)=>{
    var novoLivro = Livro.create({
        titulo: 'A Biblioteca da Meia Noite',
        autor: 'Matt Haig',
        ano: 2021,
        editora: 'Editora Bertrand Brasil',
        categoria: 'Romance',
        estoque: 100,
        valor: 39.90,
        sinopse: "A Biblioteca da Meia-Noite é um romance incrível que fala dos infinitos rumos que a vida pode tomar e da busca incessante pelo rumo certo. Nesta edição limitada, você ganha outro exemplar do livro embalado para presente.<br>Aos 35 anos, Nora Seed é uma mulher cheia de talentos e poucas conquistas. Arrependida das escolhas que fez no passado, ela vive se perguntando o que poderia ter acontecido caso tivesse vivido de maneira diferente. Após ser demitida e seu gato ser atropelado, Nora vê pouco sentido em sua existência e decide colocar um ponto final em tudo. Porém, quando se vê na Biblioteca da Meia-Noite, Nora ganha uma oportunidade única de viver todas as vidas que poderia ter vivido.<br>Neste lugar entre a vida e a morte, e graças à ajuda de uma velha amiga, Nora pode, fina..."
    })
    novoLivro = Livro.create({
        titulo: 'A Cinco Passos de Você',
        autor: 'Rachael Lippincott',
        ano: 2019,
        editora: 'Globo Livros',
        categoria: 'Romance',
        estoque: 100,
        valor: 49.90,
        sinopse: "Agora uma superprodução cinematográfica estrelada por Cole Sprouse, de “Riverdale”. 21 de março nos cinemas.<br>Stella Grant gosta de controle. Ela parece uma adolescente típica, mas em sua rotina há listas de tarefas e inúmeros remédios que deve tomar para controlar a fibrose cística, doença crônica que impede que seus pulmões funcionem como deveriam. Para conseguir um transplante, ela precisa seguir seu tratamento e eliminar qualquer chance de infecção, o que significa ficar a pelo menos seis passos de outros pacientes com a doença – sem exceção."
    })
    novoLivro = Livro.create({
        titulo: 'Rainha Charlotte',
        autor: 'Julia Quinn & Shonda Rhimes',
        ano: 2023,
        editora: 'Arqueiro',
        categoria: 'Romance',
        estoque: 100,
        valor: 59.90,
        sinopse: "Rainha Charlotte é a história da monarca que ficou consagrada na série da Netflix e conta com a participação das jovens Violet Bridgerton e lady Danbury, que, antes de serem levadas para a tela, já encantavam os leitores nos romances de Julia Quinn.<br>Em 1761, num ensolarado dia de setembro, um rei e uma princesa se veem pela primeira vez. Em questão de horas, os dois já estão casados e ela já é uma rainha.<br>Nascida na Alemanha, Charlotte de Mecklenburg-Strelitz é bela, obstinada e incrivelmente inteligente. Não são bem os atributos que a Coroa Britânica busca na esposa do jovem rei George III."
    })
    novoLivro = Livro.create({
        titulo: 'E Não Sobrou Nenhum',
        autor: 'Agatha Christie',
        ano: 2014,
        editora: 'Globo Livros',
        categoria: 'Mistério',
        estoque: 100,
        valor: 39.90,
        sinopse: " Uma ilha misteriosa, um poema infantil, dez soldadinhos de porcelana e muito suspense são os ingredientes com que Agatha Christie constrói seu romance mais importante. Na ilha do Soldado, antiga propriedade de um milionário norte-americano, dez pessoas sem nenhuma ligação aparente são confrontadas por uma voz misteriosa com fatos marcantes de seus passados.<br>Convidados pelo misterioso mr. Owen, nenhum dos presentes tem muita certeza de por que estão ali, a despeito de conjecturas pouco convincentes que os leva a crer que passariam um agradável período de descanso em mordomia. Entretanto, já na primeira noite, o mistério e o suspense se abatem sobre eles e, num instante, todos são suspeitos, todos são vítimas e todos são culpados."
    })
}

module.exports = {
    livro_post,
    livro_get_home,
    livro_get_shop,
    livro_get_id,
    test_db
}