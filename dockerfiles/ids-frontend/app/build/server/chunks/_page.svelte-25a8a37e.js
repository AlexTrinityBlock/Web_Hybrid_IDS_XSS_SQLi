import { c as create_ssr_component, v as validate_component } from './ssr-7e1a9690.js';
import { N as Nav } from './nav-90786762.js';
import 'chart.js/auto';

const Statistics = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<div class="container" data-svelte-h="svelte-pjwyo2"><br> <div class="row" id="counter-body"><div class="col-md-4 text-center counter-block"><div class="counter-text" id="negative-request-block"><br> <div id="negative-request-title">Negative <br> request</div> <br> <div id="negative-request-body" class="align-middle">0</div></div></div> <div class="col-md-4 text-center counter-block"><div class="counter-text" id="positive-request-block"><br> <div id="positive-request-title">Positive <br> request</div> <br> <div id="positive-request-body" class="align-middle">0</div></div></div> <div class="col-md-4 text-center counter-block"><div class="counter-text" id="total-request-block"><br> <div id="total-request-title">Total <br> request</div> <br> <div id="total-request-body" class="align-middle">0</div></div></div></div></div>`;
});
const Ids_chart = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<br> <div class="container ids-chart-container" data-svelte-h="svelte-883gkl"><div class="row"><div class="col-md-6 ids-chart-col"><div id="ids-doughnut-chart-canvas-append-point"><canvas height="400px" width="400px" id="ids-doughnut-chart-canvas"></canvas></div></div> <div class="col-md-6 ids-chart-col"><div><canvas height="400px" width="400px" id="ids-bar-chart-canvas"></canvas></div></div></div></div>`;
});
const css = {
  code: '@import "/static/sass/home.sass";',
  map: null
};
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let update = () => {
  };
  setInterval(update, 5e3);
  $$result.css.add(css);
  return `${validate_component(Nav, "Nav").$$render($$result, {}, {}, {})}  <div style="min-height: 500px; display:relative">${validate_component(Ids_chart, "IdsChart").$$render($$result, {}, {}, {})}</div> ${validate_component(Statistics, "Statistics").$$render($$result, {}, {}, {})} `;
});

export { Page as default };
//# sourceMappingURL=_page.svelte-25a8a37e.js.map
