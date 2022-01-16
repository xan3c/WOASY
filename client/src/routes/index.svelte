<script context="module" lang="ts">
</script>

<script lang="ts">
	import { onMount, onDestroy } from "svelte";
	import { timeRemaining, capacityRemaining } from "$lib/store";

	let handleResize = () => {};
	let canvas: HTMLCanvasElement;
	let text: string;
	let num: number;

	const f = (str: string) => {};
	f(text);

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

	let count_value;

	timeRemaining.subscribe((value) => {
		count_value = value;
	});
</script>

<div class="container">
	<h1>
		{#if $timeRemaining !== null}
			Time Remaining: {count_value}
		{/if}
		&nbsp;
		{#if $capacityRemaining !== null}
			Capacity Remaining: {$capacityRemaining}
		{/if}
	</h1>
	<canvas bind:this={canvas} />
	<button>New Game</button>
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
		flex-direction: column;
		align-items: center;
		justify-content: center;
		/* cursor: url("images/life.png"), auto; */
	}

	button {
		margin: 12px;
		width: 240px;
		height: 48px;
		font-size: 24px;
	}
</style>
