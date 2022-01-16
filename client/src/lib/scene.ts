import type { Options } from "@dicebear/avatars";
import type * as style from "@dicebear/avatars-avataaars-sprites";

export type CharacterObject = {
	x: number;
	y: number;
	options: Partial<style.Options & Options>;
	age: number;
	bio: string;
};

export type SceneObject = {
	characters: CharacterObject[];
	lifeboat: {
		x: number;
		y: number;
		maxCapacity: number;
	};
	maxTime: number;
};
