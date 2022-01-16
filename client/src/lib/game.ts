import * as PIXI from "pixi.js";
import { Key } from "$lib/input";
import png from "static/images/test.png";
import { Player } from "$lib/player";
import type { SceneObject, CharacterObject } from "$lib/scene";
import { NPC } from "./npc";
import { get_scenario } from "$lib/communication";

export class Game {
	app: PIXI.Application;
	canvas: HTMLCanvasElement;

	constructor(canvas: HTMLCanvasElement) {
		this.canvas = canvas;
	}

	async start() {
		let sceneObject = await get_scenario();

		this.app = new PIXI.Application({
			view: this.canvas,
			width: 600,
			height: 600,
			backgroundColor: 0x1c9be3,
			resolution: window.devicePixelRatio,
			autoDensity: true,
			antialias: true,
		});
		this.app.stage.sortableChildren = true;

		let NPCs = new PIXI.Container();
		NPCs.sortableChildren = true;
		this.app.stage.addChild(NPCs);

		let player = new Player();
		this.app.stage.addChild(player);
		player.zIndex = 10;

		let keyW = new Key("w");
		let keyS = new Key("s");
		let keyA = new Key("a");
		let keyD = new Key("d");

		let keySpace = new Key(" ");

		let npcList = [];
		for (const characterObject of sceneObject.characters) {
			let npc = new NPC(characterObject, this, player);
			NPCs.addChild(npc);
			npcList.push(npc);
		}

		let tick = 0;

		let svg: SVGAElement;

		// let t = PIXI.Texture.from(svg);
		// console.log(this.app.renderer.plugins.interaction);

		const animate = (dt: number) => {
			tick += 1;

			player.move(keyW, keyS, keyA, keyD);

			npcList.forEach((npc) => npc.tick());
		};

		this.app.ticker.add(animate);
	}
}
