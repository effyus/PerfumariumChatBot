var app = require('express')();
var http = require('http');
const { url } = require('inspector');
var server = http.Server(app)
var io = require('socket.io')(server);
var port = process.env.PORT || 3000;

//define url do robo
const URL_ROBO = "http://localhost:5000/perfume/resposta/";

//servidor retorna a pagina html
app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

//obtem a resposta do robo
getRespostaRobo = (msg) => {
  let data = '';

  http.get(URL_ROBO + msg, (resposta) => {
    resposta.on("data", (pedaco) => {
      data += pedaco; //recebe pedaços da resposta
    });

    resposta.on("end", () => {
      const obj = JSON.parse(data); //converte para json

      if (obj.confianca >= 0.55) {
        io.emit('chat message', "PERFUMARIUM: " + obj.resposta);
      } else {
        io.emit('chat message', "PERFUMARIUM: Não entendi a sua pergunta. Digite novamente");
      }
    });
  });
}

//gerencia conexões
io.on('connection', function (socket) {
  socket.on('chat message', function (msg) {
    io.emit('chat message', "Você: " + msg);
    getRespostaRobo(msg);
  });
});
//inicia o servidor
server.listen(port, function () {
  console.log('listening on *:' + port);
});
