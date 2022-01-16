import type { SceneObject } from "$lib/scene";

let serverURL = "http://localhost:8080";

export const get_scenario = async (): Promise<SceneObject> => {
	let url = new URL("/scenario", serverURL);

	let response = await fetch(url.toString());

	return response.json();
};

export const finished = async (gameID: string, saved: string[]) => {
	let url = new URL("/finished", serverURL);

	let response = await fetch(url.toString(), {
		method: "POST",
		headers: {
			Accept: "application/json",
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ gameID: gameID, saved: saved }),
	});

	return response.json();
};
