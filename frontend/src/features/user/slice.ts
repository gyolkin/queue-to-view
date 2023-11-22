import { createSlice } from '@reduxjs/toolkit';

import { authApi } from './api';
import type { RootState } from '@/core/store';

interface AuthState {
    isAuthenticated: boolean;
}

const initialState: AuthState = {
    isAuthenticated: false,
};

export const userSlice = createSlice({
    name: 'userSlice',
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder.addMatcher(authApi.endpoints.me.matchFulfilled, (state) => {
            state.isAuthenticated = true;
        });
        builder.addMatcher(authApi.endpoints.logout.matchFulfilled, (state) => {
            state.isAuthenticated = false;
        });
    },
});

export const selectIsAuthenticated = (state: RootState) =>
    state.userSlice.isAuthenticated;
