(function () {
  var busca = document.getElementById('busca');
  var filtros = document.getElementById('filtros');
  var filtrosAnv = document.getElementById('filtros-anvisa');
  var vazio = document.getElementById('vazio');
  if (!busca || !filtros) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card[data-busca]'));
  var secoes = Array.prototype.slice.call(document.querySelectorAll('[data-secao]'));
  var cat = 'todos';
  var anv = 'todos';

  function normaliza(s) {
    return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }

  function aplicar() {
    var termo = normaliza(busca.value.trim());
    var achou = 0;
    cards.forEach(function (c) {
      var okCat = cat === 'todos' || c.dataset.cat === cat;
      // 'nao' inclui o notificado: nenhum dos dois tem registro
      var estado = c.dataset.anv || 'nd';
      var okAnv = anv === 'todos'
        || (anv === 'sim' && estado === 'sim')
        || (anv === 'nao' && (estado === 'nao' || estado === 'nof'));
      var okTermo = !termo || normaliza(c.dataset.busca).indexOf(termo) !== -1;
      var mostra = okCat && okAnv && okTermo;
      c.hidden = !mostra;
      if (mostra) achou++;
    });
    secoes.forEach(function (s) {
      var visiveis = s.querySelectorAll('.card:not([hidden])').length;
      s.hidden = visiveis === 0;
    });
    if (vazio) vazio.hidden = achou !== 0;
  }

  function grupo(el, campo, aplicaValor) {
    if (!el) return;
    el.addEventListener('click', function (e) {
      var b = e.target.closest('.filtro');
      if (!b) return;
      aplicaValor(b.dataset[campo]);
      el.querySelectorAll('.filtro').forEach(function (x) {
        x.setAttribute('aria-pressed', String(x === b));
      });
      aplicar();
    });
  }

  busca.addEventListener('input', aplicar);
  grupo(filtros, 'cat', function (v) { cat = v; });
  grupo(filtrosAnv, 'anv', function (v) { anv = v; });
})();
