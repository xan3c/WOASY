export class Key {
	value: string;
	isDown: boolean;
	isUp: boolean;
	press?: Function;
	release?: Function;
	downHandler: Function;
	upHandler: Function;
	unsubscribe: Function;

	constructor(value_: string) {
		this.value = value_;

		this.downHandler = (event: KeyboardEvent) => {
			if (event.key === this.value) {
				if (this.isUp && this.press) this.press();
				this.isDown = true;
				this.isUp = false;
				event.preventDefault();
			}
		};

		this.upHandler = (event: KeyboardEvent) => {
			if (event.key === this.value) {
				if (this.isDown && this.release) this.release();
				this.isDown = false;
				this.isUp = true;
				event.preventDefault();
			}
		};

		window.addEventListener("keydown", this.downHandler.bind(this), false);
		window.addEventListener("keyup", this.upHandler.bind(this), false);

		this.unsubscribe = () => {
			window.removeEventListener("keydown", this.downHandler.bind(this));
			window.removeEventListener("keyup", this.downHandler.bind(this));
		};
	}
}
