import * as PIXI from "pixi.js";
import boat from "static/images/boat.png";
import type { Key } from "./input";
import type { NPC } from "./npc";

let texture = PIXI.Texture.from(boat);
texture.defaultAnchor.set(0.5, 0.5);

export class Player extends PIXI.Sprite {
	vx = 0;
	vy = 0;

	speed = 0.2;

	constructor() {
		super(texture);
		this.scale.set(0.1, 0.1);
		this.rotation = (3 * Math.PI) / 2;
		this.position.set(400, 700);
		this.zIndex = 3;
	}

	move(keyW: Key, keyS: Key, keyA: Key, keyD: Key) {
		let num_keys = 0;

		if (keyW.isDown) {
			this.vy -= this.speed;
			num_keys += 1;
		}
		if (keyS.isDown) {
			this.vy += this.speed;
			num_keys += 1;
		}
		if (keyA.isDown) {
			this.vx -= this.speed;
			num_keys += 1;
		}
		if (keyD.isDown) {
			this.vx += this.speed;
			num_keys += 1;
		}

		// very hacky way to set angle velocity
		let dSum = num_keys > 1 ? Math.sqrt(2) : 1;

		this.x += this.vx / dSum;
		this.y += this.vy / dSum;
		this.vx *= 0.9;
		this.vy *= 0.9;

		if (this.x < 10) {
			this.vx = 0;
			this.x = 10;
		}
		if (this.x > 790) {
			this.vx = 0;
			this.x = 790;
		}
		if (this.y < 10) {
			this.vy = 0;
			this.y = 10;
		}
		if (this.y > 790) {
			this.vy = 0;
			this.y = 790;
		}
	}
}
