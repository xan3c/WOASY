import * as PIXI from "pixi.js";
import png from "../../static/favicon.png";
import png2 from "static/favicon.png";
import { get_scenario } from "$lib/communication";

const texture = PIXI.Texture.from(png2);

export class Game {
	app: PIXI.Application;
	canvas: HTMLCanvasElement;

	constructor(canvas: HTMLCanvasElement) {
		this.canvas = canvas;
	}

	async start() {
		let scenario = await get_scenario();
		console.log(scenario);

		this.app = new PIXI.Application({
			view: this.canvas,
			width: 800,
			height: 800,
			resolution: window.devicePixelRatio,
			autoDensity: true,
			antialias: true,
		});

		let container = new PIXI.Container();
		this.app.stage.addChild(container);

		let graphics = new PIXI.Graphics();
		graphics.beginFill(0xffffff);
		graphics.drawCircle(0, 0, 30);
		graphics.endFill();

		this.app.stage.addChild(graphics);

		let sprite = new PIXI.Sprite(texture);
		this.app.stage.addChild(sprite);

		let tick = 0;

		let svg: SVGAElement;

		// let t = PIXI.Texture.from(svg);
		// console.log(this.app.renderer.plugins.interaction);

		sprite.interactive = true;

		(sprite as any).mouseover = (mouseData) => {
			sprite.alpha = 0.5;
		};

		(sprite as any).mouseout = (mouseData) => {
			sprite.alpha = 0.5;
		};

		const animate = (dt: number) => {
			graphics.x = 400 + 100 * Math.cos(tick / 20);
			graphics.y = 400 + 100 * Math.sin(tick / 20);

			tick += 1;
		};

		this.app.ticker.add(animate);
	}
}
