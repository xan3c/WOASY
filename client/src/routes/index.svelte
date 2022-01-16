<script lang="ts">
	import { onMount, onDestroy } from "svelte";

	let handleResize = () => {};
	let canvas: HTMLCanvasElement;

	onMount(async () => {
		const gameLib = await import("$lib/game");

		handleResize = () => {
			// game.winw.set(window.innerWidth);
			// game.winh.set(window.innerHeight);
			// game.pixelRatio.set(window.devicePixelRatio);
			// game.winResize();
		};

		handleResize();

		let game = new gameLib.Game(canvas);

		game.start();
	});
</script>

<div class="container">
	<canvas bind:this={canvas} />
</div>

<svelte:window on:resize|passive={handleResize} />

<style>
	canvas {
		padding: 0;
		margin: 0;
	}

	.container {
		margin-top: 32px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
</style>
