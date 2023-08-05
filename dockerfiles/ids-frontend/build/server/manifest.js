const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set(["favicon.png","js/bootstrap.min.js","js/bootstrap.min.js.map","sass/gpt-text-box.sass","sass/home.sass","sass/ids-chart.sass","sass/log-pagination.sass","sass/logs-table.sass","sass/manual-input.sass","sass/nav.sass","sass/statistics.sass"]),
	mimeTypes: {".png":"image/png",".js":"application/javascript",".map":"application/json",".sass":"text/x-sass"},
	_: {
		client: {"start":"_app/immutable/entry/start.08147132.js","app":"_app/immutable/entry/app.640a5cb7.js","imports":["_app/immutable/entry/start.08147132.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/singletons.636962bf.js","_app/immutable/chunks/index.0378bb41.js","_app/immutable/entry/app.640a5cb7.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/index.06801730.js"],"stylesheets":[],"fonts":[]},
		nodes: [
			__memo(() => import('./chunks/0-e3f848da.js')),
			__memo(() => import('./chunks/1-e130e178.js'))
		],
		routes: [
			
		],
		matchers: async () => {
			
			return {  };
		}
	}
}
})();

const prerendered = new Set(["/","/analysis","/manual-input","/log/1"]);

export { manifest, prerendered };
//# sourceMappingURL=manifest.js.map
