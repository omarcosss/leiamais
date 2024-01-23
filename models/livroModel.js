const Sequelize = require ('sequelize');
const db = require('../database.js');

const Livro = db.define('Livro', {
    _id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    titulo: {
        type: Sequelize.STRING,
        allowNull: false
    },
    autor: {
        type: Sequelize.STRING,
        allowNull: false
    },
    ano: {
        type: Sequelize.INTEGER,
        allowNull: false
    },
    editora: {
        type: Sequelize.STRING,
        allowNull: false
    },
    categoria: {
        type: Sequelize.STRING,
        allowNull: false
    },
    estoque: {
        type: Sequelize.INTEGER,
        allowNull: false
    },
    valor: {
        type: Sequelize.DECIMAL(5,2),
        allowNull: false
    },
    promocao: {
        type: Sequelize.DECIMAL(5,2),
        default: 0.00
    },
    valorfinal: {
        type: Sequelize.DECIMAL(5,2),
        default: 0.00
    }
})

module.exports = Livro;