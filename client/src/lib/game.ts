import * as PIXI from "pixi.js";
import { Key } from "$lib/input";
import { Player } from "$lib/player";
import type { SceneObject, CharacterObject } from "$lib/scene";
import { NPC } from "./npc";
import { finished, get_scenario } from "$lib/communication";
import { get, writable } from "svelte/store";
import { timeRemaining, capacityRemaining } from "$lib/store";

export class Game {
	gameID: string;
	app: PIXI.Application;
	canvas: HTMLCanvasElement;
	NPCs: PIXI.Container;
	isGameOver = false;
	saved: string[] = [];

	constructor(canvas: HTMLCanvasElement) {
		this.canvas = canvas;
	}

	async start() {
		let sceneObject = await get_scenario();
		this.gameID = sceneObject.gameID;

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
				this.gameOver();
			}
		}, 1000);

		const animate = (dt: number) => {
			tick += 1;

			player.move(keyW, keyS, keyA, keyD);

			this.NPCs.children.forEach((npc: NPC) => npc.tick());
		};

		this.app.ticker.add(animate);
	}

	removeNPC(npc: NPC) {
		if (get(capacityRemaining) > 0) {
			capacityRemaining.update((n) => (n -= 1));
			this.saved.push(npc.id);

			this.NPCs.removeChild(npc);

			if (get(capacityRemaining) <= 0) {
				this.gameOver();
			}
		}
	}

	async gameOver() {
		if (!this.isGameOver) {
			this.isGameOver = true;

			timeRemaining.set(null);
			capacityRemaining.set(null);

			setTimeout(() => {
				this.app.ticker.destroy();
			}, 100);

			finished(this.gameID, this.saved);
		}
	}
}
