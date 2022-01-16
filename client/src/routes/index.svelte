<script lang="ts">
	import { onMount, onDestroy } from "svelte";
	import { timeRemaining, capacityRemaining } from "$lib/store";

	let handleResize = () => {};
	let canvas: HTMLCanvasElement;

	let newGame = () => {};

	onMount(async () => {
		const gameLib = await import("$lib/game");

		newGame = () => {
			let game = new gameLib.Game(canvas);
			game.start();
		};
	});
</script>

<div class="container">
	<h1>
		{#if $timeRemaining !== null && $capacityRemaining !== null}
			Time Remaining: {$timeRemaining}
			&nbsp; Capacity Remaining: {$capacityRemaining}
		{:else}
			Game Over!
		{/if}
	</h1>
	<canvas bind:this={canvas} />
	<button on:click={newGame}>New Game</button>
</div>

<svelte:window on:resize|passive={handleResize} />

<style>
	canvas {
		padding: 0;
		margin: 0;
		width: 1000px;
		height: 800px;
	}

	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		/* cursor: url("images/life.png"), auto; */
		text-align: center;
	}

	button {
		margin: 12px;
		width: 240px;
		height: 48px;
		font-size: 24px;
	}
</style>
