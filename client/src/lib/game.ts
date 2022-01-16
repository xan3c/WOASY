import * as PIXI from "pixi.js";
import { Key } from "$lib/input";
import { Player } from "$lib/player";
import type { SceneObject, CharacterObject } from "$lib/scene";
import { NPC } from "./npc";
import { get_scenario } from "$lib/communication";
import { get } from "svelte/store";
import { timeRemaining, capacityRemaining } from "$lib/store";

export class Game {
	app: PIXI.Application;
	canvas: HTMLCanvasElement;
	NPCs: PIXI.Container;

	constructor(canvas: HTMLCanvasElement) {
		this.canvas = canvas;
	}

	async start() {
		let sceneObject = await get_scenario();

		this.app = new PIXI.Application({
			view: this.canvas,
			width: 800,
			height: 800,
			backgroundColor: 0xdddddd,
			resolution: window.devicePixelRatio,
			autoDensity: true,
			antialias: true,
		});
		this.app.stage.sortableChildren = true;

		this.NPCs = new PIXI.Container();
		this.NPCs.sortableChildren = true;
		this.app.stage.addChild(this.NPCs);

		let player = new Player();
		this.app.stage.addChild(player);

		let keyW = new Key("w");
		let keyS = new Key("s");
		let keyA = new Key("a");
		let keyD = new Key("d");

		let keySpace = new Key(" ");

		for (const characterObject of sceneObject.characters) {
			let npc = new NPC(characterObject, this, player);
			this.NPCs.addChild(npc);
		}

		let tick = 0;

		capacityRemaining.set(sceneObject.lifeboat.maxCapacity);

		timeRemaining.set(sceneObject.maxTime);
		let timer = setInterval(() => {
			timeRemaining.update((n) => (n -= 1));

			if (get(timeRemaining) <= 0) {
				clearInterval(timer);
			}
		}, 1000);

		const animate = (dt: number) => {
			tick += 1;

			player.move(keyW, keyS, keyA, keyD);

			this.NPCs.children.forEach((npc: NPC) => npc.tick());
		};

		this.app.ticker.add(animate);
	}
}
