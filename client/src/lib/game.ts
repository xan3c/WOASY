import * as PIXI from "pixi.js";
import { Key } from "$lib/input";
import png from "static/images/test.png";
import { Player } from "$lib/player";
import type { SceneObject, CharacterObject } from "$lib/scene";
import { NPC } from "./npc";

let char1: CharacterObject;
let char2: CharacterObject;
let sceneObject: SceneObject = {
	characters: [],
	lifeboat: {
		x: 0,
		y: 0,
		maxCapacity: 0,
	},
	maxTime: 0,
};
sceneObject.characters.push(char1, char2);

export class Game {
	app: PIXI.Application;
	canvas: HTMLCanvasElement;

	constructor(canvas: HTMLCanvasElement) {
		this.canvas = canvas;
	}

	async start() {
		this.app = new PIXI.Application({
			view: this.canvas,
			width: 400,
			height: 400,
			backgroundColor: 0xdddddd,
			resolution: window.devicePixelRatio,
			autoDensity: true,
			antialias: true,
		});

		let container = new PIXI.Container();
		this.app.stage.addChild(container);
		container.sortableChildren = true;

		let player = new Player();
		container.addChild(player);
		player.zIndex = 10;

		let keyW = new Key("w");
		let keyS = new Key("s");
		let keyA = new Key("a");
		let keyD = new Key("d");

		let keySpace = new Key(" ");

		let npcList = [];
		for (let i = 0; i < 4; i++) {
			let npc = new NPC(sceneObject.characters[i], this, player);
			this.app.stage.addChild(npc);
			npcList.push(npc);
		}

		let tick = 0;

		const animate = (dt: number) => {
			tick += 1;

			player.move(keyW, keyS, keyA, keyD);

			npcList.forEach((npc) => npc.tick());
		};

		this.app.ticker.add(animate);
	}
}
