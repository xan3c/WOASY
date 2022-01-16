import * as PIXI from "pixi.js";
import type { CharacterObject } from "$lib/scene";
import boat from "static/images/boat.png";
import type { Game } from "./game";
import type { Player } from "./player";
import { tick } from "svelte";

let texture = PIXI.Texture.from(boat);
texture.defaultAnchor.set(0.5, 0.5);

export class NPC extends PIXI.Sprite {
	character: CharacterObject;
	game: Game;
	player: Player;

	mouseOver = false;

	constructor(character: CharacterObject, game: Game, player: Player) {
		super(texture);
		this.scale.set(0.05, 0.05);
		this.rotation = (4 * Math.PI) / 2;
		this.character = character;
		this.game = game;
		this.player = player;

		this.interactive = true;
		(this as any).mouseover = (mouseData) => {
			this.mouseOver = true;

			let lines = character.bio.split(".").join("\n");
			let text = new PIXI.Text(lines, {
				fontFamily: "Arial",
				fontSize: 200,
				fontWeight: "bold",
				fill: 0xffffff,
				align: "center",
			});
			text.anchor.set(0.5, 0.5);
			text.position.set(0, -1000);
			text.zIndex = 100;
			this.sortableChildren = true;
			this.addChild(text);
		};
		(this as any).mouseout = (mouseData) => {
			this.mouseOver = false;

			this.removeChildren();
		};
		(this as any).mousedown = (mouseData) => {
			if (this.checkDistance()) {
				this.pickup();
			}
		};

		this.position.set(Math.random() * 400 + 100, Math.random() * 400 + 100);
	}

	pickup() {
		this.position.set(0, 0);
	}
	tick() {
		if (this.mouseOver && this.checkDistance()) {
			this.scale.set(0.06, 0.06);
		} else {
			this.scale.set(0.05, 0.05);
		}
	}

	checkDistance() {
		let d = Math.hypot(this.x - this.player.x, this.y - this.player.y);
		return d < 50;
	}
}
