import { writable } from "svelte/store";

export const timeRemaining = writable<number | null>(null);
export const capacityRemaining = writable<number | null>(null);
