import { c as create_ssr_component, v as validate_component } from './ssr-7e1a9690.js';
import { N as Nav } from './nav-90786762.js';

const Gpt_text_box = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  return `<div class="container ids-chart-container"><div class="row"><div class="col-md-12"><div class="card" id="ids-chat-card"><div class="card-body text-center"><h1 class="card-title" data-svelte-h="svelte-55rpma">Threat Analysis</h1> <hr> <div class="text-start" id="ids-chat-content" data-svelte-h="svelte-om0z4o"><p class="card-text" id="ids-chat-analysis-text">None</p></div> <hr> <div class="spinner-border text-warning" role="status" id="ids-chat-spinner"></div> <button type="button" class="btn btn-outline-secondary" id="ids-chat-btn" data-svelte-h="svelte-s28wrb"><b>Update</b></button></div></div> <br></div></div></div>`;
});
const css = {
  code: '@import "/static/sass/home.sass";',
  map: null
};
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  $$result.css.add(css);
  return `${validate_component(Nav, "Nav").$$render($$result, {}, {}, {})} ${validate_component(Gpt_text_box, "GptTextBox").$$render($$result, {}, {}, {})}`;
});

export { Page as default };
//# sourceMappingURL=_page.svelte-694a2d43.js.map
