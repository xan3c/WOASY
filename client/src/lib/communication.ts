import type { SceneObject } from "$lib/scene";

let serverURL = "http://localhost:8000";

export const get_scenario = async (): Promise<SceneObject> => {
	let url = new URL("/scenario", serverURL);

	let response = await fetch(url.toString());

	return response.json();
};
