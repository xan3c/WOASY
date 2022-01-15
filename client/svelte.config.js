import path from "path";
import preprocess from "svelte-preprocess";
import adapter from "@sveltejs/adapter-static";

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: [
		preprocess({
			// scss: {
			// 	outputStyle: "compressed",
			// },
		}),
	],

	kit: {
		/** @type {import('vite').UserConfig} */
		vite: {
			resolve: {
				alias: {
					src: path.resolve("./src"),
				},
			},
		},

		adapter: adapter({
			pages: "build",
			assets: "build",
			fallback: null,
			precompress: false,
		}),

		// this is the problem causing html files not to be generated
		// need to include "*"
		prerender: {
			crawl: true,
		},
	},
};

export default config;
