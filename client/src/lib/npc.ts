import * as PIXI from "pixi.js";
import type { CharacterObject } from "$lib/scene";
import boat from "static/images/boat.png";
import type { Game } from "./game";
import type { Player } from "./player";
import { createAvatar } from "@dicebear/avatars";
import type { Options } from "@dicebear/avatars";
import * as style from "@dicebear/avatars-avataaars-sprites";

export class NPC extends PIXI.Sprite {
	id: string;

	character: CharacterObject;
	game: Game;
	player: Player;

	mouseOver = false;

	constructor(character: CharacterObject, game: Game, player: Player) {
		super();
		this.id = character.id;
		this.anchor.set(0.5, 0.5);
		this.x = character.x;
		this.y = character.y;

		let options: Partial<style.Options & Options> = {};

		Object.keys(character.options).forEach((key) => {
			options[key] = [character.options[key]];
		});

		let svg = createAvatar(style, { ...options, mode: "include", style: "transparent" });

		let blob = new Blob([svg], { type: "image/svg+xml" });
		let url = URL.createObjectURL(blob);
		let image = document.createElement("img");
		image.src = url;

		// let t = PIXI.Texture.fromURL("data:image/svg+xml;charset=utf8," + svg);

		this.texture = PIXI.Texture.from(image);

		this.scale.set(0.45, 0.45);
		this.character = character;
		this.game = game;
		this.player = player;

		this.sortableChildren = true;

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
			text.zIndex = 2;
			this.zIndex = 1;

			this.addChild(text);
		};
		(this as any).mouseout = (mouseData) => {
			this.mouseOver = false;
			this.zIndex = 0;

			this.removeChildren();
		};
		(this as any).mousedown = (mouseData) => {
			if (this.checkDistance()) {
				this.game.removeNPC(this);
			}
		};
	}

	tick() {
		if (this.mouseOver && this.checkDistance()) {
			this.scale.set(0.5, 0.5);
		} else {
			this.scale.set(0.45, 0.45);
		}
	}

	checkDistance() {
		let d = Math.hypot(this.x - this.player.x, this.y - this.player.y);
		return d < 100;
	}
}
