import { baseApi } from '@/core/api';

export const testApi = baseApi.injectEndpoints({
    endpoints: (build) => ({
        getTests: build.query<Array<{ id: number; title: string }>, void>({
            query: () => ({
                url: '/main/',
                method: 'GET',
            }),
            keepUnusedDataFor: Infinity,
            providesTags: ['Test'],
        }),
        createTest: build.mutation<{ id: number; title: string }, string>({
            query: (title) => ({
                url: '/main/create_test/',
                method: 'POST',
                body: { title: title },
            }),
            invalidatesTags: ['Test'],
        }),
    }),
});

export const { useGetTestsQuery, useCreateTestMutation } = testApi;
