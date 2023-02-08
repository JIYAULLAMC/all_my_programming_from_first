const redux = require("redux");
const reduxLogger = require("redux-logger");
const createStore = redux.createStore;
const combineReducers = redux.combineReducers;
const logger = reduxLogger.createLogger();
const applyMiddleware =  redux.applyMiddleware

const BUY_CAKE = "BUY_CAKE";
const BUY_ICE = "BUY_ICE";

function buyCake() {
  return {
    type: BUY_CAKE,
    info: "used to buy the cake ",
  };
}

function buyIce() {
  return {
    type: BUY_ICE,
    info: "used to buy the cake ",
  };
}

const initialCakeState = {
  numOfCakes: 10,
};

const initialIceState = {
  numOfCakes: 10,
};

const cakeReducer = (state = initialCakeState, action) => {
  switch (action.type) {
    case BUY_CAKE:
      return {
        ...state,
        numOfCakes: state.numOfCakes - 1,
      };
    default:
      return state;
  }
};

const iceReducer = (state = initialIceState, action) => {
  switch (action.type) {
    case BUY_ICE:
      return {
        ...state,
        numOfIce: state.numOfIce - 1,
      };
    default:
      return state;
  }
};

const rootReducer = combineReducers({
  cake: cakeReducer,
  ice: iceReducer,
});

const store = createStore(rootReducer, applyMiddleware(logger));

console.log("initial state", store.getState());

const unsubscribe = store.subscribe(() =>{});

store.dispatch(buyCake());
store.dispatch(buyCake());
store.dispatch(buyCake());

unsubscribe();
