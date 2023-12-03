import { apiMap } from '@/constants';
import { baseApi } from '@/core/api';
import type { LoginRequest, RegisterRequest, ReadUser } from '@/features/user';

const { base_url: auth_base_url, login, register, logout } = apiMap.auth;
const { base_url: user_base_url, me } = apiMap.user;

export const authApi = baseApi.injectEndpoints({
    endpoints: (build) => ({
        register: build.mutation<ReadUser, RegisterRequest>({
            query: (credentials) => ({
                url: auth_base_url + register,
                method: 'POST',
                body: credentials,
            }),
        }),
        login: build.mutation<void, LoginRequest>({
            query: (credentials) => ({
                url: auth_base_url + login,
                method: 'POST',
                body: credentials,
            }),
        }),
        logout: build.mutation<void, void>({
            query: () => ({
                url: auth_base_url + logout,
                method: 'POST',
            }),
        }),
        me: build.query<ReadUser, void>({
            query: () => ({
                url: user_base_url + me,
                method: 'GET',
            }),
            keepUnusedDataFor: Infinity,
        }),
    }),
});

export const {
    useLoginMutation,
    useRegisterMutation,
    useLogoutMutation,
    useMeQuery,
} = authApi;
