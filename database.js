const Sequelize = require('sequelize');

const sequelize = new Sequelize('database', 'user', 'pass', {
    dialect: 'sqlite',
    // path: './data/livraria.db'
    host: './data/database.sqlite'
});

module.exports = sequelize;