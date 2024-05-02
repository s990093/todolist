interface ComponentConstantBase {
  w: number;
  h: number;
  bounded: number;
  color: string;
  opcity: number;
}
interface CardBase extends ComponentConstantBase {}

interface Constants {
  cardBase: CardBase;
}

export const Constants: Constants = {
  cardBase: {
    w: 100,
    h: 100,
    color: "#000000",
    bounded: 100,
    opcity: 50,
  },
};
