import { apiMap } from '@/constants';
import { baseApi } from '@/core/api';
import type { ReadMovie } from '@/features/movie';

const { base_url: movie_base_url, random: random_movie } = apiMap.movie;

export const movieApi = baseApi.injectEndpoints({
    endpoints: (build) => ({
        allMovies: build.query<Array<ReadMovie>, void>({
            query: () => ({
                url: movie_base_url,
                method: 'GET',
            }),
        }),
        singleMovie: build.query<ReadMovie, string>({
            query: (slug) => ({
                url: movie_base_url + '/' + slug,
                method: 'GET',
            }),
        }),
        randomMovie: build.query<ReadMovie, void>({
            query: () => ({
                url: movie_base_url + random_movie,
                method: 'GET',
            }),
        }),
    }),
});

export const { useAllMoviesQuery, useSingleMovieQuery, useRandomMovieQuery } =
    movieApi;
