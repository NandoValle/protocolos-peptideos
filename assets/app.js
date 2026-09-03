(function () {
  var busca = document.getElementById('busca');
  var filtros = document.getElementById('filtros');
  var vazio = document.getElementById('vazio');
  if (!busca || !filtros) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card[data-busca]'));
  var secoes = Array.prototype.slice.call(document.querySelectorAll('[data-secao]'));
  var cat = 'todos';

  function normaliza(s) {
    return s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  }

  function aplicar() {
    var termo = normaliza(busca.value.trim());
    var achou = 0;
    cards.forEach(function (c) {
      var okCat = cat === 'todos' || c.dataset.cat === cat;
      var okTermo = !termo || normaliza(c.dataset.busca).indexOf(termo) !== -1;
      var mostra = okCat && okTermo;
      c.hidden = !mostra;
      if (mostra) achou++;
    });
    secoes.forEach(function (s) {
      var visiveis = s.querySelectorAll('.card:not([hidden])').length;
      s.hidden = visiveis === 0;
    });
    if (vazio) vazio.hidden = achou !== 0;
  }

  busca.addEventListener('input', aplicar);
  filtros.addEventListener('click', function (e) {
    var b = e.target.closest('.filtro');
    if (!b) return;
    cat = b.dataset.cat;
    filtros.querySelectorAll('.filtro').forEach(function (x) {
      x.setAttribute('aria-pressed', String(x === b));
    });
    aplicar();
  });
})();