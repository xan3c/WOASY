import * as PIXI from "pixi.js";
import boat from "static/images/boat.png";
import type { Key } from "./input";
import type { NPC } from "./npc";

let texture = PIXI.Texture.from(boat);
texture.defaultAnchor.set(0.5, 0.5);

export class Player extends PIXI.Sprite {
	vx = 0;
	vy = 0;

	speed = 0.5;

	constructor() {
		super(texture);
		this.scale.set(0.1, 0.1);
		this.rotation = (3 * Math.PI) / 2;
	}

	move(keyW: Key, keyS: Key, keyA: Key, keyD: Key) {
		if (keyW.isDown) {
			this.vy -= this.speed;
		}
		if (keyS.isDown) {
			this.vy += this.speed;
		}
		if (keyA.isDown) {
			this.vx -= this.speed;
		}
		if (keyD.isDown) {
			this.vx += this.speed;
		}

		this.x += this.vx;
		this.y += this.vy;
		this.vx *= 0.8;
		this.vy *= 0.8;

		if (this.x < 0) {
			this.vx = 0;
			this.x = 0;
		}
		if (this.x > 400) {
			this.vx = 0;
			this.x = 400;
		}
		if (this.y < 0) {
			this.vy = 0;
			this.y = 0;
		}
		if (this.y > 400) {
			this.vy = 0;
			this.y = 400;
		}
	}
}
