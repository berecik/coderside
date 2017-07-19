//Konfiguracja Webpack
module.exports = {
    entry: [
        'whatwg-fetch', "./react/js/app.jsx", "./react/sass/main.scss",

    ],
    output: {
        filename: "static/js/coderside-react.js"
    },
    devServer: {
        inline: true,
        contentBase: './',
        port: 3000
    },

    watch: false,
    module: {
        loaders: [
            {
                test: /\.jsx$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['es2015', 'stage-2', 'react']
                }
            },
            {
                test: /\.css$/,
                loaders: ['style-loader', 'css-loader']
            },
            {
                test: /\.scss$/,
                loaders: ['style-loader', 'css-loader', 'sass-loader']
            },
            {
                test: /\.svg/,
                loaders: ['svg-url-loader']
            }
        ]
    }
}