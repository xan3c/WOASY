export type CharacterObject = {
	x: number;
	y: number;
	svg: SVGElement;
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
