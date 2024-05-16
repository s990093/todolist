"use client";
import React, { createContext, useState } from "react";

interface ContextType {
  state: {
    userID: boolean;
    user: any;
    loading: boolean;
    authenticated: boolean;
    isRegistered: boolean;
  };
  setIsRegistered: (value: boolean) => void;
}

let Context = createContext<ContextType>({
  state: {
    userID: false,
    user: undefined,
    loading: true,
    authenticated: false,
    isRegistered: false,
  },
  setIsRegistered: () => {},
});

function Provider(props: { children: React.ReactNode }) {
  const initialState = {
    userID: false,
    user: undefined,
    loading: true,
    authenticated: false,
    isRegistered: true,
  };

  const [state, updateState] = useState(initialState);

  const setIsRegistered = (value: boolean) => {
    updateState({ ...state, isRegistered: value });
  };

  return (
    <Context.Provider
      value={{
        state: state,
        setIsRegistered: setIsRegistered,
      }}
    >
      {props.children}
    </Context.Provider>
  );
}

const Consumer = Context.Consumer;
export { Provider, Consumer, Context };
