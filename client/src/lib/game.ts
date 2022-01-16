import * as PIXI from "pixi.js";

export class Game {
	app: PIXI.Application;
	canvas: HTMLCanvasElement;

	constructor(canvas: HTMLCanvasElement) {
		this.canvas = canvas;
	}

	async start() {
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

		let tick = 0;

		const animate = (dt: number) => {
			graphics.x = 400 + 100 * Math.cos(tick / 20);
			graphics.y = 400 + 100 * Math.sin(tick / 20);

			tick += 1;
		};

		this.app.ticker.add(animate);
	}
}
