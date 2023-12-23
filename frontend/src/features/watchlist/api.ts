import { apiMap } from '@/constants';
import { baseApi } from '@/core/api';

const {
    base_url: watchlist_base_url,
    watch: watchlist_watch,
    unwatch: watchlist_unwatch,
} = apiMap.watchlist;

export const watchlistApi = baseApi.injectEndpoints({
    endpoints: (build) => ({
        watchMovie: build.mutation<void, string>({
            query: (slug) => ({
                url: watchlist_base_url + '/' + slug + watchlist_watch,
                method: 'POST',
            }),
            invalidatesTags: ['Movie'],
        }),
        unwatchMovie: build.mutation<void, string>({
            query: (slug) => ({
                url: watchlist_base_url + '/' + slug + watchlist_unwatch,
                method: 'DELETE',
            }),
            invalidatesTags: ['Movie'],
        }),
    }),
});

export const { useWatchMovieMutation, useUnwatchMovieMutation } = watchlistApi;
