const redux = require('redux')
const createStore = redux.createStore


BUY_CAKE = "BUY_CAKE";
BUY_ICE = "BUY_ICE";

function buyCake() {
  return {
    type: BUY_CAKE,
    info: "this is the buy cake ",
  };
}

function buyIce() {
  return {
    type: BUY_ICE,
    info: "this is the buy cake ",
  };
}

initialState = {
  numOfCakes: 10,
  numOfIce : 5,
};

reducer = (state = initialState, action) => {
  switch (action.type) {
    case BUY_CAKE:
      return {
        ...state,
        numOfCakes: state.numOfCakes - 1,
      };
    case BUY_ICE:
      return {
        ...state,
        numOfIce: state.numOfIce - 1,
      };
    default:
      return state;
  }
};


const store = createStore(reducer)

console.log("inintial state", store.getState())

const unsubscribe = store.subscribe(()=> console.log("updated state", store.getState()))

store.dispatch(buyCake())
store.dispatch(buyCake())
store.dispatch(buyCake())
store.dispatch(buyIce())
store.dispatch(buyIce())

unsubscribe()
