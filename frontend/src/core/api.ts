import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

import { apiMap } from '@/constants';

const { base_url } = apiMap;

export interface ApiError {
    status: number;
    data: { detail: string | { [field: string]: Array<string> } };
}

export const baseApi = createApi({
    reducerPath: 'baseApi',
    baseQuery: fetchBaseQuery({
        baseUrl: base_url,
    }),
    tagTypes: ['User'],
    endpoints: () => ({}),
});
