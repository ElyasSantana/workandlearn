<div class="container">
        <div class="navbar-header">
          <h2>
            Api Work and Learn
          <h2>
</div>

<div>
  <p>
  <h3>Endpoints</h3>
  </p>
  <hr />
<p>Os endpoints iniciam com 
<a href="#">http://127.0.0.1:8000/api/empresa/</a>
<a href="#">http://127.0.0.1:8000/api/desenvolvedor/</a>
</p>
<hr />
<h4>Empresa</h4>
<p>Get, Post, de todas as Empresa: <strong>http://127.0.0.1:8000/api/empresa/</strong></p>
<p>Get, Post, Put, Patch, Delete a partir do index Empresa: <strong>http://127.0.0.1:8000/api/empresa/:id/</strong></p>

<h4>Local por Empresa</h4>
<p>Get, Post, dos Locais a partir do index Empresa: <strong>http://127.0.0.1:8000/api/empresa/:id/local/</strong></p>
<p>Get, Post, Put, Patch, Delete do Local a partir do index Empresa e Local: <strong>http://127.0.0.1:8000/api/empresa/:id/local/:id </strong></p>

<h4>Tecnologias por Empresa</h4>
<p>Get, Post, dos Locais a partir do index Empresa: <strong>http://127.0.0.1:8000/api/empresa/:id/tecnologia/</strong></p>
<p>Get, Post, Put, Patch, Delete do Local a partir do index Empresa e Tecnologia: <strong>http://127.0.0.1:8000/api/empresa/:id/tecnologia/:id </strong></p>

<hr />
<h4>Desenvolvedor</h4>
<p>Get, Post, de todos os Desenvolvedores: <strong>http://127.0.0.1:8000/api/desenvolvedor/</strong></p>
<p>Get, Post, Put, Patch, Delete a partir do index Desenvolvedor: <strong>http://127.0.0.1:8000/api/desenvolvedor/:id/</strong></p>

<h4>Endereço por Desenvolvedor</h4>
<p>Get, Post, dos Locais a partir do index Desenvolvedor: <strong>http://127.0.0.1:8000/api/desenvolvedor/:id/endereco/</strong></p>
<p>Get, Post, Put, Patch, Delete do Local a partir do index Desenvolvedor e Endereço: <strong>http://127.0.0.1:8000/api/desenvolvedor/:id/endereco/:id </strong></p>

<h4>Tecnologias de Interesse por Desenvolvedor</h4>
<p>Get, Post, dos Locais a partir do index Tecnologia: <strong>http://127.0.0.1:8000/api/cliente/:id/tecnologia/</strong></p>
<p>Get, Post, Put, Patch, Delete do Local a partir do index DEsenvolvedor e Endereço: <strong>http://127.0.0.1:8000/api/desenvolvedor/:id/tecnologia/:id </strong></p>

<hr />
<h4>Reservas</h4>
<p>Get, Post, de todas as reservas por Empresa: <strong>http://127.0.0.1:8000/api/empresa/:id/reserva</strong></p>
<p>Get, Post, Put, Patch, Delete a partir do index Empresa e Reserva: <strong>http://127.0.0.1:8000/api/empresa/:id/reserva/:id</strong></p>

<p>Get, Post, de todas as reservas por Desenvolvedor: <strong>http://127.0.0.1:8000/api/desenvolvedor/:id/reserva</strong></p>
<p>Get, Post, Put, Patch, Delete a partir do index Desenvolvedor e Reserva: <strong>http://127.0.0.1:8000/api/desenvolvedor/:id/reserva/:id</strong></p>

<h3>Exemplo</h3>

<h4>Solicitação de Reserva pelo</h4>

```json
{
  "data": "2019-11-02",
  "local": 1,
  "desenvolvedor": 1,
  "empresa": 1
}
```

<h4>Aprova da Solicitação pela Empresa</h4>

```json
{
  "aprovado": false,
  "local": 1,
  "desenvolvedor": 1
}
```

<hr />

</div>
